class Plant:
	def __init__(self, name : str, height : int, age : int):
		self.name = name
		self._height = 0
		self.set_height(height)
		self.age = 0
		self.set_age(age)
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
class Flower(Plant):
	def __init__(self, name : str, height : int, age : int,
	             color : str) -> None:
		super().__init__(name, height, age)
		self.color = color
	def show(self) -> None:
		super().show()
		print(f" Color: {self.color}")
	def bloom(self) -> None:
		print(f"{self.name} is blooming beautifully!")
class Tree(Plant):
	def __init__(self, name : str, height : int, age : int,
	             t_diam : int) -> None:
		super().__init__(name, height, age)
		self.trunk_diameter = t_diam
	def show(self) -> None:
		super().show()
		print(f" Trunk diameter: {self.trunk_diameter :.1f}")
	def produce_shade(self) -> None:
		print(f"Tree {self.name} now produces a shade of", end=" ")
		print(f"{self.get_height():.1f}cm long and",end=" ") 
		print(f"{self.trunk_diameter:.1f}cm wide.")	
class Vegetable(Plant):
	def __init__(self, name : str, height : int, age : int,
	             hv_season : str, nutr_value : int) -> None:
		super().__init__(name, height, age)
		self.harvest_season = hv_season
		self.nutritional_value = nutr_value
	def show(self) -> None:
		super().show()
		print(f" Harvest season: {self.harvest_season}")
		print(f" Nutrional value : {self.nutritional_value}")
	def grow(self) -> None:
		super().grow()
		self.nutritional_value += 1
	def age(self)  -> None:
		super().age()
		self.nutritional_value += 1
print("=== Garden Plant Types ===")
f1 = Flower("Rose", 25, 30, "red")
f1.show()
f1.bloom()
t1 = Tree("Oak", 200, 30, 5)
t1.show()
t1.produce_shade()
v1 = Vegetable("tomato", 20 ,30, "Winter", 20)
v1.show()
for i in range(11):
	v1.grow()
v1.show()