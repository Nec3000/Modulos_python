import elements as e
from .elements import create_air, create_earth


def healing_potion() -> str:
    return ("Healing potion brewed with "
            f"'{create_earth()}' and '{create_air()}'")


def strength_potion() -> str:
    return ("Strength potion brewed with '"
            f"{e.create_fire()}' and '{e.create_water()}'")
