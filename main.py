import tkinter as tk
from tkinter import ttk
from datetime import datetime
from localization import t, set_language
from alarm_audio import set_alarm_audio
from alarm_buzzer import set_alarm_buzzer
from timer import TimerApp

# 默认设置韩语
set_language("ko")

# 默认音频路径
alarm_sound = "assets/alarm.mp3"

# 更新当前时间
def update_time():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    time_label.config(text=now)
    root.after(1000, update_time)

# 打开音频闹钟设置窗口
def open_audio_alarm():
    pass  # 这里可以填写具体音频闹钟的逻辑

# 打开蜂鸣器闹钟设置窗口
def open_buzzer_alarm():
    pass  # 这里可以填写具体蜂鸣器闹钟的逻辑

# 打开秒表功能窗口
def open_timer():
    TimerApp(root)

# 切换语言
def switch_language():
    lang = language_var.get()
    if lang == "中文":
        set_language("zh")
    elif lang == "한국어":
        set_language("ko")
    refresh_ui()

# 刷新界面文字
def refresh_ui():
    root.title(t("welcome"))
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
time_label = ttk.Label(time_frame, text="", font=("Arial", 16))
time_label.pack()
update_time()

# 功能按钮
def open_audio_alarm():
    pass  # 音频闹钟功能逻辑

def open_buzzer_alarm():
    pass  # 蜂鸣器闹钟功能逻辑

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
language_var = tk.StringVar(value="한국어")
language_frame = ttk.Frame(root)
language_frame.pack(pady=10)
ttk.Label(language_frame, text="언어 선택:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
ttk.OptionMenu(language_frame, language_var, "한국어", "中文", command=lambda _: switch_language()).pack(side=tk.LEFT)

root.mainloop()
