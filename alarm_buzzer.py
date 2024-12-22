import RPi.GPIO as GPIO
import threading
from tkinter import messagebox
from datetime import datetime
from localization import t

# GPIO 引脚定义
BUZZER_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

def buzz(duration):
    """
    控制蜂鸣器响起
    :param duration: int，持续时间（秒）
    """
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    threading.Event().wait(duration)
    GPIO.output(BUZZER_PIN, GPIO.LOW)

def set_alarm_buzzer(alarm_time):
    """
    设置蜂鸣器闹钟
    :param alarm_time: datetime，闹钟时间
    """
    def alarm_thread():
        while True:
            if datetime.now() >= alarm_time:
                buzz(5)  # 蜂鸣器响 5 秒
                messagebox.showinfo(t("buzzer_alarm"), t("buzzer_alarm_triggered"))
                break
            threading.Event().wait(1)
    threading.Thread(target=alarm_thread, daemon=True).start()
