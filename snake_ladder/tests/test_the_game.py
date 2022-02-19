from snake_ladder.entry.initiate_game import GameSetup
from copy import deepcopy
from rich import print as rprint, print_json
from rich.console import Console
import json
from uuid import uuid4

console = Console()

simulation_count = 3

g = GameSetup(num_of_snakes=18, num_of_ladders=3)
player_list = g.generate_player_list(num_of_players=3)

for i in range(0, simulation_count):
    game_stat = g.start_game(str(uuid4()), deepcopy(player_list))
    print_json(json.dumps(game_stat.__dict__))
    print('', end='\n')
