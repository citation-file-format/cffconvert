from abc import ABC, abstractmethod


class Contract(ABC):

    @abstractmethod
    def test_check_cff_object(self):
        pass

    @abstractmethod
    def test_author(self):
        pass

    @abstractmethod
    def test_code_repository(self):
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
    def test_version(self):
        pass

    @abstractmethod
    def test_print(self):
        pass
