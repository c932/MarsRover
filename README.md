# MicroPython 火星探测车教学版

这是一份面向初学者的上手指南，目标是让孩子从零开始学会以下内容：

1. 在 Windows 上安装 VS Code 和 MicroPython 开发环境。
2. 把 Raspberry Pi Pico 连接到电脑并刷入 MicroPython 固件。
3. 在 VS Code 中把代码上传到 Pico。
4. 运行、停止、调试最基本的 MicroPython 程序。
5. 先完成电机测试，再逐步扩展到超声波和遥控接管。

如果是第一次接触单片机，建议严格按本文顺序操作，不要一开始就同时接很多模块。

配套文档：

- QUICKSTART.md：给孩子直接使用的超简操作卡
- LESSON_PLAN.md：给家长或老师参考的分阶段教学计划

## 一、你需要准备什么

硬件：

- Raspberry Pi Pico 或 RP2040-Zero 一块
- 一根可以传输数据的 USB 线
- Windows 电脑一台
- 小车底盘、电机、电机驱动板
- 后续再接：HC-SR04 超声波、遥控接收板

软件：

- VS Code
- MicroPico 扩展
- Pico 的 MicroPython 固件

说明：

- 很多 USB 线只能充电，不能传数据。如果 VS Code 一直找不到 Pico，先怀疑数据线。
- 初学阶段，先只接 Pico 和 USB，确认环境通了，再接电机驱动。

## 二、安装 VS Code

1. 打开 VS Code 官网下载 Windows 安装包。
2. 正常安装即可，建议勾选“添加到右键菜单”和“注册 PATH”之类的常见选项。
3. 安装完成后启动 VS Code。

如果电脑里已经有 VS Code，可以直接进入下一步。

## 三、安装 MicroPico 插件

1. 打开 VS Code。
2. 点击左侧扩展按钮。
3. 搜索 MicroPico。
4. 安装 MicroPico 扩展。
5. 安装完成后重启 VS Code 更稳妥。

安装后，你通常会看到：

- 命令面板里多出很多 MicroPico 命令。
- 底部或侧边会出现和 Pico 连接相关的入口。
- 终端中可能会有 MicroPico vREPL 相关终端。

## 四、给 Pico 刷入 MicroPython 固件

这是最关键的一步。如果板子里没有 MicroPython 固件，后面的 Python 文件是跑不起来的。

### 方法 1：手动刷固件

1. 从 Raspberry Pi 官方网站下载 Pico 对应的 MicroPython 固件，文件后缀通常是 .uf2。
2. 断开 Pico。
3. 按住 Pico 上的 BOOTSEL 按钮不要松。
4. 再把 Pico 用 USB 线接到电脑上。
5. 电脑会把 Pico 识别成一个 U 盘。
6. 把刚才下载的 .uf2 文件拖进去。
7. 复制完成后，Pico 会自动重启并退出 U 盘模式。

### 方法 2：用扩展辅助

有些版本的 MicroPico 也提供固件刷写辅助命令，但不同版本界面不完全一致。初学阶段，手动拖入 .uf2 更可靠，也更容易理解发生了什么。

### 如何判断固件刷成功

满足下面任意一种，通常就说明成功了：

- VS Code 里的 MicroPico 能连接到 Pico。
- 在 REPL 里看到 `>>>` 提示符。
- 可以执行一条简单的 Python 语句，比如 `print("hello")`。

## 五、打开这个项目

1. 在 VS Code 里点击“打开文件夹”。
2. 选择当前项目文件夹。
3. 打开后，你应该能看到这些文件：

- main.py
- motor.py
- blink.py
- radar.py
- receiver.py

文件说明：

- main.py：电机测试主程序。
- motor.py：最基础的电机控制模块。
- blink.py：板载 LED 测试程序。
- radar.py：超声波样例骨架。
- receiver.py：遥控接管样例骨架。

## 六、初始化 MicroPico 项目

如果是第一次在这个文件夹里使用 MicroPico，建议做一次初始化。

1. 按 `Ctrl+Shift+P` 打开命令面板。
2. 输入 `MicroPico: Initialize MicroPico Project`。
3. 执行后，项目里通常会生成或更新 MicroPico 相关配置。

如果项目里已经有 .micropico 文件，说明它基本已经是一个 MicroPico 项目了。

## 七、连接 Pico

1. 用 USB 数据线把 Pico 接到电脑。
2. 在 VS Code 里按 `Ctrl+Shift+P`。
3. 输入 `MicroPico: Connect`。
4. 如果连接成功，通常会看到 REPL 终端，或者状态栏显示设备已连接。

如果连接失败，优先检查：

1. USB 线是不是数据线。
2. 是否已经刷入 MicroPython 固件。
3. 是否被别的串口工具占用了。
4. 是否需要重新插拔 Pico。

