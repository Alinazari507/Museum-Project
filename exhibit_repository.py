import abc
from typing import List, Optional

class Exhibit:
    def __init__(self, id: str, title: str):
        self.id = id
        self.title = title

class ExhibitRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, exhibit: "Exhibit") -> None:

        pass

    @abc.abstractmethod
    def get_by_id(self, exhibit_id: str) -> Optional["Exhibit"]:

        pass
    @abc.abstractmethod
    def get_all(self) -> List["Exhibit"]:
        pass
    @abc.abstractmethod
    def delete(self, exhibit_id: str) -> None:
        pass
