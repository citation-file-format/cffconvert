import requests
import yaml
import re


class Citation:

    def __init__(self, url):
        self.url = url
        self.baseurl = "https://raw.githubusercontent.com"
        self.file = None
        self.file_url = None
        self.as_yaml = None

    def retrieve_file(self):

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

    def parse_yaml(self):
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
        s += "your_ref,\n"
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
        pass

