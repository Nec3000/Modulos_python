from alchemy import grimoire

if __name__ == "__main__":
    print("=== Kaboom 0 ===")
    print("Using grimoire module directly")
    recorded = grimoire.light_spell_record(
        'Fantasy', 'Earth, wind and fire')
    print("Testing record light spell: ("
          f"{recorded})")
