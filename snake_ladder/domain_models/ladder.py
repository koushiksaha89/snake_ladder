from abc import ABC, abstractmethod


class Ladder(ABC):

    def __init__(self) -> None:
        self._no_of_ladders = None
        self.ladder_map = None

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
