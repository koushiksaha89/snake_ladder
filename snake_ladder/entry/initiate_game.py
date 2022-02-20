from collections import OrderedDict, deque
from itertools import chain
from random import randrange

from faker import Faker
from snake_ladder.controllers.play_game import GameController
from snake_ladder.domain_models.game_stats import GameStats
from snake_ladder.domain_models.player import Player


class GameSetup:

    def __init__(self,
                 num_of_snakes,
                 num_of_ladders,
                 dice_count=1,
                 board_size=100) -> None:

        """
        init call for the game setup
        """
        super().__init__()
        self.game_controller = GameController(board_size)
        self.game_controller.dice_count = dice_count
        self.game_controller.num_of_snakes = num_of_snakes
        self.game_controller.num_of_ladders = num_of_ladders
        self.game_controller.assign_snake_paths()
        self.game_controller.assign_ladder_paths()
        self._fake = Faker('en_IN')

    def generate_player_list(self, num_of_players):
        """
        this generates player list for the passed num of players
        """
        _player_queue = deque()
        for player in range(1, num_of_players+1):
            fake_first_name = self._fake.first_name()
            fake_last_name = self._fake.last_name()
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

        """
        starts the game with game id and a player queue
        """

        if len(player_queue) <= 0:
            raise Exception('Player list is empty')

        turn_num = 1
        num_of_players = len(player_queue)
        sides_in_a_turn = 0
        won_player_list = []
        while player_queue:
            sides_in_a_turn += 1
            player = player_queue.popleft()
            player, turn_metrics = self.game_controller.play_game(
                player)
            player.game_id = game_id
            self.game_controller.update_stats_for_a_player(player,
                                                            turn_num,
                                                            turn_metrics)
            if sides_in_a_turn == num_of_players:
                turn_num += 1
                sides_in_a_turn = 0
            if player.is_winner is False:
                player_queue.append(player)
            else:
                won_player_list.append(self.get_player_stat(player))

        return self.get_game_stat(won_player_list, game_id)

    def get_player_stat(self, player):
        """
        this method gathers player wise stats
        """
        player_climbs_amts = list(chain.from_iterable(d.items()
                                                      for d in player.climb_amount_history))
        player_climbs_amts = [x[1] for x in player_climbs_amts]
        player_climbs_amts = list(
            chain.from_iterable(player_climbs_amts))
        player.min_amount_of_climb = min(player_climbs_amts) if len(
            player_climbs_amts) > 0 else 0
        player.max_amount_of_climb = max(player_climbs_amts) if len(
            player_climbs_amts) > 0 else 0
        player.avg_amount_of_climb = sum(
            player_climbs_amts) / len(player_climbs_amts) if sum(player_climbs_amts) != 0 else 0

        player_slide_amts = list(chain.from_iterable(d.items()
                                                     for d in player.slide_amount_history))
        player_slide_amts = [x[1] for x in player_slide_amts]
        player_slide_amts = list(
            chain.from_iterable(player_slide_amts))
        player.min_amount_of_slide = min(player_slide_amts) if len(
            player_slide_amts) > 0 else 0
        player.max_amount_of_slide = max(player_slide_amts) if len(
            player_slide_amts) > 0 else 0
        player.avg_amount_of_slide = sum(
            player_slide_amts) / len(player_slide_amts) if sum(player_slide_amts) != 0 else 0

        # turn_no_vs_climb_map
        climb_flatten = list(chain.from_iterable(
            d.items() for d in player.climb_amount_history))
        climb_flatten_map = {j[0]: sum(j[1]) for j in climb_flatten}
        climb_flatten_map = OrderedDict(
            sorted(climb_flatten_map.items(), key=lambda item: -item[1]))
        player.biggest_climb_in_a_single_turn = list(climb_flatten_map.values())[
            0] if len(climb_flatten_map) > 0 else 0

        slide_flatten = list(chain.from_iterable(
            d.items() for d in player.slide_amount_history))
        slide_flatten_map = {j[0]: sum(j[1]) for j in slide_flatten}
        slide_flatten_map = OrderedDict(
            sorted(slide_flatten_map.items(), key=lambda item: -item[1]))
        player.biggest_slide_in_a_single_turn = list(slide_flatten_map.values())[
            0] if len(slide_flatten_map) > 0 else 0

        max_value_when_turn_is_one = 0
        total_one_turn = 0
        for turn_history_6 in player.turn_history_6:
            for _, value in turn_history_6.items():
                if len(value) > len(player.longest_turn):
                    player.longest_turn = []
                    player.longest_turn.extend(value)
                if len(value) == 1:
                    total_one_turn += 1
                    max_value_when_turn_is_one = max(
                        max_value_when_turn_is_one, value[0])

        if len(player.turn_history_6) == total_one_turn:
            player.longest_turn = [max_value_when_turn_is_one]

        return player

    def get_game_stat(self, player_list, game_id):
        """
        this method collects all player individual stats and transform them into game stats
        """
        gs = GameStats()
        gs.min_number_of_rolls_to_win = min(
            [x.total_number_of_dice_rolls for x in player_list])
        gs.max_number_of_rolls_to_win = max(
            [x.total_number_of_dice_rolls for x in player_list])
        gs.avg_number_of_rolls_to_win = sum(
            [x.total_number_of_dice_rolls for x in player_list]) / len(player_list)

        gs.min_amount_of_climbs = min(
            [x.min_amount_of_climb for x in player_list])
        gs.max_amount_of_climbs = max(
            [x.max_amount_of_climb for x in player_list])
        gs.avg_amount_of_climbs = round(
            sum([x.avg_amount_of_climb for x in player_list]) / len(player_list), 2)

        gs.min_amount_of_slides = min(
            [x.min_amount_of_slide for x in player_list])
        gs.max_amount_of_slides = max(
            [x.max_amount_of_slide for x in player_list])
        gs.avg_amount_of_slides = round(
            sum([x.avg_amount_of_slide for x in player_list]) / len(player_list), 2)

        gs.biggest_climb_in_a_single_turn = max(
            [x.biggest_climb_in_a_single_turn for x in player_list])
        gs.biggest_slide_in_a_single_turn = max(
            [x.biggest_slide_in_a_single_turn for x in player_list])

        gs.min_number_of_unlucky_rolls = min(
            [x.total_no_of_unlucky_rolls for x in player_list])
        gs.max_number_of_unlucky_rolls = max(
            [x.total_no_of_unlucky_rolls for x in player_list])
        gs.avg_number_of_unlucky_rolls = round(
            sum([x.total_no_of_unlucky_rolls for x in player_list]) / len(player_list), 2)

        gs.min_number_of_lucky_rolls = min(
            [x.total_no_of_lucky_rolls for x in player_list])
        gs.max_number_of_lucky_rolls = max(
            [x.total_no_of_lucky_rolls for x in player_list])
        gs.avg_number_of_lucky_rolls = sum(
            [x.total_no_of_lucky_rolls for x in player_list]) / len(player_list)

        def sort_lists_by_maxes(*lists):
            return sorted(lists, key=lambda x: sorted(x, reverse=True), reverse=True)

        longest_turns = [x.longest_turn for x in player_list]
        gs.longest_turn = sort_lists_by_maxes(*longest_turns)[0]
        gs.game_id = game_id
        return gs
