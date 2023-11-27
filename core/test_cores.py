import os
import sys
from time import time
from litex_boards.platforms import (
    sipeed_tang_nano_9k,
    sipeed_tang_nano_20k,
    lattice_ecp5_evn,
    lattice_ecp5_vip,
)
from platforms import ecp5_45f_platform
from migen import Module
from ios import *


def get_clk_name(board: str) -> str:
    if board == "tangnano20k":
        return "clk27"
    if board == "tangnano9k":
        return "clk27"
    if board == "ecp5_45f":
        return "clk25"

    return "clk"


def check_core(
    board: str,
) -> int:  # 0 - ok, 1 - erro ao sintetizar, 2 - erro de execução
    if not os.path.isfile("build/top.fs"):
        print("Core não sintetizado")
        return 1

    return 0


def build_core(name: str, board: str, files: list[str], constraints: list[str]) -> None:
    platform = None

    if board == "tangnano9k":
        platform = sipeed_tang_nano_9k.Platform()
        platform.add_extension(ios_tang_nano_9k)
    elif board == "ecp5_45f":
        platform = ecp5_45f_platform.Platform()
    else:
        platform = sipeed_tang_nano_20k.Platform()
        platform.add_extension(ios_tang_nano_20k)

    for constraint in constraints:
        if constraint == "clk":
            # platform.request(get_clk_name(board))
            continue
        else:
            platform.request(constraint)

    for file in files:
        platform.add_source(file)

    module = Module()

    platform.build(module)


def build_and_check_cores(data: dict[str, any], board: str = "tangnano20k") -> None:
    if not "cores" in data:
        sys.exit(f"[ {time()} ] Error: cores key not found in config file")

    for i, core in enumerate(data["cores"]):
        if not core["enable"]:
            continue
        name: str = core["name"]
        repository: str = core["repository"]
        folder: str = core["folder"]
        files: list[str] = core["files"]
        constraints: str = core["constraints"]

        print(f"Log: Testing repository {i + 1} processor: {name}")

        build_core(name, board, files, constraints)

        check_core(board)

        # os.rmdir("build")
