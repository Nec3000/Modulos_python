from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    msg = ("VALID" if any(ing in allowed for ing in ingredients.split())
           else "INVALID")
    return ingredients + "-" + msg
