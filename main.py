import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
from localization import t, set_language
import alarm_audio
import alarm_buzzer
import time_display
import weather
import timer

# 默认语言为韩语
set_language("ko")

# 全局变量
alarm_sound = "assets/alarm.mp3"  # 默认音频路径


def show_time_display():
    time_display.display_time()


def set_audio_alarm():
    def confirm_alarm():
        alarm_time = alarm_input.get()
        if not alarm_time:
            messagebox.showerror(t("error"), t("error"))  # 错误提示
            return
        alarm_audio.set_alarm_audio(alarm_time, alarm_sound)
        messagebox.showinfo(t("audio_alarm"), f"{t('audio_alarm')} {alarm_time}")
        alarm_window.destroy()

    alarm_window = ttk.Toplevel(root)
    alarm_window.title(t("audio_alarm"))
    ttk.Label(alarm_window, text=f"{t('audio_alarm')} (HH:MM:SS):").pack(pady=10)
    alarm_input = ttk.Entry(alarm_window)
    alarm_input.pack(pady=5)
    ttk.Button(alarm_window, text=t("audio_alarm"), bootstyle=SUCCESS, command=confirm_alarm).pack(pady=10)


def stop_audio_alarm():
    alarm_audio.stop_alarm_audio()
    messagebox.showinfo(t("stop_audio_alarm"), t("stop_audio_alarm"))


def stop_buzzer_alarm():
    alarm_buzzer.stop_alarm_buzzer()
    messagebox.showinfo(t("stop_buzzer_alarm"), t("stop_buzzer_alarm"))


def check_weather():
    def confirm_city():
        city = city_input.get()
        if not city:
            messagebox.showerror(t("error"), t("error"))  # 错误提示
            return
        weather_info = weather.get_weather(city)
        messagebox.showinfo(t("check_weather"), weather_info)
        weather_window.destroy()

    weather_window = ttk.Toplevel(root)
    weather_window.title(t("check_weather"))
    ttk.Label(weather_window, text=f"{t('check_weather')}:").pack(pady=10)
    city_input = ttk.Entry(weather_window)
    city_input.pack(pady=5)
    ttk.Button(weather_window, text=t("check_weather"), bootstyle=PRIMARY, command=confirm_city).pack(pady=10)


def start_timer():
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

    timer_window = ttk.Toplevel(root)
    timer_window.title(t("start_timer"))
    ttk.Label(timer_window, text=f"{t('start_timer')} ({t('stop_timer')}):").pack(pady=10)
    timer_input = ttk.Entry(timer_window)
    timer_input.pack(pady=5)
    ttk.Button(timer_window, text=t("start_timer"), bootstyle=INFO, command=confirm_timer).pack(pady=10)


def change_alarm_sound():
    global alarm_sound
    new_sound = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3"), ("WAV files", "*.wav")])
    if new_sound:
        alarm_sound = new_sound
        messagebox.showinfo(t("change_alarm_sound"), f"{t('change_alarm_sound')} {new_sound}")


def switch_language():
    lang = language_var.get()
    if lang == "中文":
        set_language("zh")
    elif lang == "한국어":
        set_language("ko")
    messagebox.showinfo(t("welcome"), t("choose_function"))
    refresh_ui()


def refresh_ui():
    root.title(t("welcome"))
    for button, text_key in zip(buttons, text_keys):
        button.config(text=t(text_key))


# 主界面
root = ttk.Window(themename="solar")  # 选择主题
root.title(t("welcome"))
root.geometry("600x400")

# 语言选择
language_var = ttk.StringVar(value="한국어")
language_frame = ttk.Frame(root)
language_frame.pack(pady=10)
ttk.Label(language_frame, text="언어 선택:").pack(side=LEFT, padx=5)
ttk.OptionMenu(language_frame, language_var, "한국어", "中文", command=lambda _: switch_language()).pack(side=LEFT)

# 功能按钮
text_keys = [
    "current_time", "audio_alarm", "buzzer_alarm", 
    "stop_audio_alarm", "stop_buzzer_alarm", 
    "check_weather", "start_timer", "change_alarm_sound", "exit"
]
functions = [
    show_time_display, set_audio_alarm, stop_audio_alarm, 
    stop_buzzer_alarm, check_weather, start_timer, 
    change_alarm_sound, root.quit
]
buttons_frame = ttk.Frame(root)
buttons_frame.pack(pady=20)
buttons = []
for key, func in zip(text_keys, functions):
    button = ttk.Button(buttons_frame, text=t(key), bootstyle=PRIMARY, command=func, width=25)
    button.pack(pady=5)
    buttons.append(button)

root.mainloop()
