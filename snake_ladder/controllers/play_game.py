from collections import namedtuple
from snake_ladder.domain_models.board import Board
from snake_ladder.domain_models.player import Player


class GameController(Board):

    def __init__(self,
                 board_size=100) -> None:
        Board.__init__(self, board_size)

    def play_game(self, player: Player):

        # assumption: both ladder and snake does not exists at the same location

        while True:
            dice_value = self.roll_the_dice()
            tentative_location = confirmed_location = player.pos + dice_value

            if tentative_location <= self.board_end_loc:
                ladder_loc = self.ladder_map.get(tentative_location)
                snake_loc = self.snake_map.get(tentative_location)

                if ladder_loc is not None:
                    confirmed_location = ladder_loc

                if snake_loc is not None:
                    confirmed_location = snake_loc

                player.pos = confirmed_location
                player.is_winner = True if confirmed_location == self.board_end_loc else False

            if confirmed_location > self.board_end_loc and dice_value < 6:
                break

            if dice_value < 6 or player.is_winner == True:
                break
        return player
