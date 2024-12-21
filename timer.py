import time
import RPi.GPIO as GPIO

BUZZER_PIN = 18  # GPIO 引脚

def setup_buzzer():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUZZER_PIN, GPIO.OUT)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

def cleanup_buzzer():
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    GPIO.cleanup()

def buzz(duration=1):
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

def countdown_timer(seconds):
    """
    启动倒计时
    :param seconds: int，倒计时的秒数
    """
    setup_buzzer()
    global is_timer_running
    is_timer_running = True  # 标记倒计时是否正在运行

    try:
        while seconds > 0:
            if not is_timer_running:
                break
            print(f"남은 시간: {seconds}초", end="\r")
            time.sleep(1)
            seconds -= 1

        if is_timer_running:
            for _ in range(5):  # 蜂鸣 5 次
                buzz(0.5)
                time.sleep(0.5)
    finally:
        cleanup_buzzer()

def stop_timer():
    """
    停止倒计时
    """
    global is_timer_running
    is_timer_running = False
