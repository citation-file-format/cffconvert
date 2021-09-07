from cffconvert.behavior_shared.schemaorg_author import SchemaorgAuthorShared
from cffconvert.behavior_shared.schemaorg import SchemaorgObjectShared


class SchemaorgAuthor(SchemaorgAuthorShared):

    def __init__(self, author_cff):
        super().__init__(author_cff)
        self._behaviors = {
            'GFNAO': self._from_given_and_last_and_affiliation_and_orcid,
            'GFNA.': self._from_given_and_last_and_affiliation,
            'GFN.O': self._from_given_and_last_and_orcid,
            'GFN..': self._from_given_and_last,
            'GF.AO': self._from_given_and_last_and_affiliation_and_orcid,
            'GF.A.': self._from_given_and_last_and_affiliation,
            'GF..O': self._from_given_and_last_and_orcid,
            'GF...': self._from_given_and_last,
            'G.NAO': self._from_given_and_affiliation_and_orcid,
            'G.NA.': self._from_given_and_affiliation,
            'G.N.O': self._from_given_and_orcid,
            'G.N..': self._from_given,
            'G..AO': self._from_given_and_affiliation_and_orcid,
            'G..A.': self._from_given_and_affiliation,
            'G...O': self._from_given_and_orcid,
            'G....': self._from_given,
            '.FNAO': self._from_last_and_affiliation_and_orcid,
            '.FNA.': self._from_last_and_affiliation,
            '.FN.O': self._from_last_and_orcid,
            '.FN..': self._from_last,
            '.F.AO': self._from_last_and_affiliation_and_orcid,
            '.F.A.': self._from_last_and_affiliation,
            '.F..O': self._from_last_and_orcid,
            '.F...': self._from_last,
            '..NAO': self._from_name_and_affiliation_and_orcid,
            '..NA.': self._from_name_and_affiliation,
            '..N.O': self._from_name_and_orcid,
            '..N..': self._from_name,
            '...AO': self._from_affiliation_and_orcid,
            '...A.': self._from_affiliation,
            '....O': self._from_orcid,
            '.....': self._from_thin_air
        }

    def as_dict(self):
        state = [
            ('G', self._exists_nonempty('given-names')),
            ('F', self._exists_nonempty('family-names')),
            ('N', self._exists_nonempty('name')),
            ('A', self._exists_nonempty('affiliation')),
            ('O', self._exists_nonempty('orcid'))
        ]
        key = ''.join([item[0] if item[1] is True else '.' for item in state])
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
