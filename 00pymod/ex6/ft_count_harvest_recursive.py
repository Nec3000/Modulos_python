def	print_days(day : int, days : int):
	if (day <= days):
		print("Day:", day)
		print_days(day + 1, days)
	else:
		print("Harvest time!")

def	ft_count_harvest_recursive():
	days = int(input("Days until harvest: "))
	print_days(1, days)