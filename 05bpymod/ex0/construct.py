import sys
import os
import site


def in_enviroment() -> bool:
    return sys.base_prefix != sys.prefix


if __name__ == "__main__":
    is_env = in_enviroment()
    if is_env:
        msg = "The laboratory is sealed"
    else:
        msg = "You are working in the open"
    print(f"\nLABORATORY STATUS: {msg}\n")
    print(f"Current Python: {sys.executable}")
    print("Virtual Environment:", end=" ")
    if is_env:
        print(os.path.basename(sys.prefix))
        print("")
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system\n")
        print(f"Reagent installation path:\n{site.getsitepackages()}")
    else:
        print("None detected\n")
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.\n")
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
