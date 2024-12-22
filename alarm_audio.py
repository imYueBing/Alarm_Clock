import pygame
import threading
from tkinter import messagebox
from datetime import datetime
from localization import t

def play_alarm_sound(sound_path):
    """
    播放音频闹钟
    """
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
    messagebox.showinfo(t("audio_alarm"), t("audio_alarm_triggered"))


def set_alarm_audio(alarm_time, sound_path):
    """
    设置音频闹钟
    :param alarm_time: datetime，闹钟时间
    :param sound_path: str，音频路径
    """
    def alarm_thread():
        while True:
            if datetime.now() >= alarm_time:
                play_alarm_sound(sound_path)
                break
            threading.Event().wait(1)
    threading.Thread(target=alarm_thread, daemon=True).start()
