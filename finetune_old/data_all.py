data_all = [
    [
        {
            "from": "human",
            "value": "Input: Turn on a light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off a light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on just one light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off just one light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn all lights on\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn all lights off\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"off\") {\n    all(#Light).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the balcony light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"on\") {\n    all(#Light #balcony).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the balcony light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"off\") {\n    all(#Light #balcony).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the myroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the myroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"off\") {\n    all(#Light #myroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the entrance light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the entrance light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"off\") {\n    all(#Light #entrance).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the bedroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the bedroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"off\") {\n    all(#Light #bedroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the bathroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the bathroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"off\") {\n    all(#Light #bathroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the livingroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the livingroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"off\") {\n    all(#Light #livingroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set all lights color to red\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set all lights color to blue\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set all lights color to green\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set all lights color to white\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"white\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set all lights color to yellow\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"yellow\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set all lights color to purple\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"purple\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set balcony light color to red\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"on\") {\n    all(#Light #balcony).on()\n}\nall(#Light #balcony).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set balcony light color to blue\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"on\") {\n    all(#Light #balcony).on()\n}\nall(#Light #balcony).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set balcony light color to green\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"on\") {\n    all(#Light #balcony).on()\n}\nall(#Light #balcony).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set balcony light color to white\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"on\") {\n    all(#Light #balcony).on()\n}\nall(#Light #balcony).setColor(\"white\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set balcony light color to yellow\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"on\") {\n    all(#Light #balcony).on()\n}\nall(#Light #balcony).setColor(\"yellow\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set balcony light color to purple\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"on\") {\n    all(#Light #balcony).on()\n}\nall(#Light #balcony).setColor(\"purple\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set myroom light color to red\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nall(#Light #myroom).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set myroom light color to blue\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nall(#Light #myroom).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set myroom light color to green\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nall(#Light #myroom).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set myroom light color to white\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nall(#Light #myroom).setColor(\"white\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set myroom light color to yellow\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nall(#Light #myroom).setColor(\"yellow\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set myroom light color to purple\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nall(#Light #myroom).setColor(\"purple\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set entrance light color to red\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}\nall(#Light #entrance).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set entrance light color to blue\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}\nall(#Light #entrance).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set entrance light color to green\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}\nall(#Light #entrance).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set entrance light color to white\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}\nall(#Light #entrance).setColor(\"white\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set entrance light color to yellow\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}\nall(#Light #entrance).setColor(\"yellow\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set entrance light color to purple\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}\nall(#Light #entrance).setColor(\"purple\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set bedroom light color to red\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}\nall(#Light #bedroom).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set bedroom light color to blue\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}\nall(#Light #bedroom).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set bedroom light color to green\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}\nall(#Light #bedroom).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set bedroom light color to white\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}\nall(#Light #bedroom).setColor(\"white\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set bedroom light color to yellow\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}\nall(#Light #bedroom).setColor(\"yellow\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set bedroom light color to purple\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}\nall(#Light #bedroom).setColor(\"purple\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set bathroom light color to red\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}\nall(#Light #bathroom).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set bathroom light color to blue\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}\nall(#Light #bathroom).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set bathroom light color to green\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}\nall(#Light #bathroom).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set bathroom light color to white\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}\nall(#Light #bathroom).setColor(\"white\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set bathroom light color to yellow\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}\nall(#Light #bathroom).setColor(\"yellow\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set bathroom light color to purple\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}\nall(#Light #bathroom).setColor(\"purple\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set livingroom light color to red\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nall(#Light #livingroom).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set livingroom light color to blue\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nall(#Light #livingroom).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set livingroom light color to green\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nall(#Light #livingroom).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set livingroom light color to white\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nall(#Light #livingroom).setColor(\"white\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set livingroom light color to yellow\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nall(#Light #livingroom).setColor(\"yellow\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set livingroom light color to purple\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nall(#Light #livingroom).setColor(\"purple\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the balcony and myroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #balcony).switch != \"on\"){\n    all(#Light #balcony).on()\n}\nif(any(#Light #myroom).switch != \"on\"){\n    all(#Light #myroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the balcony and myroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #balcony).switch != \"off\"){\n    all(#Light #balcony).off()\n}\nif(any(#Light #myroom).switch != \"off\"){\n    all(#Light #myroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the entrance and bedroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #entrance).switch != \"on\"){\n    all(#Light #entrance).on()\n}\nif(any(#Light #bedroom).switch != \"on\"){\n    all(#Light #bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the entrance and bedroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #entrance).switch != \"off\"){\n    all(#Light #entrance).off()\n}\nif(any(#Light #bedroom).switch != \"off\"){\n    all(#Light #bedroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the bathroom and livingroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #bathroom).switch != \"on\"){\n    all(#Light #bathroom).on()\n}\nif(any(#Light #livingroom).switch != \"on\"){\n    all(#Light #livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the bathroom and livingroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #bathroom).switch != \"off\"){\n    all(#Light #bathroom).off()\n}\nif(any(#Light #livingroom).switch != \"off\"){\n    all(#Light #livingroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on all lights after 10 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(10 SEC)\nif (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off all lights after 10 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(10 SEC)\nif (any(#Light).switch != \"off\") {\n    all(#Light).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the balcony light after 1 minutes\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(1 MIN)\nif (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the balcony light after 38 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(38 SEC)\nif (any(#Light #balcony).switch != \"off\") {\n    all(#Light #balcony).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the myroom light after 1 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(1 SEC)\nif (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the myroom light after 1 hour\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(1 HOUR)\nif (any(#Light #myroom).switch != \"off\") {\n    all(#Light #myroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the entrance light after 23 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(23 SEC)\nif (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the entrance light after 100 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(100 SEC)\nif (any(#Light #entrance).switch != \"off\") {\n    all(#Light #entrance).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the bedroom light after 15 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(15 SEC)\nif (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the bedroom light after 2 hours\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(2 HOUR)\nif (any(#Light #bedroom).switch != \"off\") {\n    all(#Light #bedroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the bathroom light after 5 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(5 SEC)\nif (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the bathroom light after 80 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(80 SEC)\nif (any(#Light #bathroom).switch != \"off\") {\n    all(#Light #bathroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the livingroom light after 2 minutes\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(2 MIN)\nif (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the livingroom light after 10 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(10 SEC)\nif (any(#Light #livingroom).switch != \"off\") {\n    all(#Light #livingroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set all lights color to red after 10 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(10 SEC)\nif (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set all lights color to blue after 10 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(10 SEC)\nif (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nall(#Light).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the balcony light and turn off the myroom light after 2 minutes\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light).switch != \"on\") {\n    all(#Light).on()\n}\nwait until(2 MIN)\nif (any(#Light #myroom).switch != \"off\") {\n    all(#Light #myroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the balcony light and turn on the myroom light after 10 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #balcony).switch != \"off\") {\n    all(#Light #balcony).off()\n}\nwait until(1 SEC)\nif (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the entrance light and turn off the bedroom light after 5 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"on\") {\n    all(#Light #entrance).on()\n}\nwait until(5 SEC)\nif (any(#Light #bedroom).switch != \"off\") {\n    all(#Light #bedroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the entrance light and turn on the bedroom light after 30 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #entrance).switch != \"off\") {\n    all(#Light #entrance).off()\n}\nwait until(30 SEC)\nif (any(#Light #bedroom).switch != \"on\") {\n    all(#Light #bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the bathroom light in 7 am and turn off at 8 am\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 7 and (#Clock).minute == 0){\n        if (any(#Light #bathroom).switch != \"on\") {\n            all(#Light #bathroom).on()\n        }\n    }\n    if((#Clock).hour == 8 and (#Clock).minute == 0){\n        if (any(#Light #bathroom).switch != \"off\") {\n            all(#Light #bathroom).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the livingroom light in 10 pm and turn on at 6 am\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 22 and (#Clock).minute == 0){\n        all(#Light #livingroom).off()\n    }\n    if((#Clock).hour == 6 and (#Clock).minute == 0 ){\n        if (any(#Light #livingroom).switch != \"on\") {\n            all(#Light #livingroom).on()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set all lights color to red in 10 pm and turn off at 6 am\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 22 and (#Clock).minute == 0){\n        if (any(#Light).switch != \"on\") {\n            all(#Light).on()\n        }\n        all(#Light).setColor(\"red\")\n    }\n    if((#Clock).hour == 6 and (#Clock).minute == 0){\n        if (any(#Light).switch != \"off\") {\n            all(#Light).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Every day at 3pm, turn off all the lights if no one is around.\n\nServices: {'PresenceSensor': 'Functions : []\\nValues : [\\n    presence : string {\"present\"|\"not_present\"}\\n]\\nTags : []', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\nif((#Clock).hour == 15 and (#Clock).minute ==0){\n    if((#PresenceSensor).presence == \"not_present\"){\n        if (any(#Light).switch != \"off\") {\n            all(#Light).off()\n        }\n    }\n  }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the living room light at 3pm every day when no one is there.\n\nServices: {'PresenceSensor': 'Functions : []\\nValues : [\\n    presence : string {\"present\"|\"not_present\"}\\n]\\nTags : []', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\nif((#Clock).hour == 15 and (#Clock).minute ==0){\n    if((#PresenceSensor).presence == \"not_present\"){\n        if (any(#Light #livingroom).switch != \"off\") {\n            all(#Light #livingroom).off()\n        }\n    }\n  }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on all the lights in the living room and one light in my room.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\n(#Light #myroom).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on all the lights in the living room, my room, and the bathroom.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nif (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nif (any(#Light #bathroom).switch != \"on\") {\n    all(#Light #bathroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn the lights in the living room and my room blue\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if (any(#Light #livingroom).switch != \"on\") {\n    all(#Light #livingroom).on()\n}\nall(#Light #livingroom).setColor(\"blue\")\nif (any(#Light #myroom).switch != \"on\") {\n    all(#Light #myroom).on()\n}\nall(#Light #myroom).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on just one bathroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #bathroom).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on just one entrance light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #entrance).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on only one balcony light after 16 seconds\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(16 SEC)\n(#Light #balcony).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on just one balcony light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #balcony).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off just one balcony light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #balcony).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on just one myroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #myroom).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off just one myroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #myroom).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on just one entrance light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #entrance).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off just one entrance light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #entrance).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on just one bedroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #bedroom).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off just one bedroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #bedroom).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on just one bathroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #bathroom).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off just one bathroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #bathroom).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on just one livingroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #livingroom).on()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off just one livingroom light\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "(#Light #livingroom).off()"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on all light if sound is detected\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light).switch != \"on\"){\n\t    all(#Light).on()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off all light if sound is detected\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light).switch != \"off\"){\n\t    all(#Light).off()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on all living room light if sound is detected\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light #livingroom).switch != \"on\"){\n\t    all(#Light #livingroom).on()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off all living room light if sound is detected\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light #livingroom).switch != \"off\"){\n\t    all(#Light #livingroom).off()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on all entrance light if sound is detected\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light #entrance).switch != \"on\"){\n\t    all(#Light #entrance).on()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off all entrance light if sound is detected\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light #entrance).switch != \"off\"){\n\t    all(#Light #entrance).off()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on all balcony light if sound is detected\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light #balcony).switch != \"on\"){\n\t    all(#Light #balcony).on()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off all balcony light if sound is detected\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]', 'SoundSensor': 'Functions : []\\nValues : [\\n    sound : string {\"detected\"|\"not_detected\"},\\n\\tsoundPressureLevel : double [0 ~ 194]\\n]\\nTags : []'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#SoundSensor).sound == \"detected\"){\n\tif(any(#Light #balcony).switch != \"off\"){\n\t    all(#Light #balcony).off()\n         }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on all lights in my room and living room 7 minutes later\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(7 MIN)\nif(any(#Light #myroom).switch != \"on\"){\n\t    all(#Light #myroom).on()\n}\nif(any(#Light #livingroom).switch != \"on\"){\n\t    all(#Light #livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off all lights in my room and living room 7 minutes later\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(7 MIN)\nif(any(#Light #myroom).switch != \"off\"){\n\t    all(#Light #myroom).off()\n}\nif(any(#Light #livingroom).switch != \"off\"){\n\t    all(#Light #livingroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on all lights in bedroom and living room 7 minutes later\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(7 MIN)\nif(any(#Light #bedroom).switch != \"on\"){\n\t    all(#Light #bedroom).on()\n}\nif(any(#Light #bedroom).switch != \"on\"){\n\t    all(#Light #bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off all lights in bedroom and living room 7 minutes later\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(7 MIN)\nif(any(#Light #bedroom).switch != \"off\"){\n\t    all(#Light #bedroom).off()\n}\nif(any(#Light #bedroom).switch != \"off\"){\n\t    all(#Light #bedroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off all lights in bedroom and balcony 7 minutes later\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(7 MIN)\nif(any(#Light #bedroom).switch != \"off\"){\n\t    all(#Light #bedroom).off()\n}\nif(any(#Light #balcony).switch != \"off\"){\n\t    all(#Light #balcony).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on air conditioner and light in living room\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#AirConditioner #livingroom).switch != \"on\"){\nall(#AirConditioner #livingroom).on()\n}\nif(any(#Light #livingroom).switch != \"on\"){\nall(#Light #livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on air purifier and light in living room\n\nServices: {'AirPurifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\\n]\\nTags : [\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#AirPurifier #livingroom).switch != \"on\"){\nall(#AirConditioner #livingroom).on()\n}\nif(any(#Light #livingroom).switch != \"on\"){\nall(#Light #livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on air conditioner and light in balcony\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#AirConditioner #balcony).switch != \"on\"){\nall(#AirConditioner #balcony).on()\n}\nif(any(#Light #balcony).switch != \"on\"){\nall(#Light #balcony).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on air purifier and light in balcony\n\nServices: {'AirPurifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\\n]\\nTags : [\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#AirPurifier #balcony).switch != \"on\"){\nall(#AirConditioner #balcony).on()\n}\nif(any(#Light #balcony).switch != \"on\"){\nall(#Light #balcony).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on living room lights and my room robot cleaner every 1p.m.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'RobotCleaner': 'Functions : [\\n    on(),\\n    off(),\\n    setRobotCleanerCleaningMode(string mode{\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"})\\n]\\nValues : [\\n    switch : string {\"on\"|\"off\"},\\n    robotCleanerCleaningMode : string {\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"}\\n\\n]\\nTags : [\\n    livingroom\\n]', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 13 and (#Clock).minute == 0){\n\tif(any(#Light #livingroom).switch != \"on\"){\n\t    all(#Light #livingroom).on()\n        }\n\tif(any(#RobotCleaner #myroom).switch != \"on\"){\n\t    all(#RobotCleaner #myroom).on()\t\n        }\n   }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off my room lights and turn on living room robot cleaner every 1p.m.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'RobotCleaner': 'Functions : [\\n    on(),\\n    off(),\\n    setRobotCleanerCleaningMode(string mode{\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"})\\n]\\nValues : [\\n    switch : string {\"on\"|\"off\"},\\n    robotCleanerCleaningMode : string {\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"}\\n\\n]\\nTags : [\\n    livingroom\\n]', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 13 and (#Clock).minute == 0){\n\tif(any(#Light #myroom).switch != \"off\"){\n\t    all(#Light #myroom).off()\n        }\n\tif(any(#RobotCleaner #livingroom).switch != \"on\"){\n\t    all(#RobotCleaner #livingroom).on()\t\n        }\n   }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off my room lights and turn on kitchen dishwasher every 1p.m.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 13 and (#Clock).minute == 0){\n\tif(any(#Light #myroom).switch != \"off\"){\n\t    all(#Light #myroom).off()\n        }\n\tif(any(#Dishwasher #kitchen).switch != \"on\"){\n\t    all(#Dishwasher #kitchen).on()\t\n        }\n   }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on my room lights as blue and turn on living room robot cleaner every 1p.m.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 13 and (#Clock).minute == 0){\n\tif(any(#Light #livingroom).switch != \"on\"){\n\t    all(#Light #livingroom).on()\n        }\n\tall(#Light #livingroom).setColor(\"blue\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: if(any(#RobotCleaner #myroom).switch != \"on\"){\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'RobotCleaner': 'Functions : [\\n    on(),\\n    off(),\\n    setRobotCleanerCleaningMode(string mode{\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"})\\n]\\nValues : [\\n    switch : string {\"on\"|\"off\"},\\n    robotCleanerCleaningMode : string {\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"}\\n\\n]\\nTags : [\\n    livingroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "all(#RobotCleaner #myroom).on()\t\n        }\n   }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off my room lights every 3 hours\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(3 HOUR){\n\tif(any(#Light #myroom).switch != \"off\"){\n\t    all(#Light #livingroom).off()\n        }\n\t\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set all lights into green 2 hours later.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(2 HOUR)\nif(any(#Light).switch != \"on\"){\n\t    all(#Light).on()\n}\nall(#Light).setColor(\"green\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set all living room lights into red 25 seconds later.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until(25 SEC)\nif(any(#Light #Livingroom).switch != \"on\"){\n\t    all(#Light #Livingroom).on()\n}\nall(#Light #Livingroom).setColor(\"red\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on living room and my room air conditioner and light.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#AirConditioner #livingroom).switch != \"on\"){\n    all(#AirConditioner #livingroom).on()\n}\nif(any(#Light #livingroom).switch != \"on\"){\n    all(#Light #livingroom).on()\n}\nif(any(#AirConditioner #myroom).switch != \"on\"){\n    all(#AirConditioner #myroom).on()\n}\nif(any(#Light #myroom).switch != \"on\"){\n    all(#Light #myroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off living room and my room air conditioner and light.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#AirConditioner #livingroom).switch != \"off\"){\n    all(#AirConditioner #livingroom).off()\n}\nif(any(#Light #livingroom).switch != \"off\"){\n    all(#Light #livingroom).off()\n}\nif(any(#AirConditioner #myroom).switch != \"off\"){\n    all(#AirConditioner #myroom).off()\n}\nif(any(#Light #myroom).switch != \"off\"){\n    all(#Light #myroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on living room lights and turn them off 10 minutes later.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #livingroom).switch != \"on\"){\n    all(#Light #livingroom).on()\n}\nwait until(10 MIN)\nif(any(#Light #livingroom).switch != \"off\"){\n    all(#Light #livingroom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off living room light and turn them on 10 minutes later.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #livingroom).switch != \"off\"){\n    all(#Light #livingroom).off()\n}\nwait until(10 MIN)\nif(any(#Light #livingroom).switch != \"on\"){\n    all(#Light #livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off my room light and turn them on 10 minutes later.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #myroom).switch != \"off\"){\n    all(#Light #myroom).off()\n}\nwait until(10 MIN)\nif(any(#Light #myroom).switch != \"on\"){\n    all(#Light #myroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off entrance light and turn them on 10 minutes later.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #entrance).switch != \"off\"){\n    all(#Light #entrance).off()\n}\nwait until(10 MIN)\nif(any(#Light #entrance).switch != \"on\"){\n    all(#Light #entrance).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off bedroom light and turn them on 10 minutes later.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #bedroom).switch != \"off\"){\n    all(#Light #bedroom).off()\n}\nwait until(10 MIN)\nif(any(#Light #bedroom).switch != \"on\"){\n    all(#Light #bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off balcony light and turn them on 10 minutes later.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]\\nTags : []', 'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    entrance,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if(any(#Light #balcony).switch != \"off\"){\n    all(#Light #balcony).off()\n}\nwait until(10 MIN)\nif(any(#Light #balcony).switch != \"on\"){\n    all(#Light #balcony).on()\n}"
        }
    ]
]