from litex.build.generic_platform import *

ios_tang_nano_20k = [
    ("clk", 0, Pins("4"), IOStandard("LVCMOS33")),
    ("reset", 0, Pins("88"), IOStandard("LVCMOS33")),
]

ios_tang_nano_9k = [
    ("clk", 0, Pins("4"), IOStandard("LVCMOS33")),
    ("reset", 0, Pins("88"), IOStandard("LVCMOS33")),
]
