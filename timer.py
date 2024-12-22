import tkinter as tk
from datetime import datetime, timedelta

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.running = False
        self.start_time = None
        self.elapsed_time = timedelta(0)

        # 创建秒表界面
        self.frame = tk.Toplevel(root)
        self.frame.title("秒表")
        self.label = tk.Label(self.frame, text="00:00:00", font=("Arial", 24))
        self.label.pack(pady=20)
        self.start_button = tk.Button(self.frame, text="开始", command=self.start)
        self.start_button.pack(pady=5)
        self.stop_button = tk.Button(self.frame, text="停止", command=self.stop)
        self.stop_button.pack(pady=5)
        self.reset_button = tk.Button(self.frame, text="重置", command=self.reset)
        self.reset_button.pack(pady=5)

    def update(self):
        if self.running:
            current_time = datetime.now()
            self.elapsed_time = current_time - self.start_time
            self.label.config(text=str(self.elapsed_time).split(".")[0])  # 显示时分秒
            self.root.after(100, self.update)  # 每100毫秒刷新一次

    def start(self):
        if not self.running:
            self.start_time = datetime.now() - self.elapsed_time  # 恢复计时
            self.running = True
            self.update()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.start_time = None
        self.elapsed_time = timedelta(0)
        self.label.config(text="00:00:00")
