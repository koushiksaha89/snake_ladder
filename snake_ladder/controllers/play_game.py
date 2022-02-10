from snake_ladder.domain_models.board import Board
from snake_ladder.domain_models.player import Player


class GameController(Board):

    def __init__(self,
                 board_size) -> None:

        super().__init__(board_size=board_size)

    def play_game(self, player: Player, turn_num):
        # assumption: both ladder and snake does not exists at the same location
        # print(f'player_id {player.player_id} turn_no {turn_num}')
        climb_turn_dict = {turn_num : list()}
        slide_turn_dict = {turn_num : list()}
        player_rolled_six = None
        single_turn_steaks = {turn_num : list()}
        sub_turn = 0
        while True:
            
            dice_value = self.roll_the_dice()
            sub_turn += 1
            if dice_value == 6 and sub_turn == 1:
                player_rolled_six = True
            if player_rolled_six == True and sub_turn >1 :
                single_turn_steaks[turn_num].extend([dice_value])
            player.total_number_of_dice_rolls += 1
            tentative_location = confirmed_location = player.pos + dice_value
            if tentative_location <= self.board_end_loc:
                ladder_loc = self.ladder_map.get(tentative_location)
                snake_loc = self.snake_map.get(tentative_location)

                if ladder_loc is not None:
                    amount_of_climb = ladder_loc-tentative_location
                    climb_turn_dict[turn_num].extend([amount_of_climb])
                    confirmed_location = ladder_loc
                    player.total_no_of_lucky_rolls +=1

                if snake_loc is not None:
                    amount_of_slide = tentative_location-snake_loc
                    slide_turn_dict[turn_num].extend([amount_of_slide])
                    confirmed_location = snake_loc
                    player.total_no_of_unlucky_rolls +=1
                
                # Misses a snake by 1 or 2 steps
                snake_in_next_location = self.snake_map.get(tentative_location+1)
                snake_in_next_next_location = self.snake_map.get(tentative_location+2)
                if snake_in_next_location is not None or snake_in_next_next_location is not None:
                    player.total_no_of_lucky_rolls += 1

                # When they roll the exact number needed to win after 94 in a single roll
                if player.pos > 94 and player.after_94_roll_count == 0 and confirmed_location == self.board_end_loc:
                    player.total_no_of_lucky_rolls += 1
                    player.after_94_roll_count +=1
                
                if player.pos > 94:
                    player.after_94_roll_count +=1
                
                player.pos = confirmed_location
                player.is_winner = True if confirmed_location == self.board_end_loc else False

            if confirmed_location > self.board_end_loc and dice_value < 6:
                break

            if dice_value < 6 or player.is_winner == True:
                break
        
        if list(climb_turn_dict.values())[0] != []:
            player.climb_amount_history.append(climb_turn_dict)
        if list(slide_turn_dict.values())[0] != []:
            player.slide_amount_history.append(slide_turn_dict)
        if list(single_turn_steaks.values())[0] != []:
            player.turn_history_6.append(single_turn_steaks)

        return player
