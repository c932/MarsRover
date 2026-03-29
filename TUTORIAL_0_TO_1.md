# MarsRover 0 到 1 详细教程

本教程面向初学者，采用“每次只学一点、每次只加一个模块”的方式，帮助孩子一步步完成项目。

说明：

- 本文已合并原 QUICKSTART 内容。
- 你只需要按这一份文档学习和实践即可。

---

## 使用导航（先看这里）

如果时间有限，可以按下面顺序快速定位章节：

1. 新电脑拿代码：看第 2 章。
2. 连接和跑通 Pico：看第 1 章 + 第 3 章。
3. 跑电机：看第 4 章 + 第 5 章。
4. 做手动遥控：看第 6 章 + 第 7 章。
5. 做自动避障：看第 8 章 + 第 9 章。
6. 做手动防撞：看第 10 章。
7. 最终联调：看第 11 章 + 第 12 章。

---

## 右键菜单速查

本项目优先使用 VS Code 右键菜单，不要求孩子记复杂命令。

常用操作：

1. `Initialize MicroPico project`
2. `Upload project to Pico`
3. `Run current file on Pico`

如果右键里没有对应项，再使用 `Ctrl+Shift+P` 搜索同名命令。

最终要达成 3 个目标：

1. 手动控制前进、后退、左右。
2. 组合按键进入自动前进和自动避障。
3. 手动前进时遇障碍自动停止或绕行。

---

## 第 0 章：先认识 MicroPython 里的基础概念

原理讲解：

- Python 是编程语言，MicroPython 是它在单片机上的轻量版本。
- Pico 没有操作系统桌面，程序直接控制硬件引脚。
- 所以“会用库函数控制引脚”是这个项目最基础的能力。

### 0.1 machine 是什么

- machine 是 MicroPython 提供的硬件控制库。
- 你可以通过 machine 访问 GPIO、PWM、I2C、UART 等硬件资源。
- 在本项目里最常用的是 machine.Pin。

示例：

```python
from machine import Pin
```

这行的意思是：从 machine 库里拿到 Pin 这个类，后面就能创建引脚对象。

### 0.2 Pin 是什么

- Pin 可以理解为“一个可编程的电子开关接口”。
- 每个 GPIO 都对应一个 Pin 对象。
- Pin 最常见两种模式：
    - Pin.OUT：输出模式（程序控制高低电平）
    - Pin.IN：输入模式（程序读取高低电平）

示例：

```python
led = Pin("LED", Pin.OUT)
button = Pin(20, Pin.IN, Pin.PULL_DOWN)
```

含义：

- 第一行把板载 LED 配成输出。
- 第二行把 GP20 配成输入，并启用下拉，避免悬空抖动。

### 0.3 value() 有什么用

- value(1)：把输出引脚拉高（高电平）。
- value(0)：把输出引脚拉低（低电平）。
- value()：不带参数时，读取输入引脚当前值（通常是 0 或 1）。

示例：

```python
led.value(1)      # 点亮
led.value(0)      # 熄灭
state = button.value()  # 读取按键
```

### 0.4 sleep、sleep_us、ticks_us 是什么

- time.sleep(x)：延时 x 秒。
- time.sleep_us(x)：延时 x 微秒。
- time.ticks_us()：读取当前微秒计时值。
- time.ticks_diff(a, b)：安全计算两个计时值差，避免溢出问题。

为什么要它们：

- 电机动作需要持续一段时间，所以要 sleep。
- 超声波触发脉冲是微秒级，所以要 sleep_us。
- 超声波测距靠“时间差”，所以要 ticks_us 和 ticks_diff。

### 0.5 函数是什么，为什么要封装

- 函数是“可重复使用的一段命令”。
- 把 forward/backward 写成函数后，主程序像在读句子，便于理解。

示例：

```python
def forward():
        # 这里写前进动作
        pass
```

### 0.6 while True 为什么要加 sleep

