

class GameStat:

    def __init__(self,
                 instance_id) -> None:

        self.game_instance_id = instance_id

        min_number_of_rolls = None
        max_number_of_rolls = None
        avg_number_of_rolls = None

        min_amt_of_climbs = None
        max_amt_of_climbs = None
        avg_amt_of_climbs = None

        min_amt_of_slides = None
        max_amt_of_slides = None
        avg_amt_of_slides = None

        min_unlucky_rolls = None
        max_unlucky_rolls = None
        avg_unlucky_rolls = None

        min_lucky_rolls = None
        max_lucky_rolls = None
        avg_lucky_rolls = None
