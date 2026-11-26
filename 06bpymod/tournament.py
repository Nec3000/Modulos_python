import ex4 as e4
import ex3 as e3


fact = e3.CreatureFactory
strategy = e4.BattleStrategy


def battle(opps: list[tuple[fact, strategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opps)} opponents involved\n")
    for i in range(len(opps)):
        for j in range(i + 1, len(opps)):
            print("* Battle *")
            f1, s1 = opps[i]
            f2, s2 = opps[j]
            op1 = f1.create_base()
            op2 = f2.create_base()
            print(op1.describe())
            print(" vs.")
            print(op2.describe())
            print(" now fight")
            try:
                print(s1.act(op1))
                print(s2.act(op2))
                print()
            except Exception as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    print("Tournament 0 (basic)")
    print(" [ (Flameling+Normal), (Shiftling+Aggressive) ]")
    fire = e3.FlameFactory()
    normal = e4.NormalStrategy()
    transf = e3.TransformCreatureFactory()
    agressive = e4.AggressiveStrategy()
    battle([(fire, normal), (transf, agressive)])
    print("Tournament 1 (error)")
    print("[ (Shiftling+Aggressive), (Flameling+Aggressive) ]")
    battle([(fire, agressive), (transf, agressive)])


if __name__ == "__main__":
    main()
