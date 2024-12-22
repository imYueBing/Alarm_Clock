# Localization module for multi-language support

# Define translations
translations = {
    "ko": {
        "welcome": "환영합니다",
        "current_time": "현재 시간",
        "current_weather": "현재 날씨",
        "audio_alarm": "오디오 알람",
        "buzzer_alarm": "부저 알람",
        "timer": "타이머",
        "exit": "종료",
        "language_select": "언어 선택",
        "audio_alarm_set": "오디오 알람이 설정되었습니다:",
        "buzzer_alarm_set": "부저 알람이 설정되었습니다:",
        "invalid_time_format": "잘못된 시간 형식입니다. HH:MM 형식으로 입력해주세요.",
        "error": "오류",
        "confirm": "확인",
        "timer_running": "타이머 작동 중...",
        "timer_stopped": "타이머가 중지되었습니다.",
        "timer_reset": "타이머가 초기화되었습니다.",
    },
    "zh": {
        "welcome": "欢迎",
        "current_time": "当前时间",
        "current_weather": "当前天气",
        "audio_alarm": "音频闹钟",
        "buzzer_alarm": "蜂鸣器闹钟",
        "timer": "计时器",
        "exit": "退出",
        "language_select": "选择语言",
        "audio_alarm_set": "音频闹钟已设置:",
        "buzzer_alarm_set": "蜂鸣器闹钟已设置:",
        "invalid_time_format": "无效的时间格式，请输入 HH:MM。",
        "error": "错误",
        "confirm": "确认",
        "timer_running": "计时器正在运行...",
        "timer_stopped": "计时器已停止。",
        "timer_reset": "计时器已重置。",
    },
}

# Default language
current_language = "ko"

def set_language(language):
    """
    Set the current language.
    :param language: Language code (e.g., "ko", "zh")
    """
    global current_language
    current_language = language

def t(key):
    """
    Translate a key into the current language.
    :param key: Translation key
    :return: Translated string
    """
    return translations.get(current_language, {}).get(key, key)