## 八、REPL 是什么

REPL 可以理解为 Pico 上的“交互式命令行”。

连接成功后，你通常会在终端看到：

```python
>>>
```

这表示你可以直接输入 Python 代码，让 Pico 立刻执行。例如：

```python
print("hello pico")
```

REPL 特别适合：

- 临时测试一条语句
- 检查模块是否能导入
- 单独测试某个函数
- 中断死循环后继续排查问题

## 九、最基本的运行方式

在 MicroPico 里，最常见有两种运行方式。

### 方式 1：Run current file on Pico

作用：只运行当前打开的这个文件。

适合：

- 测试单个示例
- 快速验证 blink.py 或 main.py

操作方法：

1. 打开你想运行的文件。
2. 按 `Ctrl+Shift+P`。
3. 输入 `MicroPico: Run current file on Pico`。

注意：

- 这种方式不一定会把所有依赖模块一起上传。
- 如果当前文件里有 `import motor`，而 Pico 板子上没有 `motor.py`，就会报 `ImportError`。
- 所以模块化项目更推荐先上传整个项目。

### 方式 2：Upload project to Pico

作用：把整个项目的文件上传到 Pico 文件系统中。

适合：

- 你的代码分成了多个文件
- 你要运行 `import motor` 这类模块化代码
- 你想让 Pico 上保存一整套项目文件

操作方法：

1. 按 `Ctrl+Shift+P`。
2. 输入 `MicroPico: Upload project to Pico`。
3. 等上传完成后，再运行 main.py 或直接重启 Pico。

建议：

- 只要项目里存在多个 `.py` 文件，优先使用“上传整个项目”。
- 改完多个文件后，再次上传一次，保证板子上的版本和电脑里一致。

## 十、先做哪个实验

建议按下面顺序做。

### 第一步：运行 blink.py

目的：确认 VS Code、MicroPico、Pico 之间通信正常。

操作：

1. 打开 blink.py。
2. 执行 `MicroPico: Run current file on Pico`。
3. 观察板载 LED 是否闪烁 5 次。
4. 看终端是否输出开始和结束提示。

如果 blink.py 都跑不通，先不要接电机，先把环境问题解决掉。

### 第二步：运行 main.py

目的：测试电机驱动和接线是否正确。

操作：

1. 确保电机驱动接线已经完成。
2. 先执行 `MicroPico: Upload project to Pico`。
3. 打开 main.py。
4. 再执行 `MicroPico: Run current file on Pico`。
5. 观察小车是否按顺序执行：前进、后退、左转、右转。

当前项目里，main.py 默认只跑一轮，更安全，适合初学测试。

## 十一、怎样停止程序

如果程序正在 Pico 上运行，最直接的停止方法是：

1. 点击 `MicroPico vREPL` 终端。
2. 按 `Ctrl+C`。

如果成功，你通常会看到：

```python
KeyboardInterrupt
>>>
```

其他常用控制：

- `Ctrl+C`：中断当前程序。
- `Ctrl+D`：软重启 Pico。

如果程序停不下来：

1. 尝试重新点击 REPL 终端后再按 `Ctrl+C`。
2. 尝试 `Ctrl+D` 软重启。
3. 最后再考虑重新插拔 USB。

## 十二、怎样调试

MicroPython 在 Pico 上通常不是像电脑 Python 一样用 F5 做完整断点调试。最常用的调试方法其实很朴素。

### 方法 1：看 print 输出

这是最常见、最有效的方式。

例如：

```python
print("开始前进")
motor.forward()
```

优点：

- 最容易理解
- 最适合初学者
- 最适合排查程序跑到哪一步

### 方法 2：在 REPL 里单独测试模块

例如测试电机：

```python
import motor
import time

motor.forward()
time.sleep(1)
motor.stop()
```

这比每次都运行整个 main.py 更适合排查某一个小问题。

### 方法 3：最小化测试

如果一个大程序跑不通，不要一上来就改很多地方。应该把问题缩小。

顺序建议：

1. 先测 blink.py。
2. 再测 motor.py 中的单个动作。
3. 再测 main.py 整体流程。
4. 最后才接入 radar.py 和 receiver.py。

### 方法 4：逐步增加硬件

不要一开始就同时连接：

- 电机
- 超声波
- 遥控器
- 电源模块

正确做法是：

1. 先 Pico + USB。
2. 再 Pico + LED 示例。
3. 再加电机驱动。
4. 再加超声波。
5. 最后再加遥控接管。

## 十三、这个项目当前的学习版结构

### 已经完成、可以直接运行的部分

- main.py：电机测试主程序
- motor.py：基础电机控制
- blink.py：LED 测试

### 只提供样例和引导的部分

