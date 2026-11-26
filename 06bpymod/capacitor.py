import ex3 as e


def main() -> None:
    print("Testing Creature with transform capability")
    trans_fact = e.TransformCreatureFactory()
    base = trans_fact.create_base()
    evolved = trans_fact.create_evolved()
    print(" base")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())
    print(" evolved")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


if __name__ == "__main__":
    main()
