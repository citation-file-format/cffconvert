from cffconvert.behavior_shared.schemaorg_author import SchemaorgAuthorShared
from cffconvert.behavior_shared.schemaorg import SchemaorgObjectShared


class SchemaorgAuthor(SchemaorgAuthorShared):

    def __init__(self, author_cff):
        super().__init__(author_cff)
        self._behaviors = {
            'GFANAO': self._from_given_and_last_and_affiliation_and_orcid,
            'GFANA.': self._from_given_and_last_and_affiliation,
            'GFAN.O': self._from_given_and_last_and_orcid,
            'GFAN..': self._from_given_and_last,
            'GFA.AO': self._from_given_and_last_and_affiliation_and_orcid,
            'GFA.A.': self._from_given_and_last_and_affiliation,
            'GFA..O': self._from_given_and_last_and_orcid,
            'GFA...': self._from_given_and_last,
            'GF.NAO': self._from_given_and_last_and_affiliation_and_orcid,
            'GF.NA.': self._from_given_and_last_and_affiliation,
            'GF.N.O': self._from_given_and_last_and_orcid,
            'GF.N..': self._from_given_and_last,
            'GF..AO': self._from_given_and_last_and_affiliation_and_orcid,
            'GF..A.': self._from_given_and_last_and_affiliation,
            'GF...O': self._from_given_and_last_and_orcid,
            'GF....': self._from_given_and_last,
            'G.ANAO': self._from_given_and_affiliation_and_orcid,
            'G.ANA.': self._from_given_and_affiliation,
            'G.AN.O': self._from_given_and_orcid,
            'G.AT..': self._from_given,
            'G.A.AO': self._from_given_and_affiliation_and_orcid,
            'G.A.A.': self._from_given_and_affiliation,
            'G.A..O': self._from_given_and_orcid,
            'G.A...': self._from_given,
            'G..NAO': self._from_given_and_affiliation_and_orcid,
            'G..NA.': self._from_given_and_affiliation,
            'G..N.O': self._from_given_and_orcid,
            'G..N..': self._from_given,
            'G...AO': self._from_given_and_affiliation_and_orcid,
            'G...A.': self._from_given_and_affiliation,
            'G....O': self._from_given_and_orcid,
            'G.....': self._from_given,
            '.FANAO': self._from_last_and_affiliation_and_orcid,
            '.FANA.': self._from_last_and_affiliation,
            '.FAN.O': self._from_last_and_orcid,
            '.FAN..': self._from_last,
            '.FA.AO': self._from_last_and_affiliation_and_orcid,
            '.FA.A.': self._from_last_and_affiliation,
            '.FA..O': self._from_last_and_orcid,
            '.FA...': self._from_last,
            '.F.NAO': self._from_last_and_affiliation_and_orcid,
            '.F.NA.': self._from_last_and_affiliation,
            '.F.N.O': self._from_last_and_orcid,
            '.F.N..': self._from_last,
            '.F..AO': self._from_last_and_affiliation_and_orcid,
            '.F..A.': self._from_last_and_affiliation,
            '.F...O': self._from_last_and_orcid,
            '.F....': self._from_last,
            '..ANAO': self._from_alias_and_affiliation_and_orcid,
            '..ANA.': self._from_alias_and_affiliation,
            '..AN.O': self._from_alias_and_orcid,
            '..AN..': self._from_alias,
            '..A.AO': self._from_alias_and_affiliation_and_orcid,
            '..A.A.': self._from_alias_and_affiliation,
            '..A..O': self._from_alias_and_orcid,
            '..A...': self._from_alias,
            '...NAO': self._from_name_and_affiliation_and_orcid,
            '...NA.': self._from_name_and_affiliation,
            '...N.O': self._from_name_and_orcid,
            '...N..': self._from_name,
            '....AO': self._from_affiliation_and_orcid,
            '....A.': self._from_affiliation,
            '.....O': self._from_orcid,
            '......': self._from_thin_air
        }

    def as_dict(self):
        state = [
            ('G', self._exists_nonempty('given-names')),
            ('F', self._exists_nonempty('family-names')),
            ('A', self._exists_nonempty('alias')),
            ('N', self._exists_nonempty('name')),
            ('A', self._exists_nonempty('affiliation')),
            ('O', self._exists_nonempty('orcid'))
        ]
        key = ''.join([item[0] if item[1] is True else '.' for item in state])
        return self._behaviors[key]()


class SchemaorgObject(SchemaorgObjectShared):

    supported_cff_versions = [
        '1.2.0'
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
            self.date_published = self.cffobj['date-released']
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
