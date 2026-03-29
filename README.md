# MarsRover (MicroPython 教学项目)

这是一个给孩子学习 MicroPython 机器人开发的项目，目标是循序渐进完成“手动遥控 + 自动避障”。

## 项目核心目标

1. 手动控制：遥控器可控制前进、后退、左转、右转。
2. 自动模式：通过组合按键进入“自动前进 + 自动避障”。
3. 安全增强：手动前进遇障碍时可自动停止或绕行。

## 当前代码结构

- main.py：主程序（当前为教学测试入口）。
- mata.py：电机基础控制模块（已避开 motor 同名冲突）。
- receiver.py：遥控输入模块样例。
- radar.py：超声波测距模块样例。
- blink.py：环境连通测试（LED 闪烁）。

## GPIO 映射

电机（Mini L298N）：

- GP0: IN1
- GP1: IN2
- GP2: IN3
- GP3: IN4

超声波（HC-SR04）：

- GP14: Trig
- GP15: Echo

遥控接管输入：

- GP21: 后退
- GP20: 前进
- GP26: 右转
- GP22: 左转

## 快速开始

1. 新电脑先拉取仓库：
   - `git clone https://github.com/c932/MarsRover.git`
2. 连接 Pico 并确认已刷 MicroPython 固件。
3. 在 VS Code 里优先用右键菜单执行：
   - Initialize MicroPico project
   - Upload project to Pico
   - Run current file on Pico
4. 先运行 blink.py，再运行 main.py。

## 详细教程

完整从 0 到 1 教程（分章节 + 代码框架样例）请看：

- TUTORIAL_0_TO_1.md

## 其他文档

- LESSON_PLAN.md：分阶段教学计划。