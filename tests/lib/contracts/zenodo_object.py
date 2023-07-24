from abc import ABC
from abc import abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_check_cffobj(self):
        pass

    @abstractmethod
    def test_contributors(self):
        pass

    @abstractmethod
    def test_creators(self):
        pass

    @abstractmethod
    def test_keywords(self):
        pass

    @abstractmethod
    def test_license(self):
        pass

    @abstractmethod
    def test_as_string(self):
        pass

    @abstractmethod
    def test_publication_date(self):
        pass

    @abstractmethod
    def test_title(self):
        pass

    @abstractmethod
    def test_related_identifiers(self):
        pass

    @abstractmethod
    def test_upload_type(self):
        pass

    @abstractmethod
    def test_version(self):
        pass
