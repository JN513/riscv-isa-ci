module top (
    input wire clk25,
    input wire serial_rx,
    output wire serial_tx,
    output wire led_n0,
    output wire led_n1,
    output wire led_n2,
    output wire led_n3,
    output wire led_n4,
    output wire led_n5,
    input wire switch_n0,
    input wire switch_n1,
    input wire switch_n2,
    input wire switch_n3,
    input wire switch_n4,
    input wire switch_n5 // Sistema temporario, futuramente tais pinos podem ser simulados pela serial
);
    
core_top #(
    .CLK_HZ(25000000),
    .BIT_RATE(9600),
    .PAYLOAD_BITS(8)
) core (
    .clk(clk25),
    .serial_rx(serial_rx),
    .serial_tx(serial_tx),
    .led_n0(led_n0),
    .led_n1(led_n1),
    .led_n2(led_n2),
    .led_n3(led_n3),
    .led_n4(led_n4),
    .led_n5(led_n5),
    .switch_n0(switch_n0),
    .switch_n1(switch_n1),
    .switch_n2(switch_n2),
    .switch_n3(switch_n3),
    .switch_n4(switch_n4),
    .switch_n5(switch_n5)
);

endmodule
