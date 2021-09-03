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
from cffconvert.behavior_shared.apalike import ApalikeObjectShared as Shared


class ApalikeObject(Shared):

    supported_cff_versions = [
        '1.0.1',
        '1.0.2',
        '1.0.3'
    ]

    def __init__(self, cffobj, initialize_empty=False):
        super().__init__(cffobj, initialize_empty)

    def add_year(self):
        if 'date-released' in self.cffobj.keys():
            self.year = ' (' + str(self.cffobj['date-released'].year) + '). '
        return self

    def add_doi(self):
        if 'doi' in self.cffobj.keys():
            self.doi = 'DOI: http://doi.org/' + format(self.cffobj['doi']) + ' '
        return self

    def check_cffobj(self):
        if not isinstance(self.cffobj, dict):
            raise ValueError("Expected cffobj to be of type 'dict'.")
        if 'cff-version' not in self.cffobj.keys():
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        if self.cffobj['cff-version'] not in ApalikeObject.supported_cff_versions:
            raise ValueError("'cff-version': '{}' isn't a supported version."
                             .format(self.cffobj['cff-version']))
