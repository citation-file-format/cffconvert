from abc import ABC, abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_author(self):
        pass

    @abstractmethod
    def test_check_cff_object(self):
        pass

    @abstractmethod
    def test_doi(self):
        pass

    @abstractmethod
    def test_month(self):
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
