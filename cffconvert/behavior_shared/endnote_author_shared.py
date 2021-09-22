from abc import abstractmethod
from cffconvert.behavior_shared.abstract_author_shared import AbstractAuthorShared


# pylint: disable=too-few-public-methods
class EndnoteAuthorShared(AbstractAuthorShared):

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
            '____': EndnoteAuthorShared._from_thin_air
        }

    def _from_alias(self):
        return '%A ' + self._author.get('alias') + '\n'

    def _from_given_and_last(self):
        return '%A ' + self._get_full_last_name() + ', ' + self._author.get('given-names') + '\n'

    def _from_given(self):
        return '%A ' + self._author.get('given-names') + '\n'

    def _from_last(self):
        return '%A ' + self._get_full_last_name() + '\n'

    def _from_name(self):
        return '%A ' + self._author.get('name') + '\n'

    @abstractmethod
    def as_string(self):
        pass
