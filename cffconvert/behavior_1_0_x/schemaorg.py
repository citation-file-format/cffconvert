from cffconvert.behavior_shared.schemaorg import SchemaorgAuthorShared
from cffconvert.behavior_shared.schemaorg import SchemaorgObjectShared


class SchemaorgAuthor(SchemaorgAuthorShared):

    def __init__(self, author_cff):
        super().__init__(author_cff)
        self._behaviors = {
            'TTTTT': self._from_given_and_last_and_affiliation_and_orcid,
            'TTTTF': self._from_given_and_last_and_affiliation,
            'TTTFT': self._from_given_and_last_and_orcid,
            'TTTFF': self._from_given_and_last,
            'TTFTT': self._from_given_and_last_and_affiliation_and_orcid,
            'TTFTF': self._from_given_and_last_and_affiliation,
            'TTFFT': self._from_given_and_last_and_orcid,
            'TTFFF': self._from_given_and_last,
            'TFTTT': self._from_given_and_affiliation_and_orcid,
            'TFTTF': self._from_given_and_affiliation,
            'TFTFT': self._from_given_and_orcid,
            'TFTFF': self._from_given,
            'TFFTT': self._from_given_and_affiliation_and_orcid,
            'TFFTF': self._from_given_and_affiliation,
            'TFFFT': self._from_given_and_orcid,
            'TFFFF': self._from_given,
            'FTTTT': self._from_last_and_affiliation_and_orcid,
            'FTTTF': self._from_last_and_affiliation,
            'FTTFT': self._from_last_and_orcid,
            'FTTFF': self._from_last,
            'FTFTT': self._from_last_and_affiliation_and_orcid,
            'FTFTF': self._from_last_and_affiliation,
            'FTFFT': self._from_last_and_orcid,
            'FTFFF': self._from_last,
            'FFTTT': self._from_name_and_affiliation_and_orcid,
            'FFTTF': self._from_name_and_affiliation,
            'FFTFT': self._from_name_and_orcid,
            'FFTFF': self._from_name,
            'FFFTT': self._from_affiliation_and_orcid,
            'FFFTF': self._from_affiliation,
            'FFFFT': self._from_orcid,
            'FFFFF': self._from_thin_air
        }

    def as_dict(self):
        state = [
            self._exists_nonempty('given-names'),
            self._exists_nonempty('family-names'),
            self._exists_nonempty('name'),
            self._exists_nonempty('affiliation'),
            self._exists_nonempty('orcid')
        ]
        key = ''.join(['T' if item is True else 'F' for item in state])
        return self._behaviors[key]()


class SchemaorgObject(SchemaorgObjectShared):

    supported_cff_versions = [
        '1.0.1',
        '1.0.2',
        '1.0.3'
    ]

    def __init__(self, cffobj, initialize_empty=False, context="https://schema.org"):
        super().__init__(cffobj, initialize_empty, context)

    def add_author(self):
        authors_cff = self.cffobj.get('authors', list())
        authors_schemaorg = [SchemaorgAuthor(a).as_dict() for a in authors_cff]
        self.author = [a for a in authors_schemaorg if a is not None]
        return self

    def add_date_published(self):
        if 'date-released' in self.cffobj.keys():
            self.date_published = "{:d}-{:02d}-{:02d}".format(self.cffobj['date-released'].year,
                                                              self.cffobj['date-released'].month,
                                                              self.cffobj['date-released'].day)
        return self

    def add_identifier(self):
        if 'doi' in self.cffobj.keys():
            self.identifier = 'https://doi.org/{}'.format(self.cffobj['doi'])
        return self

    def check_cffobj(self):
        if not isinstance(self.cffobj, dict):
            raise ValueError('Expected cffobj to be of type \'dict\'.')
        if 'cff-version' not in self.cffobj.keys():
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        if self.cffobj['cff-version'] not in SchemaorgObject.supported_cff_versions:
            raise ValueError('\'cff-version\': \'{}\' isn\'t a supported version.'
                             .format(self.cffobj['cff-version']))
