import tkinter as tk
from time_display import ClockApp  # 时间与天气模块
from alarm_audio import set_alarm_audio  # 音频闹钟模块
from alarm_buzzer import set_alarm_buzzer  # 蜂鸣器闹钟模块
from localization import t, set_language  # 多语言模块

# 默认语言设置为韩语
set_language("ko")

def open_audio_alarm():
    """
    打开音频闹钟设置窗口
    """
    def confirm_alarm():
        alarm_time = alarm_input.get().strip()
        try:
            hours, minutes = map(int, alarm_time.split(":"))
            if 0 <= hours < 24 and 0 <= minutes < 60:
                # 设置音频闹钟
                set_alarm_audio(f"{hours:02}:{minutes:02}", "assets/alarm.mp3")
                messagebox.showinfo(t("audio_alarm"), f"{t('audio_alarm')} {alarm_time}")
                alarm_window.destroy()
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror(t("error"), t("invalid_time_format"))

    alarm_window = tk.Toplevel(root)
    alarm_window.title(t("audio_alarm"))
    tk.Label(alarm_window, text=f"{t('audio_alarm')} (HH:MM):", font=("Helvetica", 12)).pack(pady=10)
    alarm_input = tk.Entry(alarm_window, font=("Helvetica", 12))
    alarm_input.pack(pady=5)
    tk.Button(alarm_window, text=t("confirm"), command=confirm_alarm).pack(pady=10)

def open_buzzer_alarm():
    """
    打开蜂鸣器闹钟设置窗口
    """
    def confirm_alarm():
        alarm_time = alarm_input.get().strip()
        try:
            hours, minutes = map(int, alarm_time.split(":"))
            if 0 <= hours < 24 and 0 <= minutes < 60:
                # 设置蜂鸣器闹钟
                set_alarm_buzzer(f"{hours:02}:{minutes:02}")
                messagebox.showinfo(t("buzzer_alarm"), f"{t('buzzer_alarm')} {alarm_time}")
                alarm_window.destroy()
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror(t("error"), t("invalid_time_format"))

    alarm_window = tk.Toplevel(root)
    alarm_window.title(t("buzzer_alarm"))
    tk.Label(alarm_window, text=f"{t('buzzer_alarm')} (HH:MM):", font=("Helvetica", 12)).pack(pady=10)
    alarm_input = tk.Entry(alarm_window, font=("Helvetica", 12))
    alarm_input.pack(pady=5)
    tk.Button(alarm_window, text=t("confirm"), command=confirm_alarm).pack(pady=10)

if __name__ == "__main__":
    try:
        # 主窗口配置
        root = tk.Tk()
        root.title(t("welcome"))
        root.geometry("1000x600")

        # 布局配置
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=2)
        root.columnconfigure(2, weight=1)
        root.rowconfigure(0, weight=1)
        root.rowconfigure(1, weight=2)

        # 左上角 - 时钟和天气
        clock_frame = tk.Frame(root, bg="lightblue", padx=10, pady=10)
        clock_frame.grid(row=0, column=0, sticky="nsew")
        ClockApp(clock_frame)

        # 左下角 - 音频闹钟
        audio_alarm_frame = tk.Frame(root, bg="lightyellow", padx=10, pady=10)
        audio_alarm_frame.grid(row=1, column=0, sticky="nsew")
        tk.Label(audio_alarm_frame, text=t("audio_alarm"), font=("Helvetica", 14), bg="lightyellow").pack(pady=10)
        tk.Button(audio_alarm_frame, text=t("set_audio_alarm"), command=open_audio_alarm).pack(pady=10)

        # 右下角 - 蜂鸣器闹钟
        buzzer_alarm_frame = tk.Frame(root, bg="lightpink", padx=10, pady=10)
        buzzer_alarm_frame.grid(row=1, column=2, sticky="nsew")
        tk.Label(buzzer_alarm_frame, text=t("buzzer_alarm"), font=("Helvetica", 14), bg="lightpink").pack(pady=10)
        tk.Button(buzzer_alarm_frame, text=t("set_buzzer_alarm"), command=open_buzzer_alarm).pack(pady=10)

        # 中央 - 预留功能
        placeholder_frame = tk.Frame(root, bg="white", padx=10, pady=10)
        placeholder_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")
        tk.Label(placeholder_frame, text="추가 기능 자리", font=("Helvetica", 16), bg="white").pack(pady=20)

        root.mainloop()
    except Exception as e:
        print(f"오류 발생: {e}")
    finally:
        print("프로그램 종료")
