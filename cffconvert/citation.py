import os
import requests
import ruamel.yaml as yaml
import re
from datetime import datetime, date
import tempfile
from pykwalify.core import Core
from cffconvert.BibtexObject import BibtexObject
from cffconvert.CodemetaObject import CodemetaObject
from cffconvert.RisObject import RisObject
from cffconvert.SchemaorgObject import SchemaorgObject
from cffconvert.ZenodoObject import ZenodoObject
from cffconvert.EndnoteObject import EndnoteObject


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
        if self.url.startswith("https://github.com"):
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

        if not self.url[18:].startswith("/"):
            raise ValueError("Error extracting (user|organization) and/or repository " +
                             "information from the provided URL ({0}).".format(self.url))
        url_parts = self.url[19:].split('/')
        if len(url_parts) < 2:
            raise ValueError("Error extracting (user|organization) and/or repository " +
                             "information from the provided URL ({0}).".format(self.url))
        elif len(url_parts) == 2:
            org, repo, label = url_parts[0], url_parts[1], "master"
        else:
            if url_parts[2] != "tree":
                raise ValueError("Expected 'https://github.com/<org>/<repo>/tree/...' but instead "
                                 "found '{0}'".format(url_parts[2]))
            org, repo, label = url_parts[0], url_parts[1], url_parts[3]

        self.file_url = "/".join([self.baseurl, org, repo, label, "CITATION.cff"])
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
        filtered = self.filter_properties(self.yaml)
        return BibtexObject(filtered).print()

    def as_cff(self):
        filtered = self.filter_properties(self.yaml)
        return yaml.safe_dump(filtered)

    def as_codemeta(self):
        filtered = self.filter_properties(self.yaml)
        return CodemetaObject(filtered).print()

    def as_enw(self):
        filtered = self.filter_properties(self.yaml)
        return EndnoteObject(filtered).print()

    def as_schema_dot_org(self):
        filtered = self.filter_properties(self.yaml)
        return SchemaorgObject(filtered).print()

    def as_ris(self):
        filtered = self.filter_properties(self.yaml)
        return RisObject(filtered).print()

    def as_zenodojson(self):
        filtered = self.filter_properties(self.yaml)
        return ZenodoObject(filtered).print()

    def filter_properties(self, unfiltered):
        if self.ignore_suspect_keys:
            filtered = [item for item in unfiltered.items() if item[0] not in self.suspect_keys]
            return dict(filtered)
        else:
            return unfiltered
