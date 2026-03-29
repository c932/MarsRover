# 火星车超简操作卡

这份卡片是给孩子直接照着做的。

目标只有两个：

1. 让 Pico 成功运行程序。
2. 让小车电机按顺序动起来。

## 第 1 步：连接 Pico

1. 用 USB 数据线把 Pico 连到电脑。
2. 打开 VS Code。
3. 打开这个项目文件夹。

如果 Pico 连不上，先检查数据线是不是能传数据。

## 第 2 步：连接 MicroPico

1. 按 `Ctrl+Shift+P`。
2. 输入 `MicroPico: Connect`。
3. 如果成功，终端里通常会出现 `>>>`。

`>>>` 表示 Pico 已经准备好接收 Python 命令。

## 第 3 步：先试灯

1. 打开 blink.py。
2. 按 `Ctrl+Shift+P`。
3. 输入 `MicroPico: Run current file on Pico`。
4. 看 Pico 的 LED 是否闪 5 次。

如果 LED 会闪，说明开发环境基本正常。

## 第 4 步：上传整个项目

1. 按 `Ctrl+Shift+P`。
2. 输入 `MicroPico: Upload project to Pico`。

为什么要先上传整个项目：

- 因为 main.py 会用到 motor.py。
- 如果不上传整个项目，main.py 可能找不到 motor.py。

## 第 5 步：测试电机

1. 打开 main.py。
2. 按 `Ctrl+Shift+P`。
3. 输入 `MicroPico: Run current file on Pico`。
4. 观察小车是不是按这个顺序动作：

- 前进
- 后退
- 左转
- 右转

main.py 默认只跑一轮，所以比较安全。

## 第 6 步：停止程序

如果程序还在运行：

1. 点击 `MicroPico vREPL` 终端。
2. 按 `Ctrl+C`。

如果看到 `>>>`，说明程序已经停下来了。

## 第 7 步：看懂项目里几个最重要的文件

- main.py：主程序，负责按顺序测试电机。
- motor.py：控制电机前进、后退、左转、右转、停止。
- blink.py：测试 LED。
- radar.py：以后学习超声波时再看。
- receiver.py：以后学习遥控接管时再看。

## 第 8 步：可以自己尝试改什么

1. 把 main.py 的动作时间改短一点或长一点。
2. 让 main.py 只测试前进和停止。
3. 把 blink.py 改成闪 10 次。
4. 给 motor.py 增加一个新动作。

## 第 9 步：遇到问题先检查什么

### 问题 1：连不上 Pico

先检查：

1. USB 线是不是数据线。
2. Pico 有没有刷 MicroPython 固件。
3. 有没有重新插拔过板子。

### 问题 2：main.py 报找不到 motor

先做：

1. 执行 `MicroPico: Upload project to Pico`。
2. 再重新运行 main.py。

### 问题 3：电机方向不对

做法：

1. 记下是哪一步方向不对。
2. 去修改 motor.py 对应函数。
3. 重新上传项目，再测试一次。

## 第 10 步：下一关学什么

当电机测试成功后，再开始学习：

1. 超声波测距
2. 遥控器接管
3. 自动避障

先把最基础的电机跑起来，就是很好的第一关。