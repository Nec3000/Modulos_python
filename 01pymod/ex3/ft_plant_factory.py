class Plant:
	def __init__(self, name : str, height : int, days : int):
		self.name = name
		self.height = height
		self.days = days
	def show(self):
		print(f"{self.name}: {self.height :.1f}cm, {self.days} days old")
	def age(self):
		self.days += 1
	def grow(self):
		self.height += round(len(self.name) / 10, 1)
p1 = Plant("Rose", 25, 30)
p2 = Plant("Oak", 200, 365)
p3 = Plant("Cactus", 5, 90)
p4 = Plant("Sunflower", 80, 45)
p5 = Plant("Fern", 15, 120)
print ("=== Plant Factory Output ===")
print("Created:", end=" ")
p1.show()
print("Created:", end=" ")
p2.show()
print("Created:", end=" ")
p3.show()
print("Created:", end=" ")
p4.show()
print("Created:", end=" ")
p5.show()