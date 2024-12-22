import tkinter as tk
from time_display import ClockApp
from weather import get_weather
from alarm_audio import set_alarm_audio
from alarm_buzzer import set_alarm_buzzer
from threading import Thread
import time

# 天气模块的默认城市
DEFAULT_CITY = "Seoul"

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("스마트 알람 시계")
        self.root.geometry("1000x600")

        # 配置网格布局
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=2)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=2)

        # 左上角 - 当前时间和天气
        self.clock_frame = tk.Frame(root, bg="lightblue", padx=10, pady=10)
        self.clock_frame.grid(row=0, column=0, sticky="nsew")
        self.init_clock_and_weather()

        # 左下角 - 闹钟设置
        self.alarm_frame = tk.Frame(root, bg="lightyellow", padx=10, pady=10)
        self.alarm_frame.grid(row=1, column=0, sticky="nsew")
        self.init_alarm_controls()

        # 中央 - 预留功能区域
        self.schedule_frame = tk.Frame(root, bg="white", padx=10, pady=10)
        self.schedule_frame.grid(row=0, column=1, rowspan=2, sticky="nsew")
        self.init_schedule_area()

        # 右下角 - 氛围灯（预留区域）
        self.led_frame = tk.Frame(root, bg="lightpink", padx=10, pady=10)
        self.led_frame.grid(row=1, column=2, sticky="nsew")
        self.init_led_controls()

        # 右上角 - 天气显示（补充）
        self.weather_frame = tk.Frame(root, bg="lightgreen", padx=10, pady=10)
        self.weather_frame.grid(row=0, column=2, sticky="nsew")

    def init_clock_and_weather(self):
        """
        初始化时钟和天气显示
        """
        # 时钟显示
        self.clock_app = ClockApp(self.clock_frame)

        # 天气显示
        self.weather_label = tk.Label(
            self.clock_frame, text="날씨 정보 로딩 중...", font=("Helvetica", 14), bg="lightblue", wraplength=250
        )
        self.weather_label.pack(anchor="center", pady=10)

        # 启动天气更新线程
        Thread(target=self.update_weather, daemon=True).start()

    def update_weather(self):
        """
        定时更新天气信息
        """
        while True:
            weather_info = get_weather(DEFAULT_CITY)
            self.weather_label.config(text=f"현재 날씨:\n{weather_info}")
            time.sleep(600)  # 每10分钟更新一次

    def init_alarm_controls(self):
        """
        初始化闹钟设置模块
        """
        tk.Label(self.alarm_frame, text="알람 설정", font=("Helvetica", 14), bg="lightyellow").pack(pady=5)

        # 音频闹钟设置
        tk.Button(self.alarm_frame, text="오디오 알람 설정", command=self.open_audio_alarm).pack(pady=10)

        # 蜂鸣器闹钟设置
        tk.Button(self.alarm_frame, text="부저 알람 설정", command=self.open_buzzer_alarm).pack(pady=10)

    def open_audio_alarm(self):
        """
        打开音频闹钟设置窗口
        """
        alarm_window = tk.Toplevel(self.root)
        alarm_window.title("오디오 알람 설정")
        tk.Label(alarm_window, text="시간 입력 (HH:MM):", font=("Helvetica", 12)).pack(pady=10)
        alarm_input = tk.Entry(alarm_window, font=("Helvetica", 12))
        alarm_input.pack(pady=5)

        def confirm_alarm():
            alarm_time = alarm_input.get().strip()
            try:
                hours, minutes = map(int, alarm_time.split(":"))
                if 0 <= hours < 24 and 0 <= minutes < 60:
                    set_alarm_audio(f"{hours:02}:{minutes:02}", "assets/alarm.mp3")
                    tk.messagebox.showinfo("알람 설정", f"오디오 알람 설정 완료: {alarm_time}")
                    alarm_window.destroy()
                else:
                    raise ValueError
            except ValueError:
                tk.messagebox.showerror("오류", "올바른 시간 형식이 아닙니다. HH:MM 형식으로 입력해주세요.")

        tk.Button(alarm_window, text="확인", command=confirm_alarm).pack(pady=10)

    def open_buzzer_alarm(self):
        """
        打开蜂鸣器闹钟设置窗口
        """
        alarm_window = tk.Toplevel(self.root)
        alarm_window.title("부저 알람 설정")
        tk.Label(alarm_window, text="시간 입력 (HH:MM):", font=("Helvetica", 12)).pack(pady=10)
        alarm_input = tk.Entry(alarm_window, font=("Helvetica", 12))
        alarm_input.pack(pady=5)

        def confirm_alarm():
            alarm_time = alarm_input.get().strip()
            try:
                hours, minutes = map(int, alarm_time.split(":"))
                if 0 <= hours < 24 and 0 <= minutes < 60:
                    set_alarm_buzzer(f"{hours:02}:{minutes:02}")
                    tk.messagebox.showinfo("알람 설정", f"부저 알람 설정 완료: {alarm_time}")
                    alarm_window.destroy()
                else:
                    raise ValueError
            except ValueError:
                tk.messagebox.showerror("오류", "올바른 시간 형식이 아닙니다. HH:MM 형식으로 입력해주세요.")

        tk.Button(alarm_window, text="확인", command=confirm_alarm).pack(pady=10)

    def init_schedule_area(self):
        """
        初始化预留区域
        """
        tk.Label(self.schedule_frame, text="추가 기능 자리", font=("Helvetica", 16), bg="white").pack(pady=20)

    def init_led_controls(self):
        """
        初始化氛围灯控制模块
        """
        tk.Label(self.led_frame, text="무드등 제어", font=("Helvetica", 14), bg="lightpink").pack(pady=5)
        tk.Button(self.led_frame, text="무드등 ON/OFF").pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
