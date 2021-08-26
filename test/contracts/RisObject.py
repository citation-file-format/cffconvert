from abc import ABC
from abc import abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_abstract(self):
        pass

    @abstractmethod
    def test_author(self):
        pass

    @abstractmethod
    def test_check_cff_object(self):
        pass

    @abstractmethod
    def test_date(self):
        pass

    @abstractmethod
    def test_doi(self):
        pass

    @abstractmethod
    def test_keywords(self):
        pass

    @abstractmethod
    def test_print(self):
        pass

    @abstractmethod
    def test_title(self):
        pass

    @abstractmethod
    def test_url(self):
        pass

    @abstractmethod
    def test_year(self):
        pass
