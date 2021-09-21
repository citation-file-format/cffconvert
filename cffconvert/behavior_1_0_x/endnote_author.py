from cffconvert.behavior_shared.endnote_author_shared import EndnoteAuthorShared as Shared


class EndnoteAuthor(Shared):

    def __init__(self, author):
        super().__init__(author)

    def as_string(self):
        key = ''.join([
            self._has_given_name(),
            self._has_family_name(),
            '_',
            self._has_name()
        ])
        return self._behaviors[key]()
