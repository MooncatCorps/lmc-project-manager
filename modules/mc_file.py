import pathlib as pl
import tomllib as tl
import sys

def file_path() -> pl.Path:
    return pl.Path(".mooncat.toml")

def file_exists() -> bool:
    filepath = file_path()
    return filepath.exists() and filepath.is_file()

def create_file() -> None:
    with open(file_path(), "w") as file:
        file.write("[project]\nname = \"none\"")

def get_file_data() -> dict:
    file = open(file_path(), "rb")
    data = tl.load(file)
    return data

# IO

def prompt_should_create_file() -> bool:
    sys.stderr.write(f"[ERR] Could not find {file_path()}\n")

    while True:
        val = input("[ASK] Create one now? [Y/n] ").lower()
        if val in ["y", "yes"] or not val:
            return True
        elif val in ["n", "no"]:
            return False
        else:
            continue

def report_non_existent_file():
    sys.stderr.write(f"[FATAL] Could not locate {file_path()}\n")

