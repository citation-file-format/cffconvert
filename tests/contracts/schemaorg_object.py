from abc import ABC
from abc import abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_check_cffobj(self):
        pass

    @abstractmethod
    def test_author(self):
        pass

    @abstractmethod
    def test_code_repository(self):
        pass

    @abstractmethod
    def test_contributor(self):
        pass

    @abstractmethod
    def test_date_published(self):
        pass

    @abstractmethod
    def test_description(self):
        pass

    @abstractmethod
    def test_identifier(self):
        pass

    @abstractmethod
    def test_keywords(self):
        pass

    @abstractmethod
    def test_license(self):
        pass

    @abstractmethod
    def test_name(self):
        pass

    @abstractmethod
    def test_url(self):
        pass

    @abstractmethod
    def test_version(self):
        pass

    @abstractmethod
    def test_as_string(self):
        pass
