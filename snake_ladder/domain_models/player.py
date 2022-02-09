"""
test
"""
from snake_ladder.domain_models.person import Person


class Player(Person):
    """
    Test
    """

    def __init__(self, player_id,
                 first_name,
                 last_name,
                 age,
                 address,
                 mobile_number) -> None:

        super().__init__(first_name=first_name,
                         last_name=last_name,
                         age=age,
                         address=address,
                         mobile_number=mobile_number
                         )
        self.player_id = player_id
        self.pos = 0
        self.is_winner = None

    @property
    def full_name(self):
        """test
        """
        return f'{self.first_name} {self.last_name}'