- radar.py：保留了超声波接口、引脚和提示
- receiver.py：保留了遥控输入接口、引脚和提示

这是故意这样设计的，目的是让孩子自己完成后半部分，而不是直接拿一个全部写好的成品。

## 十四、GPIO 映射

### 电机控制

- GP0：左轮逻辑 1
- GP1：左轮逻辑 2
- GP2：右轮逻辑 1
- GP3：右轮逻辑 2

### 超声波雷达

- GP14：Trig
- GP15：Echo

### 遥控器接管

- GP21：后退
- GP20：前进
- GP26：右转
- GP22：左转

## 十五、常见错误和解决办法

### 1. ImportError: no module named 'motor'

原因：

- 只运行了当前文件，但没有把 motor.py 上传到 Pico。

解决：

1. 先执行 `MicroPico: Upload project to Pico`。
2. 再运行 main.py。

### 2. AttributeError: module object has no attribute 'forward'

原因：

- Pico 板子上可能残留了旧的 motor.py。

解决：

1. 重新上传整个项目。
2. 必要时清理 Pico 上旧文件后再上传。

### 3. 连接不上 Pico

优先检查：

1. 是否刷了 MicroPython 固件。
2. USB 线是否支持数据传输。
3. Pico 是否被别的软件占用。
4. 是否重新插拔过设备。

### 4. 电机方向不对

原因：

- 电机线顺序或 motor.py 的动作逻辑与实际安装方向不一致。

解决：

1. 先记录是哪一步反了。
2. 修改 motor.py 中对应函数的高低电平组合。
3. 重新上传项目并再次测试。

### 5. 程序卡住不动

常见原因：

- while True 没有 sleep
- 外设等待超时没有做好
- REPL 没有真正中断程序

解决思路：

1. 给循环加短暂 sleep。
2. 用 `Ctrl+C` 中断。
3. 缩小测试范围，从最小示例开始重测。

## 十六、推荐学习顺序

1. 安装 VS Code。
2. 安装 MicroPico。
3. 刷入 MicroPython 固件。
4. 连接 Pico，确认出现 `>>>`。
5. 运行 blink.py。
6. 上传整个项目。
7. 运行 main.py 测试电机。
8. 阅读 motor.py，尝试自己修改动作时间。
9. 补完 radar.py。
10. 补完 receiver.py。
11. 最终把 main.py 改造成自动避障加手动接管版本。

## 十七、适合孩子继续练习的任务

1. 把 main.py 改成只测试“前进”和“停止”。
2. 给 motor.py 增加一个新动作，比如原地旋转更久。
3. 在 blink.py 里改成闪烁 10 次。
4. 在 radar.py 里补完测距和超时逻辑。
5. 在 receiver.py 里写出完整的手动接管判断。
6. 把主程序从“电机测试”升级成“自动小车”。

## 十八、GitHub 同步开发指南

如果你希望两台电脑都能继续开发，或者保留历史版本，建议把项目放到 GitHub 仓库统一管理。

本项目远端仓库地址：

- https://github.com/c932/MarsRover

### 1. 第一次上传项目

在项目根目录打开 PowerShell，依次执行：

```powershell
git init
git branch -M main
git remote add origin https://github.com/c932/MarsRover.git
git add .
git commit -m "chore: initialize teaching version"
git push -u origin main
```

如果远端已经有提交历史，第一次推送可能被拒绝。可按下面“远端已有内容”步骤处理。

### 2. 日常提交流程

每次改完代码后，建议执行：

```powershell
git status
git add .
git commit -m "feat: update motor test"
git push
```

### 3. 另一台电脑同步最新代码

第一次在另一台电脑上：

```powershell
git clone https://github.com/c932/MarsRover.git
```

之后每次同步：

```powershell
git pull
```

### 4. 开发前先拉取，开发后再推送

推荐固定习惯：

1. 开工前先 `git pull`。
2. 修改代码并测试。
3. 提交 `git commit`。
4. 上传 `git push`。

### 5. 远端已有内容时的处理

如果出现“拒绝推送，远端有你本地没有的提交”，先拉取再推送：

```powershell
git pull --rebase origin main
git push origin main
```

如果 rebase 过程中有冲突：

1. 打开冲突文件并手动处理。
2. 处理后执行 `git add <冲突文件>`。
3. 执行 `git rebase --continue`。
4. 全部完成后再 `git push origin main`。

### 6. 常用检查命令

```powershell
git status
git log --oneline --decorate -n 10
git remote -v
git branch
```

### 7. 建议的提交信息模板

- feat: 新功能
- fix: 修复问题
- docs: 文档更新
- chore: 工程维护
- refactor: 重构

示例：

- `feat: add receiver command parser`
- `fix: correct motor turn direction`
- `docs: expand pico quickstart guide`