- while True 是无限循环，会一直执行。
- 如果循环里不 sleep，CPU 会被占满，系统容易不稳定。
- 所以主循环末尾几乎都要加一个短暂 sleep。

通过标准：

1. 能解释 machine 和 Pin 各自负责什么。
2. 能说出 value(1)、value(0)、value() 的区别。
3. 能解释为什么超声波代码需要微秒和超时逻辑。

错误示例（反例）+ 为什么错：

```python
from machine import Pin
led = Pin(0, Pin.IN)  # 想点灯却设成输入
led.value(1)
```

- 错因 1：要控制输出设备，模式必须是 Pin.OUT。
- 错因 2：输入模式下调用 value(1) 不等于有效输出控制。

给孩子的提问卡（3 个问题）：

1. machine 库和 Pin 类分别负责什么？
2. 为什么 value() 有时带参数、有时不带参数？
3. 为什么 while True 里一般都要放一个短暂 sleep？

---

## 第 1 章：准备开发环境

原理讲解：

- Pico 本质是一台小电脑，但它不会自己“理解”你电脑里的代码。
- VS Code 负责写代码，MicroPico 负责把代码送到 Pico 上运行。
- REPL 里的 `>>>` 可以理解为“Pico 在等你发指令”。
- 先把工具链打通，后面每一章才不会被环境问题反复打断。

目标：

- 安装 VS Code 与 MicroPico。
- Pico 能在终端显示 `>>>`。

步骤：

1. 安装 VS Code。
2. 安装 MicroPico 插件。
3. 给 Pico 刷 MicroPython 固件（uf2）。
4. 用 USB 数据线连接 Pico。
5. 在 VS Code 右键菜单执行连接相关操作。

通过标准：

- 能看到 `MicroPico vREPL`。
- 能在 REPL 输入并执行：

```python
print("hello pico")
```

错误示例（反例）+ 为什么错：

```python
print("hello")
```

- 反例说明：只在电脑终端里运行这行，不代表 Pico 真的执行了代码。
- 错因：没有完成设备连接和上传链路验证，结论不成立。

给孩子的提问卡（3 个问题）：

1. 为什么我们要先看到 `>>>` 才继续？
2. VS Code、MicroPico、Pico 三者分别做什么？
3. 为什么环境没打通时不应该急着改业务代码？

---

## 第 2 章：获取项目并同步（GitHub）

原理讲解：

- GitHub 是“代码云端仓库”，Git 是“版本记录工具”。
- `clone` 是第一次把远端仓库完整下载到本地。
- `pull` 是先同步别人改过的内容，减少冲突。
- `commit + push` 是把自己本地改动提交并上传，方便两台电脑保持一致。

目标：

- 学会在新电脑拉取项目。
- 学会日常同步。

首次拉取：

```powershell
git clone https://github.com/c932/MarsRover.git
cd MarsRover
code .
```

日常同步流程：

```powershell
git pull
# 修改代码并测试
git add .
git commit -m "feat: update chapter task"
git push
```

通过标准：

- 能在另一台电脑拉取并运行同一项目。

错误示例（反例）+ 为什么错：

```powershell
git add .
git commit -m "update"
git push
```

- 反例说明：开工前不先 `git pull`，很容易在推送时冲突或覆盖别人更新。
- 错因：没有先同步远端历史，分支基线可能过期。

给孩子的提问卡（3 个问题）：

1. clone、pull、push 分别是什么动作？
2. 为什么开工前先 pull？
3. 为什么提交信息要写清楚？

---

## 第 3 章：先跑通最小程序（LED）

原理讲解：

- LED 是最简单、最直观的输出设备，适合做“系统自检”。
- `Pin("LED", Pin.OUT)` 表示把这个引脚当作输出口。
- `toggle()` 每执行一次就切换一次亮灭状态。
- 如果 LED 示例能跑通，说明“连接、上传、执行”这条链路是正常的。

