#!/usr/bin/env python3

import sys
import os
import site


def in_enviroment() -> bool:
    return sys.base_prefix != sys.prefix


if __name__ == "__main__":
    is_env = in_enviroment()
    if is_env:
        msg = "The laboratory is sealed"
        curr = sys.executable
    else:
        msg = "You are working in the open"
        curr = os.path.realpath(sys.executable)
    print(f"\nLABORATORY STATUS: {msg}\n")
    print(f"Current Python: {curr}")
    print("Virtual Environment:", end=" ")
    if is_env:
        print(os.path.basename(sys.prefix))
        print(f"Environment Path: {sys.prefix}\n")
        print("SUCCESS: You are working in an isolated environment!")
        print("Safe to install reagents without affecting")
        print("the global system\n")
        print("Reagent installation path:")
        print(next(
            (p for p in site.getsitepackages() if p.endswith("site-packages")),
            site.getsitepackages()[0]))
    else:
        print("None detected\n")
        print("WARNING: You are in the global environment!")
        print("Every reagent you install here leaks into the whole system.\n")
        print("To seal the laboratory, run:")
        print("python3 -m venv lab_env")
        print("source lab_env/bin/activate # On Unix")
        print("lab_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
