import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    root.title("스마트 알람 시계")
    root.geometry("1000x600")

    # 当前时间显示
    clock_frame = tk.Frame(root)
    clock_frame.pack(side=tk.TOP, fill=tk.X)
    tk.Label(clock_frame, text="현재 시간", font=("Helvetica", 18)).pack()

    # 闹钟设置
    alarm_frame = tk.Frame(root)
    alarm_frame.pack(side=tk.LEFT, fill=tk.Y)
    tk.Label(alarm_frame, text="알람 설정", font=("Helvetica", 16)).pack()
    tk.Button(alarm_frame, text="오디오 알람 설정").pack()
    tk.Button(alarm_frame, text="부저 알람 설정").pack()

    # 天气信息显示
    weather_frame = tk.Frame(root)
    weather_frame.pack(side=tk.RIGHT, fill=tk.Y)
    tk.Label(weather_frame, text="현재 날씨", font=("Helvetica", 14)).pack()

    # 预留功能区域
    extra_frame = tk.Frame(root)
    extra_frame.pack(side=tk.BOTTOM, fill=tk.X)
    tk.Label(extra_frame, text="추가 기능 자리", font=("Helvetica", 16)).pack()

    root.mainloop()
