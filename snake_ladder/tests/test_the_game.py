import json
from copy import deepcopy
from uuid import uuid4

import pytest
from rich import print, print_json
from snake_ladder.entry.initiate_game import GameSetup


@pytest.mark.parametrize("num_of_snakes,num_of_ladders,num_of_players,simulation_count", [(30, 8, 4, 1)])
def test_the_game(num_of_snakes,
                  num_of_ladders,
                  num_of_players,
                  simulation_count):
    try:
        g = GameSetup(num_of_snakes=num_of_snakes,
                      num_of_ladders=num_of_ladders)
        player_list = g.generate_player_list(num_of_players=num_of_players)

        max_amt_slide = 0
        biggest_snake_start = 0
        biggest_snake_end = 0
        for snake_start, snake_end in g.game_controller.snake_map.items():
            old_snake_max = max_amt_slide
            max_amt_slide = max(max_amt_slide, (snake_start-snake_end))
            if old_snake_max != max_amt_slide:
                biggest_snake_start = snake_start
                biggest_snake_end = snake_end

        max_amt_ladder = 0
        biggest_ladder_start = 0
        biggest_ladder_end = 0
        for ladder_start, ladder_end in g.game_controller.ladder_map.items():
            old_ladder_max = max_amt_ladder
            max_amt_ladder = max(max_amt_ladder, (ladder_end - ladder_start))
            if old_ladder_max != max_amt_ladder:
                biggest_ladder_start = ladder_start
                biggest_ladder_end = ladder_end

        print(
            f"max_amt_climb:{max_amt_ladder} biggest_ladder_start:{biggest_ladder_start} biggest_ladder_end:{biggest_ladder_end}")
        print(
            f"max_amt_slide:{max_amt_slide} biggest_snake_start:{biggest_snake_start} biggest_snake_end:{biggest_snake_end}")

        for _ in range(0, simulation_count):
            game_stat = g.start_game(str(uuid4()), deepcopy(player_list))
            print_json(json.dumps(game_stat.__dict__))
            print('', end='\n')
        assert True

    except Exception as e:
        assert False


@pytest.mark.parametrize("num_of_snakes,num_of_ladders", [(30, 8)])
def test_snake_ladder_number_assignment(num_of_snakes, num_of_ladders):

    number_of_snake = num_of_snakes
    number_of_ladder = num_of_ladders
    snake_game = GameSetup(num_of_ladders=number_of_ladder,
                           num_of_snakes=number_of_snake)
    if len(snake_game.game_controller.snake_map) == number_of_snake and len(snake_game.game_controller.ladder_map) == number_of_ladder:
        assert True
    else:
        assert False


@pytest.mark.parametrize("num_of_snakes,num_of_ladders", [(30, 8)])
def test_snake_ladder_assignment(num_of_snakes, num_of_ladders):
    # no two cell can have snake and ladder
    number_of_snake = num_of_snakes
    number_of_ladder = num_of_ladders
    snake_game = GameSetup(num_of_ladders=number_of_ladder,
                           num_of_snakes=number_of_snake)

    snake_starting_points = set(snake_game.game_controller.snake_map.keys())
    ladder_starting_points = set(snake_game.game_controller.ladder_map.keys())
    intersection_starting_points = snake_starting_points.intersection(
        ladder_starting_points)

    if len(intersection_starting_points) == 0:
        assert True
    else:
        assert False


@pytest.mark.parametrize("num_of_snakes,num_of_ladders", [(30, 8)])
def test_snake_head_leg_diff(num_of_snakes, num_of_ladders):
    number_of_snake = num_of_snakes
    number_of_ladder = num_of_ladders
    snake_game = GameSetup(num_of_ladders=number_of_ladder,
                           num_of_snakes=number_of_snake)
    for key, value in snake_game.game_controller.snake_map.items():
        if key - value < 0:
            assert False
        else:
            continue

    assert True


@pytest.mark.parametrize("num_of_snakes,num_of_ladders", [(30, 8)])
def test_ladder_start_end_diff(num_of_snakes, num_of_ladders):
    number_of_snake = num_of_snakes
    number_of_ladder = num_of_ladders
    snake_game = GameSetup(num_of_ladders=number_of_ladder,
                           num_of_snakes=number_of_snake)
    for key, value in snake_game.game_controller.ladder_map.items():
        if key - value > 0:
            assert False
        else:
            continue

    assert True


GAME_INPUTS = [
    [15, 8, 3, 4],
    [17, 7, 3, 3]
]


@pytest.fixture(params=GAME_INPUTS)
def set_up_the_game(request):
    g = GameSetup(
        num_of_snakes=request.param[0], num_of_ladders=request.param[1])
    player_list = g.generate_player_list(request.param[2])
    simulation_count = request.param[3]
    return g, player_list, simulation_count


def test_play_game(set_up_the_game):
    game_obj, player_list, simulation_count = set_up_the_game
    for _ in range(0, simulation_count):
        game_stat = game_obj.start_game(str(uuid4()), deepcopy(player_list))
        print_json(json.dumps(game_stat.__dict__))
        print('', end='\n')
    assert True
