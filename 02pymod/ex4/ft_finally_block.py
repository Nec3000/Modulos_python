class GardenError(Exception):
	def __init__(self, message : str | None = None):
		super().__init__(message or "Unknown garden error")
class PlantError(GardenError):
	def __init__(self, message : str | None = None):
		super().__init__(message or "Unknown garden error")
def water_plant(plant_name : str):
	if (plant_name == plant_name.capitalize()):
		print(f"Watering {plant_name}: [OK]")
	else:
		raise PlantError(f"Invalid plant name to water: '{plant_name}'")
def test_watering_system(plants : list[str]):
	print("Testing valid plants...")
	try:
		for plant in plants:
			water_plant(plant)
	except PlantError as e:
		print(f"Caught PlantError: {e}")
		print(".. ending tests and returning to main")
	finally:
		print("Closing watering system")
test_watering_system(["Tomato", "Lettuce"])