关键函数解释：

- Pin("LED", Pin.OUT)：创建板载 LED 的输出引脚对象。
- led.toggle()：把 LED 状态在亮/灭之间切换一次。
- sleep(0.5)：暂停 0.5 秒，让肉眼能看到闪烁节奏。

目标：

- 证明代码可上传并执行。

操作：

1. 打开 `blink.py`。
2. 右键运行 `Run current file on Pico`。

基础 sample：

```python
from machine import Pin
from utime import sleep

led = Pin("LED", Pin.OUT)

for _ in range(5):
    led.toggle()
    sleep(0.5)
```

通过标准：

- LED 按预期闪烁。

错误示例（反例）+ 为什么错：

```python
for _ in range(5):
    led.toggle()
```

- 错因：没有 `sleep`，闪烁速度太快，肉眼几乎看不见变化。
- 结论：你可能误以为代码没跑，其实是跑得太快。

给孩子的提问卡（3 个问题）：

1. 为什么 LED 是最适合做第一步验证的硬件？
2. toggle 做了什么？
3. 如果把 sleep 从 0.5 改成 1.0，会看到什么变化？

---

## 第 4 章：完成电机基础模块（motor.py）

原理讲解：

- L298N 的每个电机通常由两路逻辑控制正反转。
- 同一侧电机的两个引脚一高一低，电机会按某方向转动。
- 两个都低时通常是停止状态（这里我们用作安全停车）。
- 把动作写成函数（forward/backward/...）是为了主程序可读、可复用。

关键函数解释：

- Pin(0, Pin.OUT)：把 GP0 配置为输出。
- left_in1.value(1)：给对应引脚输出高电平。
- left_in1.value(0)：给对应引脚输出低电平。
- stop()：把四路电机控制引脚都拉低，形成统一停车动作。

实现提醒：

1. 同一侧电机两路引脚不要同时置 1。
2. 每次改一个动作函数就上板测试一次。
3. 若前进方向反了，交换该侧前后逻辑即可。

目标：

- 写出前进、后退、左转、右转、停止。

代码框架 sample：

```python
from machine import Pin

# GPIO: GP0 GP1 GP2 GP3
left_in1 = Pin(0, Pin.OUT)
left_in2 = Pin(1, Pin.OUT)
right_in3 = Pin(2, Pin.OUT)
right_in4 = Pin(3, Pin.OUT)


def stop():
    left_in1.value(0)
    left_in2.value(0)
    right_in3.value(0)
    right_in4.value(0)


def forward():
    # TODO: 根据接线设置前进方向
    pass


def backward():
    # TODO: 根据接线设置后退方向
    pass


def turn_left():
    # TODO: 左轮后退 + 右轮前进
    pass


def turn_right():
    # TODO: 左轮前进 + 右轮后退
    pass
```

练习建议：

1. 先只实现 `forward()` 和 `stop()`。
2. 每次只改一个函数并上板验证。

错误示例（反例）+ 为什么错：

```python
def stop():
    left_in1.value(1)
    left_in2.value(1)
    right_in3.value(1)
    right_in4.value(1)
```

- 错因：不同驱动板对双高电平行为不一致，可能不是安全停车。
- 建议：本项目统一使用全低电平停车，行为更可控。

给孩子的提问卡（3 个问题）：

1. 为什么一个电机通常要两路逻辑控制？
2. 为什么 stop 要做成独立函数？
3. 如果前进方向反了，应该改接线还是改函数逻辑？

---

## 第 5 章：写一个电机测试主程序（main.py 第一版）

原理讲解：

- 主程序负责“调度”，电机模块负责“执行动作”。
- `run_step()` 是一个通用测试模板：执行动作 -> 等待 -> 停车。
- 每个动作后都 `motor.stop()`，可以避免动作之间相互干扰。
- 先做顺序测试能快速确认接线方向和动作映射是否正确。

