from random import randrange
from snake_ladder.controllers.play_game import GameController
from snake_ladder.domain_models.player import Player
from faker import Faker
from collections import deque
Faker.seed(4321)


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

                player.min_amount_of_climb = min(player.climb_amount_history) if len(player.climb_amount_history) else 0
                player.max_amount_of_climb = max(player.climb_amount_history) if len(player.climb_amount_history) else 0
                player.avg_amount_of_climb = sum(
                    player.climb_amount_history) / len(player.climb_amount_history) if player.max_amount_of_climb!=0 else 0

                player.min_amount_of_slide = min(player.slide_amount_history) if len(player.slide_amount_history) > 1 else 0
                player.max_amount_of_slide = max(player.slide_amount_history) if len(player.slide_amount_history) > 1 else 0
                player.avg_amount_of_slide = sum(
                    player.slide_amount_history) / len(player.slide_amount_history) if player.min_amount_of_slide !=0 else 0

                player.game_id = game_id
                break
            
            else:
                if sides_in_a_turn == num_of_players:
                    turn_num += 1
                    sides_in_a_turn = 0
                player_queue.append(player)
        
        return player
