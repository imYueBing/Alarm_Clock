import time
from datetime import datetime
from threading import Thread
from weather import get_weather
import tkinter as tk

class ClockApp:
    def __init__(self, parent_frame):
        self.frame = parent_frame

        # 当前时间显示
        self.time_label = tk.Label(self.frame, text="", font=("Helvetica", 18))
        self.time_label.pack(anchor="center", pady=10)

        # 天气信息显示
        self.weather_label = tk.Label(self.frame, text="날씨 정보 로딩 중...", font=("Helvetica", 14), wraplength=300)
        self.weather_label.pack(anchor="center", pady=10)

        self.running = True

        # 启动时间和天气更新线程
        Thread(target=self.update_time, daemon=True).start()
        Thread(target=self.update_weather, daemon=True).start()

    def update_time(self):
        """
        实时更新当前时间
        """
        while self.running:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.time_label.config(text=f"현재 시간: {current_time}")
            time.sleep(1)

    def update_weather(self):
        """
        定时更新天气信息
        """
        while self.running:
            weather_info = get_weather()
            self.weather_label.config(text=f"현재 날씨:\n{weather_info}")
            time.sleep(600)  # 每 10 分钟刷新一次
