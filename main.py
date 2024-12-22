import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
from localization import t, set_language
from alarm_audio import set_alarm_audio
from alarm_buzzer import set_alarm_buzzer

# 默认设置韩语
set_language("ko")

# 默认音频路径
alarm_sound = "assets/alarm.mp3"


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


# 主界面
root = tk.Tk()
root.title(t("welcome"))
root.geometry("600x400")

# 样式优化
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TLabel", font=("Arial", 14), padding=5)

# 功能按钮
buttons = [
    {"text": t("audio_alarm"), "command": open_audio_alarm},
    {"text": t("buzzer_alarm"), "command": open_buzzer_alarm},
    {"text": t("exit"), "command": root.quit},
]
for btn in buttons:
    ttk.Button(root, text=btn["text"], command=btn["command"]).pack(pady=10)

root.mainloop()
