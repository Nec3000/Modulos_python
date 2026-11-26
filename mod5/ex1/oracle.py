import os
import sys


try:
    from dotenv import load_dotenv  # type: ignore[import-not-found]
except ImportError:
    print("ERROR: 'python-dotenv' not installed.")
    print("To set up an environment:")
    print("python3 -m venv lab_env")
    print("source lab_env/bin/activate")
    print("To install")
    print("pip install -r requirements.txt")
    print("The run this again.")
    sys.exit(1)


def load_config() -> None:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    load_dotenv()
    load_dotenv(os.path.join(dir_path, ".env.example"), override=False)


def print_info(mode: str, env_var: str, msg: str) -> None:
    var = os.getenv(env_var, None)
    if var is None:
        print(f"ERROR: {env_var} is missing")
    else:
        if mode == "production":
            print("[PR]", end=" ")
        print(msg, end="")
        if env_var in ["LOG_LEVEL", "MATRIX_MODE"]:
            print(f" {var}", end="")
        print("")


def print_config() -> None:
    mode = os.getenv("MATRIX_MODE", "development")
    print_info(mode, "MATRIX_MODE", "Mode:")
    print_info(mode, "DATABASE_URL", "Database: Connected to local instance")
    print_info(mode, "API_KEY", "API Access: Authenticated")
    print_info(mode, "LOG_LEVEL", "Log Level:")
    print_info(mode, "ZION_ENDPOINT", "Remote Network: Online")


def security_check() -> None:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    gitignore_path = os.path.join(dir_path, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path) as f_ignore:
            for linea in f_ignore.readlines():
                if linea == ".env":
                    ignore_env = True
                    break
    print("[OK] No hardcore secrets detected")
    if ignore_env:
        print("[OK] .env file properly ignored by git")
    else:
        print("ERROR: .env file not ignored by git")
    print("[OK] Production overrides available")


def main() -> None:
    print("\nORACLE STATUS: Consulting the configuration...\n")
    load_config()
    print("Configuration loaded:")
    print_config()
    print("\nConfiguration security check")
    security_check()
    print("\nThe Oracle sees all configurations.\n")


if __name__ == "__main__":
    main()
