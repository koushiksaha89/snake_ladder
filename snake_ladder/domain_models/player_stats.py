
from abc import ABC


class PlayerStat(ABC):

    def __init__(self) -> None:

        super().__init__()

        self.total_number_of_dice_rolls = None
        self.total_climbs = None
        self.total_slides = None
        self.biggest_climb_in_a_single_turn = None
        self.biggest_slide_in_a_single_turn = None
        self.longest_turn = None
        self.total_no_of_unlucky_rolls = None
        self.total_no_of_lucky_rolls = None
