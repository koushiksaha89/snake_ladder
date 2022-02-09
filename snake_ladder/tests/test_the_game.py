from snake_ladder.entry.initiate_game import GameSetup

# todo : clear the player stat after each round
simulation_count = 5

g = GameSetup(num_of_snakes=15, num_of_ladders=13)
g.generate_player_list(num_of_players=5)

for i in range(0,simulation_count):
    winner_of_the_game = g.start_game(10)
    print(f'winner of the game {winner_of_the_game.full_name} for simulation id: {i}')
