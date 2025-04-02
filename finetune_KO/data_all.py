data_all = [
    [
        {
            "from": "human",
            "value": "Input: 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 조명 하나만 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 조명 하나만 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 모든 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 모든 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"off\") {\n    all(#Light).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"on\") {\n    all(#Light #balcony).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"off\") {\n    all(#Light #balcony).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 마이룸 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 마이룸 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"off\") {\n    all(#Light #myroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현관 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현관 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"off\") {\n    all(#Light #entrance).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"off\") {\n    all(#Light #bedroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"off\") {\n    all(#Light #bathroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"off\") {\n    all(#Light #livingroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 모든 조명 색상을 빨간색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 모든 조명 색상을 파란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 모든 조명 색상을 녹색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 모든 조명 색상을 흰색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"white\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 모든 조명 색상을 노란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"yellow\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 모든 조명 색상을 보라색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"purple\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 조명 색상을 빨간색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"on\") {\n    all(#Light #balcony).on()\n}\nall(#Light #balcony).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 조명 색상을 파란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"on\") {\n    all(#Light #balcony).on()\n}\nall(#Light #balcony).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 조명 색상을 녹색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"on\") {\n    all(#Light #balcony).on()\n}\nall(#Light #balcony).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 조명 색상을 흰색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"on\") {\n    all(#Light #balcony).on()\n}\nall(#Light #balcony).setColor(\"white\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 조명 색상을 노란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"on\") {\n    all(#Light #balcony).on()\n}\nall(#Light #balcony).setColor(\"yellow\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 조명 색상을 보라색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"on\") {\n    all(#Light #balcony).on()\n}\nall(#Light #balcony).setColor(\"purple\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 마이룸 조명 색상을 빨간색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nall(#Light #myroom).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 마이룸 조명 색상을 파란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nall(#Light #myroom).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 마이룸 조명 색상을 녹색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nall(#Light #myroom).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 마이룸 조명 색상을 흰색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nall(#Light #myroom).setColor(\"white\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 마이룸 조명 색상을 노란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nall(#Light #myroom).setColor(\"yellow\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 마이룸 조명 색상을 보라색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nall(#Light #myroom).setColor(\"purple\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 입구 조명 색상을 빨간색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}\nall(#Light #entrance).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 입구 조명 색상을 파란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}\nall(#Light #entrance).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 입구 조명 색상을 녹색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}\nall(#Light #entrance).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 입구 조명 색상을 흰색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}\nall(#Light #entrance).setColor(\"white\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 입구 조명 색상을 노란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}\nall(#Light #entrance).setColor(\"yellow\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 입구 조명 색상을 보라색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}\nall(#Light #entrance).setColor(\"purple\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 조명 색상을 빨간색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}\nall(#Light #bedroom).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 조명 색상을 파란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}\nall(#Light #bedroom).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 조명 색상을 녹색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}\nall(#Light #bedroom).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 조명 색상을 흰색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}\nall(#Light #bedroom).setColor(\"white\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 조명 색상을 노란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}\nall(#Light #bedroom).setColor(\"yellow\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 조명 색상을 보라색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}\nall(#Light #bedroom).setColor(\"purple\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실 조명 색상을 빨간색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}\nall(#Light #bathroom).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실 조명 색상을 파란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}\nall(#Light #bathroom).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실 조명 색상을 녹색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}\nall(#Light #bathroom).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실 조명 색상을 흰색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}\nall(#Light #bathroom).setColor(\"white\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실 조명 색상을 노란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}\nall(#Light #bathroom).setColor(\"yellow\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실 조명 색상을 보라색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}\nall(#Light #bathroom).setColor(\"purple\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 조명 색상을 빨간색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nall(#Light #livingroom).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 조명 색상을 파란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nall(#Light #livingroom).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 조명 색상을 녹색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nall(#Light #livingroom).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 조명 색상을 흰색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nall(#Light #livingroom).setColor(\"white\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 조명 색상을 노란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nall(#Light #livingroom).setColor(\"yellow\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 조명 색상을 보라색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nall(#Light #livingroom).setColor(\"purple\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 및 마이룸 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #balcony).switch != \"on\"){\n    all(#Light #balcony).on()\n}\nif(any(#Light #myroom).switch != \"on\"){\n    all(#Light #myroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 및 마이룸 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #balcony).switch != \"off\"){\n    all(#Light #balcony).off()\n}\nif(any(#Light #myroom).switch != \"off\"){\n    all(#Light #myroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현관 및 침실 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #entrance).switch != \"on\"){\n    all(#Light #entrance).on()\n}\nif(any(#Light #bedroom).switch != \"on\"){\n    all(#Light #bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현관 및 침실 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #entrance).switch != \"off\"){\n    all(#Light #entrance).off()\n}\nif(any(#Light #bedroom).switch != \"off\"){\n    all(#Light #bedroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실 및 거실 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #bathroom).switch != \"on\"){\n    all(#Light #bathroom).on()\n}\nif(any(#Light #livingroom).switch != \"on\"){\n    all(#Light #livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 화장실 및 거실 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #bathroom).switch != \"off\"){\n    all(#Light #bathroom).off()\n}\nif(any(#Light #livingroom).switch != \"off\"){\n    all(#Light #livingroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 10초 후 모든 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(10 SEC)\nif (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 10초 후 모든 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(10 SEC)\nif (any(#Light).switch != \"off\") {\n    all(#Light).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 1분 후 발코니 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(1 MIN)\nif (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 38초 후 발코니 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(38 SEC)\nif (any(#Light #balcony).switch != \"off\") {\n    all(#Light #balcony).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 1초 후 마이룸 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(1 SEC)\nif (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 1시간 후 마이룸 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(1 HOUR)\nif (any(#Light #myroom).switch != \"off\") {\n    all(#Light #myroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 23초 후 현관 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(23 SEC)\nif (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 100초 후 현관 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(100 SEC)\nif (any(#Light #entrance).switch != \"off\") {\n    all(#Light #entrance).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 15초 후에 침실 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(15 SEC)\nif (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 2시간 후 침실 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(2 HOUR)\nif (any(#Light #bedroom).switch != \"off\") {\n    all(#Light #bedroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 5초 후에 욕실 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(5 SEC)\nif (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 80초 후 화장실 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(80 SEC)\nif (any(#Light #bathroom).switch != \"off\") {\n    all(#Light #bathroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 2분 후에 거실 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(2 MIN)\nif (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 10초 후 거실 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(10 SEC)\nif (any(#Light #livingroom).switch != \"off\") {\n    all(#Light #livingroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 10초 후 모든 조명 색상을 빨간색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(10 SEC)\nif (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 10초 후 모든 조명 색상을 파란색으로 설정해줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(10 SEC)\nif (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 조명을 켜고 2분 후에 마이룸 조명을 꺼줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nwait until(2 MIN)\nif (any(#Light #myroom).switch != \"off\") {\n    all(#Light #myroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 조명을 끄고 10초 후에 마이룸 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"off\") {\n    all(#Light #balcony).off()\n}\nwait until(1 SEC)\nif (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현관 조명을 켜고 5초 후에 침실 조명을 꺼줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}\nwait until(5 SEC)\nif (any(#Light #bedroom).switch != \"off\") {\n    all(#Light #bedroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현관 조명을 끄고 30초 후에 침실 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"off\") {\n    all(#Light #entrance).off()\n}\nwait until(30 SEC)\nif (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 7시에 욕실 조명을 켜고 오전 8시에 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 7 and (#Clock).minute == 0){\n        if (any(#Light #bathroom).switch != \"on\") {\n            all(#Light #bathroom).on()\n        }\n    }\n    if((#Clock).hour == 8 and (#Clock).minute == 0){\n        if (any(#Light #bathroom).switch != \"off\") {\n            all(#Light #bathroom).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 10시에 거실 조명을 끄고 오전 6시에 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 22 and (#Clock).minute == 0){\n        all(#Light #livingroom).off()\n    }\n    if((#Clock).hour == 6 and (#Clock).minute == 0 ){\n        if (any(#Light #livingroom).switch != \"on\") {\n            all(#Light #livingroom).on()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 모든 조명 색상을 오후 10시에 빨간색으로 설정하고 오전 6시에 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 22 and (#Clock).minute == 0){\n        if (any(#Light).switch != \"on\") {\n            all(#Light).on()\n        }\n        all(#Light).setColor(\"red\")\n    }\n    if((#Clock).hour == 6 and (#Clock).minute == 0){\n        if (any(#Light).switch != \"off\") {\n            all(#Light).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오후 3시가 되면 주변에 아무도 없으면 모든 조명을 꺼줘.\n\nServices: {'PresenceSensor': 'Functions : []\\nValues : [\\n    presence : string {\"present\"|\"not_present\"}\\n]\\nTags : []', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\nif((#Clock).hour == 15 and (#Clock).minute ==0){\n    if((#PresenceSensor).presence == \"not_present\"){\n        if (any(#Light).switch != \"off\") {\n            all(#Light).off()\n        }\n    }\n  }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오후 3시에 아무도 없을 때 거실 조명을 꺼줘.\n\nServices: {'PresenceSensor': 'Functions : []\\nValues : [\\n    presence : string {\"present\"|\"not_present\"}\\n]\\nTags : []', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\nif((#Clock).hour == 15 and (#Clock).minute ==0){\n    if((#PresenceSensor).presence == \"not_present\"){\n        if (any(#Light #livingroom).switch != \"off\") {\n            all(#Light #livingroom).off()\n        }\n    }\n  }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실의 모든 조명을 켜고 내 방의 조명 하나만 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\n(#Light #myroom).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실, 내 방, 욕실의 모든 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nif (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nif (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실과 내 방의 조명을 파란색으로 바꾸기\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nall(#Light #livingroom).setColor(\"blue\")\nif (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nall(#Light #myroom).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실 조명 하나만 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #bathroom).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현관 조명 하나만 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #entrance).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 16초 후에 발코니 조명 하나만 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(16 SEC)\n(#Light #balcony).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 조명 하나만 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #balcony).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 조명 하나만 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #balcony).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 마이룸 조명 하나만 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #myroom).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 마이룸 조명 하나만 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #myroom).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현관 조명 하나만 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #entrance).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현관 조명 하나만 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #entrance).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 조명 하나만 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #bedroom).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 조명 하나만 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #bedroom).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실 조명 하나만 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #bathroom).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실 조명 하나만 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #bathroom).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 조명 하나만 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #livingroom).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 조명 하나만 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #livingroom).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 소리가 감지되면 모든 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light).switch != \"on\"){\n\t    all(#Light).on()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 소리가 감지되면 모든 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light).switch != \"off\"){\n\t    all(#Light).off()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 소리가 감지되면 모든 거실 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light #livingroom).switch != \"on\"){\n\t    all(#Light #livingroom).on()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 소리가 감지되면 모든 거실 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light #livingroom).switch != \"off\"){\n\t    all(#Light #livingroom).off()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 소리가 감지되면 모든 현관 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light #entrance).switch != \"on\"){\n\t    all(#Light #entrance).on()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 소리가 감지되면 모든 입구 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light #entrance).switch != \"off\"){\n\t    all(#Light #entrance).off()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 소리가 감지되면 모든 발코니 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light #balcony).switch != \"on\"){\n\t    all(#Light #balcony).on()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 소리가 감지되면 모든 발코니 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light #balcony).switch != \"off\"){\n\t    all(#Light #balcony).off()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 7분 후 내 방과 거실의 모든 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(7 MIN)\nif(any(#Light #myroom).switch != \"on\"){\n\t    all(#Light #myroom).on()\n}\nif(any(#Light #livingroom).switch != \"on\"){\n\t    all(#Light #livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 7분 후 내 방과 거실의 모든 조명을 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(7 MIN)\nif(any(#Light #myroom).switch != \"off\"){\n\t    all(#Light #myroom).off()\n}\nif(any(#Light #livingroom).switch != \"off\"){\n\t    all(#Light #livingroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 7분 후 침실과 거실의 모든 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(7 MIN)\nif(any(#Light #bedroom).switch != \"on\"){\n\t    all(#Light #bedroom).on()\n}\nif(any(#Light #bedroom).switch != \"on\"){\n\t    all(#Light #bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 7분 후 침실과 거실의 모든 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(7 MIN)\nif(any(#Light #bedroom).switch != \"off\"){\n\t    all(#Light #bedroom).off()\n}\nif(any(#Light #bedroom).switch != \"off\"){\n\t    all(#Light #bedroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 7분 후 침실과 발코니의 모든 조명을 소등해줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(7 MIN)\nif(any(#Light #bedroom).switch != \"off\"){\n\t    all(#Light #bedroom).off()\n}\nif(any(#Light #balcony).switch != \"off\"){\n\t    all(#Light #balcony).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실의 에어컨 및 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#AirConditioner #livingroom).switch != \"on\"){\nall(#AirConditioner #livingroom).on()\n}\nif(any(#Light #livingroom).switch != \"on\"){\nall(#Light #livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실의 공기청정기 및 조명 켜줘\n\nServices: {'AirPurifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\\n]\\nTags : [\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#AirPurifier #livingroom).switch != \"on\"){\nall(#AirConditioner #livingroom).on()\n}\nif(any(#Light #livingroom).switch != \"on\"){\nall(#Light #livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니의 에어컨과 조명 켜줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#AirConditioner #balcony).switch != \"on\"){\nall(#AirConditioner #balcony).on()\n}\nif(any(#Light #balcony).switch != \"on\"){\nall(#Light #balcony).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 공기청정기와 발코니 조명 켜줘\n\nServices: {'AirPurifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\\n]\\nTags : [\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#AirPurifier #balcony).switch != \"on\"){\nall(#AirConditioner #balcony).on()\n}\nif(any(#Light #balcony).switch != \"on\"){\nall(#Light #balcony).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 1시에 거실 조명과 내 방 로봇 청소기를 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'RobotCleaner': 'Functions : [\\n    on(),\\n    off(),\\n    setRobotCleanerCleaningMode(string mode{\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"})\\n]\\nValues : [\\n    switch : string {\"on\"|\"off\"},\\n    robotCleanerCleaningMode : string {\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"}\\n\\n]\\nTags : [\\n    livingroom\\n]', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 13 and (#Clock).minute == 0){\n\tif(any(#Light #livingroom).switch != \"on\"){\n\t    all(#Light #livingroom).on()\n        }\n\tif(any(#RobotCleaner #myroom).switch != \"on\"){\n\t    all(#RobotCleaner #myroom).on()\t\n        }\n   }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 1시마다 내 방 조명을 끄고 거실 로봇 청소기를 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'RobotCleaner': 'Functions : [\\n    on(),\\n    off(),\\n    setRobotCleanerCleaningMode(string mode{\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"})\\n]\\nValues : [\\n    switch : string {\"on\"|\"off\"},\\n    robotCleanerCleaningMode : string {\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"}\\n\\n]\\nTags : [\\n    livingroom\\n]', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 13 and (#Clock).minute == 0){\n\tif(any(#Light #myroom).switch != \"off\"){\n\t    all(#Light #myroom).off()\n        }\n\tif(any(#RobotCleaner #livingroom).switch != \"on\"){\n\t    all(#RobotCleaner #livingroom).on()\t\n        }\n   }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 1시마다 방 조명을 끄고 주방 식기세척기를 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 13 and (#Clock).minute == 0){\n\tif(any(#Light #myroom).switch != \"off\"){\n\t    all(#Light #myroom).off()\n        }\n\tif(any(#Dishwasher #kitchen).switch != \"on\"){\n\t    all(#Dishwasher #kitchen).on()\t\n        }\n   }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 내 방 조명을 파란색으로 켜고 오후 1시마다 거실 로봇 청소기를 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 13 and (#Clock).minute == 0){\n\tif(any(#Light #livingroom).switch != \"on\"){\n\t    all(#Light #livingroom).on()\n        }\n\tall(#Light #livingroom).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: if(any(#로봇청소기 #마이룸).switch != \"on\"){\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'RobotCleaner': 'Functions : [\\n    on(),\\n    off(),\\n    setRobotCleanerCleaningMode(string mode{\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"})\\n]\\nValues : [\\n    switch : string {\"on\"|\"off\"},\\n    robotCleanerCleaningMode : string {\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"}\\n\\n]\\nTags : [\\n    livingroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "all(#RobotCleaner #myroom).on()\t\n        }\n   }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 3시간마다 내 방 조명 꺼줘\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(3 HOUR){\n\tif(any(#Light #myroom).switch != \"off\"){\n\t    all(#Light #livingroom).off()\n        }\n\t\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 2시간 후 모든 표시등을 녹색으로 설정해줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(2 HOUR)\nif(any(#Light).switch != \"on\"){\n\t    all(#Light).on()\n}\nall(#Light).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 25초 후 모든 거실 조명을 빨간색으로 설정해줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(25 SEC)\nif(any(#Light #Livingroom).switch != \"on\"){\n\t    all(#Light #Livingroom).on()\n}\nall(#Light #Livingroom).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실과 내 방의 에어컨과 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#AirConditioner #livingroom).switch != \"on\"){\n    all(#AirConditioner #livingroom).on()\n}\nif(any(#Light #livingroom).switch != \"on\"){\n    all(#Light #livingroom).on()\n}\nif(any(#AirConditioner #myroom).switch != \"on\"){\n    all(#AirConditioner #myroom).on()\n}\nif(any(#Light #myroom).switch != \"on\"){\n    all(#Light #myroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실과 내 방의 에어컨과 조명을 꺼줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#AirConditioner #livingroom).switch != \"off\"){\n    all(#AirConditioner #livingroom).off()\n}\nif(any(#Light #livingroom).switch != \"off\"){\n    all(#Light #livingroom).off()\n}\nif(any(#AirConditioner #myroom).switch != \"off\"){\n    all(#AirConditioner #myroom).off()\n}\nif(any(#Light #myroom).switch != \"off\"){\n    all(#Light #myroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 조명을 켜고 10분 후에 꺼줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #livingroom).switch != \"on\"){\n    all(#Light #livingroom).on()\n}\nwait until(10 MIN)\nif(any(#Light #livingroom).switch != \"off\"){\n    all(#Light #livingroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 조명을 끄고 10분 후에 다시 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #livingroom).switch != \"off\"){\n    all(#Light #livingroom).off()\n}\nwait until(10 MIN)\nif(any(#Light #livingroom).switch != \"on\"){\n    all(#Light #livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 내 방 조명을 끄고 10분 후에 다시 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #myroom).switch != \"off\"){\n    all(#Light #myroom).off()\n}\nwait until(10 MIN)\nif(any(#Light #myroom).switch != \"on\"){\n    all(#Light #myroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현관 조명을 끄고 10분 후에 다시 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #entrance).switch != \"off\"){\n    all(#Light #entrance).off()\n}\nwait until(10 MIN)\nif(any(#Light #entrance).switch != \"on\"){\n    all(#Light #entrance).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 조명을 끄고 10분 후에 다시 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #bedroom).switch != \"off\"){\n    all(#Light #bedroom).off()\n}\nwait until(10 MIN)\nif(any(#Light #bedroom).switch != \"on\"){\n    all(#Light #bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 조명을 끄고 10분 후에 다시 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #balcony).switch != \"off\"){\n    all(#Light #balcony).off()\n}\nwait until(10 MIN)\nif(any(#Light #balcony).switch != \"on\"){\n    all(#Light #balcony).on()\n}"
        }
    ]
]
