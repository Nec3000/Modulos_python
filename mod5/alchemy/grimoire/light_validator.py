from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = light_spell_allowed_ingredients()
    msg = ("VALID" if any(ing in allowed for ing in ingredients.split())
           else "INVALID")
    return ingredients + "-" + msg
