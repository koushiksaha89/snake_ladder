
from abc import ABC


class PlayerStat(ABC):

    def __init__(self) -> None:

        super().__init__()

        self.total_number_of_dice_rolls = 0
        self.total_climbs = 0
        self.total_slides = 0
        self.biggest_climb_in_a_single_turn = 0
        self.biggest_slide_in_a_single_turn = 0
        self.longest_turn = 0
        self.total_no_of_unlucky_rolls = 0
        self.total_no_of_lucky_rolls = 0
