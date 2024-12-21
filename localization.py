LANGUAGES = {
    "zh": {  # 中文
        "welcome": "欢迎使用树莓派智能闹钟！",
        "choose_function": "请选择功能：",
        "current_time": "显示当前时间",
        "audio_alarm": "设置音频闹钟",
        "buzzer_alarm": "设置蜂鸣器闹钟",
        "stop_audio_alarm": "停止音频闹钟",
        "stop_buzzer_alarm": "停止蜂鸣器闹钟",
        "check_weather": "查看天气",
        "start_timer": "启动倒计时",
        "stop_timer": "停止倒计时",
        "change_alarm_sound": "更改闹钟铃声",
        "exit": "退出",
        "error": "发生错误，请重试。",
    },
    "ko": {  # 韩文
        "welcome": "라즈베리파이 스마트 알람을 환영합니다!",
        "choose_function": "기능을 선택하세요:",
        "current_time": "현재 시간 표시",
        "audio_alarm": "오디오 알람 설정",
        "buzzer_alarm": "부저 알람 설정",
        "stop_audio_alarm": "오디오 알람 정지",
        "stop_buzzer_alarm": "부저 알람 정지",
        "check_weather": "날씨 확인",
        "start_timer": "타이머 시작",
        "stop_timer": "타이머 정지",
        "change_alarm_sound": "알람 음악 변경",
        "exit": "종료",
        "error": "오류가 발생했습니다. 다시 시도해 주세요.",
    }
}

# 默认语言
current_language = "zh"

def set_language(lang_code):
    global current_language
    if lang_code in LANGUAGES:
        current_language = lang_code
    else:
        raise ValueError("Unsupported language code.")

def t(key):
    return LANGUAGES[current_language].get(key, key)
