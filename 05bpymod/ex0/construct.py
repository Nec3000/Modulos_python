import sys
import os


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
    os.path.basename(sys.prefix)