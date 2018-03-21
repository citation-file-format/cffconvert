import requests
import yaml
import re


class Citation:

    def __init__(self, url, instantiate_empty=False):
        self.url = url
        self.baseurl = None
        self.file_url = None
        self.file_contents = None
        self.as_yaml = None
        if not instantiate_empty:
            self._get_baseurl()
            self._retrieve_file()
            self._parse_yaml()

    def _get_baseurl(self):
        if self.url[0:18] == "https://github.com":
            self.baseurl = "https://raw.githubusercontent.com"
        else:
            raise Exception("Only GitHub is supported at the moment.")

    def _retrieve_file(self):

        regexp = re.compile("^" +
                            "(?P<baseurl>https://github\.com)/" +
                            "(?P<user>[^/\n]*)/" +
                            "(?P<repo>[^/\n]*)" +
                            "(/(?P<branch>[^/\n]*))?", re.IGNORECASE)
        matched = re.match(regexp, self.url).groupdict()

        self.file_url = "/".join([self.baseurl,
                                  matched["user"],
                                  matched["repo"],
                                  matched["branch"] if matched["branch"] is not None else "master",
                                  "CITATION.cff"])

        r = requests.get(self.file_url)
        if r.ok:
            self.file_contents = r.text
        else:
            raise Warning("status not '200 OK'")

    def _parse_yaml(self):
        self.as_yaml = yaml.safe_load(self.file_contents)

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
                    name += author["name-suffix"]
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
        s += construct_author_string()
        s += "DO  - " + self.as_yaml["doi"] + "\n"
        s += construct_keywords_string()
        s += "M3  - software\n"
        s += "PB  - GitHub Inc.\n"
        s += "PP  - San Francisco, USA\n"
        s +=  construct_date_string()
        s += "T1  - " + self.as_yaml["title"] + "\n"
        s += "UR  - " + self.as_yaml["repository-code"] + "\n"
        s += "ER  -\n"
        return s

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

    def as_codemeta(self):

        def resolve_spdx_license(spdx_license_code):
            licenses_url = "https://raw.githubusercontent.com/spdx/license-list-data/master/json/licenses.json"
            r = requests.get(licenses_url)
            if r.ok:
                data = r.json()
                return [license["seeAlso"][0] for license in data["licenses"] if license["licenseId"] == spdx_license_code][0]
            else:
                raise Warning("status not '200 OK'")

        def convert(author):

            family_names = list()
            for name_part in ["name-particle", "family-names", "name-suffix"]:
                if name_part in author.keys() and author[name_part] is not "":
                    family_names.append(author[name_part])

            author_str = ''
            author_str += '{\n'
            author_str += '        "@type": "Person"'
            if "given-names" in author:
                author_str += ',\n        "givenName": "{0}"'.format(author["given-names"])
            author_str += ',\n        "familyName": "{0}"'.format(" ".join(family_names))
            if "affiliation" in author:
                author_str += ',\n'
                author_str += '        "affiliation": {\n'
                author_str += '            "@type": "Organization",\n'
                author_str += '            "legalName": "{0}"\n'.format(author["affiliation"])
                author_str += '        }'
            author_str += '\n    }'
            return author_str

        s = ''
        s += '{\n'
        s += '    "@context": "http://schema.org",\n'
        s += '    "@type": "SoftwareSourceCode"'
        if "repository-code" in self.as_yaml:
            s += ',\n    "codeRepository": "{0}"'.format(self.as_yaml["repository-code"])
        if "date-released" in self.as_yaml:
            s += ',\n    "datePublished": "{0}"'.format(self.as_yaml["date-released"])
        if "authors" in self.as_yaml:
            s += ',\n    "author": [{0}]'.format(", ".join([convert(author) for author in self.as_yaml["authors"]]))
        if "keywords" in self.as_yaml:
            s += ',\n    "keywords": [{0}]'.format(", ".join(['"{0}"'.format(kw) for kw in self.as_yaml["keywords"]]))
        if "license" in self.as_yaml:
            s += ',\n    "license": "{0}"'.format(resolve_spdx_license(self.as_yaml["license"]))
        if "version" in self.as_yaml:
            s += ',\n    "version": "{0}"'.format(self.as_yaml["version"])
        if "doi" in self.as_yaml:
            s += ',\n    "identifier": "https://doi.org/{0}"'.format(self.as_yaml["doi"])
        if "title" in self.as_yaml:
            s += ',\n    "name": "{0}"'.format(self.as_yaml["title"])
        s += '\n}\n'

        return s

