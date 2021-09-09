# This style loosely tries to implement the guidelines set in the
# "How to Cite Software in APA Style"[1] blog post. The general idea of an
# APA-like format is not to rigidly follow APA rules[2], but mostly to provide an
# output that resembles something that one would find in a scientific
# publication, particularly following the "usual who-when-what-where format".
#
# Example references [1]:
# Esolang, A. N. (2014). Obscure Reference Generator [Computer software]. Washington, DC: E & K Press.
# Customized Synergy [Computer software]. (2014). Retrieved from http://customizedsynergy.com
#
# [1] https://blog.apastyle.org/apastyle/2015/01/how-to-cite-software-in-apa-style.html
# [2] https://apastyle.apa.org
from abc import abstractmethod


class ApalikeObjectShared:

    supported_apalike_props = [
        'author',
        'year',
        'title',
        'version',
        'doi',
        'url'
    ]

    def __init__(self, cffobj, initialize_empty=False):
        self.cffobj = cffobj
        self.author = None
        self.year = None
        self.title = None
        self.version = None
        self.doi = None
        self.url = None
        if initialize_empty:
            # clause for testing purposes
            pass
        else:
            self.check_cffobj()
            self.add_all()

    def __str__(self):
        items = [item for item in [self.author,
                                   self.year,
                                   self.title,
                                   self.version,
                                   self.doi,
                                   self.url] if item is not None]
        return ''.join(items)

    def add_all(self):
        self.add_author()   \
            .add_year()     \
            .add_title()    \
            .add_version()  \
            .add_doi()      \
            .add_url()
        return self

    def add_author(self):
        if 'authors' in self.cffobj.keys():
            authors = list()
            for author in self.cffobj['authors']:
                def extract_initials(self):
                    # Print initials of 'given-name'. Adapted from
                    # https://www.geeksforgeeks.org/python-print-initials-name-last-name-full/
                    # split the string into a list
                    name = self
                    num_names = name.split()
                    initials = ""
                    # traverse in the list
                    for i in range(len(num_names)):
                        name = num_names[i]
                        # adds the capital first character
                        initials += (name[0].upper()+'.')
                    return initials
                keys = author.keys()
                nameparts = [
                    author['name-particle'] if 'name-particle' in keys else None,
                    author['family-names'] if 'family-names' in keys else None,
                    author['name-suffix'] if 'name-suffix' in keys else None,
                    extract_initials(author['given-names']) if 'given-names' in keys else None
                ]
                fullname = ' '.join([namepart for namepart in nameparts if namepart is not None])
                # fullname = lastnames + ' ' + author['given-names'] if 'given-names' in keys else lastnames
                # fullname = lastnames + ' ' + self.extract_initials() if 'given-names' in keys else lastnames
                alias = author['alias'] if 'alias' in keys and author['alias'] is not None and author['alias'] != '' else None
                if fullname:
                    authors.append(format(fullname))
                elif alias:
                    authors.append(format(alias))
                else:
                    continue
            self.author = ', '.join(authors)
        return self

    @abstractmethod
    def add_year(self):
        pass

    def add_title(self):
        if 'title' in self.cffobj.keys():
            self.title = format(self.cffobj['title'])
        return self

    def add_version(self):
        if 'version' in self.cffobj.keys():
            self.version = ' (version ' + str(self.cffobj['version']) + '). '
        return self

    @abstractmethod
    def add_doi(self):
        pass

    def add_url(self):
        if 'repository-code' in self.cffobj.keys():
            self.url = 'URL: ' + format(self.cffobj['repository-code']) + '\n'
        return self

    @abstractmethod
    def check_cffobj(self):
        pass

    def print(self):
        return self.__str__()
