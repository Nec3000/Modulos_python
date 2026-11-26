from abc import ABC, abstractmethod


class Creature(ABC):
    _name: str
    _type: str

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self._name} is a {self._type} type Creature"


class Flameling(Creature):
    def __init__(self):
        self._name = "Flameling"
        self._type = "Fire"

    def attack(self):
        return f"{self._name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self):
        self._name = "Pyrodon"
        self._type = "Fire/Flying"

    def attack(self):
        return f"{self._name} uses Flamethrower!"


class TransformCapability(ABC):
    def __init__(self):
        self._transformed = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__()
        self._name = "Shiftling"
        self._type = "Normal"

    def attack(self):
        if not self._transformed:
            return f"{self._name} attacks normally"
        return f"{self._name} performs a boosted strike!"

    def transform(self):
        if not self._transformed:
            self._transformed = True
            return f"{self._name} shifts into a sharper form!"
        return "Alredy transformed"

    def revert(self):
        if self._transformed:
            self._transformed = False
            return f"{self._name} returns to normal."
        return "Alredy detransformed"


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__()
        self._name = "Morphagon"
        self._type = "Normal/Dragon"

    def attack(self):
        if not self._transformed:
            return f"{self._name} attacks normally"
        return f"{self._name} unleashes a devastating morph strike!"

    def transform(self):
        if not self._transformed:
            self._transformed = True
            return f"{self._name} morphs into a dragonic battle form!"
        return "Alredy transformed"

    def revert(self):
        if self._transformed:
            self._transformed = False
            return f"{self._name} stabilizes its form."
        return "Alredy detransformed"


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):
    def create_base(self):
        return Flameling()

    def create_evolved(self):
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self):
        return Shiftling()

    def create_evolved(self):
        return Morphagon()
