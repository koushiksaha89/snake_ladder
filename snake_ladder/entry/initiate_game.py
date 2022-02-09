from random import randrange
from snake_ladder.controllers.play_game import GameController
from snake_ladder.domain_models.player import Player
from faker import Faker
from collections import deque
from itertools import chain
Faker.seed(4321)
from collections import OrderedDict


class GameSetup:

    def __init__(self,
                 num_of_snakes,
                 num_of_ladders,
                 dice_count=1,
                 board_size=100) -> None:

        super().__init__()
        self._game_controller = GameController(board_size)
        self._game_controller.dice_count = dice_count
        self._game_controller.num_of_snakes = num_of_snakes
        self._game_controller.num_of_ladders = num_of_ladders
        self._game_controller.assign_snake_paths()
        self._game_controller.assign_ladder_paths()
        self._fake = Faker()

    def generate_player_list(self, num_of_players):

        _player_queue = deque()
        for player in range(1, num_of_players+1):
            fake_first_name, fake_last_name = self._fake.name().split(' ')
            p = Player(player_id=player,
                       first_name=fake_first_name,
                       last_name=fake_last_name,
                       age=randrange(18, 50),
                       address=self._fake.address(),
                       mobile_number=self._fake.phone_number()
                       )
            _player_queue.append(p)

        return _player_queue

    def start_game(self, game_id, player_queue):

        if len(player_queue) <= 0:
            raise Exception('Player list is empty')

        turn_num = 1
        num_of_players = len(player_queue)
        sides_in_a_turn = 0
        while player_queue:
            sides_in_a_turn += 1
            player = player_queue.popleft()
            player = self._game_controller.play_game(player, turn_num)

            if player.is_winner == True:

                player_climbs_amts = list(chain.from_iterable(d.items()
                                 for d in player.climb_amount_history))
                player_climbs_amts = [x[1] for x in player_climbs_amts]
                player_climbs_amts = list(chain.from_iterable(player_climbs_amts))
                player.min_amount_of_climb = min(player_climbs_amts) if len(
                    player_climbs_amts) > 0 else 0
                player.max_amount_of_climb = max(player_climbs_amts) if len(
                    player_climbs_amts) > 0 else 0
                player.avg_amount_of_climb = sum(
                    player_climbs_amts) / len(player_climbs_amts) if sum(player_climbs_amts) != 0 else 0


                player_slide_amts = list(chain.from_iterable(d.items()
                                 for d in player.slide_amount_history))
                player_slide_amts = [x[1] for x in player_slide_amts]
                player_slide_amts = list(chain.from_iterable(player_slide_amts))
                player.min_amount_of_slide = min(player_slide_amts) if len(
                    player_slide_amts) > 0 else 0
                player.max_amount_of_slide = max(player_slide_amts) if len(
                    player_slide_amts) > 0 else 0
                player.avg_amount_of_slide = sum(
                    player_slide_amts) / len(player_slide_amts) if sum(player_slide_amts) != 0 else 0


                player.game_id = game_id

                # turn_no_vs_climb_map
                climb_flatten = list(chain.from_iterable(d.items() for d in player.climb_amount_history))
                climb_flatten_map = {j[0]: sum(j[1]) for j in climb_flatten}
                climb_flatten_map = OrderedDict(sorted(climb_flatten_map.items(), key=lambda item: -item[1]))
                player.biggest_climb_in_a_single_turn = list(climb_flatten_map.values())[0]

                slide_flatten = list(chain.from_iterable(d.items() for d in player.slide_amount_history))
                slide_flatten_map = {j[0]: sum(j[1]) for j in slide_flatten}
                slide_flatten_map = OrderedDict(sorted(slide_flatten_map.items(), key=lambda item: -item[1]))
                player.biggest_slide_in_a_single_turn = list(slide_flatten_map.values())[0]

                break

            else:
                if sides_in_a_turn == num_of_players:
                    turn_num += 1
                    sides_in_a_turn = 0
                player_queue.append(player)

        return player
