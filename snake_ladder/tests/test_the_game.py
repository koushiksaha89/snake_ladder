from snake_ladder.entry.initiate_game import GameSetup
from copy import deepcopy
from rich import print as rprint
from rich.console import Console

console = Console()

# todo : clear the player stat after each round
simulation_count = 5

g = GameSetup(num_of_snakes=18, num_of_ladders=3)
player_list = g.generate_player_list(num_of_players=3)

for i in range(0, simulation_count):
    winner_of_the_game = g.start_game(i, deepcopy(player_list))
    console.log(
        f'winner of the game {winner_of_the_game.full_name} {winner_of_the_game.mobile_number} for simulation id: {i}')
