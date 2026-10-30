class Plant:
	def __init__(self, name : str, height : int, age : int):
		self.name = name
		self._height = 0
		self.set_height(self, height)
		self.age = 0
		self.set_age(self, age)
	def show(self):
		print(f"{self.name}: {self._height :.1f}cm, {self._age} age old")
	def age(self):
		self._age += 1
	def grow(self):
		self._height += round(len(self.name) / 10, 1)
	def get_height(self) -> int:
		return (self._height)
	def get_age(self) -> int:
		return (self._age)
	def set_height(self, new_height : int):
		if (new_height < 0):
			print(f"{self.name}: Error, height can't be negative")
			print("Height update rejected")
		else:
			self._height = new_height
			print(f"Height updated:: {self._height}cm")
	def set_age(self, new_age : int):
		if (new_age < 0):
			print(f"{self.name}: Error, age can't be negative")
			print("Age update rejected")
		else:
			self._age = new_age
			print(f"Age updated:: {self._age} days")
p1 = Plant("Rose", 25, 30)
p1.show()
p1.set_age(-1)
p1.set_age(2)
p1.age()
p1.set_height(44)
p1.set_height(-2)
p2 = Plant("Oak", 200, -365)
p2.show()