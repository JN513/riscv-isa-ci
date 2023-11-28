import os
import sys
import argparse
from core.config_manager import open_config_file
from core.repository_manager import (
    check_and_clone_repositories,
    BASE_PROCESSORS_DIR,
)
from core.test_cores import build_and_check_cores
from litex.build.generic_toolchain import GenericToolchain
from litex_patch import _build

from core.test_cores import sipeed_tang_nano_20k, Module


GenericToolchain.build = _build

platform = sipeed_tang_nano_20k.Platform()
# platform.add_extension(ios_tang_nano_20k)
platform.request("serial")
platform.request("led_n",1)
# platform.request("reset")
# platform.request("clk")

platform.add_source("rtl/uart_controler.v")
platform.add_source("rtl/uart_tx.v")
platform.add_source("rtl/uart_rx.v")

# platform.add_source("hello-word-tang-nano-20k.v")

platform.add_source("processors/stell/hardware/uart.v")
platform.add_source("processors/stell/hardware/ram-memory.v")
platform.add_source("processors/stell/hardware/system-bus.v")
platform.add_source("processors/stell/hardware/rvsteel-core.v")
platform.add_source("processors/stell/hardware/rvsteel-soc.v")

module = Module()

platform.build(module)


def main() -> None:
    data: dict[str, any] = open_config_file()
    # check_and_clone_repositories(data)

    build_and_check_cores(data)


if __name__ == "__main":
    if not os.path.exists(BASE_PROCESSORS_DIR):
        os.mkdir(BASE_PROCESSORS_DIR)

    GenericToolchain.build = _build

    main()
