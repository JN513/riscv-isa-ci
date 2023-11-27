# RISC-V ISA CI

适用于 RISC-V 内核的 CI/CD

开发用于测试基于 RISC-V 架构的处理器的软件。该软件涵盖从 HDL 语言（Verilog 或 VHDL）的处理器综合到在 FPGA 上运行的处理器执行指令等测试。

# 实现部分

- [x] 从 GIT 存储库克隆和拉取
- [x] 核心/SoC 综合
- [ ] 不同 FPGA 引脚排列的标准化
- [ ] 合成过程验证
- [ ] FPGA 录制
- [ ] 带 FPGA 的串行调试器
- [ ] 执行指令
- [ ] 自动将内存文件发送到 FPGA
