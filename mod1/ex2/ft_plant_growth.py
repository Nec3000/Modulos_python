class Plant:
	def __init__(self, name : str, height : int, days : int):
		self.name = name
		self.height = height
		self.days = days
		self.growth = 0
	def show(self):
		print(f"{self.name}: {self.height :.1f}cm, {self.days} days old")
	def age(self):
		self.days += 1
	def grow(self):
		self.height += round(len(self.name) / 10, 1)
		self.growth += round(len(self.name) / 10, 1)
print("=== Garden Plant Growth ===")
p1 = Plant("Rose", 25, 30)
p1.show()
for i in range (1, 8):
	print(f"=== Day {i} ===")
	p1.grow()
	p1.age()
	p1.show()
print(f"Growth this week: {p1.growth}cm")