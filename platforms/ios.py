from litex.build.generic_platform import *

ios_tang_nano_20k = [
    ("clk", 0, Pins("4"), IOStandard("LVCMOS33")),
    ("reset", 0, Pins("88"), IOStandard("LVCMOS33")),
]

ios_tang_nano_9k = [
    ("clk", 0, Pins("4"), IOStandard("LVCMOS33")),
    ("reset", 0, Pins("88"), IOStandard("LVCMOS33")),
    ("led_n", 0, Pins("10"), IOStandard("LVCMOS18")),
    ("led_n", 1, Pins("11"), IOStandard("LVCMOS18")),
    ("led_n", 2, Pins("13"), IOStandard("LVCMOS18")),
    ("led_n", 3, Pins("14"), IOStandard("LVCMOS18")),
    ("led_n", 4, Pins("15"), IOStandard("LVCMOS18")),
    ("led_n", 5, Pins("16"), IOStandard("LVCMOS18")),
]
