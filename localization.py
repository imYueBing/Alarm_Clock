LANGUAGES = {
    "zh": {
        "welcome": "欢迎使用树莓派智能闹钟！",
        "audio_alarm": "设置音频闹钟",
        "buzzer_alarm": "设置蜂鸣器闹钟",
        "audio_alarm_triggered": "音频闹钟响了！",
        "buzzer_alarm_triggered": "蜂鸣器闹钟响了！",
        "current_time": "当前时间",
        "error": "发生错误",
        "invalid_time_format": "无效的时间格式，请输入 HH:MM。",
    },
    "ko": {
        "welcome": "라즈베리파이 스마트 알람에 오신 것을 환영합니다!",
        "audio_alarm": "오디오 알람 설정",
        "buzzer_alarm": "부저 알람 설정",
        "audio_alarm_triggered": "오디오 알람이 울렸습니다!",
        "buzzer_alarm_triggered": "부저 알람이 울렸습니다!",
        "current_time": "현재 시간",
        "error": "오류 발생",
        "invalid_time_format": "잘못된 시간 형식입니다. HH:MM 형식으로 입력하세요.",
    },
}

current_language = "ko"

def set_language(lang_code):
    global current_language
    if lang_code in LANGUAGES:
        current_language = lang_code

def t(key):
    return LANGUAGES[current_language].get(key, key)
