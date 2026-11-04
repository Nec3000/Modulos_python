import sys

def parse(arg : str, inventory : dict[str, int]) -> tuple[str, int]:
	cleaned = arg.split(":")
	if len(cleaned) != 2:
		raise Exception(f"Error - invalid parameter {arg}")
	if cleaned[0] in inventory.keys():
		raise Exception(f"Redundant item {cleaned[0]} - discarding")
	return cleaned[0], int(cleaned[1])

def gen_inventory() -> dict[str, int]:
	inventory = dict()
	for arg in sys.argv[1:]:
		try:
			new = parse(arg, inventory)
			inventory.update([new])
		except ValueError as e:
			print(f"Quantity error for {arg.split(":")[0]}: {e}")
		except Exception as e:
			print(f"{e}")
	return inventory
def main() -> None:
	print("=== Inventory System Analysis ===")
	inventory = gen_inventory()
	if len(inventory) == 0:
		print(f"Empty inventory:(")
		return 
	l_inventory = list(inventory)
	print(f"Got inventory: {inventory}")
	print(f"Item list: {l_inventory}")
	total_items = sum(inventory.values())
	print(f"Total quantity of the {len(inventory)} items: {total_items}")
	max = l_inventory[0]
	min = l_inventory[0]
	for key in inventory.keys():
		if inventory[key] > inventory[max]:
			max = key
		if inventory[key] < inventory[min]:
			min = key
		percentil = round(inventory[key] / total_items * 100, 1)
		print(f"Item {key} represents: {percentil}%")
	print(f"Item most abundant: {max} with quantity {inventory[max]}")
	print(f"Item least abundant: {min} with quantity {inventory[min]}")
	inventory.update({"magic_item":1})
	print(f"Updated inventory: {inventory}")
main()