关键函数解释：

- run_step(name, action, duration)：把“动作测试模板”抽象成函数。
- action()：调用传进来的动作函数（如 motor.forward）。
- motor.stop()：每一步结束后强制停车，避免连贯动作带来误判。
- try/except KeyboardInterrupt：允许按 Ctrl+C 时优雅停止。

目标：

- 按顺序测试四个动作。

代码框架 sample：

```python
import time
import motor


def run_step(name, action, duration=1.0):
    print("step:", name)
    action()
    time.sleep(duration)
    motor.stop()
    time.sleep(0.3)


try:
    run_step("forward", motor.forward)
    run_step("backward", motor.backward)
    run_step("left", motor.turn_left)
    run_step("right", motor.turn_right)
    print("done")
except KeyboardInterrupt:
    motor.stop()
```

通过标准：

- 四个动作都能执行。
- `Ctrl+C` 可安全停止。

错误示例（反例）+ 为什么错：

```python
motor.forward()
time.sleep(2)
motor.backward()
```

- 错因：动作切换之间没停车缓冲，可能出现突变冲击，不利于判断。
- 建议：每个动作后先 stop，再进入下一个动作。

给孩子的提问卡（3 个问题）：

1. run_step 为什么比直接顺写动作更好？
2. 为什么每一步后要 stop？
3. try/except KeyboardInterrupt 的意义是什么？

---

## 第 6 章：实现遥控输入（receiver.py）

原理讲解：

- 遥控接收板输出的是高低电平，程序需要把电平翻译成命令。
- `Pin.IN` 表示输入模式；`Pin.PULL_DOWN` 让“未按下”状态更稳定。
- `read_states()` 返回原始事实，`get_command()` 负责业务判断。
- 分层的好处是后续改规则时，不会影响底层读引脚代码。

关键函数解释：

- Pin(21, Pin.IN, Pin.PULL_DOWN)：把 GP21 设为输入并下拉。
- read_states()：返回“原始电平字典”，不做业务推断。
- get_command()：把多个电平组合翻译成一个高层命令。
- len(active)：判断当前有几个按键被激活。

目标：

- 读 4 路引脚。
- 把输入转换为命令字符串。

代码框架 sample：

```python
from machine import Pin

backward_pin = Pin(21, Pin.IN, Pin.PULL_DOWN)
forward_pin = Pin(20, Pin.IN, Pin.PULL_DOWN)
right_pin = Pin(26, Pin.IN, Pin.PULL_DOWN)
left_pin = Pin(22, Pin.IN, Pin.PULL_DOWN)


def read_states():
    return {
        "backward": backward_pin.value(),
        "forward": forward_pin.value(),
        "right": right_pin.value(),
        "left": left_pin.value(),
    }


def get_command():
    states = read_states()
    active = [k for k, v in states.items() if v]

    if len(active) == 1:
        return active[0]
    if len(active) > 1:
        return "stop"
    return None
```

通过标准：

- 单键能识别。
- 多键冲突返回 `stop`。

错误示例（反例）+ 为什么错：

```python
forward_pin = Pin(20, Pin.IN)
```

- 错因：未配置下拉时，输入引脚可能悬空抖动，读值不稳定。
- 建议：使用 `Pin.PULL_DOWN` 保证未按下时默认稳定为 0。

给孩子的提问卡（3 个问题）：

1. read_states 和 get_command 为什么要分开？
2. 为什么多键冲突时建议返回 stop？
3. PULL_DOWN 在这个项目里解决了什么问题？

---

## 第 7 章：做手动控制主循环（main.py 第二版）

原理讲解：

- 控制循环本质是“读输入 -> 决策 -> 执行 -> 短暂休眠”。
- `apply_manual_command()` 把字符串命令映射到电机函数，主循环会更清晰。
- `time.sleep(0.05)` 很关键，它让 CPU 休息并降低抖动。
- 没有命令时主动 `stop()`，可以避免小车因旧状态继续运动。

