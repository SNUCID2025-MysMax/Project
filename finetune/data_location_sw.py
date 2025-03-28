data_location_sw = [
    [
        {
            "from": "human",
            "value": "Input: If the kitchen feeding machine is resting, open the curtains in my room.\n\nServices: {'Feeder': 'Functions : [\\n    on(),\\n\\toff(),\\n    startFeeding(),\\n    setFeedPortion(portion: double [0 ~ 2000], unit: string {\"grams\"|\"pounds\"|\"ounces\"|\"servings\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    feederOperatingState : string {\"idle\"|\"feeding\"|\"error\"}\\n]\\nTags : [\\n    livingroom,\\n    kitchen,\\n    utilityroom\\n]', 'Curtain': 'Functions : [\\n    setCurtainLevel(level: int [0 ~ 100])\\n]\\nValues : [\\n    curtain : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\\n    curtainLevel : int [0 ~ 100]\\n]\\nTags : [\\n    myroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#kitchen #Feeder).feederState == \"idle\") {\n    if ((#myroom #Curtain).curtainLevel != 100) {\n        (#myroom #Curtain).setCurtainLevel(100)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: If temperature exceeds 30°C and camera in the balcony is off, turn on the camera and set living room's air conditioner to high mode.\n\nServices: {'Camera': 'Functions : [\\n    on(),\\n\\toff(),\\n    take() : return binary : storage path for image(photo),\\n    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    image : binary : the storage path for the most recent image(photo)\\n]\\nTags : [\\n    livingroom,\\n    balcony,\\n    bedroom\\n]', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#AirQualityDetector).temperature > 30.0 and (#Camera).switch != \"on\") {\n        (#balcony #Camera).on()\n        if ((#livingroom #AirConditioner).airConditionerMode != \"high\") {\n            (#livingroom #AirConditioner).setAirConditionerMode(\"high\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Close the main door and back door if it is open at 11:05 PM every day.\n\nServices: {'DoorLock': 'Functions : []\\nValues : [\\n    door : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"unknown\"}\\n]\\nTags : [\\n    entrance,\\n    maindoor,\\n    backdoor\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 SEC){\n    if((#Clock).hour == 23 and (#Clock).minute == 5 and (#Clock).second == 0){\n        if((#maindoor #DoorLock).door != \"closed\"){\n            (#maindoor #DoorLock).close()\n        }\n        if((#backdoor #DoorLock).door != \"closed\"){\n            (#backdoor #DoorLock).close()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Close the bathroom's shade completely.\n\nServices: {'Shade': 'Functions : [\\n\\topen(),\\n\\tclose(),\\n    setShadeLevel(openPercent: int[0 ~ 100])\\n]\\nValues : [\\n    shadeLevel : int openPercent[0 ~ 100]\\n]\\nTags : [\\n    myroom,\\n    bathroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#bathroom #Shade).shadeLevel > 0) {\n    (#bathroom #Shade).setShadeLevel(0)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the irrigation system in the yard if the gas meter exceeds 50 units at 6:00 PM.\n\nServices: {'Irrigator': 'Functions : [\\n    on(),\\n    off(),\\n    startWatering(),\\n    setWaterPortion(portion: double [0 ~ 2000], unit: string {\"liters\"|\"milliliters\"|\"gallons\"|\"ounces\"})\\n]\\nValues :\\t[\\n    switch: string {\"on\"|\"off\"}\\n]\\nTags : [\\n    balcony,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 18 and (#Clock).minute == 0) {\n        if ((#GasMeter).gasMeter > 50) {\n            if ((#yard #Irrigator).switch != \"off\") {\n                (#yard #Irrigator).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the bedroom and livingroom light and set it to yellow if smoke is detected.\n\nServices: {'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    garage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#SmokeDetector).smoke == \"detected\") {\n        if ((#bedroom #Light).switch != \"on\") {\n            (#bedroom #Light).on()\n        }\n        (#bedroom #Light).setColor(\"60|100|100\")\n        if ((#livingroom #Light).switch != \"on\") {\n            (#livingroom #Light).on()\n        }\n        (#livingroom #Light).setColor(\"60|100|100\")\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Measure the concentration of fine dust (PM 10) right now and notify it through the living room's speaker.\n\nServices: {'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#livingroom #Speaker).switch != \"on\") {\n    (#livingroom #Speaker).on()\n}\n(#livingroom #Speaker).speak(\"현재 미세먼지 농도는 \" + (#AirQualityDetector).dustLevel)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Please turn on the humidifier in my room every 8 o'clock every day.\n\nServices: {'Humidifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setHumidiferMode(mode: string {\"auto\"|\"low\"|\"medium\"|\"high\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    humidifierMode : string {\"auto\"|\"low\"|\"medium\"|\"high\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop (1 MIN, (#Clock).hour == 8 and (#Clock).minute == 0) {\n    if ((#myroom #Humidifier).switch != \"on\") {\n        (#myroom #Humidifier).on()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the air purifier in the kitchen at 9:30 PM if the VOC level is below 0.01.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]', 'AirPurifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\\n]\\nTags : [\\n    kitchen,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 21 and (#Clock).minute == 30) {\n        if ((#AirQualityDetector).tvocLevel < 0.01) {\n            if ((#kitchen #AirPurifier).switch != \"off\") {\n                (#kitchen #AirPurifier).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set the robot vacuum cleaner in the warehouse to automatic mode.\n\nServices: {'RobotCleaner': 'Functions : [\\n    on(),\\n    off(),\\n    setRobotCleanerCleaningMode(string mode{\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"})\\n]\\nValues : [\\n    switch : string {\"on\"|\"off\"},\\n    robotCleanerCleaningMode : string {\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"}\\n\\n]\\nTags : [\\n    livingroom,\\n    storage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#storage #RobotCleaner).robotCleanerCleaningMode != \"auto\") {\n\t(#storage #RobotCleaner).setRobotCleanerCleaningMode(\"auto\")\n}\nif ((#livingroom #RobotCleaner).switch != \"on\") {\n    (#livingroom #RobotCleaner).on()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the utility room dehumidifier at 12:00 AM.\n\nServices: {'Dehumidifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\\n]\\nTags : [\\n    utilityroom,\\n    storage,\\n    laundryroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 0 and (#Clock).minute == 0) {\n        if ((#utilityroom #Dehumidifier).switch != \"off\") {\n            (#utilityroom #Dehumidifier).off()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Please open the window in balcony and bathroom in 1 hour, 40 minutes and 15 seconds.\n\nServices: {'Window': 'Functions : [\\n    open(),\\n    close()\\n]\\nValues : [\\n    window : string {\"closed\"|\"open\"}\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (1 HOUR)\nwait until (40 MIN)\nwait until (15 SEC)\nif ((#balcony #Window).window != \"open\") {\n    (#balcony #Window).open()\n}\nif ((#bathroom #Window).window != \"open\") {\n    (#bathroom #Window).open()\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the dishwasher in the kitchen if sound is detected.\n\nServices: {'Dishwasher': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDishwasherMode(mode: string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dishwasherMode : string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"}\\n]\\nTags : [\\n    kitchen\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#SoundSensor).sound == \"detected\") {\n        if ((#kitchen #Dishwasher).switch != \"on\") {\n            (#kitchen #Dishwasher).on()\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set the dehumidifier in the storage to cooling mode at 9:00 AM if the temperature is above 28°C.\n\nServices: {'Dehumidifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\\n]\\nTags : [\\n    utilityroom,\\n    storage,\\n    laundryroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 9 and (#Clock).minute == 0) {\n        if ((#AirQualityDetector).temperature > 28.0) {\n            if ((#storage #Dehumidifier).switch != \"on\") {\n                (#storage #Dehumidifier).on()\n            }\n            if ((#storage #Dehumidifier).dehumidifierMode != \"cooling\") {\n                (#storage #Dehumidifier).setDehumidifierMode(\"cooling\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: If the bedroom blinds are at 50%, set them to 80%.\n\nServices: {'Blind': 'Functions : [\\n    setBlindLevel(level: int [0 ~ 100])\\n]\\nValues : [\\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\\n    blindLevel : int [0 ~ 100]\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#bedroom #Blind).blindLevel == 50) {\n    (#bedroom #Blind).setBlindLevel(80)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: If the fine dust concentration is lower than 50 every hour, close the kitchen gas valve.\n\nServices: {'GasValve': 'Functions : [\\n\\topen(),\\n\\tclose()\\n]\\nValues : [\\n    valve : string {\"open\"|\"closed\"}\\n]\\nTags : [\\n    kitchen\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop (1 HOUR) {\n    if ((#AirQualityDetector).dustLevel < 50.0) {\n        (#kitchen #GasValve).close()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the speaker in the yard after 3 hours, 20 minutes, and 10 seconds.\n\nServices: {'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
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
            "value": "Input: It checks the current atmospheric pressure every 6 o'clock, and when it exceeds 1 atm, it announces through the speaker in my room, 'High pressure.'\n\nServices: {'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop (1 MIN, (#Clock).hour == 6 and (#Clock).minute == 0) {\n    if ((#WeatherProvider).pressure > 1) {\n        if ((#myroom #Speaker).switch != \"on\") {\n            (#myroom #Speaker).on()\n        }\n        (#myroom #Speaker).speak(\"고기압입니다\")\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Close the shade after 1 hour, 2 minutes and 5 seconds in the bathroom.\n\nServices: {'Shade': 'Functions : [\\n\\topen(),\\n\\tclose(),\\n    setShadeLevel(openPercent: int[0 ~ 100])\\n]\\nValues : [\\n    shadeLevel : int openPercent[0 ~ 100]\\n]\\nTags : [\\n    myroom,\\n    bathroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "wait until (1 HOUR)\nwait until (2 MIN)\nwait until (5 SEC)\nif ((#bathroom #Shade).shadeLevel > 0) {\n    (#bathroom #Shade).setShadeLevel(0)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: If CO2 level is above 1000 ppm and temperature exceeds 28°C in the office, set the blinds to 50%. If PM 1.0 level exceeds 50 in the office, set the blinds to 30%.\n\nServices: {'AirQualityDetector': 'Functions : []\\nValues : [\\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\\n    carbonDioxide : double : CO2 level,\\n    temperature : int [-460 ~ 10000],\\n    humidity : double [0 ~ 100],\\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Blind': 'Functions : [\\n    setBlindLevel(level: int [0 ~ 100])\\n]\\nValues : [\\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\\n    blindLevel : int [0 ~ 100]\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#office #AirQualityDetector).carbonDioxide > 1000.0 and (#office #AirQualityDetector).temperature > 28.0) {\n        if ((#office #Blind).blindLevel != 50) {\n            (#office #Blind).setBlindLevel(50)\n        }\n    }\n    if ((#office #AirQualityDetector).veryFineDustLevel > 50.0) {\n        if ((#office #Blind).blindLevel != 30) {\n            (#office #Blind).setBlindLevel(30)\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set the robot cleaner to map mode in the livingroom at 9:00 AM and turn on the lights if it is foggy in the livingroom.\n\nServices: {'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    garage\\n]', 'RobotCleaner': 'Functions : [\\n    on(),\\n    off(),\\n    setRobotCleanerCleaningMode(string mode{\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"})\\n]\\nValues : [\\n    switch : string {\"on\"|\"off\"},\\n    robotCleanerCleaningMode : string {\"auto\"|\"part\"|\"repeat\"|\"manual\"|\"stop\"|\"map\"}\\n\\n]\\nTags : [\\n    livingroom,\\n    storage\\n]', 'WeatherProvider': 'Functions : [\\n    getWeatherInfo(double latitude, double longitude): return string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"}\\n]\\nValues : [\\n    weather : string {\"thunderstorm\"|\"drizzle\"|\"rain\"|\"snow\"|\"mist\"|\"smoke\"|\"haze\"|\"dust\"|\"fog\"|\"sand\"|\"ash\"|\"squall\"|\"tornado\"|\"clear\"|\"clouds\"},\\n\\ttemperature : int celcius,\\n\\thumidity : double,\\n\\tpressure : double\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 9 and (#Clock).minute == 0) {\n        if ((#livingroom #RobotCleaner).robotCleanerCleaningMode != \"map\") {\n            (#livingroom #RobotCleaner).setRobotCleanerCleaningMode(\"map\")\n        }\n        if ((#livingroom #RobotCleaner).switch != \"on\") {\n            (#livingroom #RobotCleaner).on()\n        }\n        if ((#livingroom #WeatherProvider).weatherCondition == \"fog\") {\n            if ((#livingroom #Light).switch != \"on\") {\n                (#livingroom #Light).on()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set the dishwasher to quick mode in the kitchen at 8:00 AM.\n\nServices: {'Dishwasher': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDishwasherMode(mode: string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dishwasherMode : string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"}\\n]\\nTags : [\\n    kitchen\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 8 and (#Clock).minute == 0) {\n        if ((#kitchen #Dishwasher).switch != \"on\") {\n            (#kitchen #Dishwasher).on()\n        }\n        if ((#kitchen #Dishwasher).dishwasherMode != \"quick\") {\n            (#kitchen #Dishwasher).setDishwasherMode(\"quick\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: If the door is open in the entrance now, wait until the door opens and then turn on the air conditioner in the livingroom.\n\nServices: {'DoorLock': 'Functions : []\\nValues : [\\n    door : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"unknown\"}\\n]\\nTags : [\\n    entrance,\\n    maindoor,\\n    backdoor\\n]', 'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#entrance #DoorLock).door == \"opening\") {\n\twait until((#entrance #DoorLock).door == \"open\")\n    if ((#livingroom #AirConditioner).switch != \"on\") {\n        (#livingroom #AirConditioner).on()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Every 5 minutes, if the ultrafine dust concentration based on the current PM 1.0 standard is higher than 50 in the bedroom, sound the siren in the living room.\n\nServices: {'AirQualityDetector': 'Functions : []\\nValues : [\\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\\n    carbonDioxide : double : CO2 level,\\n    temperature : int [-460 ~ 10000],\\n    humidity : double [0 ~ 100],\\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Siren': 'Functions : [\\n    on(),\\n\\toff(),\\n    setSirenMode(mode: string {\"both\"|\"off\"|\"siren\"|\"strobe\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    sirenMode : string {\"both\"|\"off\"|\"siren\"|\"strobe\"}\\n]\\nTags : [\\n    livingroom,\\n    entrance,\\n    garage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop (5 MIN) {\n    if ((#bedroom #AirQualityDetector).veryFineDustLevel > 50.0) {\n        if ((#livingroom #Siren).switch != \"on\") {\n            (#livingroom #Siren).on()\n        }\n        (#livingroom #Siren).setSirenMode(\"both\")\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the TV in the livingroom if no presence is detected at 11:00 PM.\n\nServices: {'PresenceSensor': 'Functions : []\\nValues : [\\n    presence : string {\"present\"|\"not_present\"}\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage\\n]', 'Television': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetTvChannel(tvChannel: int),\\n\\tchannelUp(),\\n\\tchannelDown(),\\n    setVolume(volume: int [0 ~ 100]),\\n    volumeUp(),\\n    volumeDown(),\\n\\tmute() : void, toggle muteStatus\\n\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"}\\n\\tmuteStatus : string {\"muted\"|\"unmuted\"}\\n\\ttvChannel : int\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    bedroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 23 and (#Clock).minute == 0) {\n        if ((#livingroom #PresenceSensor).presence == \"not_present\") {\n            if ((#livingroom #Television).switch != \"off\") {\n                (#livingroom #Television).off()\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: If your dryer in the laundry room is currently in AI drying mode, play the song “music.mp3” through the speakers in the livingroom.\n\nServices: {'Dehumidifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\\n]\\nTags : [\\n    utilityroom,\\n    storage,\\n    laundryroom\\n]', 'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#laundryroom #Dehumidifier).dehumidifierMode == \"AIDrying\") {\n    if ((#livingroom #Speaker).switch != \"on\") {\n        (#livingroom #Speaker).on()\n    }\n    (#livingroom #Speaker).play(\"music.mp3\")\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: If the air purifier in the livingroom is not currently in quiet mode, say \"noisy\" through the speaker in my room.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]', 'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'AirPurifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\\n]\\nTags : [\\n    kitchen,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#livingroom #AirPurifier).airPurifierFanMode != \"quiet\") {\n    if ((#myroom #Speaker).switch != \"on\") {\n\t    (#myroom #Speaker).on()\n    }\n    (#myroom #Speaker).speak(\"시끄럽다\")\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Divide 20 by 4 and say the result through the living room speaker.\n\nServices: {'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "result = (#Calculator).div(20, 4)\nif ((#livingroom #Speaker).switch != \"on\") {\n    (#livingroom #Speaker).on()\n}\n(#livingroom #Speaker).speak(\"20을 4로 나눈 결과는 \" + result)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the camera in the livingroom and set the air purifier in the livingroom to quiet mode if humidity exceeds 60%.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]', 'AirQualityDetector': 'Functions : []\\nValues : [\\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\\n    carbonDioxide : double : CO2 level,\\n    temperature : int [-460 ~ 10000],\\n    humidity : double [0 ~ 100],\\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Camera': 'Functions : [\\n    on(),\\n\\toff(),\\n    take() : return binary : storage path for image(photo),\\n    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    image : binary : the storage path for the most recent image(photo)\\n]\\nTags : [\\n    livingroom,\\n    balcony,\\n    bedroom\\n]', 'AirPurifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\\n]\\nTags : [\\n    kitchen,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#livingroom #AirQualityDetector).humidity > 60.0) {\n        if ((#livingroom #Camera).switch != \"on\") {\n            (#livingroom #Camera).on()\n        }\n        if ((#livingroom #AirPurifier).airPurifierFanMode != \"quiet\") {\n            (#livingroom #AirPurifier).setPurifierFanMode(\"quiet\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Every 15 minutes, turn on the dishwasher in the kitchen if it is off and set it to automatic mode.\n\nServices: {'Dishwasher': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDishwasherMode(mode: string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dishwasherMode : string {\"eco\"|\"intense\"|\"auto\"|\"quick\"|\"rinse\"|\"dry\"}\\n]\\nTags : [\\n    kitchen\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop (15 MIN) {\n    if ((#kitchen #Dishwasher).switch != \"on\") {\n        (#kitchen #Dishwasher).on()\n    }\n    if ((#kitchen #Dishwasher).dishwasherMode != \"auto\") {\n        (#kitchen #Dishwasher).setDishwasherMode(\"auto\")\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Every 8 o'clock, the sound detection status is announced through the speaker in the livingroom.\n\nServices: {'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop (1 MIN, (#Clock).hour == 8 and (#Clock).minute == 0) {\n    if ((#livingroom #Speaker).switch != \"on\") {\n        (#livingroom #Speaker).on()\n    }\n    if ((#SoundSensor).sound == \"detected\") {\n        (#livingroom #Speaker).speak(현재 소리가 감지됩니다.)\n    }\n    if ((#SoundSensor).sound == \"not_detected\") {\n        (#livingroom #Speaker).speak(현재 소리가 감지되지 않았습니다.)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn off the TV in the bedroom at every midnight.\n\nServices: {'Television': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetTvChannel(tvChannel: int),\\n\\tchannelUp(),\\n\\tchannelDown(),\\n    setVolume(volume: int [0 ~ 100]),\\n    volumeUp(),\\n    volumeDown(),\\n\\tmute() : void, toggle muteStatus\\n\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"}\\n\\tmuteStatus : string {\"muted\"|\"unmuted\"}\\n\\ttvChannel : int\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    bedroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN, (#Clock).hour == 0 and (#Clock).minute == 0) {\n    if ((#bedroom #Television).switch != \"off\") {\n        (#bedroom #Television).off()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Speak \"Happy Birthday\" through the speaker in my room and yard at 8:00 AM on July 20th.\n\nServices: {'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).month == 7 and (#Clock).day == 20 and (#Clock).hour == 8 and (#Clock).minute == 0) {\n        if ((#myroom #Speaker).switch != \"on\") {\n            (#myroom #Speaker).on()\n        }\n        (#myroom #Speaker).speak(\"Happy Birthday\")\n        if ((#yard #Speaker).switch != \"on\") {\n            (#yard #Speaker).on()\n        }\n        (#yard #Speaker).speak(\"Happy Birthday\")\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the air purifier in the bedroom if fine dust level is above 50.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]', 'AirQualityDetector': 'Functions : []\\nValues : [\\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\\n    carbonDioxide : double : CO2 level,\\n    temperature : int [-460 ~ 10000],\\n    humidity : double [0 ~ 100],\\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'AirPurifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setAirPurifierFanMode(mode: string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airPurifierFanMode : string {\"auto\"|\"sleep\"|\"low\"|\"medium\"|\"high\"|\"quiet\"|\"windFree\"|\"off\"}\\n]\\nTags : [\\n    kitchen,\\n    livingroom,\\n    bedroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#bedroom #AirQualityDetector).fineDustLevel > 50.0) {\n    if ((#bedroom #AirPurifier).switch != \"on\"){\n        (#bedroom #AirPurifier).on()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Please tell me the current illuminance value through the speaker in the livingroom.\n\nServices: {'LightSensor': 'Functions : []\\nValues : [\\n    light : double\\n]', 'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#livingroom #Speaker).switch != \"on\") {\n    (#livingroom #Speaker).on()\n}\n(#livingroom #Speaker).speak(\"현재 조도 값은 \" + (#livingroom #LightSensor).light)"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set the siren to both mode in the garage at 8:00 PM every Tuesday.\n\nServices: {'Siren': 'Functions : [\\n    on(),\\n\\toff(),\\n    setSirenMode(mode: string {\"both\"|\"off\"|\"siren\"|\"strobe\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    sirenMode : string {\"both\"|\"off\"|\"siren\"|\"strobe\"}\\n]\\nTags : [\\n    livingroom,\\n    entrance,\\n    garage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 20 and (#Clock).minute == 0 and (#Clock).weekday == \"tuesday\") {\n        if ((#garage #Siren).switch != \"on\") {\n            (#garage #Siren).on()\n        }\n        if ((#garage #Siren).sirenMode != \"both\") {\n            (#garage #Siren).setSirenMode(\"both\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Output the current smoke detection status to the speaker in the livingroom now.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]', 'Speaker': 'Functions : [\\n    on(),\\n\\toff(),\\n    pause(),\\n    stop(),\\n    play(source: string),\\n    speak(text: string)\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    playbackStatus : string {\"paused\"|\"playing\"|\"stopped\"|\"fast\"|\"rewinding\"|\"buffering\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom,\\n    yard\\n]', 'SmokeDetector': 'Functions : []\\nValues : [\\n    smoke : string {\"detected\"|\"not_detected\"} \\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    bedroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    kitchen\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#livingroom #Speaker).switch != \"on\") {\n\t(#livingroom #Speaker).on()\n}\nif ((#livingroom #SmokeDetector).smoke == \"detected\") {\n    (#livingroom #Speaker).speak(현재 연기가 감지되었습니다. 확인해주세요.)\n}\nif ((#livingroom #SmokeDetector).smoke == \"not_detected\") {\n    (#livingroom #Speaker).speak(현재 연기가 감지되지 않았습니다.)\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set the light brightness to 75% in the balcony if it is below 50% at 4:00 PM.\n\nServices: {'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    garage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 16 and (#Clock).minute == 0) {\n        if ((#balcony #Light).light < 50) {\n            if ((#balcony #Light).switch != \"on\") {\n                (#balcony #Light).on()\n            }\n            (#balcony #Light).setLevel(75)\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the pump in the garden and set the light to 50% in the garden at 6:00 AM.\n\nServices: {'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    garage\\n]', 'Pump': 'Functions : [\\n    on(),\\n\\toff(),\\n    setOperationMode(string mode {\"normal\"|\"minimum\"|\"maximum\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    operationMode : string {\"normal\"|\"minimum\"|\"maximum\"}\\n]\\nTags : [\\n    balcony,\\n    garden\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 6 and (#Clock).minute == 0) {\n        if ((#garden #Pump).switch != \"on\") {\n            (#garden #Pump).on()\n        }\n        if ((#garden #Light).switch != \"on\") {\n            (#garden #Light).on()\n        }\n        (#garden #Light).setLevel(50)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set the air conditioner to heat mode in the livingroom if the weather is 'drizzle' and the temperature is below 10°C at 9:22 PM.\n\nServices: {'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 21 and (#Clock).minute == 22) {\n        if ((#WeatherProvider).weather == 'drizzle' and (#WeatherProvider).temperature < 10) {\n            if ((#livingroom #AirConditioner).airConditionerMode != \"heat\") {\n                (#livingroom #AirConditioner).setAirConditionerMode(\"heat\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Now, if the contact sensor is closed, turn off the light bulb in the kitchen.\n\nServices: {'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    garage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#ContactSensor).contact == \"closed\") {\n    if ((#kitchen #Light).switch != \"off\") {\n\t    (#kitchen #Light).off()\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: If PM 10 level is above 100 and temperature exceeds 25°C in the office, set the blinds in the office to 40%. If CO2 level is above 600 ppm in the office, set the blinds in the office to 0%.\n\nServices: {'AirQualityDetector': 'Functions : []\\nValues : [\\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\\n    carbonDioxide : double : CO2 level,\\n    temperature : int [-460 ~ 10000],\\n    humidity : double [0 ~ 100],\\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Blind': 'Functions : [\\n    setBlindLevel(level: int [0 ~ 100])\\n]\\nValues : [\\n    blind : string {\"closed\"|\"closing\"|\"open\"|\"opening\"|\"partially\"|\"paused\"|\"unknown\"},\\n    blindLevel : int [0 ~ 100]\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#office #AirQualityDetector).dustLevel > 100.0 and (#office #AirQualityDetector).temperature > 25.0) {\n        if ((#office #Blind).blindLevel != 40) {\n            (#office #Blind).setBlindLevel(40)\n        }\n    }\n    if ((#office #AirQualityDetector).carbonDioxide > 600.0) {\n        if ((#office #Blind).blindLevel != 0) {\n            (#office #Blind).setBlindLevel(0)\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the air conditioner in heat mode in the bedroom if the temperature is below 8°C at 6:08 AM.\n\nServices: {'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 6 and (#Clock).minute == 8) {\n        if ((#WeatherProvider).temperature < 8) {\n            if ((#bedroom #AirConditioner).airConditionerMode != \"heat\") {\n                (#bedroom #AirConditioner).setAirConditionerMode(\"heat\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: If the weather is currently clear, turn on the air conditioner in the livingroom.\n\nServices: {'AirConditioner': 'Functions : [\\n    on(),\\n\\toff(),\\n    setTemperature(temperature: int),\\n    setAirConditionerMode(mode: string {\"auto\"|\"cool\"|\"heat\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    airConditionerMode : string {\"auto\"|\"cool\"|\"heat\"}\\n]\\nTags : [\\n    myroom,\\n    livingroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#WeatherProvider).weather == \"clear\") {\n\tif ((#livingroom #AirConditioner).switch != \"on\") {\n\t\t(#livingroom #AirConditioner).on()\n\t}\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set the dehumidifier to weightSensing mode in the utility room at 7:00 AM if the VOC level is below 0.03.\n\nServices: {'AirQualityDetector': 'Functions : []\\nValues : [\\n    dustLevel : int [0 ~ ∞] : PM 10 dust level,\\n    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,\\n    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,\\n    carbonDioxide : double : CO2 level,\\n    temperature : int [-460 ~ 10000],\\n    humidity : double [0 ~ 100],\\n    tvocLevel : double [0 ~ 1000000] : inert gas concentration\\n]\\nTags : [\\n    bedroom,\\n    livingroom,\\n    office\\n]', 'Dehumidifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\\n]\\nTags : [\\n    utilityroom,\\n    storage,\\n    laundryroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 7 and (#Clock).minute == 0) {\n        if ((#utilityroom #AirQualityDetector).tvocLevel < 0.03) {\n            if ((#utilityroom #Dehumidifier).switch != \"on\") {\n                (#utilityroom #Dehumidifier).on()\n            }\n            if ((#utilityroom #Dehumidifier).dehumidifierMode != \"weightSensing\") {\n                (#utilityroom #Dehumidifier).setDehumidifierMode(\"weightSensing\")\n            }\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: If the contact sensor in the garage is open, turn on the light and set the brightness to 70% in the garage.\n\nServices: {'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    garage\\n]', 'ContactSensor': 'Functions : []\\nValues : [\\n    contact : string {\"open\"|\"closed\"}\\n]\\nTags : [\\n    entrance,\\n    maindoor,\\n    backdoor,\\n    garage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#garage #ContactSensor).contact == \"open\") {\n        if ((#garage #Light).switch != \"on\") {\n            (#garage #Light).on()\n        }\n        (#garage #Light).setBrightness(70)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Turn on the dehumidifier in the laundryroom and set it to thawingFrozenInside mode at 8:00 PM.\n\nServices: {'Dehumidifier': 'Functions : [\\n    on(),\\n\\toff(),\\n    setDehumidifierMode(mode: string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"})\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n    dehumidifierMode : string {\"cooling\"|\"delayWash\"|\"drying\"|\"finished\"|\"refreshing\"|\"weightSensing\"|\"wrinklePrevent\"|\"dehumidifying\"|\"AIDrying\"|\"sanitizing\"|\"internalCare\"|\"freezeProtection\"|\"continuousDehumidifying\"|\"thawingFrozenInside\"}\\n]\\nTags : [\\n    utilityroom,\\n    storage,\\n    laundryroom\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 20 and (#Clock).minute == 0) {\n        if ((#laundryroom #Dehumidifier).switch != \"on\") {\n            (#laundryroom #Dehumidifier).on()\n        }\n        if ((#laundryroom #Dehumidifier).dehumidifierMode != \"thawingFrozenInside\") {\n            (#laundryroom #Dehumidifier).setDehumidifierMode(\"thawingFrozenInside\")\n        }\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Set the my room's fan speed to 2 at 3:15 AM.\n\nServices: {'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]', 'Fan': 'Functions : [\\n    on(),\\n\\toff(),\\n    setFanSpeed(speed: int [0 ~ ∞])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\n]\\nTags : [\\n    myroom,\\n    livingroom\\n]'}"
        },
        {
            "from": "gpt",
            "value": "loop(1 MIN) {\n    if ((#Clock).hour == 3 and (#Clock).minute == 15) {\n        (#myroom #Fan).setFanSpeed(2)\n    }\n}"
        }
    ],
    [
        {
            "from": "human",
            "value": "Input: Please turn on the light in the kitchen.\n\nServices: {'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n    utilityroom,\\n    storage,\\n    garage\\n]', 'Clock': 'Functions : []\\nValues : [\\n    day : int [1~31]\\n    hour : int [0~23]\\n    minute : int [0~59]\\n    month : int [1~12]\\n    second : int [0~59]\\n    weekday : string {\"monday\"|\"tuesday\"|\"wednesday\"|\"thursday\"|\"friday\"|\"saturday\"|\"sunday\"}\\n    year : int [0 ~ 100000]\\n    isHoliday : bool {true|false}\\n    timestamp : double : unixTime\\n]'}"
        },
        {
            "from": "gpt",
            "value": "if ((#kitchen #Light).switch != \"on\") {\n\t(#kitchen #Light).on()\n}"
        }
    ]
]