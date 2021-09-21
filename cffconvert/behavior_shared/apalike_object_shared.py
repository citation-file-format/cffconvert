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
    supported_cff_versions = None

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
        return ' '.join(items) + '\n'

    def add_all(self):
        self.add_author()   \
            .add_year()     \
            .add_title()    \
            .add_version()  \
            .add_doi()      \
            .add_url()
        return self

    @abstractmethod
    def add_author(self):
        pass

    @abstractmethod
    def add_year(self):
        pass

    def add_title(self):
        if 'title' in self.cffobj.keys():
            self.title = self.cffobj['title']
        return self

    def add_version(self):
        if 'version' in self.cffobj.keys():
            self.version = '(version ' + str(self.cffobj['version']) + ').'
        return self

    @abstractmethod
    def add_doi(self):
        pass

    @abstractmethod
    def add_url(self):
        pass

    def as_string(self):
        return self.__str__()

    def check_cffobj(self):
        if not isinstance(self.cffobj, dict):
            raise ValueError("Expected cffobj to be of type 'dict'.")
        if 'cff-version' not in self.cffobj.keys():
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        if self.cffobj['cff-version'] not in self.supported_cff_versions:
            raise ValueError(f"'cff-version': '{self.cffobj['cff-version']}' isn't a supported version.")
