import requests
import yaml
import re
import json
from datetime import datetime, date


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, (datetime, date)):
            return o.isoformat()
        return o.__dict__


class Citation:

    def __init__(self, url, instantiate_empty=False, override=None, remove=None):
        self.as_yaml = None
        self.baseurl = None
        self.file_contents = None
        self.file_url = None
        self.override = override
        self.remove = remove
        self.url = url
        if not instantiate_empty:
            self._get_baseurl()
            self._retrieve_file()
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
                self.as_yaml[key] = self.override[key]
                self.file_contents = yaml.safe_dump(self.as_yaml, default_flow_style=False)

    def _parse_yaml(self):
        self.as_yaml = yaml.safe_load(self.file_contents)
        if not isinstance(self.as_yaml, dict):
            raise Exception("Provided CITATION.cff does not seem valid YAML.")

    def _remove_suspect_keys(self):
        if self.remove is not None and type(self.remove) is list:
            for key in self.remove:
                if key in self.as_yaml:
                    del(self.as_yaml[key])
                    self.file_contents = yaml.safe_dump(self.as_yaml, default_flow_style=False)

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
            self.file_contents = r.text
        else:
            raise Exception("Error requesting file: {0}".format(self.file_url))

    def as_bibtex(self):

        def get_author_string():
            arr = list()
            for author in self.as_yaml["authors"]:
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
        if "authors" in self.as_yaml:
            s += ",\nauthor = {\n"
            s += get_author_string()
            s += "\n         }"
        if "title" in self.as_yaml:
            s += ",\ntitle  = {"
            s += self.as_yaml["title"] + "}"
        if "date-released" in self.as_yaml:
            s += ",\nmonth  = {"
            s += str(self.as_yaml["date-released"].month) + "}"
            s += ",\nyear   = {"
            s += str(self.as_yaml["date-released"].year) + "}"
        if "doi" in self.as_yaml:
            s += ",\ndoi    = {"
            s += self.as_yaml["doi"] + "}"
        if "repository-code" in self.as_yaml:
            s += ",\nurl    = {"
            s += self.as_yaml["repository-code"] + "}"
        s += "\n}\n"

        return s

    def as_codemeta(self):

        def resolve_spdx_license(spdx_license_code):
            licenses_url = "https://raw.githubusercontent.com/spdx/license-list-data" + \
                           "/b541ee8a345aa93b70a08765c7bf5e423bb4d558/json/licenses.json"
            r = requests.get(licenses_url)
            if r.ok:
                data = r.json()
                return [spdx_license for spdx_license in data["licenses"]
                        if spdx_license["licenseId"] == spdx_license_code][0]["seeAlso"][0]
            else:
                raise Warning("status not '200 OK'")

        def construct_authors_arr():

            authors = list()
            for read_author in self.as_yaml["authors"]:
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
        if "repository-code" in self.as_yaml:
            d["codeRepository"] = self.as_yaml["repository-code"]
        if "date-released" in self.as_yaml:
            d["datePublished"] = self.as_yaml["date-released"].isoformat()
        if "authors" in self.as_yaml:
            d["author"] = construct_authors_arr()
        if "keywords" in self.as_yaml:
            d["keywords"] = self.as_yaml["keywords"]
        if "license" in self.as_yaml:
            d["license"] = resolve_spdx_license(self.as_yaml["license"])
        if "version" in self.as_yaml:
            d["version"] = self.as_yaml["version"]
        if "doi" in self.as_yaml:
            d["identifier"] = "https://doi.org/{0}".format(self.as_yaml["doi"])
        if "title" in self.as_yaml:
            d["name"] = self.as_yaml["title"]

        return json.dumps(d, sort_keys=True, indent=4, ensure_ascii=False)

    def as_enw(self):

        def construct_author_string():
            names = list()
            for author in self.as_yaml["authors"]:
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
            return ", ".join(["\"" + keyword + "\"" for keyword in self.as_yaml["keywords"]])

        s = ""
        s += "%0\n"
        s += "%0 Generic\n"

        if "authors" in self.as_yaml:
            s += "%A " + construct_author_string() + "\n"
        else:
            s += "%A\n"

        if "date-released" in self.as_yaml:
            s += "%D " + str(self.as_yaml["date-released"].year) + "\n"
        else:
            s += "%D\n"

        if "title" in self.as_yaml:
            s += "%T " + self.as_yaml["title"] + "\n"
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
        if "date-released" in self.as_yaml:
            s += "%8 " + str(self.as_yaml["date-released"].month) + "\n"
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
        if "keywords" in self.as_yaml:
            s += "%K " + construct_keywords_string() + "\n"
        else:
            s += "%K\n"

        s += "%X\n"
        s += "%Z\n"
        if "repository-code" in self.as_yaml:
            s += "%U " + self.as_yaml["repository-code"] + "\n"
        else:
            s += "%U\n"

        return s

    def as_json(self):
        return JSONEncoder().encode(self.as_yaml)

    def as_ris(self):
        def construct_author_string():
            names = list()
            for author in self.as_yaml["authors"]:
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
            for keyword in self.as_yaml["keywords"]:
                names.append("KW  - " + keyword + "\n")
            return "".join(names)

        def construct_date_string():
            return "PY  - " + \
                   str(self.as_yaml["date-released"].year) + "/" +\
                   str(self.as_yaml["date-released"].month).rjust(2,"0") + "/" +\
                   str(self.as_yaml["date-released"].day).rjust(2, "0") + "\n"

        s = ""
        s += "TY  - COMP\n"

        if "authors" in self.as_yaml:
            s += construct_author_string()
        else:
            s += "AU  -\n"

        if "doi" in self.as_yaml:
            s += "DO  - " + self.as_yaml["doi"] + "\n"
        else:
            s += "DO  -\n"

        if "keywords" in self.as_yaml:
            s += construct_keywords_string()
        else:
            s += "KW  -\n"

        s += "M3  - software\n"
        s += "PB  - GitHub Inc.\n"
        s += "PP  - San Francisco, USA\n"

        if "date-released" in self.as_yaml:
            s += construct_date_string()
        else:
            s += "PY  -\n"

        if "title" in self.as_yaml:
            s += "T1  - " + self.as_yaml["title"] + "\n"
        else:
            s += "T1  -\n"

        if "repository-code" in self.as_yaml:
            s += "UR  - " + self.as_yaml["repository-code"] + "\n"
        else:
            s += "UR  -\n"

        s += "ER  -\n"

        return s

    def as_zenodojson(self):

        def construct_authors_arr():

            authors = list()
            for author in self.as_yaml["authors"]:
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
                    author2["orcid"] = author["orcid"]

                if "affiliation" in author:
                    author2["affiliation"] = author["affiliation"]

                authors.append(author2)
            return authors

        d = dict()
        if "abstract" in self.as_yaml:
            d["description"] = self.as_yaml["abstract"]

        if "authors" in self.as_yaml:
            d["creators"] = construct_authors_arr()

        if "keywords" in self.as_yaml:
            d["keywords"] = self.as_yaml["keywords"]

        if "license" in self.as_yaml:
            d["license"] = {"id": self.as_yaml["license"]}

        if "title" in self.as_yaml:
            d["title"] = self.as_yaml["title"]

        return json.dumps(d, sort_keys=True, indent=4, ensure_ascii=False)
