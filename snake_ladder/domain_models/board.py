from random import randrange
from collections import defaultdict
import random
from snake_ladder.domain_models.dice import Dice
from snake_ladder.domain_models.ladder import Ladder
from snake_ladder.domain_models.snake import Snake

from abc import abstractmethod

random.seed(10)

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
        # todo: while auto generating need to make sure start and end should not be same
        if self.snake_map is None:
            self.snake_map = defaultdict()
            while True:
                end_pos = randrange(1, divmod(self.board_end_loc, 2)[0])
                start_pos = randrange(end_pos, self.board_end_loc)
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
        # todo: while auto generating need to make sure start and end should not be same
        if self.ladder_map is None:
            self.ladder_map = defaultdict()
            while True:
                end_pos = randrange(1, divmod(self.board_end_loc, 2)[0])
                start_pos = randrange(end_pos, self.board_end_loc)
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
        dice_start_index = 0
        dice_end_index = self.dice_count * 6
        return randrange(dice_start_index, dice_end_index + 1)

    @abstractmethod
    def play_game(self):
        pass
