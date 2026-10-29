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
