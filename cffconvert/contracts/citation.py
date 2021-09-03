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
    def as_apalike(self):
        pass

    @abstractmethod
    def as_bibtex(self, reference='YourReferenceHere'):
        pass

    @abstractmethod
    def as_cff(self):
        pass

    @abstractmethod
    def as_codemeta(self):
        pass

    @abstractmethod
    def as_endnote(self):
        pass

    @abstractmethod
    def as_schemaorg(self):
        pass

    @abstractmethod
    def as_ris(self):
        pass

    @abstractmethod
    def as_zenodo(self):
        pass

    @abstractmethod
    def validate(self):
        pass
