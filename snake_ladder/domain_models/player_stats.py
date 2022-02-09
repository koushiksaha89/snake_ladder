
from abc import ABC


class PlayerStat(ABC):

    def __init__(self) -> None:

        super().__init__()
        self.game_id = None
        
        self.total_number_of_dice_rolls = 0
        
        self.min_amount_of_climb = 0
        self.max_amount_of_climb = 0
        self.avg_amount_of_climb = 0
        self.climb_amount_history = []
        
        self.min_amount_of_slide = 0
        self.max_amount_of_slide = 0
        self.avg_amount_of_slide = 0
        self.slide_amount_history = []
        
        self.biggest_climb_in_a_single_turn = 0
        self.biggest_slide_in_a_single_turn = 0
        
        self.longest_turn = 0
        
        self.total_no_of_unlucky_rolls = 0
        self.total_no_of_lucky_rolls = 0

        self.after_94_roll_count = 0
