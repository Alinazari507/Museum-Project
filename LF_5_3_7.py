import abc
from typing import List

# --- 1. Domain Object ---
class Exhibit:
    def __init__(self, id: str, title: str):
        self.id = id
        self.title = title


# --- 2. Abstract Interface (The Contract) ---
class ExhibitRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, exhibit: Exhibit) -> None:
        pass

    @abc.abstractmethod
    def get_all(self) -> List[Exhibit]:
        pass

    @abc.abstractmethod
    def delete(self, exhibit_id: str) -> None:
        pass


# --- 3. Concrete Implementation (In-Memory) ---
class InMemoryExhibitRepository(ExhibitRepository):

    def __init__(self):
        self._exhibits = []  # Internal list to store data

    def add(self, exhibit: Exhibit) -> None:
        self._exhibits.append(exhibit)
        print(f"Added: {exhibit.title}")

    def get_all(self) -> List[Exhibit]:
        return self._exhibits

    def delete(self, exhibit_id: str) -> None:
        # Filter the list to remove the item with the given ID
        self._exhibits = [
            e for e in self._exhibits if e.id != exhibit_id
        ]
        print(f"Deleted exhibit with ID: {exhibit_id}")


# --- 4. Main Execution ---
if __name__ == "__main__":

    repo = InMemoryExhibitRepository()

    # Adding items
    repo.add(Exhibit("1", "Mona Lisa"))
    repo.add(Exhibit("2", "The Starry Night"))

    print("\nCurrent Museum Collection:")
    for item in repo.get_all():
        print(f"- {item.title} (ID: {item.id})")

    # Testing Delete
    repo.delete("1")

    print("\nCollection after deletion:")
    for item in repo.get_all():
        print(f"- {item.title} (ID: {item.id})")
