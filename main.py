import tkinter as tk
from time_display import ClockApp
from weather import get_weather
from alarm_audio import set_alarm_audio
from alarm_buzzer import set_alarm_buzzer
from localization import t, set_language
from threading import Thread

# 默认语言设置为韩语
set_language("ko")


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title(t("welcome"))
        self.root.geometry("800x600")

        # 主布局
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        # 顶部：时间和天气模块
        self.time_weather_frame = tk.Frame(self.root, bg="lightblue", padx=10, pady=10)
        self.time_weather_frame.grid(row=0, column=0, sticky="nsew")
        self.init_time_weather()

        # 底部：闹钟设置
        self.alarm_frame = tk.Frame(self.root, bg="lightyellow", padx=10, pady=10)
        self.alarm_frame.grid(row=1, column=0, sticky="nsew")
        self.init_alarm_controls()

    def init_time_weather(self):
        """
        初始化时间和天气显示模块
        """
        # 当前时间显示
        self.clock_app = ClockApp(self.time_weather_frame)

        # 天气信息显示
        self.weather_label = tk.Label(
            self.time_weather_frame,
            text="날씨 정보 로딩 중...",
            font=("Helvetica", 14),
            bg="lightblue",
            wraplength=500,
        )
        self.weather_label.pack(anchor="center", pady=10)

        # 启动天气更新线程
        Thread(target=self.update_weather, daemon=True).start()

    def update_weather(self):
        """
        更新天气信息
        """
        while True:
            weather_info = get_weather()
            self.weather_label.config(text=f"현재 날씨:\n{weather_info}")
            self.weather_label.update()
            self.root.after(600000)  # 每 10 分钟更新一次

    def init_alarm_controls(self):
        """
        初始化闹钟设置模块
        """
        # 音频闹钟设置
        tk.Label(
            self.alarm_frame, text=t("audio_alarm"), font=("Helvetica", 14), bg="lightyellow"
        ).pack(pady=5)
        self.audio_alarm_button = tk.Button(
            self.alarm_frame, text=t("set_audio_alarm"), command=self.open_audio_alarm
        )
        self.audio_alarm_button.pack(pady=10)

        # 蜂鸣器闹钟设置
        tk.Label(
            self.alarm_frame, text=t("buzzer_alarm"), font=("Helvetica", 14), bg="lightyellow"
        ).pack(pady=5)
        self.buzzer_alarm_button = tk.Button(
            self.alarm_frame, text=t("set_buzzer_alarm"), command=self.open_buzzer_alarm
        )
        self.buzzer_alarm_button.pack(pady=10)

    def open_audio_alarm(self):
        """
        打开音频闹钟设置窗口
        """
        alarm_window = tk.Toplevel(self.root)
        alarm_window.title(t("audio_alarm"))
        tk.Label(alarm_window, text=f"{t('audio_alarm')} (HH:MM):", font=("Helvetica", 12)).pack(pady=10)

        alarm_input = tk.Entry(alarm_window, font=("Helvetica", 12))
        alarm_input.pack(pady=5)

        def confirm_alarm():
            alarm_time = alarm_input.get().strip()
            try:
                hours, minutes = map(int, alarm_time.split(":"))
                if 0 <= hours < 24 and 0 <= minutes < 60:
                    set_alarm_audio(f"{hours:02}:{minutes:02}", "assets/alarm.mp3")
                    tk.messagebox.showinfo(t("audio_alarm"), f"{t('audio_alarm')} {alarm_time}")
                    alarm_window.destroy()
                else:
                    raise ValueError
            except ValueError:
                tk.messagebox.showerror(t("error"), t("invalid_time_format"))

        tk.Button(alarm_window, text=t("confirm"), command=confirm_alarm).pack(pady=10)

    def open_buzzer_alarm(self):
        """
        打开蜂鸣器闹钟设置窗口
        """
        alarm_window = tk.Toplevel(self.root)
        alarm_window.title(t("buzzer_alarm"))
        tk.Label(alarm_window, text=f"{t('buzzer_alarm')} (HH:MM):", font=("Helvetica", 12)).pack(pady=10)

        alarm_input = tk.Entry(alarm_window, font=("Helvetica", 12))
        alarm_input.pack(pady=5)

        def confirm_alarm():
            alarm_time = alarm_input.get().strip()
            try:
                hours, minutes = map(int, alarm_time.split(":"))
                if 0 <= hours < 24 and 0 <= minutes < 60:
                    set_alarm_buzzer(f"{hours:02}:{minutes:02}")
                    tk.messagebox.showinfo(t("buzzer_alarm"), f"{t('buzzer_alarm')} {alarm_time}")
                    alarm_window.destroy()
                else:
                    raise ValueError
            except ValueError:
                tk.messagebox.showerror(t("error"), t("invalid_time_format"))

        tk.Button(alarm_window, text=t("confirm"), command=confirm_alarm).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
