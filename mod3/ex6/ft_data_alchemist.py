import random

players =  ['Alice',
            'bob',
			'Charlie',
			'dylan',
			'Emma',
			'Gregory',
			'john',
			'kevin',
			'Liam']
print(f"Initial list of players: {players}")
players_capitalized = [player.capitalize() for player in players]
print(f"New list with all names capitalized: {players_capitalized}")
players_only_cap = [player for player in players if player == player.capitalize()]
print(f"New list of capitalized names only: {players_only_cap}")
score_dict = {player : random.randint(0, 1000) for player in players}
print(f"Score dict: {score_dict}")
avg = round(sum(score_dict[player] for player in players) / len(score_dict), 2)
print(f"Score average is {avg}")
score_higher = {player : score_dict[player]
                for player in score_dict if score_dict[player] > avg}
print(f"High scores: {score_higher}")