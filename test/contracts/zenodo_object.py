from abc import ABC
from abc import abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_check_cffobj(self, fixture):
        pass

    @abstractmethod
    def test_creators(self, fixture):
        pass

    @abstractmethod
    def test_keywords(self, fixture):
        pass

    @abstractmethod
    def test_license(self, fixture):
        pass

    @abstractmethod
    def test_print(self, fixture):
        pass

    @abstractmethod
    def test_publication_date(self, fixture):
        pass

    @abstractmethod
    def test_title(self, fixture):
        pass

    @abstractmethod
    def test_version(self, fixture):
        pass
