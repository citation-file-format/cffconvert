from abc import ABC
from abc import abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_check_cffobj(self, fixture):
        pass

    @abstractmethod
    def test_author(self, fixture):
        pass

    @abstractmethod
    def test_code_repository(self, fixture):
        pass

    @abstractmethod
    def test_date_published(self, fixture):
        pass

    @abstractmethod
    def test_description(self, fixture):
        pass

    @abstractmethod
    def test_identifier(self, fixture):
        pass

    @abstractmethod
    def test_keywords(self, fixture):
        pass

    @abstractmethod
    def test_license(self, fixture):
        pass

    @abstractmethod
    def test_name(self, fixture):
        pass

    @abstractmethod
    def test_version(self, fixture):
        pass

    @abstractmethod
    def test_as_string(self, fixture):
        pass
