import sys
import os
sys.path.append(os.path.dirname(__file__))

from typing import List, Optional
from exhibit_repository import ExhibitRepository

class Exhibit:
    def __init__(self, id: str, title: str):
        self.id = id
        self.title = title

class InMemoryExhibitRepository(ExhibitRepository):
    def __init__(self):
        self._exhibits = []
    def add(self, exhibit: "Exhibit") -> None:
        self._exhibits.append(exhibit)

    def get_all(self) -> List["Exhibit"]:
        return self._exhibits

    def delete(self, exhibit_id: str) -> None:
        # TODO:

        pass