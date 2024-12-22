import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from localization import t, set_language
from alarm_audio import set_alarm_audio
from alarm_buzzer import set_alarm_buzzer
from timer import start_countdown_timer
from weather import get_weather  # 假设从这里获取天气信息

# 默认设置韩语
set_language("ko")

# 默认音频路径
alarm_sound = "assets/alarm.mp3"

# 默认城市
DEFAULT_CITY = "Seoul"

def update_time_and_weather():
    """
    实时更新当前时间和天气显示
    """
    # 更新当前时间
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=f"{t('current_time')}: {now}")

    # 更新天气信息，仅显示城市和温度
    try:
        weather_info = get_weather(DEFAULT_CITY)  # 从 weather 模块获取天气
        if isinstance(weather_info, dict):
            city = weather_info.get("city", DEFAULT_CITY)
            temp = weather_info.get("temp", "N/A")
            weather_label.config(text=f"{city}: {temp}°C")
        else:
            weather_label.config(text=f"{DEFAULT_CITY}: N/A")
    except Exception as e:
        weather_label.config(text=f"{DEFAULT_CITY}: Error")

    root.after(60000, update_time_and_weather)  # 每分钟更新一次

# 主界面
root = tk.Tk()
root.title(t("welcome"))
root.geometry("600x400")

# 样式优化
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 14), padding=5)

# 当前时间和天气显示
time_frame = ttk.Frame(root)
time_frame.pack(pady=20)
time_label = ttk.Label(time_frame, text="", font=("Arial", 16))
time_label.pack(pady=5)  # 当前时间独占一行
weather_label = ttk.Label(time_frame, text="", font=("Arial", 14))
weather_label.pack(pady=5)  # 天气信息独占一行

# 启动时间和天气更新
update_time_and_weather()

root.mainloop()
