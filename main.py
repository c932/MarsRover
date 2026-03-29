import mata
import time
#把所有代码复制到motor并删除motor即可运行
TEST_STEP_SECONDS = 1.5
PAUSE_SECONDS = 0.5
RUN_FOREVER = False


def run_step(action_name, action, duration=TEST_STEP_SECONDS):
    """执行一次电机测试动作。"""
    print("开始测试: {}".format(action_name))
    action()
    time.sleep(duration)
    mata.stop()
    print("结束测试: {}".format(action_name))
    time.sleep(PAUSE_SECONDS)


def run_motor_test_cycle():
    """按顺序测试电机动作。"""
    run_step("前进", mata.forward)
    run_step("后退", mata.backward)
    run_step("左转", mata.turn_left)
    run_step("右转", mata.turn_right)
    mata.stop()
    print("本轮测试结束")


print("火星车电机测试程序已启动")
print("将按顺序测试: 前进 -> 后退 -> 左转 -> 右转")
print("如果方向不对，请修改 motor.py 里的动作函数")
print("如果想循环测试，把 RUN_FOREVER 改成 True")

try:
    for _ in range(1, 10):
        run_motor_test_cycle()
        if not RUN_FOREVER:
            print("测试完成，程序结束")
            break

       # print("停车 2 秒后重新开始")
    mata.stop()

except KeyboardInterrupt:
    mata.stop()
    print("系统手动紧急停机！")