import pygame

def set_alarm_audio(alarm_time, alarm_sound="assets/alarm.mp3"):
    """
    设置音频闹钟功能，在指定时间播放音频。
    :param alarm_time: str，格式为 "HH:MM:SS"
    :param alarm_sound: str，自定义音频文件路径
    """
    pygame.mixer.init()
    from datetime import datetime
    global is_alarm_running
    is_alarm_running = False  # 标记闹钟是否正在运行

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            is_alarm_running = True
            pygame.mixer.music.load(alarm_sound)
            pygame.mixer.music.play()
            break

def stop_alarm_audio():
    """
    停止音频闹钟
    """
    global is_alarm_running
    if is_alarm_running:
        pygame.mixer.music.stop()
        is_alarm_running = False
