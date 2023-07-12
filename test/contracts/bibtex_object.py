from abc import ABC
from abc import abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_author(self):
        pass

    @abstractmethod
    def test_check_cffobj(self):
        pass

    @abstractmethod
    def test_doi(self):
        pass

    @abstractmethod
    def test_month(self):
        pass

    @abstractmethod
    def test_as_string(self):
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
