from abc import ABC
from abc import abstractmethod


class Contract(ABC):

    @abstractmethod
    def _parse(self):
        pass

    @abstractmethod
    def validate(self):
        pass
