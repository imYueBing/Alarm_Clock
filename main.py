import tkinter as tk
from tkinter import messagebox, filedialog
from localization import t, set_language
import time_display
import alarm_audio
import alarm_buzzer
import weather
import timer

# 默认设置韩语
set_language("ko")

# 全局变量
alarm_sound = "assets/alarm.mp3"  # 默认音频路径


def show_time_display():
    """
    调用时间显示功能
    """
    time_display.display_time()


def set_audio_alarm():
    """
    设置音频闹钟
    """
    def confirm_alarm():
        alarm_time = alarm_input.get()
        if not alarm_time:
            messagebox.showerror(t("error"), t("error"))  # 错误提示
            return
        alarm_audio.set_alarm_audio(alarm_time, alarm_sound)
        messagebox.showinfo(t("audio_alarm"), f"{t('audio_alarm')} {alarm_time}")
        alarm_window.destroy()

    alarm_window = tk.Toplevel(root)
    alarm_window.title(t("audio_alarm"))
    tk.Label(alarm_window, text=f"{t('audio_alarm')} (HH:MM:SS):").pack(pady=10)
    alarm_input = tk.Entry(alarm_window)
    alarm_input.pack(pady=5)
    tk.Button(alarm_window, text=t("audio_alarm"), command=confirm_alarm).pack(pady=10)


def set_buzzer_alarm():
    """
    设置蜂鸣器闹钟
    """
    def confirm_alarm():
        alarm_time = alarm_input.get()
        if not alarm_time:
            messagebox.showerror(t("error"), t("error"))  # 错误提示
            return
        alarm_buzzer.set_alarm_buzzer(alarm_time)
        messagebox.showinfo(t("buzzer_alarm"), f"{t('buzzer_alarm')} {alarm_time}")
        alarm_window.destroy()

    alarm_window = tk.Toplevel(root)
    alarm_window.title(t("buzzer_alarm"))
    tk.Label(alarm_window, text=f"{t('buzzer_alarm')} (HH:MM:SS):").pack(pady=10)
    alarm_input = tk.Entry(alarm_window)
    alarm_input.pack(pady=5)
    tk.Button(alarm_window, text=t("buzzer_alarm"), command=confirm_alarm).pack(pady=10)


def stop_audio_alarm():
    """
    停止音频闹钟
    """
    alarm_audio.stop_alarm_audio()
    messagebox.showinfo(t("stop_audio_alarm"), t("stop_audio_alarm"))


def stop_buzzer_alarm():
    """
    停止蜂鸣器闹钟
    """
    alarm_buzzer.stop_alarm_buzzer()
    messagebox.showinfo(t("stop_buzzer_alarm"), t("stop_buzzer_alarm"))


def check_weather():
    """
    查看天气功能
    """
    def confirm_city():
        city = city_input.get()
        if not city:
            messagebox.showerror(t("error"), t("error"))  # 错误提示
            return
        weather_info = weather.get_weather(city)
        messagebox.showinfo(t("check_weather"), weather_info)
        weather_window.destroy()

    weather_window = tk.Toplevel(root)
    weather_window.title(t("check_weather"))
    tk.Label(weather_window, text=f"{t('check_weather')}:").pack(pady=10)
    city_input = tk.Entry(weather_window)
    city_input.pack(pady=5)
    tk.Button(weather_window, text=t("check_weather"), command=confirm_city).pack(pady=10)


def start_timer():
    """
    启动倒计时
    """
    def confirm_timer():
        try:
            seconds = int(timer_input.get())
            if seconds <= 0:
                raise ValueError
            timer.countdown_timer(seconds)
            messagebox.showinfo(t("start_timer"), t("start_timer"))
            timer_window.destroy()
        except ValueError:
            messagebox.showerror(t("error"), t("error"))

    timer_window = tk.Toplevel(root)
    timer_window.title(t("start_timer"))
    tk.Label(timer_window, text=f"{t('start_timer')} ({t('stop_timer')}):").pack(pady=10)
    timer_input = tk.Entry(timer_window)
    timer_input.pack(pady=5)
    tk.Button(timer_window, text=t("start_timer"), command=confirm_timer).pack(pady=10)


def stop_timer():
    """
    停止倒计时
    """
    timer.stop_timer()
    messagebox.showinfo(t("stop_timer"), t("stop_timer"))


def change_alarm_sound():
    """
    更改音频闹钟的铃声
    """
    global alarm_sound
    new_sound = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3"), ("WAV files", "*.wav")])
    if new_sound:
        alarm_sound = new_sound
        messagebox.showinfo(t("change_alarm_sound"), f"{t('change_alarm_sound')} {new_sound}")


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
    更新界面文本
    """
    root.title(t("welcome"))
    for button, text_key in zip(buttons, text_keys):
        button.config(text=t(text_key))


# 主界面
root = tk.Tk()
root.title(t("welcome"))

# 语言切换
language_var = tk.StringVar(value="한국어")  # 默认语言设置为韩语
tk.OptionMenu(root, language_var, "中文", "한국어", command=lambda _: switch_language()).pack(pady=10)

# 功能按钮
text_keys = [
    "current_time", "audio_alarm", "buzzer_alarm", 
    "stop_audio_alarm", "stop_buzzer_alarm", 
    "check_weather", "start_timer", "stop_timer", 
    "change_alarm_sound", "exit"
]
functions = [
    show_time_display, set_audio_alarm, set_buzzer_alarm, 
    stop_audio_alarm, stop_buzzer_alarm, 
    check_weather, start_timer, stop_timer, 
    change_alarm_sound, root.quit
]
buttons = [
    tk.Button(root, text=t(key), command=func, width=20)
    for key, func in zip(text_keys, functions)
]
for button in buttons:
    button.pack(pady=10)

root.mainloop()
