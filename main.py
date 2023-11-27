import os
import sys
import argparse
from core.config_manager import open_config_file
from core.repository_manager import (
    check_and_clone_repositories,
    check_processor_repository,
    BASE_PROCESSORS_DIR,
)

"""
from migen import Module
from litex.build.generic_toolchain import GenericToolchain
from litex_boards.platforms import (
    sipeed_tang_nano_9k,
    sipeed_tang_nano_20k,
    lattice_ecp5_evn,
    lattice_ecp5_vip,
)
from platforms import ecp5_45f_platform
from litex_patch import _build
from ios import *
"""

# GenericToolchain.build = _build

# platform = ecp5_45f_platform.Platform()
# platform.add_extension(ios_tang_nano_20k)
# platform.request("serial")
# platform.request("reset")
# platform.request("clk")

# platform.add_source("hello-word-tang-nano-20k.v")
# platform.add_source("../../hardware/uart.v")
# platform.add_source("../../hardware/ram-memory.v")
# platform.add_source("../../hardware/system-bus.v")
# platform.add_source("../../hardware/rvsteel-core.v")
# platform.add_source("../../hardware/rvsteel-soc.v")

# module = Module()

# platform.build(module)


def main() -> None:
    data: dict[str, any] = open_config_file()
    check_and_clone_repositories(data)


if __name__ == "__main__":
    if not os.path.exists(BASE_PROCESSORS_DIR):
        os.mkdir(BASE_PROCESSORS_DIR)

    # GenericToolchain.build = _build

    main()
