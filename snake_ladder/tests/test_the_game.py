import json
from copy import deepcopy
from uuid import uuid4

from rich import print, print_json
from snake_ladder.entry.initiate_game import GameSetup


def test_the_game():
    try:
        g = GameSetup(num_of_snakes=30, num_of_ladders=8)
        player_list = g.generate_player_list(num_of_players=3)
        simulation_count = 3
        for _ in range(0, simulation_count):
            game_stat = g.start_game(str(uuid4()), deepcopy(player_list))
            print_json(json.dumps(game_stat.__dict__))
            print('', end='\n')
        assert True

    except Exception as e:
        assert False


def test_snake_ladder_number_assignment():

    number_of_snake = 22
    number_of_ladder = 8
    snake_game = GameSetup(num_of_ladders=number_of_ladder,
                           num_of_snakes=number_of_snake)
    if len(snake_game.game_controller.snake_map) == number_of_snake and len(snake_game.game_controller.ladder_map) == number_of_ladder:
        assert True
    else:
        assert False

def test_snake_ladder_assignment():
    # no two cell can have snake and ladder
    number_of_snake = 22
    number_of_ladder = 8
    snake_game = GameSetup(num_of_ladders=number_of_ladder,
                           num_of_snakes=number_of_snake)

    snake_starting_points = set(snake_game.game_controller.snake_map.keys())
    ladder_starting_points = set(snake_game.game_controller.ladder_map.keys())
    intersection_starting_points = snake_starting_points.intersection(ladder_starting_points)

    if len(intersection_starting_points) == 0:
        assert True
    else:
        assert False
