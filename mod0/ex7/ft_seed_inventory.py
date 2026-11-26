def	ft_seed_inventory(type : str, quantity : int, units : str):
	if (units == "packets"):
		print(type.capitalize(), "seeds:", quantity, units, "available")
	elif (units == "grams"):
		print(type.capitalize(), "seeds:", quantity, units, "total")
	elif (units == "area"):
		print(type.capitalize(), "seeds: covers", quantity, "square meters")
	else:
		print("Unkown unit type")