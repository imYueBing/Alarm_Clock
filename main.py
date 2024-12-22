import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from localization import t, set_language
from alarm_audio import set_alarm_audio
from alarm_buzzer import set_alarm_buzzer
from timer import TimerApp
from weather import get_weather

# 默认设置韩语
set_language("ko")

# 默认音频路径
alarm_sound = "assets/alarm.mp3"

# 默认城市
DEFAULT_CITY = "Seoul"

# 更新当前时间和天气
def update_time_and_weather():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=now)

    try:
        weather_info = get_weather(DEFAULT_CITY)
        if isinstance(weather_info, dict):
            city = weather_info.get("city", DEFAULT_CITY)
            temp = weather_info.get("temp", "N/A")
            weather_label.config(text=f"{city}: {temp}°C")
        else:
            weather_label.config(text=f"{DEFAULT_CITY}: N/A")
    except Exception as e:
        weather_label.config(text=f"{DEFAULT_CITY}: Error")

    root.after(1000, update_time_and_weather)

# 打开音频闹钟设置窗口
def open_audio_alarm():
    def confirm_alarm():
        try:
            alarm_time_str = alarm_input.get()
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M")
            now = datetime.now()
            alarm_time = now.replace(hour=alarm_time.hour, minute=alarm_time.minute, second=0)
            if alarm_time < now:
                alarm_time += timedelta(days=1)
            set_alarm_audio(alarm_time, alarm_sound)
            messagebox.showinfo(t("audio_alarm"), f"{t('audio_alarm_set')} {alarm_time.strftime('%H:%M')}")
            alarm_window.destroy()
        except ValueError:
            messagebox.showerror(t("error"), t("invalid_time_format"))

    alarm_window = tk.Toplevel(root)
    alarm_window.title(t("audio_alarm"))
    tk.Label(alarm_window, text=f"{t('audio_alarm')} (HH:MM):", font=("Arial", 12)).pack(pady=10)
    alarm_input = ttk.Entry(alarm_window)
    alarm_input.pack(pady=5, padx=10)
    ttk.Button(alarm_window, text=t("confirm"), command=confirm_alarm).pack(pady=10)

# 打开蜂鸣器闹钟设置窗口
def open_buzzer_alarm():
    def confirm_alarm():
        try:
            alarm_time_str = alarm_input.get()
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M")
            now = datetime.now()
            alarm_time = now.replace(hour=alarm_time.hour, minute=alarm_time.minute, second=0)
            if alarm_time < now:
                alarm_time += timedelta(days=1)
            set_alarm_buzzer(alarm_time)
            messagebox.showinfo(t("buzzer_alarm"), f"{t('buzzer_alarm_set')} {alarm_time.strftime('%H:%M')}")
            alarm_window.destroy()
        except ValueError:
            messagebox.showerror(t("error"), t("invalid_time_format"))

    alarm_window = tk.Toplevel(root)
    alarm_window.title(t("buzzer_alarm"))
    tk.Label(alarm_window, text=f"{t('buzzer_alarm')} (HH:MM):", font=("Arial", 12)).pack(pady=10)
    alarm_input = ttk.Entry(alarm_window)
    alarm_input.pack(pady=5, padx=10)
    ttk.Button(alarm_window, text=t("confirm"), command=confirm_alarm).pack(pady=10)

# 打开秒表功能窗口
def open_timer():
    TimerApp(root)

# 切换语言
def switch_language(lang):
    if lang == "中文":
        set_language("zh")
    elif lang == "한국어":
        set_language("ko")
    refresh_ui()

# 刷新界面文字
def refresh_ui():
    root.title(t("welcome"))
    time_label_title.config(text=t("current_time"))
    weather_label_title.config(text=t("current_weather"))
    for button, text_key in zip(buttons, text_keys):
        button.config(text=t(text_key))
    language_label.config(text=t("language_select"))

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
time_label_title = ttk.Label(time_frame, text=t("current_time"), font=("Arial", 16))
time_label_title.pack()
time_label = ttk.Label(time_frame, text="", font=("Arial", 16))
time_label.pack()

weather_label_title = ttk.Label(time_frame, text=t("current_weather"), font=("Arial", 14))
weather_label_title.pack()
weather_label = ttk.Label(time_frame, text="", font=("Arial", 14))
weather_label.pack()

update_time_and_weather()

# 功能按钮
text_keys = [
    "audio_alarm", "buzzer_alarm", "timer",
    "exit"
]
functions = [
    open_audio_alarm, open_buzzer_alarm,
    open_timer, root.quit
]
buttons_frame = ttk.Frame(root)
buttons_frame.pack(pady=20)
buttons = []
for key, func in zip(text_keys, functions):
    button = ttk.Button(buttons_frame, text=t(key), command=func, width=25)
    button.pack(pady=5)
    buttons.append(button)

# 切换语言选项
language_frame = ttk.Frame(root)
language_frame.pack(pady=10)
language_label = ttk.Label(language_frame, text=t("language_select"), font=("Arial", 12))
language_label.pack(side=tk.LEFT, padx=5)
ttk.Button(language_frame, text="한국어", command=lambda: switch_language("한국어")).pack(side=tk.LEFT, padx=5)
ttk.Button(language_frame, text="中文", command=lambda: switch_language("中文")).pack(side=tk.LEFT, padx=5)

root.mainloop()
