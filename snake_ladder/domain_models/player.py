"""
test
"""


class Player:
    """
    Test
    """

    def __init__(self, player_id, first_name, last_name) -> None:
        super().__init__()
        self.player_id = player_id
        self.first_name = first_name
        self.last_name = last_name
        self.pos = 0
        self.is_winner = None
    
    @property
    def full_name(self):
        """test
        """
        return f'{self.first_name} {self.last_name}'
