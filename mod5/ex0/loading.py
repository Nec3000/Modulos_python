#!/usr/bin/env python3

import importlib.util
from importlib.metadata import version


def is_installed(name: str) -> bool:
    if importlib.util.find_spec(name) is None:
        return False
    return True


def imp(to_import: str, msg: str) -> bool:
    if is_installed(to_import):
        __import__(to_import)
        print(f"[OK] {to_import} {version(to_import)} - {msg}")
        return True
    return False


def main() -> None:
    print("\nREAGENT STATUS: Loading reagents...\n")
    print("Checking dependencies:")
    p_ok = imp("pandas", "Data manipulation ready")
    n_ok = imp("numpy", "Numerical computation ready")
    print("")
    if not p_ok:
        print("Missing: pandas")
    if not n_ok:
        print("Missing: numpy")
    if not n_ok or not p_ok:
        print("\nTo install with pip: pip install -r requirements.txt")
        print("To install with pip: poetry install\n")
    print('''pip vs Poetry:
    requirements.txt declares what to install; pip resolves it at install time.
    pyproject.toml declares the same constraints, and Poetry pins the resolved
    versions in poetry.lock so every install is identical''')
    if n_ok and p_ok:
        print("\nAll reagents present and accounted for.")


if __name__ == "__main__":
    main()