关键函数解释：

- receiver.get_command()：读到当前手动命令。
- apply_manual_command(cmd)：命令分发函数，统一处理动作映射。
- time.sleep(0.05)：循环降频，防止 CPU 占满和输出抖动。
- except KeyboardInterrupt：捕获人工中断并执行安全停车。

目标：

- 达成最终目标 1（手动四方向）。

代码框架 sample：

```python
import mata
import receiver
import time

ACTIONS = {
    "forward":  mata.forward,
    "backward": mata.backward,
    "left":     mata.turn_left,
    "right":    mata.turn_right,
    "stop":     mata.stop,
}

last_cmd = None

try:
    while True:
        cmd = receiver.get_command()

        if cmd != last_cmd:
            mata.stop()
            if cmd in ACTIONS:
                ACTIONS[cmd]()
                print(cmd)
            else:
                print("停止")
            last_cmd = cmd

        time.sleep_ms(50)
except KeyboardInterrupt:
    mata.stop()
    print("已停车，程序退出")
```

设计说明：

- `ACTIONS` 字典把命令字符串直接映射到函数，主循环不需要一堆 `if/elif`。
- 只在命令**变化时**才切换电机，避免反复发送相同指令。
- `time.sleep_ms(50)` 让轮询频率约 20 次/秒，响应灵敏且不占满 CPU。

通过标准：

- 遥控器能控制四方向。
- 松手后能停止。

错误示例（反例）+ 为什么错：

```python
while True:
    cmd = receiver.get_command()
    apply_manual_command(cmd)
```

- 错因：循环没有 sleep，CPU 占用过高，系统可能不稳定。
- 建议：在循环末尾加短延时，比如 `time.sleep_ms(50)`。

给孩子的提问卡（3 个问题）：

1. 主循环为什么是“读输入 -> 决策 -> 执行 -> 休眠”？
2. 为什么没有输入也要明确 stop？
3. 循环延时太短和太长分别有什么影响？

---

## 第 8 章：实现超声波测距（radar.py）

原理讲解：

- HC-SR04 的核心是“测时间差”：声波发出到回波返回的耗时。
- 距离由公式计算：`distance = 时间 * 声速 / 2`。
- `ticks_us()` 提供微秒级时间，适合这类短时间测量。
- 等待回波必须加超时，否则传感器异常时会把主循环卡死。

关键函数解释：

- trig.value(1) + sleep_us(10)：发送约 10 微秒触发脉冲。
- echo.value()：读取回波引脚电平。
- time.ticks_us()：获取微秒级时间戳。
- time.ticks_diff(now, start)：计算持续时间。
- return None：表示本次测距失败或超时，主程序应做容错处理。

计算说明：

- 声速约 0.0343 cm/us。
- 回波时间是“来回”时间，单程距离要除以 2。
- 所以 distance = pulse_us * 0.0343 / 2。

目标：

- 返回厘米距离。
- 带超时，避免卡死。

代码框架 sample（与 radar.py 实现一致）：

```python
from machine import Pin
import time

TRIG_PIN = 14
ECHO_PIN = 15

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)


def send_pulse():
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)


def get_distance():
    send_pulse()

    timeout = 30000

    # 等待 echo 升高（带超时）
    t0 = time.ticks_us()
    while echo.value() == 0:
        if time.ticks_diff(time.ticks_us(), t0) > timeout:
            return None  # 超时，无回波

    start = time.ticks_us()

    # 等待 echo 降低（带超时）
    while echo.value() == 1:
        if time.ticks_diff(time.ticks_us(), start) > timeout:
            return None  # 超时，物体太远或太近

    duration_us = time.ticks_diff(time.ticks_us(), start)
    distance_cm = duration_us * 0.0343 / 2
    return round(distance_cm, 1)
```

通过标准：

