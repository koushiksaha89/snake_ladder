from abc import ABC, abstractmethod
from collections import defaultdict


class Snake(ABC):

    def __init__(self) -> None:
        """test
        """
        super().__init__()
        self._no_of_snakes = None
        self.snake_map = defaultdict()

    @abstractmethod
    def assign_snake_paths(self):
        pass

    @property
    @abstractmethod
    def num_of_snakes(self):
        pass

    @num_of_snakes.setter
    @abstractmethod
    def num_of_snakes(self):
        pass
