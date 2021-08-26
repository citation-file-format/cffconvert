from abc import ABC
from abc import abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_check_cff_object(self):
        pass

    @abstractmethod
    def test_creators(self):
        pass

    @abstractmethod
    def test_doi(self):
        pass

    @abstractmethod
    def test_keywords(self):
        pass

    @abstractmethod
    def test_license(self):
        pass

    @abstractmethod
    def test_print(self):
        pass

    @abstractmethod
    def test_publication_date(self):
        pass

    @abstractmethod
    def test_title(self):
        pass

    @abstractmethod
    def test_version(self):
        pass
