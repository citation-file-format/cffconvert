from cffconvert.behavior_shared.schemaorg import SchemaorgAuthorShared
from cffconvert.behavior_shared.schemaorg import SchemaorgObjectShared


class SchemaorgAuthor(SchemaorgAuthorShared):

    def __init__(self, author_cff):
        super().__init__(author_cff)
        self._behaviors = {
            'TTTTTT': self._from_given_and_last_and_affiliation_and_orcid,
            'TTTTTF': self._from_given_and_last_and_affiliation,
            'TTTTFT': self._from_given_and_last_and_orcid,
            'TTTTFF': self._from_given_and_last,
            'TTTFTT': self._from_given_and_last_and_affiliation_and_orcid,
            'TTTFTF': self._from_given_and_last_and_affiliation,
            'TTTFFT': self._from_given_and_last_and_orcid,
            'TTTFFF': self._from_given_and_last,
            'TTFTTT': self._from_given_and_last_and_affiliation_and_orcid,
            'TTFTTF': self._from_given_and_last_and_affiliation,
            'TTFTFT': self._from_given_and_last_and_orcid,
            'TTFTFF': self._from_given_and_last,
            'TTFFTT': self._from_given_and_last_and_affiliation_and_orcid,
            'TTFFTF': self._from_given_and_last_and_affiliation,
            'TTFFFT': self._from_given_and_last_and_orcid,
            'TTFFFF': self._from_given_and_last,
            'TFTTTT': self._from_given_and_affiliation_and_orcid,
            'TFTTTF': self._from_given_and_affiliation,
            'TFTTFT': self._from_given_and_orcid,
            'TFTTFF': self._from_given,
            'TFTFTT': self._from_given_and_affiliation_and_orcid,
            'TFTFTF': self._from_given_and_affiliation,
            'TFTFFT': self._from_given_and_orcid,
            'TFTFFF': self._from_given,
            'TFFTTT': self._from_given_and_affiliation_and_orcid,
            'TFFTTF': self._from_given_and_affiliation,
            'TFFTFT': self._from_given_and_orcid,
            'TFFTFF': self._from_given,
            'TFFFTT': self._from_given_and_affiliation_and_orcid,
            'TFFFTF': self._from_given_and_affiliation,
            'TFFFFT': self._from_given_and_orcid,
            'TFFFFF': self._from_given,
            'FTTTTT': self._from_last_and_affiliation_and_orcid,
            'FTTTTF': self._from_last_and_affiliation,
            'FTTTFT': self._from_last_and_orcid,
            'FTTTFF': self._from_last,
            'FTTFTT': self._from_last_and_affiliation_and_orcid,
            'FTTFTF': self._from_last_and_affiliation,
            'FTTFFT': self._from_last_and_orcid,
            'FTTFFF': self._from_last,
            'FTFTTT': self._from_last_and_affiliation_and_orcid,
            'FTFTTF': self._from_last_and_affiliation,
            'FTFTFT': self._from_last_and_orcid,
            'FTFTFF': self._from_last,
            'FTFFTT': self._from_last_and_affiliation_and_orcid,
            'FTFFTF': self._from_last_and_affiliation,
            'FTFFFT': self._from_last_and_orcid,
            'FTFFFF': self._from_last,
            'FFTTTT': self._from_alias_and_affiliation_and_orcid,
            'FFTTTF': self._from_alias_and_affiliation,
            'FFTTFT': self._from_alias_and_orcid,
            'FFTTFF': self._from_alias,
            'FFTFTT': self._from_alias_and_affiliation_and_orcid,
            'FFTFTF': self._from_alias_and_affiliation,
            'FFTFFT': self._from_alias_and_orcid,
            'FFTFFF': self._from_alias,
            'FFFTTT': self._from_name_and_affiliation_and_orcid,
            'FFFTTF': self._from_name_and_affiliation,
            'FFFTFT': self._from_name_and_orcid,
            'FFFTFF': self._from_name,
            'FFFFTT': self._from_affiliation_and_orcid,
            'FFFFTF': self._from_affiliation,
            'FFFFFT': self._from_orcid,
            'FFFFFF': self._from_thin_air,
        }

    def as_dict(self):
        state = [
            self._exists_nonempty('given-names'),
            self._exists_nonempty('family-names'),
            self._exists_nonempty('alias'),
            self._exists_nonempty('name'),
            self._exists_nonempty('affiliation'),
            self._exists_nonempty('orcid')
        ]
        key = ''.join(['T' if item is True else 'F' for item in state])
        return self._behaviors[key]()


class SchemaorgObject(SchemaorgObjectShared):

    supported_cff_versions = [
        '1.1.0'
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
        if 'identifiers' in self.cffobj.keys():
            identifiers = self.cffobj['identifiers']
            for identifier in identifiers:
                if identifier['type'] == 'doi':
                    self.identifier = 'https://doi.org/{}'.format(identifier['value'])
                    break
        return self

    def check_cffobj(self):
        if not isinstance(self.cffobj, dict):
            raise ValueError('Expected cffobj to be of type \'dict\'.')
        if 'cff-version' not in self.cffobj.keys():
            raise ValueError('Missing key "cff-version" in CITATION.cff file.')
        if self.cffobj['cff-version'] not in SchemaorgObject.supported_cff_versions:
            raise ValueError('\'cff-version\': \'{}\' isn\'t a supported version.'
                             .format(self.cffobj['cff-version']))
