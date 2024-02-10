from abc import ABC, abstractmethod
from pathlib import Path


class WorkingFiles(ABC):
    path = Path(Path(__file__).parent.parent.parent, "data", "vacancies.csv")

    @abstractmethod
    def create_file(self) -> None:
        pass

    @abstractmethod
    def in_file(self, vacancies_list: list[dict]) -> None:
        pass

    @abstractmethod
    def out_file(self) -> list[dict]:
        pass

    @abstractmethod
    def del_file(self) -> None:
        pass
