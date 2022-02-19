from abc import abstractmethod
from collections import defaultdict
from random import randrange

from snake_ladder.domain_models.dice import Dice
from snake_ladder.domain_models.ladder import Ladder
from snake_ladder.domain_models.snake import Snake


class Board(Ladder, Snake, Dice):

    def __init__(self, board_size) -> None:

        super().__init__()
        self.board_start_loc = 0
        self.board_end_loc = board_size

    @property
    def num_of_snakes(self):
        return self._no_of_snakes

    @num_of_snakes.setter
    def num_of_snakes(self, val):
        self._no_of_snakes = val

    def assign_snake_paths(self):
        if bool(self.snake_map) is False:
            while True:
                end_pos = randrange(1, divmod(self.board_end_loc, 2)[0])
                start_pos = randrange(end_pos, self.board_end_loc)
                if end_pos == start_pos or start_pos - end_pos <=5:
                    continue

                if self.ladder_map.get(start_pos) is not None or self.ladder_map.get(end_pos) is not None:
                    continue

                self.snake_map[start_pos] = end_pos

                if len(self.snake_map.keys()) >= self.num_of_snakes:
                    break

    @property
    def num_of_ladders(self):
        return self._no_of_ladders

    @num_of_ladders.setter
    def num_of_ladders(self, value):
        self._no_of_ladders = value

    def assign_ladder_paths(self):
        if bool(self.ladder_map) is False:
            while True:
                end_pos = randrange(1, divmod(self.board_end_loc, 2)[0])
                start_pos = randrange(end_pos, self.board_end_loc)
                if end_pos == start_pos or start_pos - end_pos <=5:
                    continue

                if self.snake_map.get(start_pos) is not None or self.snake_map.get(end_pos) is not None:
                    continue

                self.ladder_map[end_pos] = start_pos

                if len(self.ladder_map.keys()) >= self.num_of_ladders:
                    break

    @property
    def dice_count(self):
        return self._no_of_dice

    @dice_count.setter
    def dice_count(self, value):
        self._no_of_dice = value

    def roll_the_dice(self):
        dice_start_index = 1
        dice_end_index = self.dice_count * 6
        return randrange(dice_start_index, dice_end_index + 1)

    @abstractmethod
    def play_game(self):
        pass
