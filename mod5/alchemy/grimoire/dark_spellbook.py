from .dark_validator import validate_ingredients as v_i


def dark_spell_allowed_ingredients() -> list[str]:
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    return f"Spell recorded: {spell_name} ({v_i(ingredients)})"
