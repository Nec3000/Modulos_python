import sys

def parse(arg : str, inventory : dict[str, int]) -> tuple[str, int]:
	cleaned = arg.split(":")
	if len(cleaned) != 2:
		raise Exception(f"Error - invalid parameter {arg}")
	if cleaned[0] in inventory.keys():
		raise Exception(f"Redundant item {cleaned[0]} - discarding")
