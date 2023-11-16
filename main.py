#!env/bin/python
import os
import sys
import json
import argparse
from time import time
from git import repo


BASE_PROCESSORS_DIR = "./processors"
CONFIG_FILE = "config.json"


def open_config_file() -> dict[str, any]:
    print(f"Log: Opening {CONFIG_FILE} file")

    if not os.path.isfile(CONFIG_FILE):
        sys.exit(f"[ {time()} ] Error: {CONFIG_FILE} file not found.")

    file = open(CONFIG_FILE, "r")

    data = json.load(file)

    file.close()

    print(f"Log: {CONFIG_FILE} file opened successfully.")

    return data


def check_and_clone_repositories(data: dict[str, any]):
    if not "cores" in data:
        sys.exit(f"[ {time()} ] Error: cores key not found in config file")

    for i, core in enumerate(data["cores"]):
        name = core["name"]
        repository = core["repository"]
        folder = core["folder"]
        files = core["files"]
        topModule = core["topModule"]
        print(name)


def main() -> None:
    data = open_config_file()
    check_and_clone_repositories(data)


if __name__ == "__main__":
    main()
