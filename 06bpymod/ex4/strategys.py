from ex3._creatures import Creature, TransformCapability
from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, c: Creature) -> str:
        ...

    @abstractmethod
    def is_valid(self, c: Creature) -> bool:
        ...


class NormalStrategy(BattleStrategy):
    def act(self, c: Creature) -> str:
        return c.attack()

    def is_valid(self, c: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    class CreatureException(Exception):
        pass

    def act(self, c: Creature) -> str:
        if not isinstance(c, TransformCapability):
            raise self.CreatureException(
                f"Invalid Creature '{c._name}' for this aggressive strategy")
        return f"{c.transform()}\n{c.attack()}\n{c.revert()}"

    def is_valid(self, c: Creature) -> bool:
        return isinstance(c, TransformCapability)
