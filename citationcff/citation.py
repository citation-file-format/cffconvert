import requests
import yaml
import re


class Citation:

    def __init__(self, url, instantiate_empty=False):
        self.url = url
        self.baseurl = "https://raw.githubusercontent.com"
        self.file_url = None
        self.file = None
        self.as_yaml = None
        if not instantiate_empty:
            self._retrieve_file()
            self._parse_yaml()

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
                                  "CITATION"])

        r = requests.get(self.file_url)
        if r.ok:
            self.file = r.text
        else:
            raise Warning("status not 200 OK")

    def _parse_yaml(self):
        self.as_yaml = yaml.safe_load(self.file)

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
                arr.append(" " * 12 + " ".join(authors))
            return " and\n".join(arr) + "\n"

        width = 8
        s = ""
        s += "@misc{"
        s += "YourReferenceHere,\n"
        s += "author".ljust(width, " ") + " = {\n"
        s += get_author_string()
        s += " " * 11 + "},\n"
        s += "title".ljust(width, " ") + " = {"
        s += self.as_yaml["title"] + "},\n"
        s += "month".ljust(width, " ") + " = {"
        s += str(self.as_yaml["date-released"].month) + "},\n"
        s += "year".ljust(width, " ") + " = {"
        s += str(self.as_yaml["date-released"].year) + "},\n"
        s += "doi".ljust(width, " ") + " = {"
        s += self.as_yaml["doi"] + "},\n"
        s += "url".ljust(width, " ") + " = {"
        s += self.as_yaml["repository"] + "}\n"
        s += "}"

        return s

    def as_csl(self):
        pass

    def as_enw(self):

        def construct_author_string():
            names = list()
            for author in self.as_yaml["authors"]:
                name = ""
                if "name-particle" in author:
                    name += author["name-particle"] + " "
                if "family-names" in author:
                    name += author["family-names"]
                if "given-names" in author:
                    name += ", " + author["given-names"]
                names.append(name)
            return " & ".join(names)

        def construct_keywords_string():
            if "keywords" in self.as_yaml:
                return ", ".join(["\"" + keyword + "\"" for keyword in self.as_yaml["keywords"]])
            else:
                return ""

        s = ""
        s += "%0\n"
        s += "%0 Generic\n"
        s += "%A " + construct_author_string() + "\n"
        s += "%D " + str(self.as_yaml["date-released"].year) + "\n"
        s += "%T " + self.as_yaml["title"] + "\n"
        s += "%E\n"
        s += "%B \n"
        s += "%C\n"
        s += "%I GitHub repository\n"
        s += "%V \n"
        s += "%6\n"
        s += "%N \n"
        s += "%P \n"
        s += "%& \n"
        s += "%Y \n"
        s += "%S \n"
        s += "%7\n"
        s += "%8 " + str(self.as_yaml["date-released"].month) + "\n"
        s += "%9\n"
        s += "%? \n"
        s += "%! \n"
        s += "%Z \n"
        s += "%@ \n"
        s += "%(\n"
        s += "%)\n"
        s += "%*\n"
        s += "%L\n"
        s += "%M\n"
        s += "\n"
        s += "\n"
        s += "%2 \n"
        s += "%3 \n"
        s += "%4 \n"
        s += "%# \n"
        s += "%$ \n"
        s += "%F YourReferenceHere\n"
        s += "%K " + construct_keywords_string() + "\n"
        s += "%X \n"
        s += "%Z \n"
        s += "%U " + self.as_yaml["repository"] + "\n"

        return s
