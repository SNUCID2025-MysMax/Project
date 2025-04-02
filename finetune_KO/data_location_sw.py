data_location_sw = [
    [
        {
            "from": "human",
            "value": "Input: 주방의 급식기가 쉬고 있으면 내 방의 커튼을 열어줘.\n\nServices: {'Feeder': 'Functions : [\\n    on(),\\n\\toff(),\\n    startFeeding(),\\n    setFeedPortion(portion: double [0 ~ 2000], unit: string {\"grams\"|\"pounds\"|\"ounces\"|\"servings\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    feederOperatingState : string {\"idle\"|\"feeding\"|\"error\"}\\n]\\nTags : [\\n    livingroom,\\n    kitchen,\\n    utilityroom\\n]', 'Curtain': 'Functions : [\\n    setCurtainLevel(level: int [0 ~ 100])\\n]\\nValues : [\\n    curtain : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\\n    curtainLevel : int [0 ~ 100]\\n]\\nTags : [\\n    myroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#kitchen #Feeder).feederState == \"idle\") {\n    if ((#myroom #Curtain).curtainLevel != 100) {\n        (#myroom #Curtain).setCurtainLevel(100)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 온도가 30°C를 초과하고 발코니의 카메라가 꺼져 있는 경우 카메라를 켜고 거실의 에어컨을 강 모드로 설정해줘.\n\nServices: {'Camera': 'Functions : [\\n    on(),\\n\\toff(),\\n    take() : return binary : storage path for image(photo),\\n    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    image : binary : the storage path for the most recent image(photo)\\n]\\nTags : [\\n    livingroom,\\n    balcony,\\n    bedroom\\n]', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector).temperature > 30.0 and (#Camera).switch != \"on\") {\n        (#balcony #Camera).on()\n        if ((#livingroom #AirConditioner).airConditionerMode != \"high\") {\n            (#livingroom #AirConditioner).setAirConditionerMode(\"high\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 오후 11시 5분에 정문과 뒷문이 열려 있으면 닫아줘.\n\nServices: {'DoorLock': 'Functions : []\\nValues : [\\n    door : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"unknown\"}\\n]\\nTags : [\\n    entrance,\\n    maindoor,\\n    backdoor\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#Clock).hour == 23 and (#Clock).minute == 5 and (#Clock).second == 0){\n        if((#maindoor #DoorLock).door != \"closed\"){\n            (#maindoor #DoorLock).close()\n        }\n        if((#backdoor #DoorLock).door != \"closed\"){\n            (#backdoor #DoorLock).close()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실의 그늘막을 완전히 닫아줘.\n\nServices: {'Shade': 'Functions : [\\n\\topen(),\\n\\tclose(),\\n    setShadeLevel(openPercent: int[0 ~ 100])\\n]\\nValues : [\\n    shadeLevel : int openPercent[0 ~ 100]\\n]\\nTags : [\\n    myroom,\\n    bathroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#bathroom #Shade).shadeLevel > 0) {\n    (#bathroom #Shade).setShadeLevel(0)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 6시에 가스 계량기가 50대를 초과하면 마당에 있는 관개 시스템을 꺼줘.\n\nServices: {'Irrigator': 'Functions : [\\n    on(),\\n    off(),\\n    startWatering(),\\n    setWaterPortion(portion: double [0 ~ 2000], unit: string {\"liters\"|\"milliliters\"|\"gallons\"|\"ounces\"})\\n]\\nValues :\\t[\\n    switch: string {\"on\"|\"off\"}\\n]\\nTags : [\\n    balcony,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 18 and (#Clock).minute == 0) {\n        if ((#GasMeter).gasMeter > 50) {\n            if ((#yard #Irrigator).switch != \"off\") {\n                (#yard #Irrigator).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실과 거실의 조명을 켜고 연기가 감지되면 노란색으로 설정해줘.\n\nServices: {'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    garage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#SmokeDetector).smoke == \"detected\") {\n        if ((#bedroom #Light).switch != \"on\") {\n            (#bedroom #Light).on()\n        }\n        (#bedroom #Light).setColor(\"60|100|100\")\n        if ((#livingroom #Light).switch != \"on\") {\n            (#livingroom #Light).on()\n        }\n        (#livingroom #Light).setColor(\"60|100|100\")\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현재 미세먼지(PM 10) 농도를 측정하여 거실의 스피커를 통해 알려줘.\n\nServices: {'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#livingroom #Speaker).switch != \"on\") {\n    (#livingroom #Speaker).on()\n}\n(#livingroom #Speaker).speak(\"현재 미세먼지 농도는 \" + (#AirQualityDetector).dustLevel)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매일 8시마다 내 방의 가습기를 켜줘.\n\nServices: {'Humidifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setHumidiferMode(mode: string {\"auto\"|\"low\"|\"medium\"|\"high\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    humidifierMode : string {\"auto\"|\"low\"|\"medium\"|\"high\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop (1 MIN, (#Clock).hour == 8 and (#Clock).minute == 0) {\n    if ((#myroom #Humidifier).switch != \"on\") {\n        (#myroom #Humidifier).on()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: VOC 수치가 0.01 이하인 경우 오후 9시 30분에 주방의 공기청정기를 꺼줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]', 'AirPurifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\\n]\\nTags : [\\n    kitchen,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 21 and (#Clock).minute == 30) {\n        if ((#AirQualityDetector).tvocLevel < 0.01) {\n            if ((#kitchen #AirPurifier).switch != \"off\") {\n                (#kitchen #AirPurifier).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 창고에 있는 로봇 청소기를 자동 모드로 설정해줘.\n\nServices: {'RobotCleaner': 'Functions : [\\n    on(),\\n    off(),\\n    setRobotCleanerCleaningMode(string mode{\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"})\\n]\\nValues : [\\n    switch : string {\"on\"|\"off\"},\\n    robotCleanerCleaningMode : string {\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"}\\n\\n]\\nTags : [\\n    livingroom,\\n    storage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#storage #RobotCleaner).robotCleanerCleaningMode != \"auto\") {\n\t(#storage #RobotCleaner).setRobotCleanerCleaningMode(\"auto\")\n}\nif ((#livingroom #RobotCleaner).switch != \"on\") {\n    (#livingroom #RobotCleaner).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 12시에 다용도실 제습기를 꺼줘.\n\nServices: {'Dehumidifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\\n]\\nTags : [\\n    utilityroom,\\n    storage,\\n    laundryroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 0 and (#Clock).minute == 0) {\n        if ((#utilityroom #Dehumidifier).switch != \"off\") {\n            (#utilityroom #Dehumidifier).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 1시간 40분 15초 후에 발코니와 욕실의 창문을 열어줘.\n\nServices: {'Window': 'Functions : [\\n    open(),\\n    close()\\n]\\nValues : [\\n    window : string {\"closed\"|\"open\"}\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (1 HOUR)\nwait until (40 MIN)\nwait until (15 SEC)\nif ((#balcony #Window).window != \"open\") {\n    (#balcony #Window).open()\n}\nif ((#bathroom #Window).window != \"open\") {\n    (#bathroom #Window).open()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 소리가 감지되면 주방의 식기세척기를 켜줘.\n\nServices: {'Dishwasher': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDishwasherMode(mode: string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dishwasherMode : string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"}\\n]\\nTags : [\\n    kitchen\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#SoundSensor).sound == \"detected\") {\n        if ((#kitchen #Dishwasher).switch != \"on\") {\n            (#kitchen #Dishwasher).on()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 온도가 28°C 이상인 경우 오전 9시에 보관함의 제습기를 냉각 모드로 설정해줘.\n\nServices: {'Dehumidifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\\n]\\nTags : [\\n    utilityroom,\\n    storage,\\n    laundryroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 9 and (#Clock).minute == 0) {\n        if ((#AirQualityDetector).temperature > 28.0) {\n            if ((#storage #Dehumidifier).switch != \"on\") {\n                (#storage #Dehumidifier).on()\n            }\n            if ((#storage #Dehumidifier).dehumidifierMode != \"cooling\") {\n                (#storage #Dehumidifier).setDehumidifierMode(\"cooling\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 침실 블라인드가 50%인 경우 80%로 설정해줘.\n\nServices: {'Blind': 'Functions : [\\n    setBlindLevel(level: int [0 ~ 100])\\n]\\nValues : [\\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\\n    blindLevel : int [0 ~ 100]\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#bedroom #Blind).blindLevel == 50) {\n    (#bedroom #Blind).setBlindLevel(80)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매시간 미세먼지 농도가 50보다 낮으면 주방 가스 밸브를 잠가줘.\n\nServices: {'GasValve': 'Functions : [\\n\\topen(),\\n\\tclose()\\n]\\nValues : [\\n    valve : string {\"open\"|\"closed\"}\\n]\\nTags : [\\n    kitchen\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop (1 HOUR) {\n    if ((#AirQualityDetector).dustLevel < 50.0) {\n        (#kitchen #GasValve).close()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 3시간 20분 10초 후에 마당에 있는 스피커를 꺼줘.\n\nServices: {'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (3 HOUR)\nwait until (20 MIN)\nwait until (10 SEC)\nif ((#yard #Speaker).switch != \"off\") {\n    (#yard #Speaker).off()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the gas valve in the kitchen if smoke is detected in the kitchen or livingroom.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]', 'GasValve': 'Functions : [\\n\\topen(),\\n\\tclose()\\n]\\nValues : [\\n    valve : string {\"open\"|\"closed\"}\\n]\\nTags : [\\n    kitchen\\n]', 'SmokeDetector': 'Functions : []\\nValues : [\\n    smoke : string {\"detected\"|\"not_detected\"} \\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    bedroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    kitchen\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#kitchen #SmokeDetector).smoke == \"detected\" or (#livingroom #SmokeDetector).smoke == \"detected\") {\n        if ((#kitchen #GasValve).valve != \"closed\") {\n            (#kitchen #GasValve).close()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 6시마다 현재 기압을 확인하고 1기압을 넘으면 방 안 스피커를 통해 '고기압입니다'라고 알려줘.\n\nServices: {'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop (1 MIN, (#Clock).hour == 6 and (#Clock).minute == 0) {\n    if ((#WeatherProvider).pressure > 1) {\n        if ((#myroom #Speaker).switch != \"on\") {\n            (#myroom #Speaker).on()\n        }\n        (#myroom #Speaker).speak(\"고기압입니다\")\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 욕실에서 1시간 2분 5초 후에 그늘막을 닫아줘.\n\nServices: {'Shade': 'Functions : [\\n\\topen(),\\n\\tclose(),\\n    setShadeLevel(openPercent: int[0 ~ 100])\\n]\\nValues : [\\n    shadeLevel : int openPercent[0 ~ 100]\\n]\\nTags : [\\n    myroom,\\n    bathroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (1 HOUR)\nwait until (2 MIN)\nwait until (5 SEC)\nif ((#bathroom #Shade).shadeLevel > 0) {\n    (#bathroom #Shade).setShadeLevel(0)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 사무실의 CO2 수치가 1000ppm 이상이고 온도가 28°C를 초과하는 경우 블라인드를 50%로 설정해줘. 사무실의 PM 1.0 수치가 50을 초과하는 경우 블라인드를 30%로 설정해줘.\n\nServices: {'AirQualityDetector': 'Functions : []\\nValues : [\\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\\n    carbonDioxide : double : CO2 level,\\n    temperature : int [-460 ~ 10000],\\n    humidity : double [0 ~ 100],\\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Blind': 'Functions : [\\n    setBlindLevel(level: int [0 ~ 100])\\n]\\nValues : [\\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\\n    blindLevel : int [0 ~ 100]\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#office #AirQualityDetector).carbonDioxide > 1000.0 and (#office #AirQualityDetector).temperature > 28.0) {\n        if ((#office #Blind).blindLevel != 50) {\n            (#office #Blind).setBlindLevel(50)\n        }\n    }\n    if ((#office #AirQualityDetector).veryFineDustLevel > 50.0) {\n        if ((#office #Blind).blindLevel != 30) {\n            (#office #Blind).setBlindLevel(30)\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 9시에 거실에서 로봇청소기를 지도 모드로 설정하고 거실에 안개가 낀 경우 조명을 켜줘.\n\nServices: {'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    garage\\n]', 'RobotCleaner': 'Functions : [\\n    on(),\\n    off(),\\n    setRobotCleanerCleaningMode(string mode{\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"})\\n]\\nValues : [\\n    switch : string {\"on\"|\"off\"},\\n    robotCleanerCleaningMode : string {\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"}\\n\\n]\\nTags : [\\n    livingroom,\\n    storage\\n]', 'WeatherProvider': 'Functions : [\\n    getWeatherInfo(double latitude, double longitude): return string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"}\\n]\\nValues : [\\n    weather : string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"},\\n\\ttemperature : int celcius,\\n\\thumidity : double,\\n\\tpressure : double\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 9 and (#Clock).minute == 0) {\n        if ((#livingroom #RobotCleaner).robotCleanerCleaningMode != \"map\") {\n            (#livingroom #RobotCleaner).setRobotCleanerCleaningMode(\"map\")\n        }\n        if ((#livingroom #RobotCleaner).switch != \"on\") {\n            (#livingroom #RobotCleaner).on()\n        }\n        if ((#livingroom #WeatherProvider).weatherCondition == \"fog\") {\n            if ((#livingroom #Light).switch != \"on\") {\n                (#livingroom #Light).on()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 8시에 주방에서 식기세척기를 빠른 모드로 설정해줘.\n\nServices: {'Dishwasher': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDishwasherMode(mode: string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dishwasherMode : string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"}\\n]\\nTags : [\\n    kitchen\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 8 and (#Clock).minute == 0) {\n        if ((#kitchen #Dishwasher).switch != \"on\") {\n            (#kitchen #Dishwasher).on()\n        }\n        if ((#kitchen #Dishwasher).dishwasherMode != \"quick\") {\n            (#kitchen #Dishwasher).setDishwasherMode(\"quick\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 지금 현관에 문이 열려 있으면 문이 열릴 때까지 기다렸다가 거실에 있는 에어컨을 켜줘.\n\nServices: {'DoorLock': 'Functions : []\\nValues : [\\n    door : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"unknown\"}\\n]\\nTags : [\\n    entrance,\\n    maindoor,\\n    backdoor\\n]', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#entrance #DoorLock).door == \"opening\") {\n\twait until((#entrance #DoorLock).door == \"open\")\n    if ((#livingroom #AirConditioner).switch != \"on\") {\n        (#livingroom #AirConditioner).on()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 5분마다 침실에서 현재 PM 1.0 기준 초미세먼지 농도가 50보다 높으면 거실에서 사이렌을 울려줘.\n\nServices: {'AirQualityDetector': 'Functions : []\\nValues : [\\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\\n    carbonDioxide : double : CO2 level,\\n    temperature : int [-460 ~ 10000],\\n    humidity : double [0 ~ 100],\\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Siren': 'Functions : [\\n    on(),\\n\\toff(),\\n    setSirenMode(mode: string {\"both\"|\"off\"|\"siren\"|\"strobe\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    sirenMode : string {\"both\"|\"off\"|\"siren\"|\"strobe\"}\\n]\\nTags : [\\n    livingroom,\\n    entrance,\\n    garage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop (5 MIN) {\n    if ((#bedroom #AirQualityDetector).veryFineDustLevel > 50.0) {\n        if ((#livingroom #Siren).switch != \"on\") {\n            (#livingroom #Siren).on()\n        }\n        (#livingroom #Siren).setSirenMode(\"both\")\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 11시에 아무도 감지되지 않으면 거실의 TV를 꺼줘.\n\nServices: {'PresenceSensor': 'Functions : []\\nValues : [\\n    presence : string {\"present\"|\"not_present\"}\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage\\n]', 'Television': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetTvChannel(tvChannel: int),\\n\\tchannelUp(),\\n\\tchannelDown(),\\n    setVolume(volume: int [0 ~ 100]),\\n    volumeUp(),\\n    volumeDown(),\\n\\tmute() : void, toggle muteStatus\\n\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"}\\n\\tmuteStatus : string {\"muted\"|\"unmuted\"}\\n\\ttvChannel : int\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    bedroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 23 and (#Clock).minute == 0) {\n        if ((#livingroom #PresenceSensor).presence == \"not_present\") {\n            if ((#livingroom #Television).switch != \"off\") {\n                (#livingroom #Television).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 세탁실의 건조기가 현재 AI 건조 모드에 있는 경우 거실의 스피커를 통해 \"music.mp3\" 노래를 재생해줘.\n\nServices: {'Dehumidifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\\n]\\nTags : [\\n    utilityroom,\\n    storage,\\n    laundryroom\\n]', 'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#laundryroom #Dehumidifier).dehumidifierMode == \"AIDrying\") {\n    if ((#livingroom #Speaker).switch != \"on\") {\n        (#livingroom #Speaker).on()\n    }\n    (#livingroom #Speaker).play(\"music.mp3\")\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실의 공기청정기가 현재 저소음 모드가 아닌 경우 내 방의 스피커를 통해 \"시끄러워\"라고 말해줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]', 'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'AirPurifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\\n]\\nTags : [\\n    kitchen,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#livingroom #AirPurifier).airPurifierFanMode != \"quiet\") {\n    if ((#myroom #Speaker).switch != \"on\") {\n\t    (#myroom #Speaker).on()\n    }\n    (#myroom #Speaker).speak(\"시끄러워\")\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 20을 4로 나누고 거실 스피커를 통해 결과를 말해줘.\n\nServices: {'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "result = (#Calculator).div(20, 4)\nif ((#livingroom #Speaker).switch != \"on\") {\n    (#livingroom #Speaker).on()\n}\n(#livingroom #Speaker).speak(\"20을 4로 나눈 결과는 \" + result)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실의 카메라를 켜고 습도가 60%를 초과하면 거실의 공기청정기를 저소음 모드로 설정해줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]', 'AirQualityDetector': 'Functions : []\\nValues : [\\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\\n    carbonDioxide : double : CO2 level,\\n    temperature : int [-460 ~ 10000],\\n    humidity : double [0 ~ 100],\\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Camera': 'Functions : [\\n    on(),\\n\\toff(),\\n    take() : return binary : storage path for image(photo),\\n    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    image : binary : the storage path for the most recent image(photo)\\n]\\nTags : [\\n    livingroom,\\n    balcony,\\n    bedroom\\n]', 'AirPurifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\\n]\\nTags : [\\n    kitchen,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#livingroom #AirQualityDetector).humidity > 60.0) {\n        if ((#livingroom #Camera).switch != \"on\") {\n            (#livingroom #Camera).on()\n        }\n        if ((#livingroom #AirPurifier).airPurifierFanMode != \"quiet\") {\n            (#livingroom #AirPurifier).setPurifierFanMode(\"quiet\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 15분마다 주방의 식기세척기가 꺼져 있는 경우 전원을 켜고 자동 모드로 설정해줘.\n\nServices: {'Dishwasher': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDishwasherMode(mode: string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dishwasherMode : string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"}\\n]\\nTags : [\\n    kitchen\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop (15 MIN) {\n    if ((#kitchen #Dishwasher).switch != \"on\") {\n        (#kitchen #Dishwasher).on()\n    }\n    if ((#kitchen #Dishwasher).dishwasherMode != \"auto\") {\n        (#kitchen #Dishwasher).setDishwasherMode(\"auto\")\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 8시마다 거실의 스피커를 통해 소리 감지 상태가 안내해줘.\n\nServices: {'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop (1 MIN, (#Clock).hour == 8 and (#Clock).minute == 0) {\n    if ((#livingroom #Speaker).switch != \"on\") {\n        (#livingroom #Speaker).on()\n    }\n    if ((#SoundSensor).sound == \"detected\") {\n        (#livingroom #Speaker).speak(현재 소리가 감지됩니다.)\n    }\n    if ((#SoundSensor).sound == \"not_detected\") {\n        (#livingroom #Speaker).speak(현재 소리가 감지되지 않았습니다.)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 자정이 되면 침실의 TV를 꺼줘.\n\nServices: {'Television': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetTvChannel(tvChannel: int),\\n\\tchannelUp(),\\n\\tchannelDown(),\\n    setVolume(volume: int [0 ~ 100]),\\n    volumeUp(),\\n    volumeDown(),\\n\\tmute() : void, toggle muteStatus\\n\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"}\\n\\tmuteStatus : string {\"muted\"|\"unmuted\"}\\n\\ttvChannel : int\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    bedroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN, (#Clock).hour == 0 and (#Clock).minute == 0) {\n    if ((#bedroom #Television).switch != \"off\") {\n        (#bedroom #Television).off()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 7월 20일 오전 8시에 내 방과 마당에 있는 스피커를 통해 \"생일 축하합니다\"라고 말해줘.\n\nServices: {'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).month == 7 and (#Clock).day == 20 and (#Clock).hour == 8 and (#Clock).minute == 0) {\n        if ((#myroom #Speaker).switch != \"on\") {\n            (#myroom #Speaker).on()\n        }\n        (#myroom #Speaker).speak(\"Happy Birthday\")\n        if ((#yard #Speaker).switch != \"on\") {\n            (#yard #Speaker).on()\n        }\n        (#yard #Speaker).speak(\"생일 축하합니다\")\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 미세먼지 농도가 50 이상이면 침실에서 공기청정기를 켜줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]', 'AirQualityDetector': 'Functions : []\\nValues : [\\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\\n    carbonDioxide : double : CO2 level,\\n    temperature : int [-460 ~ 10000],\\n    humidity : double [0 ~ 100],\\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'AirPurifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\\n]\\nTags : [\\n    kitchen,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#bedroom #AirQualityDetector).fineDustLevel > 50.0) {\n    if ((#bedroom #AirPurifier).switch != \"on\"){\n        (#bedroom #AirPurifier).on()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 거실에 있는 스피커를 통해 현재 조도 값을 알려줘.\n\nServices: {'LightSensor': 'Functions : []\\nValues : [\\n    light : double\\n]', 'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#livingroom #Speaker).switch != \"on\") {\n    (#livingroom #Speaker).on()\n}\n(#livingroom #Speaker).speak(\"현재 조도 값은 \" + (#livingroom #LightSensor).light)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 매주 화요일 오후 8시에 차고에서 사이렌을 두 가지 모드로 설정해줘.\n\nServices: {'Siren': 'Functions : [\\n    on(),\\n\\toff(),\\n    setSirenMode(mode: string {\"both\"|\"off\"|\"siren\"|\"strobe\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    sirenMode : string {\"both\"|\"off\"|\"siren\"|\"strobe\"}\\n]\\nTags : [\\n    livingroom,\\n    entrance,\\n    garage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 20 and (#Clock).minute == 0 and (#Clock).weekday == \"tuesday\") {\n        if ((#garage #Siren).switch != \"on\") {\n            (#garage #Siren).on()\n        }\n        if ((#garage #Siren).sirenMode != \"both\") {\n            (#garage #Siren).setSirenMode(\"both\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현재 연기 감지 상태를 거실의 스피커로 출력해줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]', 'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'SmokeDetector': 'Functions : []\\nValues : [\\n    smoke : string {\"detected\"|\"not_detected\"} \\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    bedroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    kitchen\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#livingroom #Speaker).switch != \"on\") {\n\t(#livingroom #Speaker).on()\n}\nif ((#livingroom #SmokeDetector).smoke == \"detected\") {\n    (#livingroom #Speaker).speak(현재 연기가 감지되었습니다. 확인해주세요.)\n}\nif ((#livingroom #SmokeDetector).smoke == \"not_detected\") {\n    (#livingroom #Speaker).speak(현재 연기가 감지되지 않았습니다.)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 4시에 50% 미만인 경우 발코니의 조명 밝기를 75%로 설정해줘.\n\nServices: {'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    garage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 16 and (#Clock).minute == 0) {\n        if ((#balcony #Light).light < 50) {\n            if ((#balcony #Light).switch != \"on\") {\n                (#balcony #Light).on()\n            }\n            (#balcony #Light).setLevel(75)\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 6시에 정원의 펌프를 켜고 정원의 조명을 50%로 설정해줘.\n\nServices: {'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    garage\\n]', 'Pump': 'Functions : [\\n    on(),\\n\\toff(),\\n    setOperationMode(string mode {\"normal\"|\"minimum\"|\"maximum\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    operationMode : string {\"normal\"|\"minimum\"|\"maximum\"}\\n]\\nTags : [\\n    balcony,\\n    garden\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 6 and (#Clock).minute == 0) {\n        if ((#garden #Pump).switch != \"on\") {\n            (#garden #Pump).on()\n        }\n        if ((#garden #Light).switch != \"on\") {\n            (#garden #Light).on()\n        }\n        (#garden #Light).setLevel(50)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오후 9시 22분에 날씨가 '이슬비'이고 기온이 10°C 미만인 경우 거실의 에어컨을 난방 모드로 설정해줘.\n\nServices: {'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 21 and (#Clock).minute == 22) {\n        if ((#WeatherProvider).weather == 'drizzle' and (#WeatherProvider).temperature < 10) {\n            if ((#livingroom #AirConditioner).airConditionerMode != \"heat\") {\n                (#livingroom #AirConditioner).setAirConditionerMode(\"heat\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 이제 접촉 센서가 닫혀 있으면 주방의 전구를 꺼줘.\n\nServices: {'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    garage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#ContactSensor).contact == \"closed\") {\n    if ((#kitchen #Light).switch != \"off\") {\n\t    (#kitchen #Light).off()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 사무실의 PM 10 수치가 100 이상이고 온도가 25°C를 초과하는 경우 사무실의 블라인드를 40%로 설정해줘. 사무실의 CO2 수치가 600ppm 이상인 경우 사무실의 블라인드를 0%로 설정해줘.\n\nServices: {'AirQualityDetector': 'Functions : []\\nValues : [\\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\\n    carbonDioxide : double : CO2 level,\\n    temperature : int [-460 ~ 10000],\\n    humidity : double [0 ~ 100],\\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Blind': 'Functions : [\\n    setBlindLevel(level: int [0 ~ 100])\\n]\\nValues : [\\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\\n    blindLevel : int [0 ~ 100]\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#office #AirQualityDetector).dustLevel > 100.0 and (#office #AirQualityDetector).temperature > 25.0) {\n        if ((#office #Blind).blindLevel != 40) {\n            (#office #Blind).setBlindLevel(40)\n        }\n    }\n    if ((#office #AirQualityDetector).carbonDioxide > 600.0) {\n        if ((#office #Blind).blindLevel != 0) {\n            (#office #Blind).setBlindLevel(0)\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 6시 8분에 기온이 8°C 미만인 경우 침실에서 난방 모드로 에어컨을 켜줘.\n\nServices: {'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 6 and (#Clock).minute == 8) {\n        if ((#WeatherProvider).temperature < 8) {\n            if ((#bedroom #AirConditioner).airConditionerMode != \"heat\") {\n                (#bedroom #AirConditioner).setAirConditionerMode(\"heat\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 현재 날씨가 맑으면 거실에 있는 에어컨을 켜줘.\n\nServices: {'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#WeatherProvider).weather == \"clear\") {\n\tif ((#livingroom #AirConditioner).switch != \"on\") {\n\t\t(#livingroom #AirConditioner).on()\n\t}\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 오전 7시에 다용도실의 제습기를 무게감지 모드로 설정하고 VOC 수치가 0.03 이하인 경우 제습기를 작동해줘.\n\nServices: {'AirQualityDetector': 'Functions : []\\nValues : [\\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\\n    carbonDioxide : double : CO2 level,\\n    temperature : int [-460 ~ 10000],\\n    humidity : double [0 ~ 100],\\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Dehumidifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\\n]\\nTags : [\\n    utilityroom,\\n    storage,\\n    laundryroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 7 and (#Clock).minute == 0) {\n        if ((#utilityroom #AirQualityDetector).tvocLevel < 0.03) {\n            if ((#utilityroom #Dehumidifier).switch != \"on\") {\n                (#utilityroom #Dehumidifier).on()\n            }\n            if ((#utilityroom #Dehumidifier).dehumidifierMode != \"weightSensing\") {\n                (#utilityroom #Dehumidifier).setDehumidifierMode(\"weightSensing\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 차고의 접촉 센서가 열려 있으면 조명을 켜고 차고의 밝기를 70%로 설정해줘.\n\nServices: {'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    garage\\n]', 'ContactSensor': 'Functions : []\\nValues : [\\n    contact : string {\"open\"|\"closed\"}\\n]\\nTags : [\\n    entrance,\\n    maindoor,\\n    backdoor,\\n    garage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#garage #ContactSensor).contact == \"open\") {\n        if ((#garage #Light).switch != \"on\") {\n            (#garage #Light).on()\n        }\n        (#garage #Light).setBrightness(70)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 세탁실에 있는 제습기를 켜고 오후 8시에 해동 모드로 설정해줘.\n\nServices: {'Dehumidifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\\n]\\nTags : [\\n    utilityroom,\\n    storage,\\n    laundryroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 20 and (#Clock).minute == 0) {\n        if ((#laundryroom #Dehumidifier).switch != \"on\") {\n            (#laundryroom #Dehumidifier).on()\n        }\n        if ((#laundryroom #Dehumidifier).dehumidifierMode != \"thawingFrozenInside\") {\n            (#laundryroom #Dehumidifier).setDehumidifierMode(\"thawingFrozenInside\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 새벽 3시 15분에 내 방의 선풍기 속도를 2로 설정해줘.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]', 'Fan': 'Functions : [\\n    on(),\\n\\toff(),\\n    setFanSpeed(speed: int [0 ~ ∞])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\n]\\nTags : [\\n    myroom,\\n    livingroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 3 and (#Clock).minute == 15) {\n        (#myroom #Fan).setFanSpeed(2)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: 주방의 불을 켜줘.\n\nServices: {'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    garage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#kitchen #Light).switch != \"on\") {\n\t(#kitchen #Light).on()\n}"
        }
    ]
]
