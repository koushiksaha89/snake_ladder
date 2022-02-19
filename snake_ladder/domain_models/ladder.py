from abc import ABC, abstractmethod
from collections import defaultdict


class Ladder(ABC):

    def __init__(self) -> None:
        super().__init__()
        self._no_of_ladders = None
        self.ladder_map = defaultdict()

    @abstractmethod
    def assign_ladder_paths(self):
        pass

    @property
    @abstractmethod
    def num_of_ladders(self):
        pass

    @num_of_ladders.setter
    @abstractmethod
    def num_of_ladders(self):
        pass
