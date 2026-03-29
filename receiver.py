from machine import Pin

# 这是“遥控接管模块学习样例”，不是最终成品。
# 可以先学会读引脚电平，再自己写出控制命令判断逻辑。

# GP21: 后退，GP20: 前进，GP26: 右转，GP22: 左转
backward_pin = Pin(21, Pin.IN, Pin.PULL_DOWN)
forward_pin = Pin(20, Pin.IN, Pin.PULL_DOWN)
right_pin = Pin(26, Pin.IN, Pin.PULL_DOWN)
left_pin = Pin(22, Pin.IN, Pin.PULL_DOWN)


def read_states():
    """样例：读取 4 路输入的高低电平。"""
    return {
        "backward": backward_pin.value(),
        "forward": forward_pin.value(),
        "right": right_pin.value(),
        "left": left_pin.value(),
    }


def get_command():
    """根据输入状态返回一个动作指令。

    当前文件只保留样例思路：
    1. 先调用 read_states() 读取 4 路状态。
    2. 如果只有一路为高电平，就返回对应动作。
    3. 如果多路同时为高电平，可以返回 "stop"。
    4. 如果都没有输入，就返回 None。
    """
    states = read_states()

    # 下面这段只是示例写法，可以自己改出不同规则。
    active_commands = [name for name, value in states.items() if value]

    if len(active_commands) == 1:
        return active_commands[0]

    if len(active_commands) > 1:
        return "stop"

    return None