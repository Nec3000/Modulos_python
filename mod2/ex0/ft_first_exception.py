def input_temperature(temp_str : str):
	return int(temp_str)
def test_temperature():
	for test in [25, "abc"]:
		try:
			print(f"Input data is '{test}'")
			input_temperature(test)
			print(f"Temperature is now {test}°C")
		except ValueError as e:
			print(f"Caught input_temperature error: {e}")
		finally:
			print("")
test_temperature()