- 靠近障碍时数值明显减小。
- 无障碍时不会卡死。

错误示例（反例）+ 为什么错：

```python
while echo.value() == 0:
    pass
```

- 错因：没有超时保护，传感器异常时会无限等待。
- 建议：配合 ticks_us 和 ticks_diff 做超时返回。

给孩子的提问卡（3 个问题）：

1. 为什么超声波测距要用微秒级时间？
2. 为什么距离公式里要除以 2？
3. 为什么超时时返回 None 而不是随便给个数字？

---

## 第 9 章：组合按键进入自动模式

原理讲解：

- 项目需要“模式管理”，至少包含 MANUAL 和 AUTO 两种状态。
- 组合键相当于模式切换开关，比单键更不容易误触。
- AUTO 模式里仍然是循环决策：先看距离，再决定前进或避障。
- 避障动作通常是短动作序列：停 -> 退 -> 转 -> 再评估。

关键函数解释：

- mode 变量：保存当前工作模式（MANUAL 或 AUTO）。
- check_mode_switch(states)：读取组合键并返回模式切换结果。
- run_auto_step(distance, safe_cm)：自动模式下执行一步动作。
- safe_cm：安全阈值，低于它就触发避障流程。

实现提醒：

1. 组合键建议增加“持续按下时间”判定，减少误触。
2. AUTO 模式也要保留退出路径，防止失控。

目标：

- 达成最终目标 2（组合键触发自动前进 + 避障）。

建议组合键：

- 进入自动：`forward + right`
- 退出自动：`backward + left`

代码框架 sample（主程序片段）：

```python
mode = "MANUAL"  # MANUAL / AUTO


def check_mode_switch(states):
    # states 来自 receiver.read_states()
    if states["forward"] and states["right"]:
        return "AUTO"
    if states["backward"] and states["left"]:
        return "MANUAL"
    return None


def run_auto_step(distance, safe_cm=20):
    if distance is None:
        motor.stop()
        return

    if distance < safe_cm:
        motor.stop()
        time.sleep(0.1)
        motor.backward()
        time.sleep(0.2)
        motor.turn_right()
        time.sleep(0.3)
        motor.stop()
    else:
        motor.forward()
```

通过标准：

- 组合键能进入和退出自动模式。
- 自动模式会前进且能避障。

错误示例（反例）+ 为什么错：

```python
if states["forward"]:
    mode = "AUTO"
```

- 错因：用单键切模式太容易误触，手动控制体验会混乱。
- 建议：使用组合键并增加持续按下判定。

给孩子的提问卡（3 个问题）：

1. 为什么要有 mode 状态变量？
2. 自动模式里最核心的判断条件是什么？
3. 为什么组合键比单键更适合切模式？

---

## 第 10 章：手动模式加入安全保护

原理讲解：

- 手动优先不等于无条件执行，安全规则应有更高优先级。
- 这里采用“命令覆盖”思想：先得到手动命令，再做安全修正。
- 只对 `forward` 做前向防撞，可以避免误伤后退和转向控制体验。
- 第一版先实现“紧急停止”，稳定后再升级“自动绕行”。

关键函数解释：

- apply_safety_for_manual(cmd, distance, emergency_cm)：手动命令安全覆盖函数。
- emergency_cm：紧急阈值，越小越激进，越大越保守。
- return "stop"：最简单可靠的安全策略。
- return cmd：表示不触发安全覆盖，维持人工命令。

参数调试建议：

1. 先从 15 cm 开始调。
2. 触发太频繁就减小阈值。
3. 反应太慢就增大阈值。

目标：

- 达成最终目标 3（手动前进遇障碍自动停止或绕行）。

代码框架 sample（含绕行逻辑）：

