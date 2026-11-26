import ex3 as e


def test_fact(f: e.CreatureFactory) -> None:
    print("Testing factory")
    base = f.create_base()
    evolved = f.create_evolved()
    print(base.describe())
    print(base.attack())
    print(evolved.describe())
    print(evolved.attack())
    print()


def test_battle(f1: e.CreatureFactory, f2: e.CreatureFactory) -> None:
    print("Testing battle")
    b1 = f1.create_base()
    b2 = f2.create_base()
    print(b1.describe())
    print(" vs.")
    print(b2.describe())
    print(" fight!")
    print(b1.attack())
    print(b2.attack())


def main() -> None:
    fire_fact = e.FlameFactory()
    test_fact(fire_fact)
    transf_fact = e.TransformCreatureFactory()
    test_fact(transf_fact)
    test_battle(fire_fact, transf_fact)


if __name__ == "__main__":
    main()
