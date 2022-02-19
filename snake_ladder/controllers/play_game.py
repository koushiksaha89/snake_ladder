from snake_ladder.domain_models.board import Board
from snake_ladder.domain_models.board_objects import BoardObjecs
from snake_ladder.domain_models.player import Player


class GameController(Board):

    def __init__(self,
                 board_size) -> None:

        super().__init__(board_size=board_size)

    def play_game(self, player: Player):

        sub_turn = 0
        player_turn_metrics = []

        while True:
            turn_metrics_dict = dict()
            sub_turn += 1
            ladder_loc = None
            snake_loc = None
            confirmed_location = None
            tentative_location = None

             # rolling the dice and recording the dice vs sub-turn count
            dice_value = self.roll_the_dice()
            turn_metrics_dict['starting_loc'] = player.pos
            turn_metrics_dict['sub_turn_number'] = sub_turn
            turn_metrics_dict['sub_turn_dice_value'] = dice_value

            # getting the tentative location after dice roll
            tentative_location = confirmed_location = player.pos + dice_value
            turn_metrics_dict['tentative_loc'] = tentative_location
            # tentative location should be with-in the current board size
            if tentative_location <= self.board_end_loc:
                ladder_loc = self.ladder_map.get(tentative_location)
                snake_loc = self.snake_map.get(tentative_location)

                # check for ladder existence
                if ladder_loc is not None:
                    confirmed_location = ladder_loc
                    turn_metrics_dict['object_kind'] = BoardObjecs.LADDER

                # check for snake existence
                if snake_loc is not None:
                    confirmed_location = snake_loc
                    turn_metrics_dict['object_kind'] = BoardObjecs.SNAKE

                if snake_loc is None and ladder_loc is None:
                    turn_metrics_dict['object_kind'] = None

                # updating player location to confirmed location
                player.pos = confirmed_location

                # updating the winnning status of the player
                player.is_winner = True if confirmed_location == self.board_end_loc else False

            else:
                turn_metrics_dict['object_kind'] = None

            turn_metrics_dict['confirm_loc'] = player.pos
            player_turn_metrics.append(turn_metrics_dict)

            # when the confirmed_location if beyond the board size the dice value is less than 6
            if confirmed_location > self.board_end_loc and dice_value < 6:
                break

            # when dice value is less than 6 and player has already won
            if dice_value < 6 or player.is_winner == True:
                break

        return player, player_turn_metrics

    def update_stats_for_a_player(self,
                                  player,
                                  turn_num,
                                  turn_metrics):

        climb_turn_dict = {turn_num: list()}
        slide_turn_dict = {turn_num: list()}
        single_turn_steaks = {turn_num: list()}
        player_rolled_six_at_first_turn = True if turn_metrics[
            0]['sub_turn_dice_value'] == 6 else False

        for each_turn_metrics in turn_metrics:

            sub_turn_no = each_turn_metrics['sub_turn_number']
            dice_value = each_turn_metrics['sub_turn_dice_value']
            object_kind = each_turn_metrics['object_kind']

            # Misses a snake by 1 or 2 steps
            snake_in_next_location = self.snake_map.get(dice_value + 1)
            snake_in_next_next_location = self.snake_map.get(
                dice_value + 2)
            if snake_in_next_location is not None or snake_in_next_next_location is not None:
                player.total_no_of_lucky_rolls += 1

            if object_kind is BoardObjecs.LADDER:
                amount_of_climb = each_turn_metrics['confirm_loc'] - \
                    each_turn_metrics['starting_loc']
                climb_turn_dict[turn_num].extend([amount_of_climb])
                player.total_no_of_lucky_rolls += 1

            if object_kind is BoardObjecs.SNAKE:
                amount_of_slide = each_turn_metrics['tentative_loc'] - \
                    each_turn_metrics['confirm_loc']
                slide_turn_dict[turn_num].extend([amount_of_slide])
                player.total_no_of_unlucky_rolls += 1

            if player_rolled_six_at_first_turn == True and len(turn_metrics) > 1 and sub_turn_no > 1:
                single_turn_steaks[turn_num].extend([dice_value])

            # When they roll the exact number needed to win after 94 in a single roll
            if each_turn_metrics['starting_loc'] > 94 and len(turn_metrics) == 0 and each_turn_metrics['confirm_loc'] == self.board_end_loc:
                player.total_no_of_lucky_rolls += 1

        player.total_number_of_dice_rolls = player.total_number_of_dice_rolls + \
            len(turn_metrics)

        if list(climb_turn_dict.values())[0] != []:
            player.climb_amount_history.append(climb_turn_dict)
        if list(slide_turn_dict.values())[0] != []:
            player.slide_amount_history.append(slide_turn_dict)
        if list(single_turn_steaks.values())[0] != []:
            player.turn_history_6.append(single_turn_steaks)