```python
STOP_CM       = 20   # 前方距离小于此值时停车（厘米）
AVOID_TURN_MS = 600  # 绕行转向持续时间（毫秒）
AVOID_FWD_MS  = 400  # 绕行后向前走的时间（毫秒）


def is_clear():
    """返回前方是否畅通。"""
    d = radar.get_distance()
    return d is None or d > STOP_CM


def try_avoid():
    """先试右转，再试左转，都堵则停车。返回是否成功绕行。"""
    # 向右探路
    mata.turn_right()
    time.sleep_ms(AVOID_TURN_MS)
    mata.stop()
    if is_clear():
        mata.forward()
        time.sleep_ms(AVOID_FWD_MS)
        mata.stop()
        return True

    # 右侧不通 → 转回并继续向左转
    mata.turn_left()
    time.sleep_ms(AVOID_TURN_MS * 2)
    mata.stop()
    if is_clear():
        mata.forward()
        time.sleep_ms(AVOID_FWD_MS)
        mata.stop()
        return True

    # 两侧都堵 → 转回大致原方向放弃
    mata.turn_right()
    time.sleep_ms(AVOID_TURN_MS)
    mata.stop()
    return False
```

集成思路：

1. 主循环收到 `forward` 命令时，先测距。
2. 距离小于 `STOP_CM` → 停车并调用 `try_avoid()`。
3. `try_avoid()` 返回 `True` → 绕行成功，继续响应遥控。
4. 返回 `False` → 设置 `stuck = True`，停车等待手动换向。
5. 按其他方向键时自动解除 `stuck` 状态。

参数调整建议：

- `STOP_CM` 越大反应越早，先从 20 cm 开始。
- `AVOID_TURN_MS` 取决于车速，转得不够就加大。

通过标准：

- 手动前进时不硬撞。
- 手动后退和转向仍能正常使用。

错误示例（反例）+ 为什么错：

```python
if distance < emergency_cm:
    return "stop"
```

- 错因：没有限定 cmd == forward，会导致后退和转向也被错误阻断。
- 建议：只对前进命令启用前向防撞策略。

给孩子的提问卡（3 个问题）：

1. 为什么安全策略优先级要高于手动命令？
2. 为什么第一版建议先做 stop 而不是直接绕行？
3. emergency_cm 应该如何调试？

---

## 第 11 章：最终 main.py 组织建议

原理讲解：

- 复杂项目要“拆函数、分职责”，不要把所有逻辑堆进 while 循环。
- 模式切换、手动控制、自动避障、安全覆盖应各自独立。
- 主循环只保留骨架流程，便于阅读、排错和扩展。
- 这种结构在以后加新功能时改动最小，代码更不容易乱。

关键函数解释：

- apply_manual_command：只负责动作执行，不负责模式判断。
- check_mode_switch：只负责模式变更，不直接控制电机。
- run_auto_step：只负责自动逻辑的一步，不管理循环。
- apply_safety_for_manual：只负责安全覆盖规则。

设计原则：

1. 一个函数只做一类事。
2. 先判断模式，再执行对应逻辑。
3. 每次循环都留出短暂休眠。

建议函数拆分：

1. `apply_manual_command(cmd)`
2. `run_auto_step(distance, safe_cm)`
3. `check_mode_switch(states)`
4. `apply_safety_for_manual(cmd, distance, emergency_cm)`

最终 main.py sample（已实测）：

