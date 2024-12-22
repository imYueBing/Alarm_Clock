import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from localization import t, set_language
from alarm_audio import set_alarm_audio
from alarm_buzzer import set_alarm_buzzer
from timer import start_countdown_timer
from weather import get_weather

# 默认设置韩语
set_language("ko")

# 默认音频路径
alarm_sound = "assets/alarm.mp3"


def update_time():
    """
    实时更新当前时间显示
    """
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=now)
    root.after(1000, update_time)


def open_audio_alarm():
    """
    打开音频闹钟设置窗口
    """
    def confirm_alarm():
        try:
            alarm_time_str = alarm_input.get()
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M")
            now = datetime.now()
            alarm_time = now.replace(hour=alarm_time.hour, minute=alarm_time.minute, second=0)
            if alarm_time < now:
                alarm_time += timedelta(days=1)
            set_alarm_audio(alarm_time, alarm_sound)
            messagebox.showinfo(t("audio_alarm"), f"{t('audio_alarm')} {alarm_time.strftime('%H:%M')}")
            alarm_window.destroy()
        except ValueError:
            messagebox.showerror(t("error"), t("invalid_time_format"))

    alarm_window = tk.Toplevel(root)
    alarm_window.title(t("audio_alarm"))
    tk.Label(alarm_window, text=f"{t('audio_alarm')} (HH:MM):", font=("Arial", 12)).pack(pady=10)
    alarm_input = ttk.Entry(alarm_window)
    alarm_input.pack(pady=5, padx=10)
    ttk.Button(alarm_window, text=t("audio_alarm"), command=confirm_alarm).pack(pady=10)


def open_buzzer_alarm():
    """
    打开蜂鸣器闹钟设置窗口
    """
    def confirm_alarm():
        try:
            alarm_time_str = alarm_input.get()
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M")
            now = datetime.now()
            alarm_time = now.replace(hour=alarm_time.hour, minute=alarm_time.minute, second=0)
            if alarm_time < now:
                alarm_time += timedelta(days=1)
            set_alarm_buzzer(alarm_time)
            messagebox.showinfo(t("buzzer_alarm"), f"{t('buzzer_alarm')} {alarm_time.strftime('%H:%M')}")
            alarm_window.destroy()
        except ValueError:
            messagebox.showerror(t("error"), t("invalid_time_format"))

    alarm_window = tk.Toplevel(root)
    alarm_window.title(t("buzzer_alarm"))
    tk.Label(alarm_window, text=f"{t('buzzer_alarm')} (HH:MM):", font=("Arial", 12)).pack(pady=10)
    alarm_input = ttk.Entry(alarm_window)
    alarm_input.pack(pady=5, padx=10)
    ttk.Button(alarm_window, text=t("buzzer_alarm"), command=confirm_alarm).pack(pady=10)


def open_countdown_timer():
    """
    打开倒计时设置窗口
    """
    def confirm_timer():
        try:
            seconds = int(timer_input.get())
            if seconds <= 0:
                raise ValueError
            start_countdown_timer(seconds)
            messagebox.showinfo(t("start_timer"), t("timer_started"))
            timer_window.destroy()
        except ValueError:
            messagebox.showerror(t("error"), t("invalid_time_format"))

    timer_window = tk.Toplevel(root)
    timer_window.title(t("start_timer"))
    tk.Label(timer_window, text=t("start_timer"), font=("Arial", 12)).pack(pady=10)
    timer_input = ttk.Entry(timer_window)
    timer_input.pack(pady=5, padx=10)
    ttk.Button(timer_window, text=t("start_timer"), command=confirm_timer).pack(pady=10)


def open_weather_query():
    """
    打开天气查询窗口
    """
    def confirm_city():
        city = city_input.get()
        if not city:
            messagebox.showerror(t("error"), t("invalid_city"))
            return
        weather_info = get_weather(city)
        messagebox.showinfo(t("check_weather"), weather_info)
        weather_window.destroy()

    weather_window = tk.Toplevel(root)
    weather_window.title(t("check_weather"))
    tk.Label(weather_window, text=t("check_weather"), font=("Arial", 12)).pack(pady=10)
    city_input = ttk.Entry(weather_window)
    city_input.pack(pady=5, padx=10)
    ttk.Button(weather_window, text=t("check_weather"), command=confirm_city).pack(pady=10)


def switch_language():
    """
    切换语言
    """
    lang = language_var.get()
    if lang == "中文":
        set_language("zh")
    elif lang == "한국어":
        set_language("ko")
    messagebox.showinfo(t("welcome"), t("choose_function"))
    refresh_ui()


def refresh_ui():
    """
    刷新界面文字
    """
    root.title(t("welcome"))
    time_title_label.config(text=t("current_time"))
    for button, text_key in zip(buttons, text_keys):
        button.config(text=t(text_key))


# 主界面
root = tk.Tk()
root.title(t("welcome"))
root.geometry("600x400")

# 样式优化
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 14), padding=5)

# 当前时间显示
time_frame = ttk.Frame(root)
time_frame.pack(pady=20)
time_title_label = ttk.Label(time_frame, text=t("current_time"), font=("Arial", 16))
time_title_label.pack(side=tk.LEFT, padx=5)
time_label = ttk.Label(time_frame, text="", font=("Arial", 16))
time_label.pack(side=tk.LEFT)
update_time()

# 语言选择
language_var = tk.StringVar(value="한국어")
language_frame = ttk.Frame(root)
language_frame.pack(pady=10)
ttk.Label(language_frame, text="언어 선택:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
ttk.OptionMenu(language_frame, language_var, "한국어", "中文", command=lambda _: switch_language()).pack(side=tk.LEFT)

# 功能按钮
text_keys = [
    "audio_alarm", "buzzer_alarm", "start_timer",
    "check_weather", "exit"
]
functions = [
    open_audio_alarm, open_buzzer_alarm,
    open_countdown_timer, open_weather_query,
    root.quit
]
buttons_frame = ttk.Frame(root)
buttons_frame.pack(pady=20)
buttons = []
for key, func in zip(text_keys, functions):
    button = ttk.Button(buttons_frame, text=t(key), command=func, width=25)
    button.pack(pady=5)
    buttons.append(button)

root.mainloop()
