#
# This file is part of LiteX-Boards.
#
# Copyright (c) 2019 Arnaud Durand <arnaud.durand@unifr.ch>
# Copyright (c) 2022 Martin Hubacek @hubmartin (Twitter)
# SPDX-License-Identifier: BSD-2-Clause

from litex.build.generic_platform import *
from litex.build.lattice import LatticeECP5Platform
from litex.build.openfpgaloader import OpenFPGALoader

import os

# IOs ----------------------------------------------------------------------------------------------

_io = [
    # Clk / Rst
    ("clk25", 0, Pins("P3"), IOStandard("LVCMOS33")),
    # Serial
    (
        "serial",
        0,
        Subsignal("rx", Pins("H18"), IOStandard("LVCMOS33")),
        Subsignal("tx", Pins("J17"), IOStandard("LVCMOS33")),
    ),
    ("led_n", 0, Pins("R3"), IOStandard("LVCMOS33")),
    ("led_n", 1, Pins("M4"), IOStandard("LVCMOS33")),
    ("led_n", 2, Pins("L5"), IOStandard("LVCMOS33")),
    ("led_n", 3, Pins("J16"), IOStandard("LVCMOS33")),
    ("led_n", 4, Pins("N4"), IOStandard("LVCMOS33")),
    ("led_n", 5, Pins("L4"), IOStandard("LVCMOS33")),
    ("led_n", 6, Pins("P16"), IOStandard("LVCMOS33")),
    ("led_n", 7, Pins("J18"), IOStandard("LVCMOS33")),
    ("btn_n", 0, Pins("R1"), IOStandard("LVCMOS33")),
    ("btn_n", 1, Pins("U1"), IOStandard("LVCMOS33")),
    ("btn_n", 2, Pins("W1"), IOStandard("LVCMOS33")),
    ("btn_n", 3, Pins("M1"), IOStandard("LVCMOS33")),
    ("btn_n", 4, Pins("T1"), IOStandard("LVCMOS33")),
    ("btn_n", 5, Pins("Y2"), IOStandard("LVCMOS33")),
    ("btn_n", 6, Pins("V1"), IOStandard("LVCMOS33")),
    ("btn_n", 7, Pins("N2"), IOStandard("LVCMOS33")),
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
        return OpenFPGALoader(cable="cmsisdap")

    def do_finalize(self, fragment):
        LatticeECP5Platform.do_finalize(self, fragment)
        self.add_period_constraint(self.lookup_request("clk25", loose=True), 1e9 / 25e6)
