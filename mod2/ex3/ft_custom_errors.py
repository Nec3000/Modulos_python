class GardenError(Exception):
	def __init__(self, message : str | None = None):
		super().__init__(message or "Unknown garden error")
class PlantError(GardenError):
	def __init__(self, message : str | None = None):
		super().__init__(message or "Unknown garden error")
class WaterError(GardenError):
	def __init__(self, message : str | None = None):
		super().__init__(message or "Unknown garden error")

def raise_custom(error : str):
	match error:
		case "PlantError":
			raise PlantError("The tomato plant is wilting!")
		case "WaterError":
			raise WaterError("Not enough water in the tank!")
def test_custom():
	print("Testing PlantError...")
	try:
		raise_custom("PlantError")
	except PlantError as e:
		print(f"Caught PlantError: {e}")
	print("")
	print("Testing WaterError...")
	try:
		raise_custom("WaterError")
	except WaterError as e:
		print(f"Caught WaterError: {e}")
	print("")
	print("Testing catching all garden errors...")
	try:
		raise_custom("PlantError")
	except GardenError as e:
		print(f"Caught GardenError: {e}")
	try:
		raise_custom("WaterError")
	except GardenError as e:
		print(f"Caught GardenError: {e}")