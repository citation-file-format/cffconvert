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


class ApalikeObject:

    supported_cff_versions = ['1.0.3', '1.1.0', '1.2.0']
    supported_pure_props = ['author', 'year', 'title', 'version', 'doi', 'url']

    def __init__(self, cff_object, initialize_empty=False):
        self.cff_object = cff_object
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
            self.check_cff_object()
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
        if 'authors' in self.cff_object.keys():
            authors = list()
            for author in self.cff_object['authors']:
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

    def add_year(self):
        version = self.cff_object['cff-version']
        if version in ['1.0.1', '1.0.2', '1.0.3', '1.1.0']:
            if 'date-released' in self.cff_object.keys():
                self.year = ' (' + str(self.cff_object['date-released'].year) + '). '
        elif version in ['1.2.0']:
            if 'date-released' in self.cff_object.keys():
                self.year = ' (' + self.cff_object['date-released'][:4] + '). '
        else:
            raise ValueError("Unsupported schema version")
        return self

    def add_title(self):
        if 'title' in self.cff_object.keys():
            self.title = format(self.cff_object['title'])
        return self

    def add_version(self):
        if 'version' in self.cff_object.keys():
            self.version = ' (version ' + str(self.cff_object['version']) + '). '
        return self

    def add_doi(self):
        version = self.cff_object['cff-version']
        if version in ['1.0.3', '1.1.0', '1.2.0']:
            if 'doi' in self.cff_object.keys():
                self.doi = 'DOI: http://doi.org/' + format(self.cff_object['doi']) + ' '

        if version in ['1.1.0', '1.2.0']:
            if 'identifiers' in self.cff_object.keys():
                identifiers = self.cff_object['identifiers']
                for identifier in identifiers:
                    if identifier['type'] == 'doi':
                        self.doi = 'doi: ' + format(identifier['value']) + '. '
                        break
        return self

    def add_url(self):
        if 'repository-code' in self.cff_object.keys():
            self.url = 'URL: ' + format(self.cff_object['repository-code']) + '\n'
        return self

    def check_cff_object(self):
        if not isinstance(self.cff_object, dict):
            raise ValueError('Expected cff_object to be of type \'dict\'.')
        if 'cff-version' not in self.cff_object.keys():
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        if self.cff_object['cff-version'] not in ApalikeObject.supported_cff_versions:
            raise ValueError('\'cff-version\': \'{}\' isn\'t a supported version.'
                             .format(self.cff_object['cff-version']))

    def print(self):
        return self.__str__()
