import math

def convert_inp(arg: str) -> int | None:
	try:
		return round(float(arg), 1)
	except ValueError as e:
		print(f"Invalid parameter: {arg} : {e}")
		return None
def get_player_pos() -> tuple[float, float, float]:
	inp = input("Enter new coordinates as floats in format 'x,y,z': ")
	inp = inp.split(',')
	if (len(inp) != 3):
		print("Invalid syntax")
		return get_player_pos()
	coords = [coord for num in inp if (coord := convert_inp(num)) is not None]
	if len(coords) != 3:
		return get_player_pos()
	return coords
def calculate_distance(c1 : set[float], c2 : set[float]) -> float:
	return round(math.sqrt((c1[0] - c2[0])** 2 +
	                (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2), 4)
def main():
	print("=== Game Coordinate System ===")
	print("")
	print("Get a first set of coordinates")
	coords1 = get_player_pos()
	print(f"Got a first tuple: {coords1}")
	print(f"It includes: X={coords1[0]}, Y={coords1[1]}, Z={coords1[2]}")
	print(f"Distance to center: "
	      f"{calculate_distance(coords1, (0, 0, 0))})")
	print("")
	print("Get a second set of coordinates")
	coords2 = get_player_pos()
	print(f"Distance between the 2 sets of coordinates:"
	      f"{calculate_distance(coords1, coords2)}")
main()
