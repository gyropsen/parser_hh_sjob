from abc import ABC, abstractmethod
from pathlib import Path


class WorkingFiles(ABC):
    path = Path(Path(__file__).parent.parent.parent, "data", "vacancies.csv")

    @abstractmethod
    def in_file(self, data):
        pass

    @abstractmethod
    def out_file(self):
        pass

    @abstractmethod
    def del_file(self):
        pass
