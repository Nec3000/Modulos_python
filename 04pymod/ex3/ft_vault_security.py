def secure_archive(fname : str, mode : str = "r", to_write : str | None = None) -> tuple[bool, str]:
    if mode != "r" and mode != "w":
        return False, "Invalid mode, try r (read) or w (write)"
    if mode == "w" and to_write is None:
        return False, "Error, nothing to write"
    try:
        with open(fname, mode) as f:
            if mode == "r":
                return True, f.read()
            else:
                f.write(to_write)
                return True, "Content successfully written to file"
    except Exception as e:
        return False, str(e)