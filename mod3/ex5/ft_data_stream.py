import typing
import random

def gen_event(players : list[str], actions : list[str]) -> typing.Generator[tuple[str, str], None, None]:
	while True:
		yield random.choice(players), random.choice(actions)
def consume_event(list_events : list[tuple[str, str]]) -> typing.Generator[tuple[str, str], None, None]:
	while list_events:
		indx = random.randint(0, len(list_events) - 1)
		deleted = list_events[indx]
		del list_events[indx]
		yield deleted
print("=== Game Data Stream Processor ===")
players = [
	'Alice',
	'Bob',
	'Charlie',
	'Dylan'
]
actions = [
	'eat',
	'sleep',
	'move',
	'climb',
	'swim',
	'run',
	'grab',
	'release',
	'use'
]
gen = gen_event(players, actions)
for i in range(1000):
	player, action = next(gen)
	print(f"Event {i}: Player {player} did action {action}")
list_events = [next(gen) for _ in range(10)]
print(f"Built list of 10 events: {list_events}")
consumer = consume_event(list_events)
for event in consumer:
	print(f"Got event from list: {event}")
	print(f"Remains in list: {list_events}")