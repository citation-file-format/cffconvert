from abc import ABC
from abc import abstractmethod


class Contract(ABC):

    @abstractmethod
    def _get_schema(self):
        pass

    @abstractmethod
    def _parse(self):
        pass

    @abstractmethod
    def as_bibtex(self):
        pass

    @abstractmethod
    def validate(self):
        pass
