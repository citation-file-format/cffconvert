import os
import requests
import ruamel.yaml as yaml
import re
import json
from datetime import datetime, date
import tempfile
from pykwalify.core import Core
from cffconvert.BibtexObject import BibtexObject
from cffconvert.CodemetaObject import CodemetaObject
from cffconvert.EndnoteObject import EndnoteObject
from cffconvert.RisObject import RisObject
from cffconvert.SchemaorgObject import SchemaorgObject
from cffconvert.ZenodoObject import ZenodoObject


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        return o.__dict__


class Citation:

    def __init__(self, url=None, cffstr=None, ignore_suspect_keys=False, override=None, remove=None, suspect_keys=None,
                 instantiate_empty=False, validate=False, raise_exception=False):

        def xor(condition1, condition2):
            conditions = [condition1, condition2]
            return False in conditions and True in conditions

        if not xor(url is None, cffstr is None):
            raise ValueError("You should specify either \'url\' or \'cffstr\'.")

        self.url = url
        self.cffstr = cffstr
        self.yaml = None
        self.baseurl = None
        self.file_url = None
        self.override = override
        self.remove = remove
        self.ignore_suspect_keys = ignore_suspect_keys
        self.validate = validate
        self.raise_exception = raise_exception
        self.schema = None
        if suspect_keys is None:
            self.suspect_keys = ["doi", "version", "date-released", "commit"]
        else:
            if isinstance(suspect_keys, list):
                self.suspect_keys = suspect_keys
            else:
                raise ValueError("Provided argument \'suspect_keys\' should be instance of list.")

        if not instantiate_empty:
            if self.cffstr is None:
                # still have to retrieve the cff string
                self._get_baseurl()
                self._retrieve_file()

            if self.validate:
                self._validate()

            self._parse_yaml()
            self._override_suspect_keys()
            self._remove_suspect_keys()

    def _get_baseurl(self):
        if self.url[0:18] == "https://github.com":
            self.baseurl = "https://raw.githubusercontent.com"
        else:
            raise Exception("Only 'https://github.com' URLs are supported at the moment.")

    def _override_suspect_keys(self):
        if self.override is not None and type(self.override) is dict:
            for key in self.override.keys():
                self.yaml[key] = self.override[key]
                self.cffstr = yaml.safe_dump(self.yaml, default_flow_style=False)

    def _parse_yaml(self):
        self.yaml = yaml.safe_load(self.cffstr)
        if not isinstance(self.yaml, dict):
            raise ValueError("Provided CITATION.cff does not seem valid YAML.")
        # correct dates that have been entered as strings in the YAML:
        if 'date-released' in self.yaml.keys() and isinstance(self.yaml['date-released'], str):
            self.yaml['date-released'] = datetime.strptime(self.yaml['date-released'], '%Y-%m-%d')

    def _remove_suspect_keys(self):
        if self.remove is not None and type(self.remove) is list:
            for key in self.remove:
                if key in self.yaml:
                    del(self.yaml[key])
                    self.cffstr = yaml.safe_dump(self.yaml, default_flow_style=False)

    def _retrieve_file(self):
        regexp = re.compile(r"^" +
                            "(?P<baseurl>https://github.com)/" +
                            "(?P<org>[^/\n]*)/" +
                            "(?P<repo>[^/\n]*)" +
                            "(/tree/(?P<label>[^/\n]*))?", re.IGNORECASE)

        matched = re.match(regexp, self.url)
        if matched is None:
            raise Exception("Error extracting (user|organization) and/or repository " +
                            "information from the provided URL ({0}).".format(self.url))
        else:
            url_parts = matched.groupdict()

        self.file_url = "/".join([self.baseurl,
                                  url_parts["org"],
                                  url_parts["repo"],
                                  url_parts["label"] if url_parts["label"] is not None else "master",
                                  "CITATION.cff"])

        r = requests.get(self.file_url)
        if r.ok:
            self.cffstr = r.text
        else:
            raise Exception("Error requesting file: {0}".format(self.file_url))

    def _validate(self):
        regexp = re.compile(r"^cff-version: (['|\"])?(?P<semver>[\d\.]*)(['\"])?\s*$")
        semver = None
        has_no_cff_version_key = True
        for line in self.cffstr.split("\n"):
            if line[0:12] == "cff-version:":
                has_no_cff_version_key = False
                matched = re.match(regexp, line)
                if matched is not None:
                    semver = matched.groupdict()["semver"]
                    break

        if has_no_cff_version_key:
            raise ValueError("Unable to identify the schema version. Does the CFF include the 'cff-version' key?")
        if semver is None:
            raise ValueError("Unrecognized value for key \"cff-version\".")

        schema_urls = {
            "1.0.1": "https://raw.githubusercontent.com/citation-file-format/schema/1.0.1/CFF-Core/schema.yaml",
            "1.0.2": "https://raw.githubusercontent.com/citation-file-format/schema/1.0.2/CFF-Core/schema.yaml",
            "1.0.3": "https://raw.githubusercontent.com/citation-file-format/schema/1.0.3-1/CFF-Core/schema.yaml",
            "1.1.0": "https://raw.githubusercontent.com/citation-file-format/citation-file-format/1.1.0/schema.yaml"
        }

        try:
            schema_url = schema_urls[semver]
        except KeyError as e:
            versions = '"' + '", "'.join(sorted(schema_urls.keys())) + '"'
            raise Exception("\"{0}\" is not a supported release. Instead, use one of {1}."
                            .format(semver, versions))

        r = requests.get(schema_url)
        r.raise_for_status()
        self.schema = r.text

        with tempfile.TemporaryDirectory() as tmpdir:

            datafile = os.path.join(tmpdir, "data.yaml")
            schemafile = os.path.join(tmpdir, "schema.yaml")
            with open(datafile, "w") as f:
                f.write(self.cffstr)
            with open(schemafile, "w") as f:
                f.write(self.schema)

            c = Core(source_file=datafile, schema_files=[schemafile])
            c.validate(raise_exception=self.raise_exception)

        return self

    def as_bibtex(self):
        return BibtexObject(self.yaml).print()

    def as_cff(self, indent=4, sort_keys=True, ensure_ascii=False):
        return json.dumps(self.yaml, sort_keys=sort_keys,
                          indent=indent, ensure_ascii=ensure_ascii)

    def as_codemeta(self):
        return CodemetaObject(self.yaml).print()

    def as_enw(self):
        return EndnoteObject(self.yaml).print()

    def as_json(self):
        return JSONEncoder().encode(self.yaml)

    def as_schema_dot_org(self):
        return SchemaorgObject(self.yaml).print()

    def as_ris(self):
        return RisObject(self.yaml).print()

    def as_zenodojson(self):
        return ZenodoObject(self.yaml).print()
