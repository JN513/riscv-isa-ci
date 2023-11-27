#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2019 Arnaud Durand <arnaud.durand@unifr.ch>
# Copyright (c) 2022 Martin Hubacek @hubmartin (Twitter)
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import *
from litex.build.lattice import LatticeECP5Platform
from litex.build.lattice.programmer import OpenOCDJTAGProgrammer

import os

# IOs ----------------------------------------------------------------------------------------------

_io = [
    # Clk / Rst
    ("clk25", 0, Pins("P3"), IOStandard("LVCMOS33")),
    ("rst_n", 0, Pins("AH1"), IOStandard("LVCMOS33")),
    ("reset", 0, Pins("A11"), IOStandard("LVCMOS25")),
    # Serial
    (
        "serial",
        0,
        Subsignal("rx", Pins("E1"), IOStandard("LVCMOS25")),  # LVCMOS25
        Subsignal("tx", Pins("E4"), IOStandard("LVCMOS25")),  # LVCMOS25
    ),
]

# Platform -----------------------------------------------------------------------------------------


class Platform(LatticeECP5Platform):
    default_clk_name = "clk25"
    default_clk_period = 1e9 / 25e6

    def __init__(self, toolchain="trellis", **kwargs):
        LatticeECP5Platform.__init__(
            self, "LFE5U-45F-6BG381C", _io, toolchain=toolchain, **kwargs
        )

    def request(self, *args, **kwargs):
        return LatticeECP5Platform.request(self, *args, **kwargs)

    def create_programmer(self):
        return OpenOCDJTAGProgrammer("openocd_evn_ecp5.cfg")

    def do_finalize(self, fragment):
        LatticeECP5Platform.do_finalize(self, fragment)
        self.add_period_constraint(self.lookup_request("clk25", loose=True), 1e9 / 25e6)
