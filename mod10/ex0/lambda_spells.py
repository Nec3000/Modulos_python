from typing import TypedDict


artifact = TypedDict('artifact', {
    "name": str,
    "power": int,
    "type": str
})
mage = TypedDict('mage', {
    "name": str,
    "power": int,
    "element": str
})
stat = TypedDict('stat', {
    "max_power": int,
    "min_power": int,
    "avg_power": float
})


def artifact_sorter(artifacts: list[artifact]) -> list[artifact]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[mage], min_power: int) -> list[mage]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[mage]) -> stat:
    if len(mages) == 0:
        return {
            "max_power": 0,
            "min_power": 0,
            "avg_power": 0.00
        }
    return {
        "max_power": (max(mages, key=lambda x: x["power"])["power"]),
        "min_power": (min(mages, key=lambda x: x["power"])["power"]),
        "avg_power": round(sum(map(lambda m: m["power"], mages))
                           / len(mages), 2)
    }


def main() -> None:
    print("\nTesting artifact sorter...")
    artifacts = [artifact({"name": "Ring", "power": 25, "type": "earth"}),
                 artifact({"name": "Staff", "power": 30, "type": "ice"}),
                 artifact({"name": "Orb", "power": 45, "type": "fire"})]
    mages = [mage({"name": "Yuno", "power": 25, "element": "air"}),
             mage({"name": "Gandalf", "power": 30, "element": "ice"}),
             mage({"name": "Julius", "power": 45, "element": "time"})]
    print("\nTesting artifact sorter...")
    print(f"Before sorting: {artifacts}")
    print(f"After sorting: {artifact_sorter(artifacts)}")
    print()
    print("Testing mage filter...")
    print(f"Before filter: {mages}")
    print(f"After filter: {power_filter(mages, 31)}")
    print()
    print("Testing spell transformer")
    print(f"Spells transformed: {spell_transformer(["fireball", "Wish"])}")
    print()
    print("Testing mage stats")
    print(f"Mage statistics: {mage_stats(mages)}")


if __name__ == "__main__":
    main()
