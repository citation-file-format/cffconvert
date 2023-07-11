from cffconvert.behavior_shared.schemaorg_urls_shared import SchemaorgUrlsShared as Shared


# pylint: disable=too-few-public-methods
class SchemaorgUrls(Shared):

    def as_tuple(self):
        key = ''.join([
            self._has_identifiers_url(),
            self._has_repository(),
            self._has_repository_artifact(),
            self._has_repository_code(),
            self._has_url()
        ])
        return self._behaviors[key]()
