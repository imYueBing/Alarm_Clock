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

def set_alarm_buzzer(alarm_time):
    """
    设置蜂鸣器闹钟功能，在指定时间触发蜂鸣器。
    :param alarm_time: str，格式为 "HH:MM:SS"
    """
    setup_buzzer()
    from datetime import datetime
    global is_buzzer_running
    is_buzzer_running = False  # 标记蜂鸣器是否正在运行

    try:
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            if current_time == alarm_time:
                is_buzzer_running = True
                for _ in range(5):
                    if not is_buzzer_running:
                        break
                    buzz(0.5)
                    time.sleep(0.5)
                break
    finally:
        cleanup_buzzer()

def stop_alarm_buzzer():
    """
    停止蜂鸣器闹钟
    """
    global is_buzzer_running
    if is_buzzer_running:
        is_buzzer_running = False
