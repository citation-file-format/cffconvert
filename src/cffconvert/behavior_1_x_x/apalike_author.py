from cffconvert.behavior_1_x_x.abstract_author import AbstractAuthor


# pylint: disable=too-few-public-methods
class ApalikeAuthor(AbstractAuthor):

    def __init__(self, author):
        super().__init__(author)
        self._behaviors = {
            'GFAN': self._from_given_and_last,
            'GFA_': self._from_given_and_last,
            'GF_N': self._from_given_and_last,
            'GF__': self._from_given_and_last,
            'G_AN': self._from_given,
            'G_A_': self._from_given,
            'G__N': self._from_given,
            'G___': self._from_given,
            '_FAN': self._from_last,
            '_FA_': self._from_last,
            '_F_N': self._from_last,
            '_F__': self._from_last,
            '__AN': self._from_alias,
            '__A_': self._from_alias,
            '___N': self._from_name,
            '____': ApalikeAuthor._from_thin_air
        }

    def _from_alias(self):
        return self._author.get('alias')

    def _from_given_and_last(self):
        return self._get_full_last_name() + ' ' + self._get_initials()

    def _from_given(self):
        return self._author.get('given-names')

    def _from_last(self):
        return self._get_full_last_name()

    def _from_name(self):
        return self._author.get('name')

    def _get_initials(self):
        given_names = self._author.get('given-names').split(' ')
        return ''.join([given_name[0] + '.' for given_name in given_names])

    def as_string(self):
        key = ''.join([
            self._has_given_name(),
            self._has_family_name(),
            self._has_alias(),
            self._has_name()
        ])
        return self._behaviors[key]()