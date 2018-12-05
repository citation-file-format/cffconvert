import sys
import os
import requests
import ruamel.yaml as yaml
import re
import json
from datetime import datetime, date
import tempfile
from pykwalifire.core import Core


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        return o.__dict__


class Citation:

    def __init__(self, url=None, cffstr=None, ignore_suspect_keys=False, override=None, remove=None, suspect_keys=None,
                 instantiate_empty=False, validate=False):

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

    def _key_should_be_included(self, key):
        if not self.ignore_suspect_keys:
            return key in self.yaml
        elif key in self.suspect_keys:
            return False
        else:
            return key in self.yaml

    def _override_suspect_keys(self):
        if self.override is not None and type(self.override) is dict:
            for key in self.override.keys():
                self.yaml[key] = self.override[key]
                self.cffstr = yaml.safe_dump(self.yaml, default_flow_style=False)

    def _parse_yaml(self):
        self.yaml = yaml.safe_load(self.cffstr)
        if not isinstance(self.yaml, dict):
            raise ValueError("Provided CITATION.cff does not seem valid YAML.")

    def _remove_suspect_keys(self):
        if self.remove is not None and type(self.remove) is list:
            for key in self.remove:
                if key in self.yaml:
                    del(self.yaml[key])
                    self.cffstr = yaml.safe_dump(self.yaml, default_flow_style=False)

    def _retrieve_file(self):
        regexp = re.compile("^" +
                            "(?P<baseurl>https://github\.com)/" +
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
        regexp = re.compile("^cff-version: (['|\"])?(?P<semver>[\d\.]*)(['\"])?\s*$")
        semver = None
        for line in self.cffstr.split("\n"):
            matched = re.match(regexp, line)
            if matched is not None:
                semver = matched.groupdict()["semver"]
                break

        if semver is None:
            raise ValueError("Unable to identify the schema version. Does the CFF include the 'cff-version' key?")
        schema_url = "https://raw.githubusercontent.com/citation-file-format/" +\
                     "schema/{0}/CFF-Core/schema.yaml".format(semver)
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
            try:
                c.validate(raise_exception=True)
            except Exception as e:
                pass

        return self

    def as_bibtex(self):

        def get_author_string():
            arr = list()
            for author in self.yaml["authors"]:
                authors = list()
                if "given-names" in author:
                    authors.append(author["given-names"])
                if "name-particle" in author:
                    authors.append(author["name-particle"])
                if "family-names" in author:
                    authors.append(author["family-names"])
                if "name-suffix" in author:
                    authors.append(author["name-suffix"])
                arr.append(" " * 12 + " ".join(authors))
            return " and\n".join(arr)

        s = ""
        s += "@misc{"
        s += "YourReferenceHere"
        if self._key_should_be_included("authors"):
            s += ",\nauthor = {\n"
            s += get_author_string()
            s += "\n         }"
        if self._key_should_be_included("title"):
            s += ",\ntitle  = {"
            s += self.yaml["title"] + "}"
        if self._key_should_be_included("date-released"):
            s += ",\nmonth  = {"
            s += str(self.yaml["date-released"].month) + "}"
            s += ",\nyear   = {"
            s += str(self.yaml["date-released"].year) + "}"
        if self._key_should_be_included("doi"):
            s += ",\ndoi    = {"
            s += self.yaml["doi"] + "}"
        if self._key_should_be_included("repository-code"):
            s += ",\nurl    = {"
            s += self.yaml["repository-code"] + "}"
        s += "\n}\n"

        return s

    def as_cff(self, indent=4, sort_keys=True, ensure_ascii=False):
        return json.dumps(self.yaml, sort_keys=sort_keys, indent=indent, ensure_ascii=ensure_ascii)

    def as_codemeta(self):

        def resolve_spdx_license(spdx_license_code):
            licenses_url = "https://raw.githubusercontent.com/spdx/license-list-data" + \
                           "/b541ee8a345aa93b70a08765c7bf5e423bb4d558/json/licenses.json"
            r = requests.get(licenses_url)
            if r.ok:
                data = r.json()
                for license in data["licenses"]:
                    if license["licenseId"] == spdx_license_code:
                        return license["seeAlso"][0]
                raise ValueError("Provided license {0} not in list of licenses".format(spdx_license_code))
            else:
                raise Warning("status not '200 OK'")

        def construct_authors_arr():

            authors = list()
            for read_author in self.yaml["authors"]:
                write_author = dict()
                write_author["@type"] = "Person"

                if "given-names" in read_author:
                    write_author["givenName"] = read_author["given-names"]

                family_name = ""
                if "name-particle" in read_author:
                    family_name += read_author["name-particle"] + " "
                if "family-names" in read_author:
                    family_name += read_author["family-names"]
                if "name-suffix" in read_author:
                    family_name += " " + read_author["name-suffix"]
                write_author["familyName"] = family_name

                if "orcid" in read_author:
                    write_author["@id"] = read_author["orcid"]

                if "affiliation" in read_author:
                    write_author["affiliation"] = {
                        "@type": "Organization",
                        "legalName": read_author["affiliation"]
                    }

                authors.append(write_author)
            return authors

        d = dict()
        d["@context"] = [
            "https://doi.org/10.5063/schema/codemeta-2.0",
            "http://schema.org"
        ]
        d["@type"] = "SoftwareSourceCode"
        if self._key_should_be_included("repository-code"):
            d["codeRepository"] = self.yaml["repository-code"]
        if self._key_should_be_included("date-released"):
            d["datePublished"] = self.yaml["date-released"].isoformat()
        if self._key_should_be_included("authors"):
            d["author"] = construct_authors_arr()
        if self._key_should_be_included("keywords"):
            d["keywords"] = self.yaml["keywords"]
        if self._key_should_be_included("license"):
            d["license"] = resolve_spdx_license(self.yaml["license"])
        if self._key_should_be_included("version"):
            d["version"] = self.yaml["version"]
        if self._key_should_be_included("doi"):
            d["identifier"] = "https://doi.org/{0}".format(self.yaml["doi"])
        if self._key_should_be_included("title"):
            d["name"] = self.yaml["title"]

        return json.dumps(d, sort_keys=True, indent=4, ensure_ascii=False)

    def as_enw(self):

        def construct_author_string():
            names = list()
            for author in self.yaml["authors"]:
                name = ""
                if "name-particle" in author:
                    name += author["name-particle"] + " "
                if "family-names" in author:
                    name += author["family-names"]
                if "name-suffix" in author:
                    name += " " + author["name-suffix"]
                if "given-names" in author:
                    name += ", " + author["given-names"]
                names.append(name)
            return " & ".join(names)

        def construct_keywords_string():
            return ", ".join(["\"" + keyword + "\"" for keyword in self.yaml["keywords"]])

        s = ""
        s += "%0\n"
        s += "%0 Generic\n"

        if self._key_should_be_included("authors"):
            s += "%A " + construct_author_string() + "\n"
        else:
            s += "%A\n"

        if self._key_should_be_included("date-released"):
            s += "%D " + str(self.yaml["date-released"].year) + "\n"
        else:
            s += "%D\n"

        if self._key_should_be_included("title"):
            s += "%T " + self.yaml["title"] + "\n"
        else:
            s += "%T\n"

        s += "%E\n"
        s += "%B\n"
        s += "%C\n"
        s += "%I GitHub repository\n"
        s += "%V\n"
        s += "%6\n"
        s += "%N\n"
        s += "%P\n"
        s += "%&\n"
        s += "%Y\n"
        s += "%S\n"
        s += "%7\n"
        if self._key_should_be_included("date-released"):
            s += "%8 " + str(self.yaml["date-released"].month) + "\n"
        else:
            s += "%8\n"

        s += "%9\n"
        s += "%?\n"
        s += "%!\n"
        s += "%Z\n"
        s += "%@\n"
        s += "%(\n"
        s += "%)\n"
        s += "%*\n"
        s += "%L\n"
        s += "%M\n"
        s += "\n"
        s += "\n"
        s += "%2\n"
        s += "%3\n"
        s += "%4\n"
        s += "%#\n"
        s += "%$\n"
        s += "%F YourReferenceHere\n"
        if self._key_should_be_included("keywords"):
            s += "%K " + construct_keywords_string() + "\n"
        else:
            s += "%K\n"

        s += "%X\n"
        s += "%Z\n"
        if self._key_should_be_included("repository-code"):
            s += "%U " + self.yaml["repository-code"] + "\n"
        else:
            s += "%U\n"

        return s

    def as_json(self):
        return JSONEncoder().encode(self.yaml)

    def as_ris(self):
        def construct_author_string():
            names = list()
            for author in self.yaml["authors"]:
                name = "AU  - "
                if "name-particle" in author:
                    name += author["name-particle"] + " "
                if "family-names" in author:
                    name += author["family-names"]
                if "name-suffix" in author:
                    name += " " + author["name-suffix"]
                if "given-names" in author:
                    name += ", " + author["given-names"]
                name += "\n"
                names.append(name)
            return "".join(names)

        def construct_keywords_string():
            names = list()
            for keyword in self.yaml["keywords"]:
                names.append("KW  - " + keyword + "\n")
            return "".join(names)

        def construct_date_string():
            return "PY  - " + \
                   str(self.yaml["date-released"].year) + "/" +\
                   str(self.yaml["date-released"].month).rjust(2,"0") + "/" +\
                   str(self.yaml["date-released"].day).rjust(2, "0") + "\n"

        s = ""
        s += "TY  - COMP\n"

        if self._key_should_be_included("authors"):
            s += construct_author_string()
        else:
            s += "AU  -\n"

        if self._key_should_be_included("doi"):
            s += "DO  - " + self.yaml["doi"] + "\n"
        else:
            s += "DO  -\n"

        if self._key_should_be_included("keywords"):
            s += construct_keywords_string()
        else:
            s += "KW  -\n"

        s += "M3  - software\n"
        s += "PB  - GitHub Inc.\n"
        s += "PP  - San Francisco, USA\n"

        if self._key_should_be_included("date-released"):
            s += construct_date_string()
        else:
            s += "PY  -\n"

        if self._key_should_be_included("title"):
            s += "T1  - " + self.yaml["title"] + "\n"
        else:
            s += "T1  -\n"

        if self._key_should_be_included("repository-code"):
            s += "UR  - " + self.yaml["repository-code"] + "\n"
        else:
            s += "UR  -\n"

        s += "ER  -\n"

        return s

    def as_zenodojson(self):

        def construct_authors_arr():

            authors = list()
            for author in self.yaml["authors"]:
                name = ""
                if "name-particle" in author:
                    name += author["name-particle"] + " "
                if "family-names" in author:
                    name += author["family-names"]
                if "name-suffix" in author:
                    name += " " + author["name-suffix"]
                if "given-names" in author:
                    name += ", " + author["given-names"]

                author2 = {"name": name}
                if "orcid" in author:
                    author2["orcid"] = author["orcid"].replace('https://orcid.org/', '')

                if "affiliation" in author:
                    author2["affiliation"] = author["affiliation"]

                authors.append(author2)
            return authors

        if self.ignore_suspect_keys is False and len(self.suspect_keys) > 0:
            print("Note: suspect keys will be included in the output.", file=sys.stderr)

        d = dict()
        if self._key_should_be_included("abstract"):
            d["description"] = self.yaml["abstract"]

        if self._key_should_be_included("authors"):
            d["creators"] = construct_authors_arr()

        if self._key_should_be_included("date-released"):
            d["publication_date"] = self.yaml["date-released"].isoformat()

        if self._key_should_be_included("doi"):
            d["doi"] = self.yaml["doi"]

        if self._key_should_be_included("keywords"):
            d["keywords"] = self.yaml["keywords"]

        if self._key_should_be_included("license"):
            d["license"] = {"id": self.yaml["license"]}

        if self._key_should_be_included("title"):
            d["title"] = self.yaml["title"]

        if self._key_should_be_included("version"):
            d["version"] = self.yaml["version"]

        return json.dumps(d, sort_keys=True, indent=4, ensure_ascii=False)
