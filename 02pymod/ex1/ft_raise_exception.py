def input_temperature(temp_str : str):
	temp = int(temp_str)
	if temp < 0:
		raise ValueError(f"{temp}ºC is too cold for plant (min 0ºC)")
	if temp > 40:
		raise ValueError(f"{temp}ºC is too hot for plant (max 40ºC)")
	return temp
def test_temperature():
	for test in ["25", "abc", "100", "-50"]:
		try:
			print(f"Input data is '{test}'")
			input_temperature(test)
			print(f"Temperature is now {test}°C")
		except ValueError as e:
			print(f"Caught input_temperature error: {e}")
		finally:
			print("")
test_temperature()