#!env/bin/python
import os
import sys
import json
import argparse
from time import time
from git import Repo, FetchInfo


BASE_PROCESSORS_DIR = "./processors"
CONFIG_FILE = "config.json"
LOG_DIR = "./logs"
OUT_DIR = "./out"
DEVICE = "GW1NR-LV9QN88PC6/I5"


def open_config_file() -> dict[str, any]:
    print(f"Log: Opening {CONFIG_FILE} file")

    if not os.path.isfile(CONFIG_FILE):
        sys.exit(f"[ {time()} ] Error: {CONFIG_FILE} file not found.")

    file = open(CONFIG_FILE, "r")

    data: dict[str, any] = json.load(file)

    file.close()

    print(f"Log: {CONFIG_FILE} file opened successfully.")

    return data


def checks_yosys_synthesis_test_and_generates_compiled_file(
    name: str, folder: str, files: list[str], cstfile: str
) -> None:
    print(f"Log: run yosys cli")

    yosys_command_str: str = ""

    for i in files:
        yosys_command_str += f"read_verilog {i}; "

    yosys_command_str += f"synth_gowin -json {OUT_DIR}/{folder}.json"

    print(f"Log: synthesizing verilog")

    os.system(
        f"yosys -p '{yosys_command_str}' -d -t -q -l {LOG_DIR}/log-{folder}.txt > {LOG_DIR}/{folder}-execution-result.txt"
    )

    if not os.path.isfile(f"{OUT_DIR}/{folder}.json"):
        sys.exit(f"[ {time()} ] Error: Unable to generate {folder}.json file")

    print(f"Log: make pnr")

    os.system(
        f"nextpnr-gowin --json {OUT_DIR}/{folder}.json \
              --write {OUT_DIR}/pnr{folder}.json \
              --device {DEVICE} \
              --cst {cstfile}"
    )

    if not os.path.isfile(f"{OUT_DIR}/pnr{folder}.json"):
        sys.exit(
            f"[ {time()} ] Error: Unable to generate pnr{folder}.json file")

    print(f"Log: generating fs")

    os.system(
        f"gowin_pack -d {DEVICE} -o {OUT_DIR}/{folder}.fs {OUT_DIR}/pnr{folder}.json"
    )

    if not os.path.isfile(f"{OUT_DIR}/{folder}.fs"):
        sys.exit(f"[ {time()} ] Error: Unable to generate {folder}.fs file")


def check_processor_repository(name: str, repository: str, folder: str) -> None:
    path = os.path.join(BASE_PROCESSORS_DIR, folder)

    repo = None

    if not os.path.exists(path):
        print(f"Log: cloning repository")
        repo = Repo.clone_from(repository, path)
    else:
        print(f"Log: Opening repository")
        repo = Repo(path)

    print(f"Log: Updating repository")
    repo.git.pull()


def check_and_clone_repositories(data: dict[str, any]) -> None:
    print(f"Log: Pulling changes from repositories")
    if not "cores" in data:
        sys.exit(f"[ {time()} ] Error: cores key not found in config file")

    for i, core in enumerate(data["cores"]):
        if not core["enable"]:
            continue
        name: str = core["name"]
        repository: str = core["repository"]
        folder: str = core["folder"]
        files: list[str] = core["files"]
        cstfile: str = core["cstfile"]

        print(f"Log: updating repository {i} processor: {name}")

        check_processor_repository(name, repository, folder)

        checks_yosys_synthesis_test_and_generates_compiled_file(
            name, folder, files, cstfile
        )


def main() -> None:
    data: dict[str, any] = open_config_file()
    check_and_clone_repositories(data)


if __name__ == "__main__":
    main()
