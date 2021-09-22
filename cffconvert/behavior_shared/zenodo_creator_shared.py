from abc import abstractmethod
from cffconvert.behavior_shared.abstract_author_shared import AbstractAuthorShared


# pylint: disable=too-few-public-methods
class ZenodoCreatorShared(AbstractAuthorShared):

    def __init__(self, author):
        super().__init__(author)
        self._behaviors = {
            'GFANAO': self._from_given_and_last_and_affiliation_and_orcid,
            'GFANA_': self._from_given_and_last_and_affiliation,
            'GFAN_O': self._from_given_and_last_and_orcid,
            'GFAN__': self._from_given_and_last,
            'GFA_AO': self._from_given_and_last_and_affiliation_and_orcid,
            'GFA_A_': self._from_given_and_last_and_affiliation,
            'GFA__O': self._from_given_and_last_and_orcid,
            'GFA___': self._from_given_and_last,
            'GF_NAO': self._from_given_and_last_and_affiliation_and_orcid,
            'GF_NA_': self._from_given_and_last_and_affiliation,
            'GF_N_O': self._from_given_and_last_and_orcid,
            'GF_N__': self._from_given_and_last,
            'GF__AO': self._from_given_and_last_and_affiliation_and_orcid,
            'GF__A_': self._from_given_and_last_and_affiliation,
            'GF___O': self._from_given_and_last_and_orcid,
            'GF____': self._from_given_and_last,
            'G_ANAO': self._from_given_and_affiliation_and_orcid,
            'G_ANA_': self._from_given_and_affiliation,
            'G_AN_O': self._from_given_and_orcid,
            'G_AT__': self._from_given,
            'G_A_AO': self._from_given_and_affiliation_and_orcid,
            'G_A_A_': self._from_given_and_affiliation,
            'G_A__O': self._from_given_and_orcid,
            'G_A___': self._from_given,
            'G__NAO': self._from_given_and_affiliation_and_orcid,
            'G__NA_': self._from_given_and_affiliation,
            'G__N_O': self._from_given_and_orcid,
            'G__N__': self._from_given,
            'G___AO': self._from_given_and_affiliation_and_orcid,
            'G___A_': self._from_given_and_affiliation,
            'G____O': self._from_given_and_orcid,
            'G_____': self._from_given,
            '_FANAO': self._from_last_and_affiliation_and_orcid,
            '_FANA_': self._from_last_and_affiliation,
            '_FAN_O': self._from_last_and_orcid,
            '_FAN__': self._from_last,
            '_FA_AO': self._from_last_and_affiliation_and_orcid,
            '_FA_A_': self._from_last_and_affiliation,
            '_FA__O': self._from_last_and_orcid,
            '_FA___': self._from_last,
            '_F_NAO': self._from_last_and_affiliation_and_orcid,
            '_F_NA_': self._from_last_and_affiliation,
            '_F_N_O': self._from_last_and_orcid,
            '_F_N__': self._from_last,
            '_F__AO': self._from_last_and_affiliation_and_orcid,
            '_F__A_': self._from_last_and_affiliation,
            '_F___O': self._from_last_and_orcid,
            '_F____': self._from_last,
            '__ANAO': self._from_alias_and_affiliation_and_orcid,
            '__ANA_': self._from_alias_and_affiliation,
            '__AN_O': self._from_alias_and_orcid,
            '__AN__': self._from_alias,
            '__A_AO': self._from_alias_and_affiliation_and_orcid,
            '__A_A_': self._from_alias_and_affiliation,
            '__A__O': self._from_alias_and_orcid,
            '__A___': self._from_alias,
            '___NAO': self._from_name_and_affiliation_and_orcid,
            '___NA_': self._from_name_and_affiliation,
            '___N_O': self._from_name_and_orcid,
            '___N__': self._from_name,
            '____AO': self._from_affiliation_and_orcid,
            '____A_': self._from_affiliation,
            '_____O': self._from_orcid,
            '______': ZenodoCreatorShared._from_thin_air
        }

    def _from_affiliation(self):
        return {
            'affiliation': self._author.get('affiliation')
        }

    def _from_affiliation_and_orcid(self):
        return {
            'affiliation': self._author.get('affiliation'),
            'orcid': self._get_id_from_orcid_url()
        }

    def _from_alias(self):
        return {
            'name': self._author.get('alias')
        }

    def _from_alias_and_affiliation(self):
        return {
            'affiliation': self._author.get('affiliation'),
            'name': self._author.get('alias')
        }

    def _from_alias_and_affiliation_and_orcid(self):
        return {
            'affiliation': self._author.get('affiliation'),
            'name': self._author.get('alias'),
            'orcid': self._get_id_from_orcid_url()
        }

    def _from_alias_and_orcid(self):
        return {
            'name': self._author.get('alias'),
            'orcid': self._get_id_from_orcid_url()
        }

    def _from_given(self):
        return {
            'name': self._author.get('given-names')
        }

    def _from_given_and_affiliation(self):
        return {
            'affiliation': self._author.get('affiliation'),
            'name': self._author.get('given-names')
        }

    def _from_given_and_affiliation_and_orcid(self):
        return {
            'affiliation': self._author.get('affiliation'),
            'name': self._author.get('given-names'),
            'orcid': self._get_id_from_orcid_url()
        }

    def _from_given_and_last(self):
        return {
            'name': self._get_full_last_name() + ', ' + self._author.get('given-names')
        }

    def _from_given_and_last_and_affiliation(self):
        return {
            'affiliation': self._author.get('affiliation'),
            'name': self._get_full_last_name() + ', ' + self._author.get('given-names')
        }

    def _from_given_and_last_and_affiliation_and_orcid(self):
        return {
            'affiliation': self._author.get('affiliation'),
            'name': self._get_full_last_name() + ', ' + self._author.get('given-names'),
            'orcid': self._get_id_from_orcid_url()
        }

    def _from_given_and_last_and_orcid(self):
        return {
            'name': self._get_full_last_name() + ', ' + self._author.get('given-names'),
            'orcid': self._get_id_from_orcid_url()
        }

    def _from_given_and_orcid(self):
        return {
            'name': self._author.get('given-names'),
            'orcid': self._get_id_from_orcid_url()
        }

    def _from_last(self):
        return {
            'name': self._get_full_last_name()
        }

    def _from_last_and_affiliation(self):
        return {
            'affiliation': self._author.get('affiliation'),
            'name': self._get_full_last_name()
        }

    def _from_last_and_affiliation_and_orcid(self):
        return {
            'affiliation': self._author.get('affiliation'),
            'name': self._get_full_last_name(),
            'orcid': self._get_id_from_orcid_url()
        }

    def _from_last_and_orcid(self):
        return {
            'name': self._get_full_last_name(),
            'orcid': self._get_id_from_orcid_url()
        }

    def _from_name(self):
        return {
            'name': self._author.get('name')
        }

    def _from_name_and_affiliation(self):
        return {
            'affiliation': self._author.get('affiliation'),
            'name': self._author.get('name')
        }

    def _from_name_and_affiliation_and_orcid(self):
        return {
            'affiliation': self._author.get('affiliation'),
            'name': self._author.get('name'),
            'orcid': self._get_id_from_orcid_url()
        }

    def _from_name_and_orcid(self):
        return {
            'name': self._author.get('name'),
            'orcid': self._get_id_from_orcid_url()
        }

    def _from_orcid(self):
        return {
            'orcid': self._get_id_from_orcid_url()
        }

    def _get_id_from_orcid_url(self):
        return self._author.get('orcid').replace('https://orcid.org/', '')

    @abstractmethod
    def as_dict(self):
        pass
