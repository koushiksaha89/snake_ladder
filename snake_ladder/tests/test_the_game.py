from snake_ladder.entry.initiate_game import GameSetup
from copy import deepcopy

# todo : clear the player stat after each round
simulation_count = 8

g = GameSetup(num_of_snakes=15, num_of_ladders=13)
player_list = g.generate_player_list(num_of_players=3)

for i in range(0, simulation_count):
    winner_of_the_game = g.start_game(10, deepcopy(player_list))
    print(
        f'winner of the game {winner_of_the_game.full_name} for simulation id: {i}')
