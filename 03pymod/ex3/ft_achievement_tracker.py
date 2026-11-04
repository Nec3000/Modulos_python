import random

def gen_player_achievements(achievements : list[str]) -> set[str]:
	res = set()
	for i in range(random.randint(2, len(achievements))):
		res.add(achievements[random.randint(0, len(achievements) - 1)])
	return res
def main():
	achievements = [
			'Crafting Genius',
			'Strategist',
			'World Savior',
			'Speed Runner',
			'Survivor',
			'Master Explorer',
			'Treasure Hunter',
			'Unstoppable',
			'First Steps',
			'Collector Supreme'
			'Untouchable',
			'Sharp Mind',
			'Boss Slayer'
	]
	alice = gen_player_achievements(achievements)
	bob = gen_player_achievements(achievements)
	charlie = gen_player_achievements(achievements)
	dylan = gen_player_achievements(achievements)
	total_all = alice | bob | charlie | dylan
	common_all = alice & bob & charlie & dylan
	only_alice = alice - (bob | charlie | dylan)
	only_bob = bob - (alice | charlie | dylan)
	only_charlie = charlie - (bob | alice | dylan)
	only_dylan = dylan - (bob | charlie | alice)
	missing_alice = (bob | charlie | dylan) - alice
	missing_bob = (alice | charlie | dylan) - bob
	missing_charlie = (bob | alice | dylan) - charlie 
	missing_dylan = (bob | charlie | alice) - dylan

	print("=== Achievement Tracker System ===")
	print("")
	print(f"Player Alice: {alice}")
	print(f"Player Bob: {bob}")
	print(f"Player Charlie: {charlie}")
	print(f"Player Dylan: {dylan}")
	print("")
	print(f"All distinct achievements: {total_all}")
	print(f"Common achievements: {common_all}")
	print("")
	print(f"Only Alice has: {only_alice}")
	print(f"Only Bob has: {only_bob}")
	print(f"Only Charlie has: {only_charlie}")
	print(f"Only Dylan has: {only_dylan}")
	print("")
	print(f"Alice is missing: {missing_alice}")
	print(f"Bob is missing: {missing_bob}")
	print(f"Charlie is missing: {missing_charlie}")
	print(f"Dylan is missing: {missing_dylan}")
main()