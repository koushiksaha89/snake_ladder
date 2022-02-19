from snake_ladder.entry.initiate_game import GameSetup
from copy import deepcopy
from rich import print as rprint
from rich.console import Console

console = Console()

simulation_count = 5

g = GameSetup(num_of_snakes=18, num_of_ladders=3)
player_list = g.generate_player_list(num_of_players=3)

for i in range(0, simulation_count):
    game_stat = g.start_game(i, deepcopy(player_list))
    console.log(
        f'game stat {game_stat.__dict__} for simulation id: {i}' ,end='\n\n')
