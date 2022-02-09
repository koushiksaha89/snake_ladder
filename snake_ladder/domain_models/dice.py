from abc import ABC, abstractmethod

class Dice(ABC):

    def __init__(self) -> None:
        super().__init__()
        self._no_of_dice = None
        self.dice_name = None
    
    @property
    @abstractmethod
    def dice_count(self):
        pass

    @dice_count.setter
    @abstractmethod
    def dice_count(self, dice_count):
        pass

    @abstractmethod
    def roll_the_dice(self, current_location):
        pass