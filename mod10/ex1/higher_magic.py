from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def comb(target: str, power: int) -> tuple[str, str]:
        return spell1(target, power), spell2(target, power)
    return comb


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def damage(target: str, power: int) -> str:
    return f"Damage {target} for {power} HP"


comb = spell_combiner(heal, damage)
print(comb("Nico", 67))