```python
import receiver
import mata
import radar
import time

STOP_CM       = 20
AVOID_TURN_MS = 600
AVOID_FWD_MS  = 400

ACTIONS = {
    "forward":  mata.forward,
    "backward": mata.backward,
    "left":     mata.turn_left,
    "right":    mata.turn_right,
    "stop":     mata.stop,
}


def is_clear():
    d = radar.get_distance()
    return d is None or d > STOP_CM


def try_avoid():
    mata.turn_right()
    time.sleep_ms(AVOID_TURN_MS)
    mata.stop()
    if is_clear():
        mata.forward()
        time.sleep_ms(AVOID_FWD_MS)
        mata.stop()
        return True

    mata.turn_left()
    time.sleep_ms(AVOID_TURN_MS * 2)
    mata.stop()
    if is_clear():
        mata.forward()
        time.sleep_ms(AVOID_FWD_MS)
        mata.stop()
        return True

    mata.turn_right()
    time.sleep_ms(AVOID_TURN_MS)
    mata.stop()
    return False


print("遥控 + 自动避障启动")
print("前进时距离 < {} cm 自动绕行，Ctrl+C 退出".format(STOP_CM))

last_cmd = None
stuck = False

try:
    while True:
        cmd = receiver.get_command()

        if cmd != "forward":
            stuck = False

        if cmd == "forward":
            if stuck:
                if cmd != last_cmd:
                    print("前方受阻，请手动换向")
                    last_cmd = cmd
                time.sleep_ms(50)
                continue

            dist = radar.get_distance()
            if dist is not None and dist <= STOP_CM:
                mata.stop()
                print("障碍 {:.1f} cm，尝试绕行...".format(dist))
                if try_avoid():
                    print("绕行成功")
                else:
                    print("绕行失败，停车")
                    stuck = True
                last_cmd = None
                continue

        if cmd != last_cmd:
            mata.stop()
            if cmd in ACTIONS:
                ACTIONS[cmd]()
                print(cmd)
            else:
                print("停止")
            last_cmd = cmd

        time.sleep_ms(50)

except KeyboardInterrupt:
    mata.stop()
    print("已停车，程序退出")
```

错误示例（反例）+ 为什么错：

```python
while True:
    # 所有逻辑全部写在这里，几百行
    pass
```

- 错因：职责混杂，排错困难，后续扩展非常痛苦。
- 建议：按“模式切换/手动/自动/安全”拆分函数。

给孩子的提问卡（3 个问题）：

1. 为什么大循环里不应该堆太多细节？
2. 一个函数只做一件事有什么好处？
3. 你能画出主循环的数据流顺序吗？

---

## 第 12 章：最终验收清单

原理讲解：

- 验收清单的作用是“防止自我感觉完成”。
- 每条都能实测，说明系统在真实场景下具备稳定性。
- 只有同时满足手动、自动、安全三条主线，项目才算闭环。
- 建议每次改动后复测清单，避免新功能破坏旧功能。

验收方法建议：

1. 每次只验证一条，不要同时测全部条件。
2. 先静态环境测试，再在复杂场景复测。
3. 每条通过后打勾并记录参数（如 safe_cm）。

请逐条验证：

1. 手动四方向控制正常。
2. 组合键能进入自动模式。
3. 自动模式能前进并避障。
4. 组合键能退出自动模式。
5. 手动前进遇障碍会停止或绕行。
6. 主循环包含短暂 `sleep`。
7. 可用 `Ctrl+C` 安全停止。

全部通过后，项目即达到目标。

错误示例（反例）+ 为什么错：

```text
只测了一次前进，其他不测，就宣布完成。
```

- 错因：没有覆盖手动、自动、安全三条主线，结果不可靠。
- 建议：按清单逐项打勾，并记录测试场景与参数。

给孩子的提问卡（3 个问题）：

1. 你最有把握通过的是哪一项？为什么？
2. 你最不稳定的是哪一项？下一步怎么改？
3. 如果给同学演示，你会按什么顺序展示功能？

---

## 常见问题速查

1. 报 `ImportError: no module named mata`
- 先右键执行 `Upload project to Pico` 再运行。

2. 程序停不下来
- 切到 `MicroPico vREPL`，按 `Ctrl+C`。

3. 电机方向相反
- 调整 `mata.py` 对应函数里的 `LEFT_MOTOR_REVERSED` / `RIGHT_MOTOR_REVERSED` 标志位。

4. 超声波偶发卡住
- 检查 `radar.py` 是否给等待 echo 的 while 加了超时。
