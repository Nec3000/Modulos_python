#!/usr/bin/env python3

import importlib.util
from importlib.metadata import version


def is_installed(name: str) -> bool:
    if importlib.util.find_spec(name) is None:
        print(f"Missing: {name}")
        print("To install with pip: pip -r requirements.txt")
        print("To install with pip: poetry install")
        return False
    return True


def imp(to_import: str, msg: str) -> None:
    if is_installed(to_import):
        __import__(to_import)
        print(f"[OK] {to_import} {version(to_import)} - {msg}")


imp("pandas", "Data manipulation ready")
imp("numpy", "Numerical computation ready")
