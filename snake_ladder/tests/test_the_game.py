from snake_ladder.entry.initiate_game import GameSetup

g = GameSetup(num_of_snakes=15, num_of_ladders=13)
g.generate_player_list(num_of_players=5)
winner_of_the_game = g.start_game(10)

print(f'winner of the game {winner_of_the_game.__dict__}')
