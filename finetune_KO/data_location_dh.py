data_location_dh = [
    [
        {
            "from": "human",
            "value": "Input: 매일 아침 7시에 거실 조명 켜줘\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'Light': 'Functions : [\n    on(),\n    off(),\n    setColor(color: string {\"{hue}|{saturation}|{brightness}\"})\n    setLevel(level int [0 ~ 100])\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    light : double\n]\nTags : [\n    myroom,\n    balcony,\n    entrance,\n    bedroom,\n    bathroom,\n    livingroom\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN, (#Clock).hour == 7 and (#Clock).minute == 0) {\n    if (any(#Light #livingroom).switch != \"on\"){\n      all(#Light #livingroom).on()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오후 6시에 30분 동안 내 방의 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN, (#Clock).hour == 18 and (#Clock).minute == 0) {\n    if (any(#Light #myroom).switch != \"on\"){\n    all(#Light #myroom).on()\n    }\n    wait until (30 MIN)\n    if (any(#Light #myroom).switch != \"off\"){\n    all(#Light #myroom).off()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오후 6시부터 오전 8시까지 모든 조명을 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN, (#Clock).hour >= 18 or (#Clock).hour < 8) {\n    if (any(#Light).switch != \"off\"){\n    all(#Light).off()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 아침 7시에 전등 켜줘\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN, (#Clock).hour == 7 and (#Clock).minute == 0) {\n    if ((#Light).switch != \"on\"){\n    (#Light).on()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오후 6시에 30분 동안 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN, (#Clock).hour == 18 and (#Clock).minute == 0) {\n    if ((#Light).switch != \"on\"){\n    (#Light).on()\n    }\n    wait until (30 MIN)\n    if ((#Light).switch != \"off\"){\n    (#Light).off()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오후 6시에 30분 동안 모든 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN, (#Clock).hour == 18 and (#Clock).minute == 0) {\n    if (any(#Light).switch != \"on\"){\n    all(#Light).on()\n    }\n    wait until (30 MIN)\n    if (any(#Light).switch != \"off\"){\n    all(#Light).off()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Turn off the light in balcony from 6 PM to 8 AM every day.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN, (#Clock).hour >= 18 or (#Clock).hour < 8) {\n    if (any(#Light #balcony).switch != \"off\"){\n    all(#Light #balcony).off()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오후 6시부터 오전 8시까지 조명을 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"
        },
        {
            "from": "human",
            "value": "Input: 매일 아침 7시에 거실의 전등 하나만 켜줘\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN, (#Clock).hour == 7 and (#Clock).minute == 0) {\n    if ((#Light #livingroom).switch != \"on\"){\n      (#Light #livingroom).on()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오후 6시에 30분 동안 내 방의 전등 하나만 켜줘\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN, (#Clock).hour == 18 and (#Clock).minute == 0) {\n    if ((#Light #myroom).switch != \"on\"){\n    (#Light #myroom).on()\n    }\n    wait until (30 MIN)\n    if ((#Light #myroom).switch != \"off\"){\n    (#Light #myroom).off()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오후 6시부터 오전 8시까지 현관 조명 하나를 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN, (#Clock).hour >= 18 or (#Clock).hour < 8) {\n    if ((#Light #entrance).switch != \"off\"){\n    (#Light #entrance).off()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 평일 오전 6시에 정원 관개기를 켜고 120ml로 물을 주기 시작해.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Irrigator': 'Functions : [\n    on(),\n    off(),\n    startWatering(),\n    setWaterPortion(portion: double [0 ~ 2000], unit: string {\"liters\"|\"milliliters\"|\"gallons\"|\"ounces\"})\n]\nValues : [\n    switch: string {\"on\"|\"off\"}\n]\nTags:[Garden,Greenhouse]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).weekday == \"monday\" or (#Clock).weekday == \"tuesday\" or (#Clock).weekday == \"wednesday\" or (#Clock).weekday == \"thursday\" or (#Clock).weekday == \"friday\") {\n        if ((#Clock).hour == 6 and (#Clock).minute == 0) {\n            if (any(#Irrigator #Garden).switch != \"on\") {\n                all(#Irrigator #Garden).on()\n            }\n            all(#Irrigator #Garden).setWaterPortion(120.0, \"mililiters\")\n            all(#Irrigator #Garden).startWatering()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 평일 오전 6시에 뒤뜰 관개기를 켜고 120ml로 물을 주기 시작해.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Irrigator': 'Functions : [\n    on(),\n    off(),\n    startWatering(),\n    setWaterPortion(portion: double [0 ~ 2000], unit: string {\"liters\"|\"milliliters\"|\"gallons\"|\"ounces\"})\n]\nValues : [\n    switch: string {\"on\"|\"off\"}\n]\nTags:[Backyard,Patio]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).weekday == \"monday\" or (#Clock).weekday == \"tuesday\" or (#Clock).weekday == \"wednesday\" or (#Clock).weekday == \"thursday\" or (#Clock).weekday == \"friday\") {\n        if ((#Clock).hour == 6 and (#Clock).minute == 0) {\n            if ((#Irrigator #Backyard).switch != \"on\") {\n                (#Irrigator #Backyard).on()\n            }\n            (#Irrigator #Backyard).setWaterPortion(120.0, \"mililiters\")\n            (#Irrigator #Backyard).startWatering()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 모든 관개기를 켜고 평일 오전 6시에 120ml로 물을 주기 시작해.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Irrigator': 'Functions : [\n    on(),\n    off(),\n    startWatering(),\n    setWaterPortion(portion: double [0 ~ 2000], unit: string {\"liters\"|\"milliliters\"|\"gallons\"|\"ounces\"})\n]\nValues : [\n    switch: string {\"on\"|\"off\"}\n]\nTags:[Rooftop,UrbanGarden]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).weekday == \"monday\" or (#Clock).weekday == \"tuesday\" or (#Clock).weekday == \"wednesday\" or (#Clock).weekday == \"thursday\" or (#Clock).weekday == \"friday\") {\n        if ((#Clock).hour == 6 and (#Clock).minute == 0) {\n            if (any(#Irrigator).switch != \"on\") {\n                all(#Irrigator).on()\n            }\n            all(#Irrigator).setWaterPortion(120.0, \"mililiters\")\n            all(#Irrigator).startWatering()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실의 습도가 50% 이상이면 거실에 있는 에어컨을 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[LivingRoom,Bedroom]', 'HumiditySensor': 'Functions : []\nValues : [\n    humidity : double[0 ~ 100]\n]\nTags:[Bedroom,Bathroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(10 SEC){\n    if((#HumiditySensor #Bedroom).humidity >= 50.0){\n        if(any(#AirConditioner #LivingRoom).switch != \"on\"){\n            all(#AirConditioner #LivingRoom).on()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 사무실의 습도가 50% 이상이면 회의실에 있는 에어컨을 한 대 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[], 'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[ConferenceRoom,LivingRoom]', 'HumiditySensor': 'Functions : []\nValues : [\n    humidity : double[0 ~ 100]\n]\nTags:[Office,Bathroom]'}"
        }
    ],
    [
        {
            "from": "gpt",
            "value": "loop(10 SEC){\n    if((#HumiditySensor #Office).humidity >= 50.0){\n        if((#AirConditioner #ConferenceRoom).switch != \"on\"){\n            (#AirConditioner).on()\n        }\n    }\n}"
        },
        {
            "from": "human",
            "value": "Input: 온실의 습도가 50% 이상이면 제어실의 모든 에어컨을 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[], 'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[ControlRoom,Office]', 'HumiditySensor': 'Functions : []\nValues : [\n    humidity : double[0 ~ 100]\n]\nTags:[Greenhouse,LivingRoom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(10 SEC){\n    if((#HumiditySensor #Greenhouse).humidity >= 50.0){\n        if(any(#AirConditioner #ControlRoom).switch != \"on\"){\n            all(#AirConditioner #ControlRoom).on()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 2시에 주방 냉장고를 쾌속냉각 모드로 설정해줘.\n\nServices: {\n'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []',\n'Refrigerator': 'Functions : [\n    on(),\n    off(),\n    setRefrigeratorMode(string mode{\"RapidCool\"|\"RapidFreeze\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    refrigeratorMode : string {\"RapidCool\"|\"RapidFreeze\"}\n]\nTags: [Kitchen, Garage]'\n}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 14 and (#Clock).minute == 0) {\n        if (any(#Refrigerator #Kitchen).refrigeratorMode != \"RapidCool\") {\n            all(#Refrigerator #Kitchen).setRefrigeratorMode(\"RapidCool\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 2시에 지하실 냉장고 1대를 RapidCool 모드로 설정해줘.\n\nServices: {\n'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []',\n'Refrigerator': 'Functions : [\n    on(),\n    off(),\n    setRefrigeratorMode(string mode{\"RapidCool\"|\"RapidFreeze\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    refrigeratorMode : string {\"RapidCool\"|\"RapidFreeze\"}\n]\nTags: [Basement, Pantry]'\n}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 14 and (#Clock).minute == 0) {\n        if ((#Refrigerator #Basement).refrigeratorMode != \"RapidCool\") {\n            (#Refrigerator #Basement).setRefrigeratorMode(\"RapidCool\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 정원 관개 시스템을 켜고 오후 1시에 뒤뜰 가스 밸브가 열려 있으면 170ml로 물을 주기 시작해.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'GasValve': 'Functions : [\n    open(),\n    close()\n]\nValues : [\n    valve : string {\"open\"|\"closed\"}\n]\nTags:[Backyard,Garage]', 'Irrigator': 'Functions : [\n    on(),\n    off(),\n    startWatering(),\n    setWaterPortion(portion: double [0 ~ 2000], unit: string {\"liters\"|\"milliliters\"|\"gallons\"|\"ounces\"})\n]\nValues : [\n    switch: string {\"on\"|\"off\"}\n]\nTags:[Garden,Greenhouse]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 13 and (#Clock).minute == 0) {\n        if ((#GasValve #Backyard).valve == \"open\") {\n            if ((#Irrigator #Garden).switch != \"on\") {\n                (#Irrigator #Garden).on()\n            }\n            (#Irrigator #Garden).startWatering(170)\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 잔디 관개 시스템을 켜고 오후 1시에 파티오 가스 밸브가 열려 있으면 170ml로 물을 주기 시작해.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'GasValve': 'Functions : [\n    open(),\n    close()\n]\nValues : [\n    valve : string {\"open\"|\"closed\"}\n]\nTags:[Patio,Basement]', 'Irrigator': 'Functions : [\n    on(),\n    off(),\n    startWatering(),\n    setWaterPortion(portion: double [0 ~ 2000], unit: string {\"liters\"|\"milliliters\"|\"gallons\"|\"ounces\"})\n]\nValues : [\n    switch: string {\"on\"|\"off\"}\n]\nTags:[Lawn,Orchard]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 13 and (#Clock).minute == 0) {\n        if ((#GasValve #Patio).valve == \"open\") {\n            if (any(#Irrigator #Lawn).switch != \"on\") {\n                all(#Irrigator #Lawn).on()\n            }\n            all(#Irrigator #Lawn).startWatering(170)\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 테라스 가스 밸브가 열려 있으면 화단 관개 시스템을 켜고 오후 1시에 170ml로 물을 주기 시작해.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'GasValve': 'Functions : [\n    open(),\n    close()\n]\nValues : [\n    valve : string {\"open\"|\"closed\"}\n]\nTags:[Terrace,Shed]', 'Irrigator': 'Functions : [\n    on(),\n    off(),\n    startWatering(),\n    setWaterPortion(portion: double [0 ~ 2000], unit: string {\"liters\"|\"milliliters\"|\"gallons\"|\"ounces\"})\n]\nValues : [\n    switch: string {\"on\"|\"off\"}\n]\nTags:[Flowerbed,Farm]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 13 and (#Clock).minute == 0) {\n        if ((#GasValve #Terrace).valve == \"open\") {\n            if ((#Irrigator #Flowerbed).switch != \"on\") {\n                (#Irrigator #Flowerbed).on()\n            }\n            (#Irrigator #Flowerbed).startWatering(170)\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현관문이 현재 닫혀 있는 경우 복도 스피커에 문이 닫혔다고 말해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'DoorLock': 'Functions : []\nValues : [\n    door : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"unknown\"}\n]\nTags:[FrontDoor]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[Hallway]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#DoorLock #FrontDoor).door == \"closed\") {\n    if (all(#Speaker #Hallway).switch == \"off\") {\n        all(#Speaker #Hallway).on()\n    }\n    all(#Speaker #Hallway).speak(\"문이 닫혀 있으므로 엽니다.\")\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현관문이 현재 닫혀 있는 경우 복도 스피커 한 대에 문이 닫혔다고 말해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'DoorLock': 'Functions : []\nValues : [\n    door : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"unknown\"}\n]\nTags:[FrontDoor]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[Hallway]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#DoorLock #FrontDoor).door == \"closed\") {\n    if ((#Speaker #Hallway).switch == \"off\") {\n        (#Speaker #Hallway).on()\n    }\n    (#Speaker #Hallway).speak(\"문이 닫혀 있으므로 엽니다.\")\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현관문이 현재 닫혀 있는 경우 모든 복도 스피커에 문이 닫혔다고 알려줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'DoorLock': 'Functions : []\nValues : [\n    door : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"unknown\"}\n]\nTags:[FrontDoor]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[Hallway]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#DoorLock #FrontDoor).door == \"closed\") {\n    if ((#Speaker #Hallway).switch == \"off\") {\n        all(#Speaker #Hallway).on()\n    }\n    all(#Speaker #Hallway).speak(\"문이 닫혀 있으므로 엽니다.\")\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주 출입문이 현재 닫혀 있는 경우 거실 스피커에 문이 닫혀 있다고 알려줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'DoorLock': 'Functions : []\nValues : [\n    door : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"unknown\"}\n]\nTags:[MainEntrance]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[LivingRoom]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#DoorLock #MainEntrance).door == \"closed\") {\n    if (any(#Speaker #LivingRoom).switch != \"on\") {\n        all(#Speaker #LivingRoom).on()\n    }\n    (#Speaker #LivingRoom).speak(\"문이 닫혀 있으므로 엽니다.\")\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주 출입문이 현재 닫혀 있는 경우 거실 스피커 한 대에 문이 닫혔다고 알려줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'DoorLock': 'Functions : []\nValues : [\n    door : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"unknown\"}\n]\nTags:[MainEntrance]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[\n    LivingRoom\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#DoorLock #MainEntrance).door == \"closed\") {\n    if ((#Speaker #LivingRoom).switch != \"on\") {\n        (#Speaker #LivingRoom).on()\n    }\n    (#Speaker #LivingRoom).speak(\"문이 닫혀 있으므로 엽니다.\")\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 차고 문이 현재 닫혀 있는 경우 주방 스피커에 문이 닫혀 있다고 말해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'DoorLock': 'Functions : []\nValues : [\n    door : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"unknown\"}\n]\nTags:[Garage]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[Kitchen]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#DoorLock #Garage).door == \"closed\") {\n    if (any(#Speaker #Kitchen).switch != \"on\") {\n        all(#Speaker #Kitchen).on()\n    }\n    (#Speaker #Kitchen).speak(\"문이 닫혀 있으므로 엽니다.\")\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 차고 문이 현재 닫혀 있는 경우 주방 스피커에 문이 닫혀 있다고 알려줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'DoorLock': 'Functions : []\nValues : [\n    door : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"unknown\"}\n]\nTags:[Garage]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[Kitchen]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#DoorLock #Garage).door == \"closed\") {\n    if ((#Speaker #Kitchen).switch != \"on\") {\n        (#Speaker #Kitchen).on()\n    }\n    (#Speaker #Kitchen).speak(\"문이 닫혀 있으므로 엽니다.\")\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방에서 연기가 감지되면 거실 카메라를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'SmokeDetector': 'Functions : []\nValues : [\n    smoke : string {\"detected\"|\"not_detected\"}\n]\nTags:[Kitchen,Garage]', 'Camera': 'Functions : [\n    on(),\n    off(),\n    take() : return binary : storage path for image(photo),\n    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    image : binary : the storage path for the most recent image(photo)\n]\nTags:[LivingRoom,Basement]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#SmokeDetector #Kitchen).smoke == \"detected\") {\n        if (any(#Camera #LivingRoom).switch != \"on\") {\n            all(#Camera #LivingRoom).on()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방에서 연기가 감지되면 거실에 있는 모든 카메라를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\nday : int [1~31]\nhour : int [0~23]\nminute : int [0~59]\nmonth : int [1~12]\nsecond : int [0~59]\nweekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\nyear : int [0 ~ 100000]\nisHoliday : bool {true|false}\ntimestamp : double : unixTime\n]\nTags:[]', 'SmokeDetector': 'Functions : []\nValues : [\nsmoke : string {\"detected\"|\"not_detected\"}\n]\nTags:[Kitchen,Garage]', 'Camera': 'Functions : [\non(),\noff(),\ntake() : return binary : storage path for image(photo),\ntakeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n]\nValues : [\nswitch : string {\"on\"|\"off\"},\nimage : binary : the storage path for the most recent image(photo)\n]\nTags:[LivingRoom,Basement]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\nif ((#SmokeDetector #Kitchen).smoke == \"detected\") {\n    if (any(#Camera #LivingRoom).switch != \"on\") {\n        all(#Camera #LivingRoom).on()\n    }\n}\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방에서 연기가 감지되면 거실 카메라 한 대를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\nday : int [1~31]\nhour : int [0~23]\nminute : int [0~59]\nmonth : int [1~12]\nsecond : int [0~59]\nweekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\nyear : int [0 ~ 100000]\nisHoliday : bool {true|false}\ntimestamp : double : unixTime\n]\nTags:[]', 'SmokeDetector': 'Functions : []\nValues : [\nsmoke : string {\"detected\"|\"not_detected\"}\n]\nTags:[Kitchen,Garage]', 'Camera': 'Functions : [\non(),\noff(),\ntake() : return binary : storage path for image(photo),\ntakeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n]\nValues : [\nswitch : string {\"on\"|\"off\"},\nimage : binary : the storage path for the most recent image(photo)\n]\nTags:[LivingRoom,Basement]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\nif ((#SmokeDetector #Kitchen).smoke == \"detected\") {\n    if ((#Camera #LivingRoom).switch != \"on\") {\n        (#Camera #LivingRoom).on()\n    }\n}\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 지하실에서 연기가 감지되면 복도 카메라를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'SmokeDetector': 'Functions : []\nValues : [\n    smoke : string {\"detected\"|\"not_detected\"}\n]\nTags:[Basement,Attic]', 'Camera': 'Functions : [\n    on(),\n    off(),\n    take() : return binary : storage path for image(photo),\n    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    image : binary : the storage path for the most recent image(photo)\n]\nTags:[Hallway,Garage]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#SmokeDetector #Basement).smoke == \"detected\") {\n        if (any(#Camera #Hallway).switch != \"on\") {\n            all(#Camera #Hallway).on()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on one hallway camera if smoke in the basement is detected.\n\n    Services: {'Clock': 'Functions : []\n    Values : [\n        day : int [1~31]\n        hour : int [0~23]\n        minute : int [0~59]\n        month : int [1~12]\n        second : int [0~59]\n        weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n        year : int [0 ~ 100000]\n        isHoliday : bool {true|false}\n        timestamp : double : unixTime\n    ]\n    Tags:[]', 'SmokeDetector': 'Functions : []\n    Values : [\n        smoke : string {\"detected\"|\"not_detected\"}\n    ]\n    Tags:[Basement,Attic]', 'Camera': 'Functions : [\n        on(),\n        off(),\n        take() : return binary : storage path for image(photo),\n        takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n    ]\n    Values : [\n        switch : string {\"on\"|\"off\"},\n        image : binary : the storage path for the most recent image(photo)\n    ]\n    Tags:[Hallway,Garage]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n        if ((#SmokeDetector #Basement).smoke == \"detected\") {\n            if ((#Camera #Hallway).switch != \"on\") {\n                (#Camera #Hallway).on()\n            }\n        }\n    }"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실에서 연기가 감지되면 사무실 카메라를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'SmokeDetector': 'Functions : []\nValues : [\n    smoke : string {\"detected\"|\"not_detected\"}\n]\nTags:[LivingRoom,DiningRoom]', 'Camera': 'Functions : [\n    on(),\n    off(),\n    take() : return binary : storage path for image(photo),\n    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    image : binary : the storage path for the most recent image(photo)\n]\nTags:[Office,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#SmokeDetector #LivingRoom).smoke == \"detected\") {\n        if (any(#Camera #Office).switch != \"on\") {\n            all(#Camera #Office).on()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실에서 연기가 감지되면 사무실 카메라를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\nday : int [1~31]\nhour : int [0~23]\nminute : int [0~59]\nmonth : int [1~12]\nsecond : int [0~59]\nweekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\nyear : int [0 ~ 100000]\nisHoliday : bool {true|false}\ntimestamp : double : unixTime\n]\nTags:[]', 'SmokeDetector': 'Functions : []\nValues : [\nsmoke : string {\"detected\"|\"not_detected\"}\n]\nTags:[LivingRoom,DiningRoom]', 'Camera': 'Functions : [\non(),\noff(),\ntake() : return binary : storage path for image(photo),\ntakeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n]\nValues : [\nswitch : string {\"on\"|\"off\"},\nimage : binary : the storage path for the most recent image(photo)\n]\nTags:[Office,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n  if ((#SmokeDetector #LivingRoom).smoke == \"detected\") {\n      if ((#Camera #Office).switch != \"on\") {\n          (#Camera #Office).on()\n      }\n  }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주말 오전 7시에 거실 TV를 켜고 주방에서 음악을 재생해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[Kitchen,Bathroom]',\n'Television': 'Functions : [\n    on(),\n    off(),\n    setTvChannel(tvChannel: int),\n    channelUp(),\n    channelDown(),\n    setVolume(volume: int [0 ~ 100]),\n    volumeUp(),\n    volumeDown(),\n    mute() : void, toggle muteStatus\nValues : [\n    switch : string {\"on\"|\"off\"},\n    muteStatus : string {\"muted\"|\"unmuted\"},\n    tvChannel : int\n]\nTags:[LivingRoom,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).weekday == \"saturday\" or (#Clock).weekday == \"sunday\") {\n        if ((#Clock).hour == 7 and (#Clock).minute == 0) {\n            if ((#Television #LivingRoom).switch != \"on\") {\n                all(#Television #LivingRoom).on()\n            }\n            if ((#Speaker #Kitchen).switch != \"on\") {\n                (#Speaker #Kitchen).on()\n            }\n            (#Speaker #Kitchen).play(\"music.mp3\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주말 오전 7시에 침실 TV를 켜고 욕실에서 음악을 재생해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[Bathroom,Garage]',\n'Television': 'Functions : [\n    on(),\n    off(),\n    setTvChannel(tvChannel: int),\n    channelUp(),\n    channelDown(),\n    setVolume(volume: int [0 ~ 100]),\n    volumeUp(),\n    volumeDown(),\n    mute() : void, toggle muteStatus\nValues : [\n    switch : string {\"on\"|\"off\"},\n    muteStatus : string {\"muted\"|\"unmuted\"},\n    tvChannel : int\n]\nTags:[Bedroom,Attic]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).weekday == \"saturday\" or (#Clock).weekday == \"sunday\") {\n        if ((#Clock).hour == 7 and (#Clock).minute == 0) {\n            if ((#Television #Bedroom).switch != \"on\") {\n                (#Television #Bedroom).on()\n            }\n            if ((#Speaker #Bathroom).switch != \"on\") {\n                (#Speaker #Bathroom).on()\n            }\n            (#Speaker #Bathroom).play(\"music.mp3\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주말 오전 7시에 주방 TV를 켜고 지하실에서 음악을 틀어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[Basement,Office]',\n'Television': 'Functions : [\n    on(),\n    off(),\n    setTvChannel(tvChannel: int),\n    channelUp(),\n    channelDown(),\n    setVolume(volume: int [0 ~ 100]),\n    volumeUp(),\n    volumeDown(),\n    mute() : void, toggle muteStatus\nValues : [\n    switch : string {\"on\"|\"off\"},\n    muteStatus : string {\"muted\"|\"unmuted\"},\n    tvChannel : int\n]\nTags:[Kitchen,Den]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).weekday == \"saturday\" or (#Clock).weekday == \"sunday\") {\n        if ((#Clock).hour == 7 and (#Clock).minute == 0) {\n            if ((#Television #Kitchen).switch != \"on\") {\n                (#Television #Kitchen).on()\n            }\n            if ((#Speaker #Basement).switch != \"on\") {\n                (#Speaker #Basement).on()\n            }\n            (#Speaker #Basement).play(\"music.mp3\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 11시에 주방 냉장고를 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Refrigerator': 'Functions : [\n    on(),\n    off(),\n    setRefrigeratorMode(string mode{\"RapidCool\"|\"RapidFreeze\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    refrigeratorMode : string {\"RapidCool\"|\"RapidFreeze\"}\n]\nTags:[Kitchen]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 23 and (#Clock).minute == 0) {\n        if ((#Refrigerator #Kitchen).switch != \"off\") {\n            (#Refrigerator #Kitchen).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 11시에 지하실 냉장고를 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Refrigerator': 'Functions : [\n    on(),\n    off(),\n    setRefrigeratorMode(string mode{\"RapidCool\"|\"RapidFreeze\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    refrigeratorMode : string {\"RapidCool\"|\"RapidFreeze\"}\n]\nTags:[Basement]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 23 and (#Clock).minute == 0) {\n        if ((#Refrigerator #Basement).switch != \"off\") {\n            (#Refrigerator #Basement).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 11시에 차고 냉장고를 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Refrigerator': 'Functions : [\n    on(),\n    off(),\n    setRefrigeratorMode(string mode{\"RapidCool\"|\"RapidFreeze\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    refrigeratorMode : string {\"RapidCool\"|\"RapidFreeze\"}\n]\nTags:[Garage]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 23 and (#Clock).minute == 0) {\n        if ((#Refrigerator #Garage).switch != \"off\") {\n            (#Refrigerator #Garage).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 2시간 후에 에어컨을 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[LivingRoom,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (2 HOUR)\nif ((#AirConditioner #LivingRoom).switch != \"on\") {\n    (#AirConditioner #LivingRoom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 2시간 후에 사무실 에어컨을 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[LivingRoom,Office,GuestRoom]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (2 HOUR)\nif ((#AirConditioner #Office).switch == \"off\") {\n    (#AirConditioner #Office).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 2시간 후에 주방 에어컨을 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[Bedroom,GuestRoom,Kitchen]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (2 HOUR)\nif ((#AirConditioner #Kitchen).switch == \"off\") {\n    (#AirConditioner #Kitchen).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 7시 30분에 거실 커튼을 열어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []', 'Curtain': 'Functions : [\n    setCurtainLevel(level: int [0 ~ 100])\n]\nValues : [\n    curtain : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    curtainLevel : int [0 ~ 100]\n]\nTags: [Livingroom,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 7 and (#Clock).minute == 30) {\n        if ((#Curtain #Livingroom).switch == \"off\") {\n            (#Curtain #Livingroom).on()\n        }\n        (#Curtain #Livingroom).open()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 7시 30분에 주방 커튼을 열어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []', 'Curtain': 'Functions : [\n    setCurtainLevel(level: int [0 ~ 100])\n]\nValues : [\n    curtain : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    curtainLevel : int [0 ~ 100]\n]\nTags: [Kitchen,Diningroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 7 and (#Clock).minute == 30) {\n        if ((#Curtain #Kitchen).switch == \"off\") {\n            (#Curtain #Kitchen).on()\n        }\n        (#Curtain #Kitchen).open()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 7시 30분에 침실 커튼을 열어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []', 'Curtain': 'Functions : [\n    setCurtainLevel(level: int [0 ~ 100])\n]\nValues : [\n    curtain : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    curtainLevel : int [0 ~ 100]\n]\nTags: [Bedroom,Guestroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 7 and (#Clock).minute == 30) {\n        if ((#Curtain #Bedroom).switch == \"off\") {\n            (#Curtain #Bedroom).on()\n        }\n        (#Curtain #Bedroom).open()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오후 6시에 거실 커튼을 75%까지 열어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Curtain': 'Functions : [\n    setCurtainLevel(level: int [0 ~ 100])\n]\nValues : [\n    curtain : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    curtainLevel : int [0 ~ 100]\n]\nTags:[LivingRoom,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop (1 MIN, (#Clock).hour == 18 and (#Clock).minute == 0) {\n    if ((#Curtain #LivingRoom).curtainLevel != 75) {\n        (#Curtain #LivingRoom).setCurtainLevel(75)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오후 6시에 거실 커튼을 75%까지 열어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Curtain': 'Functions : [\n    setCurtainLevel(level: int [0 ~ 100])\n]\nValues : [\n    curtain : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    curtainLevel : int [0 ~ 100]\n]\nTags:[Bedroom,Office,LivingRoom,GuestRoom]'}"
        },
        {
            "from": "gpt",
            "value": "loop (1 MIN, (#Clock).hour == 18 and (#Clock).minute == 0) {\n    if ((#Curtain #LivingRoom).curtainLevel != 75) {\n        (#Curtain #LivingRoom).setCurtainLevel(75)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오후 6시에 거실 커튼을 75%까지 열어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Curtain': 'Functions : [\n    setCurtainLevel(level: int [0 ~ 100])\n]\nValues : [\n    curtain : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    curtainLevel : int [0 ~ 100]\n]\nTags:[,Kitchen,LivingRoom,Basement,Attic]'}"
        },
        {
            "from": "gpt",
            "value": "loop (1 MIN, (#Clock).hour == 18 and (#Clock).minute == 0) {\n    if ((#Curtain #LivingRoom).curtainLevel != 75) {\n        (#Curtain #LivingRoom).setCurtainLevel(75)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실의 습도가 55% 이상이면 오후 5시에 침실 가습기를 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Humidifier': 'Functions : [\n    on(),\n    off(),\n    setHumidiferMode(mode: string {\"auto\"|\"low\"|\"medium\"|\"high\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    humidifierMode : string {\"auto\"|\"low\"|\"medium\"|\"high\"}\n]\nTags:[Bedroom]', 'HumiditySensor': 'Functions : []\nValues : [\n    humidity : double[0 ~ 100]\n]\nTags:[LivingRoom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 17 and (#Clock).minute == 0) {\n        if ((#HumiditySensor #LivingRoom).humidity > 55.0) {\n            if ((#Humidifier #Bedroom).switch == \"on\") {\n                (#Humidifier #Bedroom).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 지하실의 습도가 55% 이상이면 오후 5시에 사무실 가습기를 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Humidifier': 'Functions : [\n    on(),\n    off(),\n    setHumidiferMode(mode: string {\"auto\"|\"low\"|\"medium\"|\"high\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    humidifierMode : string {\"auto\"|\"low\"|\"medium\"|\"high\"}\n]\nTags:[Office]', 'HumiditySensor': 'Functions : []\nValues : [\n    humidity : double[0 ~ 100]\n]\nTags:[Basement]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 17 and (#Clock).minute == 0) {\n        if ((#HumiditySensor #Basement).humidity > 55.0) {\n            if ((#Humidifier #Office).switch == \"on\") {\n                (#Humidifier #Office).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 다락방의 습도가 55% 이상이면 오후 5시에 아기방 가습기를 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Humidifier': 'Functions : [\n    on(),\n    off(),\n    setHumidiferMode(mode: string {\"auto\"|\"low\"|\"medium\"|\"high\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    humidifierMode : string {\"auto\"|\"low\"|\"medium\"|\"high\"}\n]\nTags:[Nursery]', 'HumiditySensor': 'Functions : []\nValues : [\n    humidity : double[0 ~ 100]\n]\nTags:[Attic]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 17 and (#Clock).minute == 0) {\n        if ((#HumiditySensor #Attic).humidity > 55.0) {\n            if ((#Humidifier #Nursery).switch == \"on\") {\n                (#Humidifier #Nursery).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 선풍기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Fan': 'Functions : [\n    on(),\n    off(),\n    setFanSpeed(speed: int [0 ~ ∞])\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n]\nTags:[Livingroom,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Fan #Livingroom).switch == \"off\") {\n    (#Fan #Livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 선풍기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Fan': 'Functions : [\n    on(),\n    off(),\n    setFanSpeed(speed: int [0 ~ ∞])\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n]\nTags:[Bedroom,Office]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Fan #Bedroom).switch == \"off\") {\n    (#Fan #Bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방 선풍기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Fan': 'Functions : [\n    on(),\n    off(),\n    setFanSpeed(speed: int [0 ~ ∞])\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n]\nTags:[Kitchen,DiningRoom]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Fan #Kitchen).switch == \"off\") {\n    (#Fan #Kitchen).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방 블라인드가 70%인 경우 거실 커튼을 40%로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []', 'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags: [Kitchen,Bedroom]', 'Curtain': 'Functions : [\n    setCurtainLevel(level: int [0 ~ 100])\n]\nValues : [\n    curtain : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    curtainLevel : int [0 ~ 100]\n]\nTags: [LivingRoom,Basement]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Blind #Kitchen).blindLevel == 70) {\n        (#Curtain #LivingRoom).setCurtainLevel(40)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 사무실 블라인드가 70%인 경우 식당 커튼을 40%로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []', 'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags: [Office,Garage]', 'Curtain': 'Functions : [\n    setCurtainLevel(level: int [0 ~ 100])\n]\nValues : [\n    curtain : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    curtainLevel : int [0 ~ 100]\n]\nTags: [DiningRoom,Hallway]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Blind #Office).blindLevel == 70) {\n        (#Curtain #DiningRoom).setCurtainLevel(40)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 블라인드가 70%인 경우 침실 커튼을 40%로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []', 'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags: [LivingRoom,Attic]', 'Curtain': 'Functions : [\n    setCurtainLevel(level: int [0 ~ 100])\n]\nValues : [\n    curtain : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    curtainLevel : int [0 ~ 100]\n]\nTags: [Bedroom,Study]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Blind #LivingRoom).blindLevel == 70) {\n        (#Curtain #Bedroom).setCurtainLevel(40)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 지하실 건조기를 연속 제습 모드로 변경해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Basement, LaundryRoom]'}"
        },
        {
            "from": "gpt",
            "value": "\n        if((#Dehumidifier #Basement).switch != \"on\"){\n            (#Dehumidifier #Basement).on()\n        }\n        if ((#Dehumidifier #Basement).dehumidifierMode != \"continuousDehumidifying\") {\n    (#Dehumidifier #Basement).setDeHumidifierMode(\"continuousDehumidifying\")\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실 건조기를 연속 제습 모드로 변경해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Bathroom, LaundryRoom]'}"
        },
        {
            "from": "gpt",
            "value": "\n          if((#Dehumidifier #Bathroom).switch != \"on\"){\n            (#Dehumidifier #Bathroom).on()\n        }\n        if ((#Dehumidifier #Bathroom).dehumidifierMode != \"continuousDehumidifying\") {\n    (#Dehumidifier #Bathroom).setDeHumidifierMode(\"continuousDehumidifying\")\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 다락방 건조기를 연속 제습 모드로 변경해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Attic, StorageRoom]'}"
        },
        {
            "from": "gpt",
            "value": "\n        if((#Dehumidifier #Attic).switch != \"on\"){\n            (#Dehumidifier #Attic).on()\n        }\n        if ((#Dehumidifier #Attic).dehumidifierMode != \"continuousDehumidifying\") {\n    (#Dehumidifier #Attic).setDeHumidifierMode(\"continuousDehumidifying\")\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오전 6시에 거실 공기 청정기를 켜고 평일 오후 7시에 복도에서 움직임이 감지되면 사진을 찍고 거실 스피커를 통해 움직임이 감지되었다고 말해줘.\n\nServices: {\n    'Camera': 'Functions : [\n        on(),\n        off(),\n        take() : return binary : storage path for image(photo),\n        takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n    ]\n    Values : [\n        switch : string {\"on\"|\"off\"},\n        image : binary : the storage path for the most recent image(photo)\n    ]\n    Tags:[LivingRoom,Office]',\n\n    'MotionSensor': 'Functions : []\n    Values : [\n        motion : string {\"active\"|\"inactive\"}\n    ]\n    Tags:[Hallway,Garage]',\n\n    'Clock': 'Functions : []\n    Values : [\n        day : int [1~31],\n        hour : int [0~23],\n        minute : int [0~59],\n        month : int [1~12],\n        second : int [0~59],\n        weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"},\n        year : int [0 ~ 100000],\n        isHoliday : bool {true|false},\n        timestamp : double : unixTime\n    ]\n    Tags:[]',\n\n    'AirPurifier': 'Functions : [\n        on(),\n        off(),\n        setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\n    ]\n    Values : [\n        switch : string {\"on\"|\"off\"},\n        airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\n    ]\n    Tags:[LivingRoom,Bedroom]',\n\n    'Speaker': 'Functions : [\n        on(),\n        off(),\n        pause(),\n        stop(),\n        play(source: string),\n        speak(text: string)\n    ]\n    Values : [\n        switch : string {\"on\"|\"off\"},\n        playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n    ]\n    Tags:[LivingRoom,Kitchen]'\n}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#Clock).hour == 6 and (#Clock).minute == 0 and (#Clock).second == 0){\n        if((#AirPurifier #LivingRoom).switch != \"on\"){\n            (#AirPurifier #LivingRoom).on()\n        }\n    }\n    if((#Clock).hour == 19 and (#Clock).minute == 0 and (#Clock).second == 0){\n        if((#Clock).weekday == \"monday\" or (#Clock).weekday == \"tuesday\" or (#Clock).weekday == \"wednesday\" or (#Clock).weekday == \"thursday\" or (#Clock).weekday == \"friday\"){\n            if((#MotionSensor #Hallway).motion == \"active\"){\n                if((#Camera #LivingRoom).switch != \"on\"){\n                    (#Camera #LivingRoom).on()\n                }\n                (#Camera #LivingRoom).take()\n                (#Speaker #LivingRoom).speak(\"움직임이 감지되었습니다.\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오전 6시에 주방 공기청정기를 켜고 평일 오후 7시에 뒤뜰에서 움직임이 감지되면 사진을 찍고 주방 스피커를 통해 움직임이 감지되었다고 말해줘.\n\nServices: {\n    'Camera': 'Functions : [\n        on(),\n        off(),\n        take() : return binary : storage path for image(photo),\n        takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n    ]\n    Values : [\n        switch : string {\"on\"|\"off\"},\n        image : binary : the storage path for the most recent image(photo)\n    ]\n    Tags:[Kitchen,Bedroom]',\n\n    'MotionSensor': 'Functions : []\n    Values : [\n        motion : string {\"active\"|\"inactive\"}\n    ]\n    Tags:[Backyard,Driveway]',\n\n    'Clock': 'Functions : []\n    Values : [\n        day : int [1~31],\n        hour : int [0~23],\n        minute : int [0~59],\n        month : int [1~12],\n        second : int [0~59],\n        weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"},\n        year : int [0 ~ 100000],\n        isHoliday : bool {true|false},\n        timestamp : double : unixTime\n    ]\n    Tags:[]',\n\n    'AirPurifier': 'Functions : [\n        on(),\n        off(),\n        setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\n    ]\n    Values : [\n        switch : string {\"on\"|\"off\"},\n        airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\n    ]\n    Tags:[Kitchen,Office]',\n\n    'Speaker': 'Functions : [\n        on(),\n        off(),\n        pause(),\n        stop(),\n        play(source: string),\n        speak(text: string)\n    ]\n    Values : [\n        switch : string {\"on\"|\"off\"},\n        playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n    ]\n    Tags:[Kitchen,Bathroom]'\n}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#Clock).hour == 6 and (#Clock).minute == 0 and (#Clock).second == 0){\n        if((#AirPurifier #Kitchen).switch != \"on\"){\n            (#AirPurifier #Kitchen).on()\n        }\n    }\n    if((#Clock).hour == 19 and (#Clock).minute == 0 and (#Clock).second == 0){\n        if((#Clock).weekday == \"monday\" or (#Clock).weekday == \"tuesday\" or (#Clock).weekday == \"wednesday\" or (#Clock).weekday == \"thursday\" or (#Clock).weekday == \"friday\"){\n            if((#MotionSensor #Backyard).motion == \"active\"){\n                if((#Camera #Kitchen).switch != \"on\"){\n                    (#Camera #Kitchen).on()\n                }\n                (#Camera #Kitchen).take()\n                (#Speaker #Kitchen).speak(\"움직임이 감지되었습니다.\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오전 6시에 침실 공기청정기를 켜고 평일 오후 7시에 지하실에서 움직임이 감지되면 사진을 찍고 침실 스피커를 통해 움직임이 감지되었다고 말해줘.\n\nServices: {\n    'Camera': 'Functions : [\n        on(),\n        off(),\n        take() : return binary : storage path for image(photo),\n        takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n    ]\n    Values : [\n        switch : string {\"on\"|\"off\"},\n        image : binary : the storage path for the most recent image(photo)\n    ]\n    Tags:[Bedroom,Garage]',\n\n    'MotionSensor': 'Functions : []\n    Values : [\n        motion : string {\"active\"|\"inactive\"}\n    ]\n    Tags:[Basement,Patio]',\n\n    'Clock': 'Functions : []\n    Values : [\n        day : int [1~31],\n        hour : int [0~23],\n        minute : int [0~59],\n        month : int [1~12],\n        second : int [0~59],\n        weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"},\n        year : int [0 ~ 100000],\n        isHoliday : bool {true|false},\n        timestamp : double : unixTime\n    ]\n    Tags:[]',\n\n    'AirPurifier': 'Functions : [\n        on(),\n        off(),\n        setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\n    ]\n    Values : [\n        switch : string {\"on\"|\"off\"},\n        airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\n    ]\n    Tags:[Bedroom,LivingRoom]',\n\n    'Speaker': 'Functions : [\n        on(),\n        off(),\n        pause(),\n        stop(),\n        play(source: string),\n        speak(text: string)\n    ]\n    Values : [\n        switch : string {\"on\"|\"off\"},\n        playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n    ]\n    Tags:[Bedroom,Garage]'\n}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#Clock).hour == 6 and (#Clock).minute == 0 and (#Clock).second == 0){\n        if((#AirPurifier #Bedroom).switch != \"on\"){\n            (#AirPurifier #Bedroom).on()\n        }\n    }\n    if((#Clock).hour == 19 and (#Clock).minute == 0 and (#Clock).second == 0){\n        if((#Clock).weekday == \"monday\" or (#Clock).weekday == \"tuesday\" or (#Clock).weekday == \"wednesday\" or (#Clock).weekday == \"thursday\" or (#Clock).weekday == \"friday\"){\n            if((#MotionSensor #Basement).motion == \"active\"){\n                if((#Camera #Bedroom).switch != \"on\"){\n                    (#Camera #Bedroom).on()\n                }\n                (#Camera #Bedroom).take()\n                (#Speaker #Bedroom).speak(\"움직임이 감지되었습니다.\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 외부 온도가 10도 미만인 경우 침실 에어컨을 난방 모드로 켜고 22도로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'WeatherProvider': 'Functions : [\n    getWeatherInfo(double latitude, double longitude): return string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"}\n]\nValues : [\n    weather : string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"},\n    temperature : int celcius,\n    humidity : double,\n    pressure : double\n]\nTags:[]', 'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[Bedroom,LivingRoom]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#WeatherProvider).temperature < 10) {\n    if ((#AirConditioner #Bedroom).switch == \"off\") {\n        (#AirConditioner #Bedroom).on()\n    }\n    (#AirConditioner #Bedroom).setAirConditionerMode(\"heat\")\n    (#AirConditioner #Bedroom).setTemperature(22)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 외부 온도가 10도보다 낮으면 주방 에어컨을 난방 모드로 켜고 22도로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'WeatherProvider': 'Functions : [\n    getWeatherInfo(double latitude, double longitude): return string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"}\n]\nValues : [\n    weather : string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"},\n    temperature : int celcius,\n    humidity : double,\n    pressure : double\n]\nTags:[]', 'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[Kitchen,Bathroom]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#WeatherProvider).temperature < 10) {\n    if ((#AirConditioner #Kitchen).switch == \"off\") {\n        (#AirConditioner #Kitchen).on()\n    }\n    (#AirConditioner #Kitchen).setAirConditionerMode(\"heat\")\n    (#AirConditioner #Kitchen).setTemperature(22)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 외부 온도가 10도 미만인 경우 지하실 에어컨을 난방 모드로 켜고 22도로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'WeatherProvider': 'Functions : [\n    getWeatherInfo(double latitude, double longitude): return string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"}\n]\nValues : [\n    weather : string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"},\n    temperature : int celcius,\n    humidity : double,\n    pressure : double\n]\nTags:[]', 'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[Basement,Office]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#WeatherProvider).temperature < 10) {\n    if ((#AirConditioner #Basement).switch == \"off\") {\n        (#AirConditioner #Basement).on()\n    }\n    (#AirConditioner #Basement).setAirConditionerMode(\"heat\")\n    (#AirConditioner #Basement).setTemperature(22)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 가습기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Humidifier': 'Functions : [\n    on(),\n    off(),\n    setHumidiferMode(mode: string {\"auto\"|\"low\"|\"medium\"|\"high\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    humidifierMode : string {\"auto\"|\"low\"|\"medium\"|\"high\"}\n]\nTags:[Livingroom,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Humidifier #Livingroom).switch == \"off\") {\n    (#Humidifier #Livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방 가습기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Humidifier': 'Functions : [\n    on(),\n    off(),\n    setHumidiferMode(mode: string {\"auto\"|\"low\"|\"medium\"|\"high\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    humidifierMode : string {\"auto\"|\"low\"|\"medium\"|\"high\"}\n]\nTags:[Kitchen,Office]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Humidifier #Kitchen).switch == \"off\") {\n    (#Humidifier #Kitchen).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 가습기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Humidifier': 'Functions : [\n    on(),\n    off(),\n    setHumidiferMode(mode: string {\"auto\"|\"low\"|\"medium\"|\"high\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    humidifierMode : string {\"auto\"|\"low\"|\"medium\"|\"high\"}\n]\nTags:[Bedroom,Bathroom]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Humidifier #Bedroom).switch == \"off\") {\n    (#Humidifier #Bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 8시에 거실 로봇청소기를 자동 모드로 설정하고 비가 오면 주방 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'WeatherProvider': 'Functions : [\n    getWeatherInfo(double latitude, double longitude): return string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"}\n]\nValues : [\n    weather : string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"},\n    temperature : int celcius,\n    humidity : double,\n    pressure : double\n]\nTags:[]', 'RobotCleaner': 'Functions : [\n    on(),\n    off(),\n    setRobotCleanerCleaningMode(string mode{\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    robotCleanerCleaningMode : string {\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"}\n]\nTags:[LivingRoom]', 'Light': 'Functions : [\n    on(),\n    off(),\n    setColor(color: string {\"{hue}|{saturation}|{brightness}\"})\n    setLevel(level int [0 ~ 100])\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    light : double\n]\nTags:[Kitchen]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 8 and (#Clock).minute == 0) {\n        if ((#RobotCleaner #LivingRoom).robotCleanerCleaningMode != \"auto\") {\n            (#RobotCleaner #LivingRoom).setRobotCleanerCleaningMode(\"auto\")\n        }\n        if ((#WeatherProvider).weather == \"rain\") {\n            if (any(#Light #Kitchen).switch != \"on\") {\n                all(#Light #Kitchen).on()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 8시에 침실 로봇 청소기를 자동 모드로 설정하고 비가 오면 차고 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'WeatherProvider': 'Functions : [\n    getWeatherInfo(double latitude, double longitude): return string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"}\n]\nValues : [\n    weather : string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"},\n    temperature : int celcius,\n    humidity : double,\n    pressure : double\n]\nTags:[]', 'RobotCleaner': 'Functions : [\n    on(),\n    off(),\n    setRobotCleanerCleaningMode(string mode{\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    robotCleanerCleaningMode : string {\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"}\n]\nTags:[Bedroom]', 'Light': 'Functions : [\n    on(),\n    off(),\n    setColor(color: string {\"{hue}|{saturation}|{brightness}\"})\n    setLevel(level int [0 ~ 100])\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    light : double\n]\nTags:[Garage]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 8 and (#Clock).minute == 0) {\n        if ((#RobotCleaner #Bedroom).robotCleanerCleaningMode != \"auto\") {\n            (#RobotCleaner #Bedroom).setRobotCleanerCleaningMode(\"auto\")\n        }\n        if ((#WeatherProvider).weather == \"rain\") {\n            if (any(#Light #Garage).switch != \"on\") {\n                all(#Light #Garage).on()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 8시에 복도 로봇 청소기를 자동 모드로 설정하고 비가 오는 경우 욕실 조명을 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'WeatherProvider': 'Functions : [\n    getWeatherInfo(double latitude, double longitude): return string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"}\n]\nValues : [\n    weather : string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"},\n    temperature : int celcius,\n    humidity : double,\n    pressure : double\n]\nTags:[]', 'RobotCleaner': 'Functions : [\n    on(),\n    off(),\n    setRobotCleanerCleaningMode(string mode{\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    robotCleanerCleaningMode : string {\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"}\n]\nTags:[Hallway]', 'Light': 'Functions : [\n    on(),\n    off(),\n    setColor(color: string {\"{hue}|{saturation}|{brightness}\"})\n    setLevel(level int [0 ~ 100])\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    light : double\n]\nTags:[Bathroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 8 and (#Clock).minute == 0) {\n        if ((#RobotCleaner #Hallway).robotCleanerCleaningMode != \"auto\") {\n            (#RobotCleaner #Hallway).setRobotCleanerCleaningMode(\"auto\")\n        }\n        if ((#WeatherProvider).weather == \"rain\") {\n            if (any(#Light #Bathroom).switch != \"on\") {\n                all(#Light #Bathroom).on()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: PM 10 수치가 100 이상이고 온도가 25°C를 초과하는 경우 거실 에어컨을 켜고 냉방 모드로 설정해줘. CO2 수치가 600ppm 이상이면 거실 에어컨을 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[LivingRoom,Bedroom,Basement]',\n'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[LivingRoom,Bedroom]'}\n"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector #LivingRoom).dustLevel > 100.0 and (#AirQualityDetector #LivingRoom).temperature > 25.0) {\n        if ((#AirConditioner #LivingRoom).switch == \"off\") {\n            (#AirConditioner #LivingRoom).on()\n        }\n        if ((#AirConditioner #LivingRoom).airConditionerMode != \"cool\") {\n            (#AirConditioner #LivingRoom).setAirConditionerMode(\"cool\")\n        }\n    }\n    if ((#AirQualityDetector #LivingRoom).carbonDioxide > 600.0) {\n        if ((#AirConditioner #LivingRoom).switch == \"on\") {\n            (#AirConditioner #LivingRoom).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: PM 10 수치가 100 이상이고 온도가 25°C를 초과하는 경우 사무실 에어컨을 켜고 냉방 모드로 설정해줘. CO2 수치가 600ppm 이상이면 사무실 에어컨을 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[Office,Workshop]',\n'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[Office,ServerRoom]'}\n"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector #Office).dustLevel > 100.0 and (#AirQualityDetector #Office).temperature > 25.0) {\n        if ((#AirConditioner #Office).switch == \"off\") {\n            (#AirConditioner #Office).on()\n        }\n        if ((#AirConditioner #Office).airConditionerMode != \"cool\") {\n            (#AirConditioner #Office).setAirConditionerMode(\"cool\")\n        }\n    }\n    if ((#AirQualityDetector #Office).carbonDioxide > 600.0) {\n        if ((#AirConditioner #Office).switch == \"on\") {\n            (#AirConditioner #Office).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: PM 10 수치가 100 이상이고 온도가 25°C를 초과하면 지하실 에어컨을 켜고 냉방 모드로 설정해줘. CO2 수치가 600ppm 이상이면 지하실 에어컨을 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[Garage,Basement]',\n'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[Basement,Attic]'}\n"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector #Basement).dustLevel > 100.0 and (#AirQualityDetector #Basement).temperature > 25.0) {\n        if ((#AirConditioner #Basement).switch == \"off\") {\n            (#AirConditioner #Basement).on()\n        }\n        if ((#AirConditioner #Basement).airConditionerMode != \"cool\") {\n            (#AirConditioner #Basement).setAirConditionerMode(\"cool\")\n        }\n    }\n    if ((#AirQualityDetector #Basement).carbonDioxide > 600.0) {\n        if ((#AirConditioner #Basement).switch == \"on\") {\n            (#AirConditioner #Basement).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 30분마다 거실 가습기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Humidifier': 'Functions : [\n    on(),\n\toff(),\n    setHumidiferMode(mode: string {\"auto\"|\"low\"|\"medium\"|\"high\"})\n]\nValues : [\n\tswitch : string {\"on\"|\"off\"},\n    humidifierMode : string {\"auto\"|\"low\"|\"medium\"|\"high\"}\n]\nTags:[LivingRoom,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop (30 MIN) {\n        if ((#Humidifier #Livingroom).switch == \"off\") {\n            (#Humidifier #Livingroom).on()\n        }\n\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 30분마다 침실 가습기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Humidifier': 'Functions : [\n    on(),\n\toff(),\n    setHumidiferMode(mode: string {\"auto\"|\"low\"|\"medium\"|\"high\"})\n]\nValues : [\n\tswitch : string {\"on\"|\"off\"},\n    humidifierMode : string {\"auto\"|\"low\"|\"medium\"|\"high\"}\n]\nTags:[Office,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop (30 MIN) {\n        if ((#Humidifier #Bedroom).switch == \"off\") {\n            (#Humidifier #Bedroom).on()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 30분마다 사무실 가습기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Humidifier': 'Functions : [\n    on(),\n\toff(),\n    setHumidiferMode(mode: string {\"auto\"|\"low\"|\"medium\"|\"high\"})\n]\nValues : [\n\tswitch : string {\"on\"|\"off\"},\n    humidifierMode : string {\"auto\"|\"low\"|\"medium\"|\"high\"}\n]\nTags:[Office,Garage]'}"
        },
        {
            "from": "gpt",
            "value": "loop (30 MIN) {\n        if ((#Humidifier #Office).switch == \"off\") {\n            (#Humidifier #Office).on()\n        }\n\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: PM 10 수치가 100 이상이고 온도가 25°C를 초과하는 경우 거실 에어컨을 켜고 냉방 모드로 설정해줘. CO2 수치가 600ppm 이상이면 거실 에어컨을 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[LivingRoom,Bedroom,Basement]',\n'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[LivingRoom,Bedroom]'}\n"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector #LivingRoom).dustLevel > 100.0 and (#AirQualityDetector #LivingRoom).temperature > 25.0) {\n        if ((#AirConditioner #LivingRoom).switch == \"off\") {\n            (#AirConditioner #LivingRoom).on()\n        }\n        if ((#AirConditioner #LivingRoom).airConditionerMode != \"cool\") {\n            (#AirConditioner #LivingRoom).setAirConditionerMode(\"cool\")\n        }\n    }\n    if ((#AirQualityDetector #LivingRoom).carbonDioxide > 600.0) {\n        if ((#AirConditioner #LivingRoom).switch == \"on\") {\n            (#AirConditioner #LivingRoom).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: PM 10 수치가 100 이상이고 온도가 25°C를 초과하는 경우 사무실 에어컨을 켜고 냉방 모드로 설정해줘. CO2 수치가 600ppm 이상이면 사무실 에어컨을 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[Office,Workshop]',\n'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[Office,ServerRoom]'}\n"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector #Office).dustLevel > 100.0 and (#AirQualityDetector #Office).temperature > 25.0) {\n        if ((#AirConditioner #Office).switch == \"off\") {\n            (#AirConditioner #Office).on()\n        }\n        if ((#AirConditioner #Office).airConditionerMode != \"cool\") {\n            (#AirConditioner #Office).setAirConditionerMode(\"cool\")\n        }\n    }\n    if ((#AirQualityDetector #Office).carbonDioxide > 600.0) {\n        if ((#AirConditioner #Office).switch == \"on\") {\n            (#AirConditioner #Office).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: PM 10 수치가 100 이상이고 온도가 25°C를 초과하는 경우 침실 에어컨을 켜고 냉방 모드로 설정해줘. CO2 수치가 600ppm 이상이면 침실 에어컨을 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[Bedroom,LivingRoom]',\n'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[Bedroom,GuestRoom]'}\n"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector #Bedroom).dustLevel > 100.0 and (#AirQualityDetector #Bedroom).temperature > 25.0) {\n        if ((#AirConditioner #Bedroom).switch == \"off\") {\n            (#AirConditioner #Bedroom).on()\n        }\n        if ((#AirConditioner #Bedroom).airConditionerMode != \"cool\") {\n            (#AirConditioner #Bedroom).setAirConditionerMode(\"cool\")\n        }\n    }\n    if ((#AirQualityDetector #Bedroom).carbonDioxide > 600.0) {\n        if ((#AirConditioner #Bedroom).switch == \"on\") {\n            (#AirConditioner #Bedroom).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 8시 30분에 기온이 26도 이상이면 거실 선풍기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Fan': 'Functions : [\n    on(),\n    off(),\n    setFanSpeed(speed: int [0 ~ ∞])\n]\nValues : [\n    switch : string {\"on\"|\"off\"}\n]\nTags:[LivingRoom,Bedroom]', 'TemperatureSensor': 'Functions : []\nValues : [\n    temperature: int [-460 ~ 10000]\n]\nTags:[LivingRoom,Bathroom]'}"
        },
        {
            "from": "gpt",
            "value": "wait until((#Clock).hour == 8 && (#Clock).minute == 30)\nif((#TemperatureSensor #LivingRoom).temperature >=26){\n    if((#Fan #LivingRoom).switch != \"on\"){\n        (#Fan #LivingRoom).on()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 8시 30분에 기온이 26도 이상이면 사무실 선풍기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Fan': 'Functions : [\n    on(),\n    off(),\n    setFanSpeed(speed: int [0 ~ ∞])\n]\nValues : [\n    switch : string {\"on\"|\"off\"}\n]\nTags:[Office,StudyRoom]', 'TemperatureSensor': 'Functions : []\nValues : [\n    temperature: int [-460 ~ 10000]\n]\nTags:[Office,Balcony]'}"
        },
        {
            "from": "gpt",
            "value": "wait until((#Clock).hour == 8 && (#Clock).minute == 30)\nif((#TemperatureSensor #Office).temperature >=26){\n    if((#Fan #Office).switch != \"on\"){\n        (#Fan #Office).on()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 8시 30분에 기온이 26도 이상이면 침실 선풍기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Fan': 'Functions : [\n    on(),\n    off(),\n    setFanSpeed(speed: int [0 ~ ∞])\n]\nValues : [\n    switch : string {\"on\"|\"off\"}\n]\nTags:[Bedroom,GuestRoom]', 'TemperatureSensor': 'Functions : []\nValues : [\n    temperature: int [-460 ~ 10000]\n]\nTags:[Bedroom,Kitchen]'}"
        },
        {
            "from": "gpt",
            "value": "wait until((#Clock).hour == 8 && (#Clock).minute == 30)\nif((#TemperatureSensor #Bedroom).temperature >=26){\n    if((#Fan #Bedroom).switch != \"on\"){\n        (#Fan #Bedroom).on()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실의 현재 습도가 70%를 초과하면 거실 창문을 열어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Window': 'Functions : [\n    open(),\n    close()\n]\nValues : [\n    window : string {\"closed\"|\"open\"}\n]\nTags:[Livingroom,Office]', 'HumiditySensor': 'Functions : []\nValues : [\n    humidity : double[0 ~ 100]\n]\nTags:[Bedroom,Bathroom]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#HumiditySensor #Bedroom).humidity > 70) {\n    if (any(#Window #Livingroom).window == \"closed\") {\n        all(#Window #Livingroom).open()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실의 현재 습도가 70%를 초과하는 경우 거실 창문 하나를 열어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Window': 'Functions : [\n    open(),\n    close()\n]\nValues : [\n    window : string {\"closed\"|\"open\"}\n]\nTags:[Livingroom,Office]', 'HumiditySensor': 'Functions : []\nValues : [\n    humidity : double[0 ~ 100]\n]\nTags:[Bedroom,Bathroom]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#HumiditySensor #Bedroom).humidity > 70) {\n    if ((#Window #Livingroom).window == \"closed\") {\n        (#Window #Livingroom).open()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 온실의 현재 습도가 70%를 초과하면 다락방 창을 열어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Window': 'Functions : [\n    open(),\n    close()\n]\nValues : [\n    window : string {\"closed\"|\"open\"}\n]\nTags:[Attic,Garage]', 'HumiditySensor': 'Functions : []\nValues : [\n    humidity : double[0 ~ 100]\n]\nTags:[Greenhouse,Sauna]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#HumiditySensor #Greenhouse).humidity > 70) {\n    if (any(#Window #Attic).window == \"closed\") {\n        all(#Window #Attic).open()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방의 현재 습도가 70%를 초과하면 침실 창문을 열어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Window': 'Functions : [\n    open(),\n    close()\n]\nValues : [\n    window : string {\"closed\"|\"open\"}\n]\nTags:[Bedroom,Livingroom]', 'HumiditySensor': 'Functions : []\nValues : [\n    humidity : double[0 ~ 100]\n]\nTags:[Kitchen,Bathroom]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#HumiditySensor #Kitchen).humidity > 70) {\n    if ((#Window #Bedroom).window == \"closed\") {\n        (#Window #Bedroom).open()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 스피커를 통해 10분마다 주방의 가스 사용량을 알려줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[LivingRoom,Bedroom]', 'GasMeter': 'Functions : []\nValues : [\n    gasMeter : double,\n    gasMeterCalorific : double : amount of heat produced (kJ),\n    gasMeterTime : double seconds,\n    gasMeterVolume : double\n]\nTags:[Basement,Kitchen]'}"
        },
        {
            "from": "gpt",
            "value": "loop (10 MIN) {\n    if ((#Speaker #LivingRoom).switch == \"off\") {\n        (#Speaker #LivingRoom).on()\n    }\n    (#Speaker #LivingRoom).speak(\"Gas usage time is \" + (#GasMeter #Kitchen).gasMeterTime)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 사무실 스피커를 통해 10분마다 차고에 사용된 가스 양을 알려줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[Office,Bathroom]', 'GasMeter': 'Functions : []\nValues : [\n    gasMeter : double,\n    gasMeterCalorific : double : amount of heat produced (kJ),\n    gasMeterTime : double seconds,\n    gasMeterVolume : double\n]\nTags:[Garage,Attic]'}"
        },
        {
            "from": "gpt",
            "value": "loop (10 MIN) {\n    if ((#Speaker #Office).switch == \"off\") {\n        (#Speaker #Office).on()\n    }\n    (#Speaker #Office).speak(\"Gas usage time is \" + (#GasMeter #Garage).gasMeterTime)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 스피커를 통해 10분마다 차고의 가스 사용량을 알려줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[Garage,Basement]', 'GasMeter': 'Functions : []\nValues : [\n    gasMeter : double,\n    gasMeterCalorific : double : amount of heat produced (kJ),\n    gasMeterTime : double seconds,\n    gasMeterVolume : double\n]\nTags:[LivingRoom,Bathroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop (10 MIN) {\n    if ((#Speaker #Garage).switch == \"off\") {\n        (#Speaker #Garage).on()\n    }\n    (#Speaker #Garage).speak(\"Gas usage time is \" + (#GasMeter #LivingRoom).gasMeterTime)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 12분 후 거실 스피커를 통해 'Hello World'라고 말해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags: [LivingRoom, Bedroom, Office]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (12 MIN)\nif ((#Speaker #LivingRoom).switch == \"off\") {\n    (#Speaker #LivingRoom).on()\n}\n(#Speaker #LivingRoom).speak(\"Hello World\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 12분 후 침실 스피커를 통해 'Hello World'라고 말해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags: [Bedroom, Kitchen, Garage]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (12 MIN)\nif ((#Speaker #Bedroom).switch == \"off\") {\n    (#Speaker #Bedroom).on()\n}\n(#Speaker #Bedroom).speak(\"Hello World\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 12분 후 주방 스피커를 통해 'Hello World'라고 말해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags: [Kitchen, Bathroom, Hallway]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (12 MIN)\nif ((#Speaker #Kitchen).switch == \"off\") {\n    (#Speaker #Kitchen).on()\n}\n(#Speaker #Kitchen).speak(\"Hello World\")"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 1시간 후 현재 누적된 지하실 가스 사용 시간과 거실 스피커의 가스 사용량을 알려줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[LivingRoom,Bedroom]', 'GasMeter': 'Functions : []\nValues : [\n    gasMeter : double,\n    gasMeterCalorific : double : amount of heat produced (kJ),\n    gasMeterTime : double seconds,\n    gasMeterVolume : double\n]\nTags:[Basement,Kitchen]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (1 HOUR)\nusage_time = (#GasMeter #Basement).gasMeterTime\nusage_amount = (#GasMeter #Basement).gasMeterVolume\n(#Speaker #LivingRoom).speak(\"현재 누적 가스 사용 시간은 \" + usage_time)\n(#Speaker #LivingRoom).speak(\"현재 사용된 가스의 양은 \" + usage_amount)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 1시간 후 현재 누적 차고지 가스 사용 시간과 사무실 스피커의 가스 사용량을 알려줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[Office,Hallway]', 'GasMeter': 'Functions : []\nValues : [\n    gasMeter : double,\n    gasMeterCalorific : double : amount of heat produced (kJ),\n    gasMeterTime : double seconds,\n    gasMeterVolume : double\n]\nTags:[Attic,Garage]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (1 HOUR)\nusage_time = (#GasMeter #Garage).gasMeterTime\nusage_amount = (#GasMeter #Garage).gasMeterVolume\n(#Speaker #Office).speak(\"현재 누적 가스 사용 시간은 \" + usage_time)\n(#Speaker #Office).speak(\"현재 사용된 가스의 양은 \" + usage_amount)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 1시간 후 현재 누적된 주방 가스 사용 시간과 다락방 스피커의 가스 사용량을 알려줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[Bathroom,Garage]', 'GasMeter': 'Functions : []\nValues : [\n    gasMeter : double,\n    gasMeterCalorific : double : amount of heat produced (kJ),\n    gasMeterTime : double seconds,\n    gasMeterVolume : double\n]\nTags:[Kitchen,Attic]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (1 HOUR)\nusage_time = (#GasMeter #Kitchen).gasMeterTime\nusage_amount = (#GasMeter #Kitchen).gasMeterVolume\n(#Speaker #Attic).speak(\"현재 누적 가스 사용 시간은 \" + usage_time)\n(#Speaker #Attic).speak(\"현재 사용된 가스의 양은 \" + usage_amount)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 7시에 거실 블라인드가 열려 있으면 100ml로 정원에 물을 주기 시작해.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags:[LivingRoom,Bedroom]', 'Irrigator': 'Functions : [\n    on(),\n    off(),\n    startWatering(),\n    setWaterPortion(portion: double [0 ~ 2000], unit: string {\"liters\"|\"milliliters\"|\"gallons\"|\"ounces\"})\n]\nValues : [\n    switch: string {\"on\"|\"off\"}\n]\nTags:[Greenhouse,Garden]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 7 and (#Clock).minute == 0) {\n        if ((#Blind #LivingRoom).blind == \"open\") {\n            if ((#Irrigator #Garden).switch == \"off\") {\n                (#Irrigator #Garden).on()\n            }\n            (#Irrigator #Garden).startWatering(100)\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 7시에 주방 블라인드가 열려 있으면 발코니에 100ml로 물을 주기 시작해.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags:[Kitchen,Office]', 'Irrigator': 'Functions : [\n    on(),\n    off(),\n    startWatering(),\n    setWaterPortion(portion: double [0 ~ 2000], unit: string {\"liters\"|\"milliliters\"|\"gallons\"|\"ounces\"})\n]\nValues : [\n    switch: string {\"on\"|\"off\"}\n]\nTags:[Balcony,Patio]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 7 and (#Clock).minute == 0) {\n        if ((#Blind #Kitchen).blind == \"open\") {\n            if ((#Irrigator #Balcony).switch == \"off\") {\n                (#Irrigator #Balcony).on()\n            }\n            (#Irrigator #Balcony).startWatering(100)\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 7시에 침실 블라인드가 열려 있으면 100ml로 테라스에 물을 주기 시작해.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags:[Hallway,Bedroom]', 'Irrigator': 'Functions : [\n    on(),\n    off(),\n    startWatering(),\n    setWaterPortion(portion: double [0 ~ 2000], unit: string {\"liters\"|\"milliliters\"|\"gallons\"|\"ounces\"})\n]\nValues : [\n    switch: string {\"on\"|\"off\"}\n]\nTags:[Backyard,Terrace]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 7 and (#Clock).minute == 0) {\n        if ((#Blind #Bedroom).blind == \"open\") {\n            if ((#Irrigator #Terrace).switch == \"off\") {\n                (#Irrigator #Terrace).on()\n            }\n            (#Irrigator #Terrace).startWatering(100)\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 블라인드가 닫혀 있는 경우 오전 11시에 정원 관개 시스템을 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags:[Livingroom,Office]',\n'Irrigator': 'Functions : [\n    on(),\n    off(),\n    startWatering(),\n    setWaterPortion(portion: double [0 ~ 2000], unit: string {\"liters\"|\"milliliters\"|\"gallons\"|\"ounces\"})\n]\nValues : [\n    switch: string {\"on\"|\"off\"}\n]\nTags:[Garden,Greenhouse]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 11 and (#Clock).minute == 0) {\n        if ((#Blind #Livingroom).blind == \"closed\") {\n            if ((#Irrigator #Garden).switch == \"on\") {\n                (#Irrigator #Garden).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 블라인드가 닫혀 있는 경우 오전 11시에 파티오 관개 시스템을 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags:[Bathroom,Bedroom]',\n'Irrigator': 'Functions : [\n    on(),\n    off(),\n    startWatering(),\n    setWaterPortion(portion: double [0 ~ 2000], unit: string {\"liters\"|\"milliliters\"|\"gallons\"|\"ounces\"})\n]\nValues : [\n    switch: string {\"on\"|\"off\"}\n]\nTags:[Frontyard,Patio]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 11 and (#Clock).minute == 0) {\n        if ((#Blind #Bedroom).blind == \"closed\") {\n            if ((#Irrigator #Patio).switch == \"on\") {\n                (#Irrigator #Patio).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 식당 블라인드가 닫혀 있는 경우 오전 11시에 옥상 관개 시스템을 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags:[Library,Diningroom]',\n'Irrigator': 'Functions : [\n    on(),\n    off(),\n    startWatering(),\n    setWaterPortion(portion: double [0 ~ 2000], unit: string {\"liters\"|\"milliliters\"|\"gallons\"|\"ounces\"})\n]\nValues : [\n    switch: string {\"on\"|\"off\"}\n]\nTags:[Terrace,Rooftop]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 11 and (#Clock).minute == 0) {\n        if ((#Blind #Diningroom).blind == \"closed\") {\n            if ((#Irrigator #Rooftop).switch == \"on\") {\n                (#Irrigator #Rooftop).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 7시마다 주방의 연기 감지 상태가 스피커를 통해 안내해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'SmokeDetector': 'Functions : []\nValues : [\n    smoke : string {\"detected\"|\"not_detected\"}\n]\nTags:[LivingRoom,Kitchen]',\n'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[Bedroom,Office]'}"
        },
        {
            "from": "gpt",
            "value": "loop (1 MIN, (#Clock).hour == 7 and (#Clock).minute == 0) {\n    if ((#Speaker).switch == \"off\") {\n        (#Speaker).on()\n    }\n    if ((#SmokeDetector #Kitchen).smoke == \"detected\") {\n        (#Speaker).speak(\"현재 연기가 감지되었습니다. 확인해주세요.\")\n    }\n    if ((#SmokeDetector #Kitchen).smoke == \"not_detected\") {\n        (#Speaker).speak(\"현재 연기가 감지되지 않았습니다.\")\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 7시마다 차고 내 연기 감지 상태가 스피커를 통해 안내해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'SmokeDetector': 'Functions : []\nValues : [\n    smoke : string {\"detected\"|\"not_detected\"}\n]\nTags:[Basement,Garage]',\n'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[Kitchen,DiningRoom]'}"
        },
        {
            "from": "gpt",
            "value": "loop (1 MIN, (#Clock).hour == 7 and (#Clock).minute == 0) {\n    if ((#Speaker).switch == \"off\") {\n        (#Speaker).on()\n    }\n    if ((#SmokeDetector #Garage).smoke == \"detected\") {\n        (#Speaker).speak(\"현재 연기가 감지되었습니다. 확인해주세요.\")\n    }\n    if ((#SmokeDetector #Garage).smoke == \"not_detected\") {\n        (#Speaker).speak(\"현재 연기가 감지되지 않았습니다.\")\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매 7시마다 스피커를 통해 화장실 연기 감지 상태가 안내해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'SmokeDetector': 'Functions : []\nValues : [\n    smoke : string {\"detected\"|\"not_detected\"}\n]\nTags:[Attic,Bathroom]',\n'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[LivingRoom,Balcony]'}"
        },
        {
            "from": "gpt",
            "value": "loop (1 MIN, (#Clock).hour == 7 and (#Clock).minute == 0) {\n    if ((#Speaker).switch == \"off\") {\n        (#Speaker).on()\n    }\n    if ((#SmokeDetector #Bathroom).smoke == \"detected\") {\n        (#Speaker).speak(\"현재 연기가 감지되었습니다. 확인해주세요.\")\n    }\n    if ((#SmokeDetector #Bathroom).smoke == \"not_detected\") {\n        (#Speaker).speak(\"현재 연기가 감지되지 않았습니다.\")\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 지하실 가스 밸브를 잠가줘.\n\nServices: {'GasValve': 'Functions : [\n    open(),\n    close()\n]\nValues : [\n    valve : string {\"open\"|\"closed\"}\n]\nTags:[Basement,Kitchen]', 'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#GasValve #Basement).valve == \"open\") {\n    (#GasValve #Basement).close()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방 가스 밸브를 잠가줘.\n\nServices: {'GasValve': 'Functions : [\n    open(),\n    close()\n]\nValues : [\n    valve : string {\"open\"|\"closed\"}\n]\nTags:[LaundryRoom,Kitchen]', 'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#GasValve #Kitchen).valve == \"open\") {\n    (#GasValve #Kitchen).close()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 실외 가스 밸브를 닫아줘.\n\nServices: {'GasValve': 'Functions : [\n    open(),\n    close()\n]\nValues : [\n    valve : string {\"open\"|\"closed\"}\n]\nTags:[Garage,Outdoor]', 'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#GasValve #Outdoor).valve == \"open\") {\n    (#GasValve #Outdoor).close()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 TV 채널을 8시간 중 7번으로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Television': 'Functions : [\n    on(),\n    off(),\n    setTvChannel(tvChannel: int),\n    channelUp(),\n    channelDown(),\n    setVolume(volume: int [0 ~ 100]),\n    volumeUp(),\n    volumeDown(),\n    mute() : void, toggle muteStatus\n\nValues : [\n    switch : string {\"on\"|\"off\"}\n    muteStatus : string {\"muted\"|\"unmuted\"}\n    tvChannel : int\n]\nTags:[LivingRoom,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (8 HOUR)\nif ((#Television #LivingRoom).switch == \"off\") {\n    (#Television #LivingRoom).on()\n}\n(#Television #LivingRoom).setTVChannel(7)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 TV 채널을 8시간 중 7번으로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Television': 'Functions : [\n    on(),\n    off(),\n    setTvChannel(tvChannel: int),\n    channelUp(),\n    channelDown(),\n    setVolume(volume: int [0 ~ 100]),\n    volumeUp(),\n    volumeDown(),\n    mute() : void, toggle muteStatus\n\nValues : [\n    switch : string {\"on\"|\"off\"}\n    muteStatus : string {\"muted\"|\"unmuted\"}\n    tvChannel : int\n]\nTags:[GuestRoom,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (8 HOUR)\nif ((#Television #Bedroom).switch == \"off\") {\n    (#Television #Bedroom).on()\n}\n(#Television #Bedroom).setTVChannel(7)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방 TV 채널을 8시간에 7로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Television': 'Functions : [\n    on(),\n    off(),\n    setTvChannel(tvChannel: int),\n    channelUp(),\n    channelDown(),\n    setVolume(volume: int [0 ~ 100]),\n    volumeUp(),\n    volumeDown(),\n    mute() : void, toggle muteStatus\n\nValues : [\n    switch : string {\"on\"|\"off\"}\n    muteStatus : string {\"muted\"|\"unmuted\"}\n    tvChannel : int\n]\nTags:[LivingRoom,Kitchen]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (8 HOUR)\nif ((#Television #Kitchen).switch == \"off\") {\n    (#Television #Kitchen).on()\n}\n(#Television #Kitchen).setTVChannel(7)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방에서 연기가 감지되면 주방 식기세척기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'SmokeDetector': 'Functions : []\nValues : [\n    smoke : string {\"detected\"|\"not_detected\"}\n]\nTags:[Kitchen,Basement]', 'Dishwasher': 'Functions : [\n    on(),\n    off(),\n    setDishwasherMode(mode: string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dishwasherMode : string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"}\n]\nTags:[Kitchen,LaundryRoom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#SmokeDetector #Kitchen).smoke == \"detected\") {\n        if ((#Dishwasher #Kitchen).switch == \"off\") {\n            (#Dishwasher #Kitchen).on()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 지하실에서 연기가 감지되면 식당 식기세척기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'SmokeDetector': 'Functions : []\nValues : [\n    smoke : string {\"detected\"|\"not_detected\"}\n]\nTags:[LivingRoom,Basement]', 'Dishwasher': 'Functions : [\n    on(),\n    off(),\n    setDishwasherMode(mode: string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dishwasherMode : string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"}\n]\nTags:[Garage,DiningRoom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#SmokeDetector #Basement).smoke == \"detected\") {\n        if ((#Dishwasher #DiningRoom).switch == \"off\") {\n            (#Dishwasher #DiningRoom).on()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 차고에서 연기가 감지되면 다용도실 식기세척기를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'SmokeDetector': 'Functions : []\nValues : [\n    smoke : string {\"detected\"|\"not_detected\"}\n]\nTags:[Workshop,Garage]', 'Dishwasher': 'Functions : [\n    on(),\n    off(),\n    setDishwasherMode(mode: string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dishwasherMode : string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"}\n]\nTags:[Bathroom,UtilityRoom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#SmokeDetector #Garage).smoke == \"detected\") {\n        if ((#Dishwasher #UtilityRoom).switch == \"off\") {\n            (#Dishwasher #UtilityRoom).on()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 커튼을 완전히 닫아줘.\n\nServices: {\n    'Clock': 'Functions : []\n    Values : [\n        day : int [1~31]\n        hour : int [0~23]\n        minute : int [0~59]\n        month : int [1~12]\n        second : int [0~59]\n        weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n        year : int [0 ~ 100000]\n        isHoliday : bool {true|false}\n        timestamp : double : unixTime\n    ]',\n    'Curtain': 'Functions : [\n        setCurtainLevel(level: int [0 ~ 100])\n    ]\n    Values : [\n        curtain : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n        curtainLevel : int [0 ~ 100]\n    ]\n    Tags:[LivingRoom,Bedroom]'\n}"
        },
        {
            "from": "gpt",
            "value": "if ((#Curtain #LivingRoom).curtainLevel > 0) {\n    (#Curtain #LivingRoom).setCurtainLevel(0)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 커튼을 완전히 닫아줘.\n\nServices: {\n    'Clock': 'Functions : []\n    Values : [\n        day : int [1~31]\n        hour : int [0~23]\n        minute : int [0~59]\n        month : int [1~12]\n        second : int [0~59]\n        weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n        year : int [0 ~ 100000]\n        isHoliday : bool {true|false}\n        timestamp : double : unixTime\n    ]',\n    'Curtain': 'Functions : [\n        setCurtainLevel(level: int [0 ~ 100])\n    ]\n    Values : [\n        curtain : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n        curtainLevel : int [0 ~ 100]\n    ]\n    Tags:[Office,Bedroom]'\n}"
        },
        {
            "from": "gpt",
            "value": "if ((#Curtain #Bedroom).curtainLevel > 0) {\n    (#Curtain #Bedroom).setCurtainLevel(0)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 사무실 커튼을 완전히 닫아줘.\n\nServices: {\n    'Clock': 'Functions : []\n    Values : [\n        day : int [1~31]\n        hour : int [0~23]\n        minute : int [0~59]\n        month : int [1~12]\n        second : int [0~59]\n        weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n        year : int [0 ~ 100000]\n        isHoliday : bool {true|false}\n        timestamp : double : unixTime\n    ]',\n    'Curtain': 'Functions : [\n        setCurtainLevel(level: int [0 ~ 100])\n    ]\n    Values : [\n        curtain : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n        curtainLevel : int [0 ~ 100]\n    ]\n    Tags:[Kitchen,Office]'\n}"
        },
        {
            "from": "gpt",
            "value": "if ((#Curtain #Office).curtainLevel > 0) {\n    (#Curtain #Office).setCurtainLevel(0)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 8시에 침실 제습기가 냉각 모드에 있는 경우 완료 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Bedroom,Basement]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 20 and (#Clock).minute == 0) {\n        if ((#Dehumidifier #Bedroom).dehumidifierMode == \"cooling\") {\n            (#Dehumidifier #Bedroom).setDehumidifierMode(\"finished\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 차고 제습기가 오후 8시에 냉각 모드에 있는 경우 완료 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Attic,Garage]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 20 and (#Clock).minute == 0) {\n        if ((#Dehumidifier #Garage).dehumidifierMode == \"cooling\") {\n            (#Dehumidifier #Garage).setDehumidifierMode(\"finished\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 8시에 욕실 제습기가 냉각 모드에 있는 경우 완료 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Closet,Bathroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 20 and (#Clock).minute == 0) {\n        if ((#Dehumidifier #Bathroom).dehumidifierMode == \"cooling\") {\n            (#Dehumidifier #Bathroom).setDehumidifierMode(\"finished\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매월 마지막 날 오후 11시 30분에 거실 에어컨을 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[LivingRoom,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).day == 31 and (#Clock).hour == 23 and (#Clock).minute == 30) {\n        if ((#AirConditioner #LivingRoom).switch == \"on\") {\n            (#AirConditioner #LivingRoom).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매월 마지막 날 오후 11시 30분에 사무실 에어컨을 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[Garage,Office]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).day == 31 and (#Clock).hour == 23 and (#Clock).minute == 30) {\n        if ((#AirConditioner #Office).switch == \"on\") {\n            (#AirConditioner #Office).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매월 마지막 날 오후 11시 30분에 식당의 에어컨을 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirConditioner': 'Functions : [\n    on(),\n    off(),\n    setTemperature(temperature: int),\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\n]\nTags:[Balcony,DiningRoom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).day == 31 and (#Clock).hour == 23 and (#Clock).minute == 30) {\n        if ((#AirConditioner #DiningRoom).switch == \"on\") {\n            (#AirConditioner #DiningRoom).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 정원 카메라로 3시간 동안 10배속으로 타임랩스 사진을 촬영해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Camera': 'Functions : [\n    on(),\n    off(),\n    take() : return binary : storage path for image(photo),\n    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    image : binary : the storage path for the most recent image(photo)\n]\nTags:[Garden,Backyard]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Camera #Garden).switch == \"off\") {\n    (#Camera #Garden).on()\n}\n(#Camera #Garden).takeTimelapse(3.0, 10.0)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주차장 카메라로 3시간 동안 10배속으로 타임랩스 사진을 촬영해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Camera': 'Functions : [\n    on(),\n    off(),\n    take() : return binary : storage path for image(photo),\n    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    image : binary : the storage path for the most recent image(photo)\n]\nTags:[Garage,ParkingLot]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Camera #ParkingLot).switch == \"off\") {\n    (#Camera #ParkingLot).on()\n}\n(#Camera #ParkingLot).takeTimelapse(3.0, 10.0)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 발코니 카메라로 10배속으로 3시간 동안 타임랩스 사진을 찍어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Camera': 'Functions : [\n    on(),\n    off(),\n    take() : return binary : storage path for image(photo),\n    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    image : binary : the storage path for the most recent image(photo)\n]\nTags:[Roof,Balcony]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Camera #Balcony).switch == \"off\") {\n    (#Camera #Balcony).on()\n}\n(#Camera #Balcony).takeTimelapse(3.0, 10.0)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: VOC 수치가 0.03 이하인 경우 거실 카메라를 켜고 침실 공기청정기를 낮음 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[Livingroom,Bedroom]', 'AirPurifier': 'Functions : [\n    on(),\n    off(),\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\n]\nTags:[Bedroom,Office]', 'Camera': 'Functions : [\n    on(),\n    off(),\n    take() : return binary : storage path for image(photo),\n    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    image : binary : the storage path for the most recent image(photo)\n]\nTags:[Livingroom,Basement]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector).tvocLevel < 0.03) {\n        if ((#Camera #Livingroom).switch == \"off\") {\n            (#Camera #Livingroom).on()\n        }\n        if ((#AirPurifier #Bedroom).airPurifierFanMode != \"low\") {\n            (#AirPurifier #Bedroom).setPurifierFanMode(\"low\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: VOC 수치가 0.03 이하인 경우 복도 카메라를 켜고 주방 공기청정기를 저감 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[Livingroom,Kitchen]', 'AirPurifier': 'Functions : [\n    on(),\n    off(),\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\n]\nTags:[Study,Kitchen]', 'Camera': 'Functions : [\n    on(),\n    off(),\n    take() : return binary : storage path for image(photo),\n    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    image : binary : the storage path for the most recent image(photo)\n]\nTags:[Garage,Hallway]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector).tvocLevel < 0.03) {\n        if ((#Camera #Hallway).switch == \"off\") {\n            (#Camera #Hallway).on()\n        }\n        if ((#AirPurifier #Kitchen).airPurifierFanMode != \"low\") {\n            (#AirPurifier #Kitchen).setPurifierFanMode(\"low\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: VOC 수치가 0.03 이하인 경우 차고 카메라를 켜고 사무실 공기청정기를 저감 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[Garage,Office]', 'AirPurifier': 'Functions : [\n    on(),\n    off(),\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\n]\nTags:[Livingroom,Office]', 'Camera': 'Functions : [\n    on(),\n    off(),\n    take() : return binary : storage path for image(photo),\n    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    image : binary : the storage path for the most recent image(photo)\n]\nTags:[Bedroom,Garage]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector).tvocLevel < 0.03) {\n        if ((#Camera #Garage).switch == \"off\") {\n            (#Camera #Garage).on()\n        }\n        if ((#AirPurifier #Office).airPurifierFanMode != \"low\") {\n            (#AirPurifier #Office).setPurifierFanMode(\"low\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 지하실의 습도가 40% 미만인 경우 거실 블라인드를 40%로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []',\n\n'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags: [LivingRoom,Bedroom]',\n\n'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags: [Basement,Kitchen]'}\n"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector #Basement).humidity < 40) {\n        (#Blind #LivingRoom).setBlindLevel(40)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 다락방의 습도가 40% 미만인 경우 사무실 블라인드를 40%로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []',\n\n'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags: [Library,Office]',\n\n'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags: [Basement,Attic]'}\n"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector #Attic).humidity < 40) {\n        (#Blind #Office).setBlindLevel(40)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실의 습도가 40% 미만인 경우 주방 블라인드를 40%로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0 ~ 59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []',\n\n'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags: [DiningRoom,Kitchen]',\n\n'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags: [LaundryRoom,Bathroom]'}\n"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector #Bathroom).humidity < 40) {\n        (#Blind #Kitchen).setBlindLevel(40)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 블라인드가 부분적으로 열려 있는 경우 완전히 닫아줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags:[Bedroom,LivingRoom]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Blind #Bedroom).blind == \"partially\") {\n    (#Blind #Bedroom).setBlindLevel(0)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방 블라인드가 부분적으로 열려 있는 경우 완전히 닫아줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags:[DiningRoom,Kitchen]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Blind #Kitchen).blind == \"partially\") {\n    (#Blind #Kitchen).setBlindLevel(0)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 사무실 블라인드가 부분적으로 열려 있는 경우 완전히 닫아줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags:[Library,Office]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Blind #Office).blind == \"partially\") {\n    (#Blind #Office).setBlindLevel(0)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 조명이 켜져 있는 경우 오후 11시에 지하실 제습기를 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Basement]',\n'Light': 'Functions : [\n    on(),\n    off(),\n    setColor(color: string {\"{hue}|{saturation}|{brightness}\"})\n    setLevel(level int [0 ~ 100])\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    light : double\n]\nTags:[LivingRoom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 23 and (#Clock).minute == 0) {\n        if ((#Light #LivingRoom).switch == \"on\") {\n            if ((#Dehumidifier #Basement).switch == \"on\") {\n                (#Dehumidifier #Basement).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방 조명이 켜져 있는 경우 오후 11시에 욕실 제습기를 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Bathroom]',\n'Light': 'Functions : [\n    on(),\n    off(),\n    setColor(color: string {\"{hue}|{saturation}|{brightness}\"})\n    setLevel(level int [0 ~ 100])\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    light : double\n]\nTags:[Kitchen]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 23 and (#Clock).minute == 0) {\n        if ((#Light #Kitchen).switch == \"on\") {\n            if ((#Dehumidifier #Bathroom).switch == \"on\") {\n                (#Dehumidifier #Bathroom).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 조명이 켜져 있는 경우 밤 11시에 차고 제습기를 꺼줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]',\n'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Garage]',\n'Light': 'Functions : [\n    on(),\n    off(),\n    setColor(color: string {\"{hue}|{saturation}|{brightness}\"})\n    setLevel(level int [0 ~ 100])\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    light : double\n]\nTags:[Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 23 and (#Clock).minute == 0) {\n        if ((#Light #Bedroom).switch == \"on\") {\n            if ((#Dehumidifier #Garage).switch == \"on\") {\n                (#Dehumidifier #Garage).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 내일 기숙사 식당의 점심 메뉴를 거실 스피커로 알려줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'MenuProvider': 'Functions : [\n    menu(command: string) : command format {\"{오늘|내일} {학생식당|수의대식당|전망대(3식당)|예술계식당(아름드리리)|기숙사식당|아워홈|동원관식당(113동)|웰스토리(220동)|투굿(공대간이식당)|자하연식당|301동식당} {아침|점심|저녁}\"}\n    todayMenu()\n]\nValues : []\nTags:[]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[LivingRoom,Office]'}"
        },
        {
            "from": "gpt",
            "value": "menu_info = (#MenuProvider).menu(\"내일 기숙사식당 점심\")\nif ((#Speaker #LivingRoom).switch == \"off\") {\n    (#Speaker #LivingRoom).on()\n}\n(#Speaker #LivingRoom).speak(menu_info)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 내일 기숙사 식당의 점심 메뉴를 침실 스피커로 알려줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'MenuProvider': 'Functions : [\n    menu(command: string) : command format {\"{오늘|내일} {학생식당|수의대식당|전망대(3식당)|예술계식당(아름드리리)|기숙사식당|아워홈|동원관식당(113동)|웰스토리(220동)|투굿(공대간이식당)|자하연식당|301동식당} {아침|점심|저녁}\"}\n    todayMenu()\n]\nValues : []\nTags:[Kitchen,Cafeteria]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[]'}"
        },
        {
            "from": "gpt",
            "value": "menu_info = (#MenuProvider).menu(\"내일 기숙사식당 점심\")\nif ((#Speaker #Bedroom).switch == \"off\") {\n    (#Speaker #Bedroom).on()\n}\n(#Speaker #Bedroom).speak(menu_info)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 내일 기숙사 식당의 점심 메뉴를 기숙사 스피커로 알려줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'MenuProvider': 'Functions : [\n    menu(command: string) : command format {\"{오늘|내일} {학생식당|수의대식당|전망대(3식당)|예술계식당(아름드리리)|기숙사식당|아워홈|동원관식당(113동)|웰스토리(220동)|투굿(공대간이식당)|자하연식당|301동식당} {아침|점심|저녁}\"}\n    todayMenu()\n]\nValues : []\nTags:[]', 'Speaker': 'Functions : [\n    on(),\n    off(),\n    pause(),\n    stop(),\n    play(source: string),\n    speak(text: string)\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\n]\nTags:[DormRoom,Library]'}"
        },
        {
            "from": "gpt",
            "value": "menu_info = (#MenuProvider).menu(\"내일 기숙사식당 점심\")\nif ((#Speaker #DormRoom).switch == \"off\") {\n    (#Speaker #DormRoom).on()\n}\n(#Speaker #DormRoom).speak(menu_info)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 5시에 지하실 제습기를 켜고 내부 관리 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Basement,LivingRoom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 17 and (#Clock).minute == 0) {\n        if ((#Dehumidifier #Basement).switch == \"off\") {\n            (#Dehumidifier #Basement).on()\n        }\n        if ((#Dehumidifier #Basement).dehumidifierMode != \"internalCare\") {\n            (#Dehumidifier #Basement).setDehumidifierMode(\"internalCare\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 차고 제습기를 켜고 오후 5시에 내부 관리 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Bathroom,Garage]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 17 and (#Clock).minute == 0) {\n        if ((#Dehumidifier #Garage).switch == \"off\") {\n            (#Dehumidifier #Garage).on()\n        }\n        if ((#Dehumidifier #Garage).dehumidifierMode != \"internalCare\") {\n            (#Dehumidifier #Garage).setDehumidifierMode(\"internalCare\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 5시에 욕실 제습기를 켜고 내부 관리 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Attic,Bathroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 17 and (#Clock).minute == 0) {\n        if ((#Dehumidifier #Bathroom).switch == \"off\") {\n            (#Dehumidifier #Bathroom).on()\n        }\n        if ((#Dehumidifier #Bathroom).dehumidifierMode != \"internalCare\") {\n            (#Dehumidifier #Bathroom).setDehumidifierMode(\"internalCare\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실의 CO2 수치가 600ppm 이상인 경우 오후 7시에 침실 제습기를 AID건조 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[Livingroom]', 'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 19 and (#Clock).minute == 0) {\n        if ((#AirQualityDetector #Livingroom).carbonDioxide > 600.0) {\n            if ((#Dehumidifier #Bedroom).switch == \"off\") {\n                (#Dehumidifier #Bedroom).on()\n            }\n            if ((#Dehumidifier #Bedroom).dehumidifierMode != \"AIDrying\") {\n                (#Dehumidifier #Bedroom).setDehumidifierMode(\"AIDrying\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방의 CO2 수치가 600ppm 이상인 경우 오후 7시에 사무실 제습기를 AID건조 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[Kitchen]', 'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Office]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 19 and (#Clock).minute == 0) {\n        if ((#AirQualityDetector #Kitchen).carbonDioxide > 600.0) {\n            if ((#Dehumidifier #Office).switch == \"off\") {\n                (#Dehumidifier #Office).on()\n            }\n            if ((#Dehumidifier #Office).dehumidifierMode != \"AIDrying\") {\n                (#Dehumidifier #Office).setDehumidifierMode(\"AIDrying\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 식당의 CO2 수치가 600ppm 이상인 경우 오후 7시에 지하실 제습기를 건조 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[Diningroom]', 'Dehumidifier': 'Functions : [\n    on(),\n    off(),\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\n]\nTags:[Basement]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 19 and (#Clock).minute == 0) {\n        if ((#AirQualityDetector #Diningroom).carbonDioxide > 600.0) {\n            if ((#Dehumidifier #Basement).switch == \"off\") {\n                (#Dehumidifier #Basement).on()\n            }\n            if ((#Dehumidifier #Basement).dehumidifierMode != \"AIDrying\") {\n                (#Dehumidifier #Basement).setDehumidifierMode(\"AIDrying\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주말 오후 9시에 거실 조명을 켜고 파란색으로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Light': 'Functions : [\n    on(),\n    off(),\n    setColor(color: string {\"{hue}|{saturation}|{brightness}\"})\n    setLevel(level int [0 ~ 100])\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    light : double\n]\nTags:[Livingroom,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).weekday == \"saturday\" or (#Clock).weekday == \"sunday\") {\n        if ((#Clock).hour == 21 and (#Clock).minute == 0) {\n            if ((#Light #Livingroom).switch == \"off\") {\n                all(#Light #Livingroom).on()\n            }\n            all(#Light #Livingroom).setColor(\"240|100|100\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주말 오후 9시에 주방 조명을 켜고 파란색으로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Light': 'Functions : [\n    on(),\n    off(),\n    setColor(color: string {\"{hue}|{saturation}|{brightness}\"})\n    setLevel(level int [0 ~ 100])\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    light : double\n]\nTags:[Livingroom,Kitchen,Hallway]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).weekday == \"saturday\" or (#Clock).weekday == \"sunday\") {\n        if ((#Clock).hour == 21 and (#Clock).minute == 0) {\n            if (any(#Light #Kitchen).switch != \"on\") {\n                all(#Light #Kitchen).on()\n            }\n            all(#Light #Kitchen).setColor(\"240|100|100\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주말 오후 9시에 침실 조명을 켜고 파란색으로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Light': 'Functions : [\n    on(),\n    off(),\n    setColor(color: string {\"{hue}|{saturation}|{brightness}\"})\n    setLevel(level int [0 ~ 100])\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    light : double\n]\nTags:[Kitchen,Bedroom,Bathroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).weekday == \"saturday\" or (#Clock).weekday == \"sunday\") {\n        if ((#Clock).hour == 21 and (#Clock).minute == 0) {\n            if (any(#Light #Bedroom).switch != \"on\") {\n                all(#Light #Bedroom).on()\n            }\n            all(#Light #Bedroom).setColor(\"240|100|100\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실 TV를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Television': 'Functions : [\n    on(),\n\toff(),\n\tsetTvChannel(tvChannel: int),\n\tchannelUp(),\n\tchannelDown(),\n    setVolume(volume: int [0 ~ 100]),\n    volumeUp(),\n    volumeDown(),\n\tmute() : void, toggle muteStatus\n\nValues : [\n\tswitch : string {\"on\"|\"off\"}\n\tmuteStatus : string {\"muted\"|\"unmuted\"}\n\ttvChannel : int\n]\nTags:[LivingRoom,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Television #Livingroom).switch == \"off\") {\n\t(#Television #Livingroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 TV를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Television': 'Functions : [\n    on(),\n\toff(),\n\tsetTvChannel(tvChannel: int),\n\tchannelUp(),\n\tchannelDown(),\n    setVolume(volume: int [0 ~ 100]),\n    volumeUp(),\n    volumeDown(),\n\tmute() : void, toggle muteStatus\n\nValues : [\n\tswitch : string {\"on\"|\"off\"}\n\tmuteStatus : string {\"muted\"|\"unmuted\"}\n\ttvChannel : int\n]\nTags:[Livingroom,Bedroom,GuestRoom]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Television #Bedroom).switch == \"off\") {\n\t(#Television #Bedroom).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방 TV를 켜줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Television': 'Functions : [\n    on(),\n\toff(),\n\tsetTvChannel(tvChannel: int),\n\tchannelUp(),\n\tchannelDown(),\n    setVolume(volume: int [0 ~ 100]),\n    volumeUp(),\n    volumeDown(),\n\tmute() : void, toggle muteStatus\n\nValues : [\n\tswitch : string {\"on\"|\"off\"}\n\tmuteStatus : string {\"muted\"|\"unmuted\"}\n\ttvChannel : int\n]\nTags:[Bedroom,Guestroom,Kitchen, DiningRoom]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#Television #Kitchen).switch == \"off\") {\n\t(#Television #Kitchen).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실의 VOC 수치가 0.05 미만인 경우 오후 6시에 주방 식기세척기를 에코 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[LivingRoom]', 'Dishwasher': 'Functions : [\n    on(),\n    off(),\n    setDishwasherMode(mode: string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dishwasherMode : string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"}\n]\nTags:[Kitchen]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 18 and (#Clock).minute == 0) {\n        if ((#AirQualityDetector #LivingRoom).tvocLevel < 0.05) {\n            if ((#Dishwasher #Kitchen).switch == \"off\") {\n                (#Dishwasher #Kitchen).on()\n            }\n            if ((#Dishwasher #Kitchen).dishwasherMode != \"eco\") {\n                (#Dishwasher #Kitchen).setDishwaherMode(\"eco\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 복도의 VOC 수치가 0.05 미만인 경우 오후 6시에 사무실 식기세척기를 에코 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[Livingroom,Basement,Hallway]', 'Dishwasher': 'Functions : [\n    on(),\n    off(),\n    setDishwasherMode(mode: string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dishwasherMode : string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"}\n]\nTags:[Livingroom,Kitchen,Office]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 18 and (#Clock).minute == 0) {\n        if ((#AirQualityDetector #Hallway).tvocLevel < 0.05) {\n            if ((#Dishwasher #Office).switch == \"off\") {\n                (#Dishwasher #Office).on()\n            }\n            if ((#Dishwasher #Office).dishwasherMode != \"eco\") {\n                (#Dishwasher #Office).setDishwaherMode(\"eco\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 차고의 VOC 수치가 0.05 미만인 경우 오후 6시에 지하실 식기세척기를 에코 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags:[Garage]', 'Dishwasher': 'Functions : [\n    on(),\n    off(),\n    setDishwasherMode(mode: string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"})\n]\nValues : [\n    switch : string {\"on\"|\"off\"},\n    dishwasherMode : string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"}\n]\nTags:[Basement]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 18 and (#Clock).minute == 0) {\n        if ((#AirQualityDetector #Garage).tvocLevel < 0.05) {\n            if ((#Dishwasher #Basement).switch == \"off\") {\n                (#Dishwasher #Basement).on()\n            }\n            if ((#Dishwasher #Basement).dishwasherMode != \"eco\") {\n                (#Dishwasher #Basement).setDishwaherMode(\"eco\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 날씨가 맑으면 매일 오후 5시에 거실 창문을 모두 열어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'WeatherProvider': 'Functions : [\n    getWeatherInfo(double latitude, double longitude): return string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"}\n]\nValues : [\n    weather : string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"},\n    temperature : int celcius,\n    humidity : double,\n    pressure : double\n]\nTags:[]', 'Window': 'Functions : [\n    open(),\n    close()\n]\nValues : [\n    window : string {\"closed\"|\"open\"}\n]\nTags:[LivingRoom,Bedroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 17 and (#Clock).minute == 0){\n        if((#WeatherProvider).weather == \"clear\"){\n            if(all(#Window #LivingRoom).window != \"open\"){\n                all(#Window #LivingRoom).open()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 날씨가 맑으면 매일 오후 5시에 침실 창문을 열어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'WeatherProvider': 'Functions : [\n    getWeatherInfo(double latitude, double longitude): return string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"}\n]\nValues : [\n    weather : string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"},\n    temperature : int celcius,\n    humidity : double,\n    pressure : double\n]\nTags:[]', 'Window': 'Functions : [\n    open(),\n    close()\n]\nValues : [\n    window : string {\"closed\"|\"open\"}\n]\nTags:[Kitchen,Livingroom,Bedroom,Bathroom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 17 and (#Clock).minute == 0){\n        if((#WeatherProvider).weather == \"clear\"){\n            if(any(#Window #Bedroom).window != \"open\"){\n                all(#Window #Bedroom).open()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 날씨가 맑으면 매일 오후 5시에 주방 창문을 열어줘.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'WeatherProvider': 'Functions : [\n    getWeatherInfo(double latitude, double longitude): return string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"}\n]\nValues : [\n    weather : string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"},\n    temperature : int celcius,\n    humidity : double,\n    pressure : double\n]\nTags:[]', 'Window': 'Functions : [\n    open(),\n    close()\n]\nValues : [\n    window : string {\"closed\"|\"open\"}\n]\nTags:[Basement,Livingroom,Kitchen,DiningRoom]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN){\n    if((#Clock).hour == 17 and (#Clock).minute == 0){\n        if((#WeatherProvider).weather == \"clear\"){\n            if((#Window #Kitchen).window != \"open\"){\n                (#Window #Kitchen).open()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실의 스마트 플러그를 꺼줘.\n\nServices: {'SmartPlug': 'Functions : [\n    on(),\n\toff()\n]\nValues : [\n\tswitch : string {\"on\"|\"off\"},\n    chargingState : string {\"charging\"|\"discharging\"|\"stopped\"|\"fullyCharged\"|\"error\"},\n    voltage : double,\n    current : double\n]\nTags:[LivingRoom,Bedroom,Kitchen]', 'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#SmartPlug #LivingRoom).switch == \"on\") {\n    (#SmartPlug #LivingRoom).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 차고에서 스마트 플러그를 꺼줘.\n\nServices: {'SmartPlug': 'Functions : [\n    on(),\n\toff()\n]\nValues : [\n\tswitch : string {\"on\"|\"off\"},\n    chargingState : string {\"charging\"|\"discharging\"|\"stopped\"|\"fullyCharged\"|\"error\"},\n    voltage : double,\n    current : double\n]\nTags:[Basement,Garage,Workshop]', 'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#SmartPlug #Garage).switch == \"on\") {\n    (#SmartPlug #Garage).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 사무실의 스마트 플러그를 꺼줘.\n\nServices: {'SmartPlug': 'Functions : [\n    on(),\n\toff()\n]\nValues : [\n\tswitch : string {\"on\"|\"off\"},\n    chargingState : string {\"charging\"|\"discharging\"|\"stopped\"|\"fullyCharged\"|\"error\"},\n    voltage : double,\n    current : double\n]\nTags:[Kitchen,Office,Study]', 'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#SmartPlug #Office).switch == \"on\") {\n    (#SmartPlug #Office).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: PM 10 수치가 150 이상이고 VOC 수치가 0.1 이상이면 거실 블라인드를 80%로 설정해줘. CO2 수치가 400ppm 미만인 경우 침실 블라인드를 0%로 설정해줘.\n\nServices: {\n'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []',\n\n'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags: [LivingRoom,Bedroom]',\n\n'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags: [Kitchen,Office]'\n}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector).dustLevel > 150.0 and (#AirQualityDetector).tvocLevel > 0.1) {\n        if ((#Blind #LivingRoom).blindLevel != 80) {\n            (#Blind #LivingRoom).setBlindLevel(80)\n        }\n    }\n    if ((#AirQualityDetector).carbonDioxide < 400.0) {\n        if ((#Blind #Bedroom).blindLevel != 0) {\n            (#Blind #Bedroom).setBlindLevel(0)\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: PM 10 수치가 150 이상이고 VOC 수치가 0.1 이상이면 사무실 블라인드를 80%로 설정해줘. CO2 수치가 400ppm 미만인 경우 주방 블라인드를 0%로 설정해줘.\n\nServices: {\n'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []',\n\n'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags: [Office,Kitchen]',\n\n'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags: [LivingRoom,Bedroom]'\n}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector).dustLevel > 150.0 and (#AirQualityDetector).tvocLevel > 0.1) {\n        if ((#Blind #Office).blindLevel != 80) {\n            (#Blind #Office).setBlindLevel(80)\n        }\n    }\n    if ((#AirQualityDetector).carbonDioxide < 400.0) {\n        if ((#Blind #Kitchen).blindLevel != 0) {\n            (#Blind #Kitchen).setBlindLevel(0)\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: PM 10 수치가 150 이상이고 VOC 수치가 0.1 이상이면 지하실 블라인드를 80%로 설정해줘. CO2 수치가 400ppm 미만인 경우 다락 블라인드를 0%로 설정해줘.\n\nServices: {\n'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags: []',\n\n'Blind': 'Functions : [\n    setBlindLevel(level: int [0 ~ 100])\n]\nValues : [\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\n    blindLevel : int [0 ~ 100]\n]\nTags: [Basement,Attic]',\n\n'AirQualityDetector': 'Functions : []\nValues : [\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\n    carbonDioxide : double : CO2 level,\n    temperature : int [-460 ~ 10000],\n    humidity : double [0 ~ 100],\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\n]\nTags: [Garage,Bathroom]'\n}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector).dustLevel > 150.0 and (#AirQualityDetector).tvocLevel > 0.1) {\n        if ((#Blind #Basement).blindLevel != 80) {\n            (#Blind #Basement).setBlindLevel(80)\n        }\n    }\n    if ((#AirQualityDetector).carbonDioxide < 400.0) {\n        if ((#Blind #Attic).blindLevel != 0) {\n            (#Blind #Attic).setBlindLevel(0)\n        }\n    }\n}"
        }
    ]
]
