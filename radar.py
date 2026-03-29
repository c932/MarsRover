from machine import Pin
import time

# 这是“超声波模块学习样例”，不是最终成品。
# 目标是给孩子保留接口和思路，让他自己一步步补全功能。

TRIG_PIN = 14
ECHO_PIN = 15

trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)


def send_pulse():
    """样例：先发出一个 10 微秒触发脉冲。"""
    trig.value(0)
    time.sleep_us(2)
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)


def get_distance():
    """返回前方距离，当前只提供实现提示。

    建议自己完成以下步骤：
    1. 调用 send_pulse() 发射超声波。
    2. 等待 echo 从 0 变成 1，记录起始时间。
    3. 等待 echo 从 1 变回 0，记录结束时间。
    4. 增加超时保护，避免 while 一直卡死。
    5. 用公式把脉冲时长转换为厘米。

    公式示例：
    distance_cm = pulse_duration_us * 0.0343 / 2
    """
    send_pulse()

    # TODO: 在这里补上完整测距逻辑。
    # 提示：可以使用 time.ticks_us() 和 time.ticks_diff()。
    # 建议超时时间先从 30000 微秒开始尝试。

    return None