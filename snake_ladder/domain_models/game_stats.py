class GameStats:

    def __init__(self) -> None:
        super().__init__()

        self.min_number_of_rolls_to_win = None
        self.max_number_of_rolls_to_win = None
        self.avg_number_of_rolls_to_win = None

        self.min_amount_of_climbs = None
        self.max_amount_of_climbs = None
        self.avg_amount_of_climbs = None
        
        self.min_amount_of_slides = None
        self.max_amount_of_slides = None
        self.avg_amount_of_slides = None

        self.biggest_climb_in_a_single_turn = None
        
        self.biggest_slide_in_a_single_turn = None

        self.longest_turn = None

        self.min_number_of_unlucky_rolls = None
        self.max_number_of_unlucky_rolls = None
        self.avg_number_of_unlucky_rolls = None

        self.min_number_of_lucky_rolls = None
        self.max_number_of_lucky_rolls = None
        self.avg_number_of_lucky_rolls = None