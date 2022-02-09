from collections import deque
from distutils import dep_util
from random import randrange

from faker import Faker
from snake_ladder.controllers.play_game import GameController
from snake_ladder.domain_models.player import Player

from copy import deepcopy

no_of_players = randrange(2, 5)
player_queue = deque()
fake = Faker()
Faker.seed(4321)

for player in range(1, no_of_players+1):
        fake_first_name, fake_last_name = fake.name().split(' ')
        p = Player(player_id=player,
                   first_name=fake_first_name,
                   last_name=fake_last_name,
                   age = randrange(18,50),
                   address = fake.address(),
                   mobile_number = fake.phone_number()
                   )
        player_queue.append(p)

player_queue_copy = deepcopy(player_queue)

number_of_simulations = 5
game_controller = GameController()
game_controller.dice_count = 1
game_controller.num_of_snakes = 13
game_controller.num_of_ladders = 9
game_controller.assign_snake_paths()
game_controller.assign_ladder_paths()

for i in range(0, number_of_simulations):

    print(f'simulation number {i}')
    player_queue = deepcopy(player_queue_copy)
    while player_queue:
        player = player_queue.popleft()
        player_state = game_controller.play_game(player)
        if player_state.is_winner == False:
            player_queue.append(player)
        if player.is_winner == True:
            print(
                f'player id: {player.player_id} full_name: {player.full_name} pos: {player.pos} winning status: {player.is_winner}')
