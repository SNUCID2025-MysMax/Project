data_location_dh = [
[
    {
        "from": "human",
        "value": """Input: Turn on the living room light at 7 o'clock every morning

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'Light': 'Functions : [
    on(),
    off(),
    setColor(color: string {\"{hue}|{saturation}|{brightness}\"})
    setLevel(level int [0 ~ 100])
]
Values : [
    switch : string {\"on\"|\"off\"},
    light : double
]
Tags : [
    myroom,
    balcony,
    entrance,
    bedroom,
    bathroom,
    livingroom
]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN, (#Clock).hour == 7 and (#Clock).minute == 0) {
    if (any(#Light #livingroom).switch != "on"){
      all(#Light #livingroom).on()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the light in my room for 30 minutes every day at 6pm

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN, (#Clock).hour == 18 and (#Clock).minute == 0) {
    if (any(#Light #myroom).switch != "on"){
    all(#Light #myroom).on()
    }
    wait until (30 MIN)
    if (any(#Light #myroom).switch != "off"){
    all(#Light #myroom).off()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn off all lights from 6 PM to 8 AM every day.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN, (#Clock).hour >= 18 or (#Clock).hour < 8) {
    if (any(#Light).switch != "off"){
    all(#Light).off()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the light at 7 o'clock every morning

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN, (#Clock).hour == 7 and (#Clock).minute == 0) {
    if ((#Light).switch != "on"){
    (#Light).on()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the light for 30 minutes every day at 6pm

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN, (#Clock).hour == 18 and (#Clock).minute == 0) {
    if ((#Light).switch != "on"){
    (#Light).on()
    }
    wait until (30 MIN)
    if ((#Light).switch != "off"){
    (#Light).off()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on all the lights for 30 minutes every day at 6pm

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN, (#Clock).hour == 18 and (#Clock).minute == 0) {
    if (any(#Light).switch != "on"){
    all(#Light).on()
    }
    wait until (30 MIN)
    if (any(#Light).switch != "off"){
    all(#Light).off()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Turn off the light in balcony from 6 PM to 8 AM every day.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN, (#Clock).hour >= 18 or (#Clock).hour < 8) {
    if (any(#Light #balcony).switch != "off"){
    all(#Light #balcony).off()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn off the light from 6 PM to 8 AM every day.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"""
    },
    {
        "from": "human",
        "value": """Input: Turn on the one light in the living room at 7 o'clock every morning

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN, (#Clock).hour == 7 and (#Clock).minute == 0) {
    if ((#Light #livingroom).switch != "on"){
      (#Light #livingroom).on()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the one light in my room for 30 minutes every day at 6pm

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN, (#Clock).hour == 18 and (#Clock).minute == 0) {
    if ((#Light #myroom).switch != "on"){
    (#Light #myroom).on()
    }
    wait until (30 MIN)
    if ((#Light #myroom).switch != "off"){
    (#Light #myroom).off()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn off one entrance light in from 6 PM to 8 AM every day.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',  'Light': 'Functions : [\\n    on(),\\n\\toff(),\\n\\tsetColor(color: string {\"{hue}|{saturation}|{brightness}\"})\\n\\tsetLevel(level int [0 ~ 100])\\n]\\nValues : [\\n\\tswitch : string {\"on\"|\"off\"},\\n\\tlight : double\\n]\\nTags : [\\n    myroom,\\n    balcony,\\n    entrance,\\n    bedroom,\\n    bathroom,\\n    livingroom,\\n]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN, (#Clock).hour >= 18 or (#Clock).hour < 8) {
    if ((#Light #entrance).switch != "off"){
    (#Light #entrance).off()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the garden irrigator and start watering with 120 ml at 6:00 AM on weekdays.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Irrigator': 'Functions : [
    on(),
    off(),
    startWatering(),
    setWaterPortion(portion: double [0 ~ 2000], unit: string {"liters"|"milliliters"|"gallons"|"ounces"})
]
Values : [
    switch: string {"on"|"off"}
]
Tags:[Garden,Greenhouse]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).weekday == "monday" or (#Clock).weekday == "tuesday" or (#Clock).weekday == "wednesday" or (#Clock).weekday == "thursday" or (#Clock).weekday == "friday") {
        if ((#Clock).hour == 6 and (#Clock).minute == 0) {
            if (any(#Irrigator #Garden).switch != "on") {
                all(#Irrigator #Garden).on()
            }
            all(#Irrigator #Garden).setWaterPortion(120.0, "mililiters")
            all(#Irrigator #Garden).startWatering()
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on one backyard irrigator and start watering with 120 ml at 6:00 AM on weekdays.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Irrigator': 'Functions : [
    on(),
    off(),
    startWatering(),
    setWaterPortion(portion: double [0 ~ 2000], unit: string {"liters"|"milliliters"|"gallons"|"ounces"})
]
Values : [
    switch: string {"on"|"off"}
]
Tags:[Backyard,Patio]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).weekday == "monday" or (#Clock).weekday == "tuesday" or (#Clock).weekday == "wednesday" or (#Clock).weekday == "thursday" or (#Clock).weekday == "friday") {
        if ((#Clock).hour == 6 and (#Clock).minute == 0) {
            if ((#Irrigator #Backyard).switch != "on") {
                (#Irrigator #Backyard).on()
            }
            (#Irrigator #Backyard).setWaterPortion(120.0, "mililiters")
            (#Irrigator #Backyard).startWatering()
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on all the irrigators and start watering with 120 ml at 6:00 AM on weekdays.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Irrigator': 'Functions : [
    on(),
    off(),
    startWatering(),
    setWaterPortion(portion: double [0 ~ 2000], unit: string {"liters"|"milliliters"|"gallons"|"ounces"})
]
Values : [
    switch: string {"on"|"off"}
]
Tags:[Rooftop,UrbanGarden]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).weekday == "monday" or (#Clock).weekday == "tuesday" or (#Clock).weekday == "wednesday" or (#Clock).weekday == "thursday" or (#Clock).weekday == "friday") {
        if ((#Clock).hour == 6 and (#Clock).minute == 0) {
            if (any(#Irrigator).switch != "on") {
                all(#Irrigator).on()
            }
            all(#Irrigator).setWaterPortion(120.0, "mililiters")
            all(#Irrigator).startWatering()
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If the humidity in the bedroom is above 50%, turn on the air conditioner in the living room.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[LivingRoom,Bedroom]', 'HumiditySensor': 'Functions : []
Values : [
    humidity : double[0 ~ 100]
]
Tags:[Bedroom,Bathroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(10 SEC){
    if((#HumiditySensor #Bedroom).humidity >= 50.0){
        if(any(#AirConditioner #LivingRoom).switch != "on"){
            all(#AirConditioner #LivingRoom).on()
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If the humidity in the office is above 50%, turn on one air conditioner in the conference room.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[], 'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[ConferenceRoom,LivingRoom]', 'HumiditySensor': 'Functions : []
Values : [
    humidity : double[0 ~ 100]
]
Tags:[Office,Bathroom]'}"""
    }
],
[
    {
        "from": "gpt",
        "value": """loop(10 SEC){
    if((#HumiditySensor #Office).humidity >= 50.0){
        if((#AirConditioner #ConferenceRoom).switch != "on"){
            (#AirConditioner).on()
        }
    }
}"""
    },
    {
        "from": "human",
        "value": """Input: If the humidity in the greenhouse is above 50%, turn on all the air conditioner in the control room.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[], 'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[ControlRoom,Office]', 'HumiditySensor': 'Functions : []
Values : [
    humidity : double[0 ~ 100]
]
Tags:[Greenhouse,LivingRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(10 SEC){
    if((#HumiditySensor #Greenhouse).humidity >= 50.0){
        if(any(#AirConditioner #ControlRoom).switch != "on"){
            all(#AirConditioner #ControlRoom).on()
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Set the kitchen refrigerator to RapidCool mode at 2:00 PM.

Services: {
'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []',
'Refrigerator': 'Functions : [
    on(),
    off(),
    setRefrigeratorMode(string mode{"RapidCool"|"RapidFreeze"})
]
Values : [
    switch : string {"on"|"off"},
    refrigeratorMode : string {"RapidCool"|"RapidFreeze"}
]
Tags: [Kitchen, Garage]'
}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 14 and (#Clock).minute == 0) {
        if (any(#Refrigerator #Kitchen).refrigeratorMode != "RapidCool") {
            all(#Refrigerator #Kitchen).setRefrigeratorMode("RapidCool")
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Set one basement refrigerator to RapidCool mode at 2:00 PM.

Services: {
'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []',
'Refrigerator': 'Functions : [
    on(),
    off(),
    setRefrigeratorMode(string mode{"RapidCool"|"RapidFreeze"})
]
Values : [
    switch : string {"on"|"off"},
    refrigeratorMode : string {"RapidCool"|"RapidFreeze"}
]
Tags: [Basement, Pantry]'
}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 14 and (#Clock).minute == 0) {
        if ((#Refrigerator #Basement).refrigeratorMode != "RapidCool") {
            (#Refrigerator #Basement).setRefrigeratorMode("RapidCool")
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on any garden irrigation system and start watering with 170 ml at 1:00 PM if the backyard gas valve is open.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'GasValve': 'Functions : [
    open(),
    close()
]
Values : [
    valve : string {"open"|"closed"}
]
Tags:[Backyard,Garage]', 'Irrigator': 'Functions : [
    on(),
    off(),
    startWatering(),
    setWaterPortion(portion: double [0 ~ 2000], unit: string {"liters"|"milliliters"|"gallons"|"ounces"})
]
Values : [
    switch: string {"on"|"off"}
]
Tags:[Garden,Greenhouse]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 13 and (#Clock).minute == 0) {
        if ((#GasValve #Backyard).valve == "open") {
            if ((#Irrigator #Garden).switch != "on") {
                (#Irrigator #Garden).on()
            }
            (#Irrigator #Garden).startWatering(170)
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the lawn irrigation system and start watering with 170 ml at 1:00 PM if the patio gas valve is open.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'GasValve': 'Functions : [
    open(),
    close()
]
Values : [
    valve : string {"open"|"closed"}
]
Tags:[Patio,Basement]', 'Irrigator': 'Functions : [
    on(),
    off(),
    startWatering(),
    setWaterPortion(portion: double [0 ~ 2000], unit: string {"liters"|"milliliters"|"gallons"|"ounces"})
]
Values : [
    switch: string {"on"|"off"}
]
Tags:[Lawn,Orchard]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 13 and (#Clock).minute == 0) {
        if ((#GasValve #Patio).valve == "open") {
            if (any(#Irrigator #Lawn).switch != "on") {
                all(#Irrigator #Lawn).on()
            }
            all(#Irrigator #Lawn).startWatering(170)
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on a flowerbed irrigation system and start watering with 170 ml at 1:00 PM if the terrace gas valve is open.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'GasValve': 'Functions : [
    open(),
    close()
]
Values : [
    valve : string {"open"|"closed"}
]
Tags:[Terrace,Shed]', 'Irrigator': 'Functions : [
    on(),
    off(),
    startWatering(),
    setWaterPortion(portion: double [0 ~ 2000], unit: string {"liters"|"milliliters"|"gallons"|"ounces"})
]
Values : [
    switch: string {"on"|"off"}
]
Tags:[Flowerbed,Farm]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 13 and (#Clock).minute == 0) {
        if ((#GasValve #Terrace).valve == "open") {
            if ((#Irrigator #Flowerbed).switch != "on") {
                (#Irrigator #Flowerbed).on()
            }
            (#Irrigator #Flowerbed).startWatering(170)
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If the front door is currently closed, tell the hallway speaker that the door is closed.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'DoorLock': 'Functions : []
Values : [
    door : string {"closed"|"closing"|"open"|"opening"|"unknown"}
]
Tags:[FrontDoor]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[Hallway]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#DoorLock #FrontDoor).door == "closed") {
    if (all(#Speaker #Hallway).switch == "off") {
        all(#Speaker #Hallway).on()
    }
    all(#Speaker #Hallway).speak("문이 닫혀 있으므로 엽니다.")
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If the front door is currently closed, tell one hallway speaker that the door is closed.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'DoorLock': 'Functions : []
Values : [
    door : string {"closed"|"closing"|"open"|"opening"|"unknown"}
]
Tags:[FrontDoor]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[Hallway]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#DoorLock #FrontDoor).door == "closed") {
    if ((#Speaker #Hallway).switch == "off") {
        (#Speaker #Hallway).on()
    }
    (#Speaker #Hallway).speak("문이 닫혀 있으므로 엽니다.")
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If the front door is currently closed, tell all the hallway speakers that the door is closed.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'DoorLock': 'Functions : []
Values : [
    door : string {"closed"|"closing"|"open"|"opening"|"unknown"}
]
Tags:[FrontDoor]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[Hallway]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#DoorLock #FrontDoor).door == "closed") {
    if ((#Speaker #Hallway).switch == "off") {
        all(#Speaker #Hallway).on()
    }
    all(#Speaker #Hallway).speak("문이 닫혀 있으므로 엽니다.")
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If the main entrance door is currently closed, tell the living room speaker that the door is closed.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'DoorLock': 'Functions : []
Values : [
    door : string {"closed"|"closing"|"open"|"opening"|"unknown"}
]
Tags:[MainEntrance]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[LivingRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#DoorLock #MainEntrance).door == "closed") {
    if (any(#Speaker #LivingRoom).switch != "on") {
        all(#Speaker #LivingRoom).on()
    }
    (#Speaker #LivingRoom).speak("문이 닫혀 있으므로 엽니다.")
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If the main entrance door is currently closed, tell one living room speaker that the door is closed.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'DoorLock': 'Functions : []
Values : [
    door : string {"closed"|"closing"|"open"|"opening"|"unknown"}
]
Tags:[MainEntrance]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[
    LivingRoom
]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#DoorLock #MainEntrance).door == "closed") {
    if ((#Speaker #LivingRoom).switch != "on") {
        (#Speaker #LivingRoom).on()
    }
    (#Speaker #LivingRoom).speak("문이 닫혀 있으므로 엽니다.")
}"""
    }
],
[   {
    "from": "human",
    "value": """Input: If the garage door is currently closed, tell the kitchen speaker that the door is closed.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'DoorLock': 'Functions : []
Values : [
    door : string {"closed"|"closing"|"open"|"opening"|"unknown"}
]
Tags:[Garage]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[Kitchen]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#DoorLock #Garage).door == "closed") {
    if (any(#Speaker #Kitchen).switch != "on") {
        all(#Speaker #Kitchen).on()
    }
    (#Speaker #Kitchen).speak("문이 닫혀 있으므로 엽니다.")
}"""
    }
],
[    {
    "from": "human",
    "value": """Input: If the garage door is currently closed, tell any kitchen speaker that the door is closed.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'DoorLock': 'Functions : []
Values : [
    door : string {"closed"|"closing"|"open"|"opening"|"unknown"}
]
Tags:[Garage]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[Kitchen]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#DoorLock #Garage).door == "closed") {
    if ((#Speaker #Kitchen).switch != "on") {
        (#Speaker #Kitchen).on()
    }
    (#Speaker #Kitchen).speak("문이 닫혀 있으므로 엽니다.")
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the living room camera if smoke in the kitchen is detected.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'SmokeDetector': 'Functions : []
Values : [
    smoke : string {"detected"|"not_detected"}
]
Tags:[Kitchen,Garage]', 'Camera': 'Functions : [
    on(),
    off(),
    take() : return binary : storage path for image(photo),
    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
]
Values : [
    switch : string {"on"|"off"},
    image : binary : the storage path for the most recent image(photo)
]
Tags:[LivingRoom,Basement]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#SmokeDetector #Kitchen).smoke == "detected") {
        if (any(#Camera #LivingRoom).switch != "on") {
            all(#Camera #LivingRoom).on()
        }
    }
}"""
    }
],
[
{
    "from": "human",
    "value": """Input: Turn on all cameras in the living room if smoke in the kitchen is detected.

Services: {'Clock': 'Functions : []
Values : [
day : int [1~31]
hour : int [0~23]
minute : int [0~59]
month : int [1~12]
second : int [0~59]
weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
year : int [0 ~ 100000]
isHoliday : bool {true|false}
timestamp : double : unixTime
]
Tags:[]', 'SmokeDetector': 'Functions : []
Values : [
smoke : string {"detected"|"not_detected"}
]
Tags:[Kitchen,Garage]', 'Camera': 'Functions : [
on(),
off(),
take() : return binary : storage path for image(photo),
takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
]
Values : [
switch : string {"on"|"off"},
image : binary : the storage path for the most recent image(photo)
]
Tags:[LivingRoom,Basement]'}"""
},
{
    "from": "gpt",
    "value": """loop(1 MIN) {
if ((#SmokeDetector #Kitchen).smoke == "detected") {
    if (any(#Camera #LivingRoom).switch != "on") {
        all(#Camera #LivingRoom).on()
    }
}
}"""
}
],
[
{
    "from": "human",
    "value": """Input: Turn on one living room camera if smoke in the kitchen is detected.

Services: {'Clock': 'Functions : []
Values : [
day : int [1~31]
hour : int [0~23]
minute : int [0~59]
month : int [1~12]
second : int [0~59]
weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
year : int [0 ~ 100000]
isHoliday : bool {true|false}
timestamp : double : unixTime
]
Tags:[]', 'SmokeDetector': 'Functions : []
Values : [
smoke : string {"detected"|"not_detected"}
]
Tags:[Kitchen,Garage]', 'Camera': 'Functions : [
on(),
off(),
take() : return binary : storage path for image(photo),
takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
]
Values : [
switch : string {"on"|"off"},
image : binary : the storage path for the most recent image(photo)
]
Tags:[LivingRoom,Basement]'}"""
},
{
    "from": "gpt",
    "value": """loop(1 MIN) {
if ((#SmokeDetector #Kitchen).smoke == "detected") {
    if ((#Camera #LivingRoom).switch != "on") {
        (#Camera #LivingRoom).on()
    }
}
}"""
}
],
[
    {
        "from": "human",
        "value": """Input: Turn on the hallway camera if smoke in the basement is detected.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'SmokeDetector': 'Functions : []
Values : [
    smoke : string {"detected"|"not_detected"}
]
Tags:[Basement,Attic]', 'Camera': 'Functions : [
    on(),
    off(),
    take() : return binary : storage path for image(photo),
    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
]
Values : [
    switch : string {"on"|"off"},
    image : binary : the storage path for the most recent image(photo)
]
Tags:[Hallway,Garage]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#SmokeDetector #Basement).smoke == "detected") {
        if (any(#Camera #Hallway).switch != "on") {
            all(#Camera #Hallway).on()
        }
    }
}"""
    }
],
[
        {
            "from": "human",
            "value": """Input: Turn on one hallway camera if smoke in the basement is detected.

    Services: {'Clock': 'Functions : []
    Values : [
        day : int [1~31]
        hour : int [0~23]
        minute : int [0~59]
        month : int [1~12]
        second : int [0~59]
        weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
        year : int [0 ~ 100000]
        isHoliday : bool {true|false}
        timestamp : double : unixTime
    ]
    Tags:[]', 'SmokeDetector': 'Functions : []
    Values : [
        smoke : string {"detected"|"not_detected"}
    ]
    Tags:[Basement,Attic]', 'Camera': 'Functions : [
        on(),
        off(),
        take() : return binary : storage path for image(photo),
        takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
    ]
    Values : [
        switch : string {"on"|"off"},
        image : binary : the storage path for the most recent image(photo)
    ]
    Tags:[Hallway,Garage]'}"""
        },
        {
            "from": "gpt",
            "value": """loop(1 MIN) {
        if ((#SmokeDetector #Basement).smoke == "detected") {
            if ((#Camera #Hallway).switch != "on") {
                (#Camera #Hallway).on()
            }
        }
    }"""
        }
],
[    {
        "from": "human",
        "value": """Input: Turn on the office camera if smoke in the living room is detected.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'SmokeDetector': 'Functions : []
Values : [
    smoke : string {"detected"|"not_detected"}
]
Tags:[LivingRoom,DiningRoom]', 'Camera': 'Functions : [
    on(),
    off(),
    take() : return binary : storage path for image(photo),
    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
]
Values : [
    switch : string {"on"|"off"},
    image : binary : the storage path for the most recent image(photo)
]
Tags:[Office,Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#SmokeDetector #LivingRoom).smoke == "detected") {
        if (any(#Camera #Office).switch != "on") {
            all(#Camera #Office).on()
        }
    }
}"""
    }
],
[    {
    "from": "human",
    "value": """Input: Turn on any office camera if smoke in the living room is detected.

Services: {'Clock': 'Functions : []
Values : [
day : int [1~31]
hour : int [0~23]
minute : int [0~59]
month : int [1~12]
second : int [0~59]
weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
year : int [0 ~ 100000]
isHoliday : bool {true|false}
timestamp : double : unixTime
]
Tags:[]', 'SmokeDetector': 'Functions : []
Values : [
smoke : string {"detected"|"not_detected"}
]
Tags:[LivingRoom,DiningRoom]', 'Camera': 'Functions : [
on(),
off(),
take() : return binary : storage path for image(photo),
takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
]
Values : [
switch : string {"on"|"off"},
image : binary : the storage path for the most recent image(photo)
]
Tags:[Office,Bedroom]'}"""
},
{
    "from": "gpt",
    "value": """loop(1 MIN) {
  if ((#SmokeDetector #LivingRoom).smoke == "detected") {
      if ((#Camera #Office).switch != "on") {
          (#Camera #Office).on()
      }
  }
}"""
}
],
[
    {
        "from": "human",
        "value": """Input: Turn on the living room TV and play music in the kitchen at 7:00 AM on weekends.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[Kitchen,Bathroom]',
'Television': 'Functions : [
    on(),
    off(),
    setTvChannel(tvChannel: int),
    channelUp(),
    channelDown(),
    setVolume(volume: int [0 ~ 100]),
    volumeUp(),
    volumeDown(),
    mute() : void, toggle muteStatus
Values : [
    switch : string {"on"|"off"},
    muteStatus : string {"muted"|"unmuted"},
    tvChannel : int
]
Tags:[LivingRoom,Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).weekday == "saturday" or (#Clock).weekday == "sunday") {
        if ((#Clock).hour == 7 and (#Clock).minute == 0) {
            if ((#Television #LivingRoom).switch != "on") {
                all(#Television #LivingRoom).on()
            }
            if ((#Speaker #Kitchen).switch != "on") {
                (#Speaker #Kitchen).on()
            }
            (#Speaker #Kitchen).play("music.mp3")
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the bedroom TV and play music in the bathroom at 7:00 AM on weekends.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[Bathroom,Garage]',
'Television': 'Functions : [
    on(),
    off(),
    setTvChannel(tvChannel: int),
    channelUp(),
    channelDown(),
    setVolume(volume: int [0 ~ 100]),
    volumeUp(),
    volumeDown(),
    mute() : void, toggle muteStatus
Values : [
    switch : string {"on"|"off"},
    muteStatus : string {"muted"|"unmuted"},
    tvChannel : int
]
Tags:[Bedroom,Attic]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).weekday == "saturday" or (#Clock).weekday == "sunday") {
        if ((#Clock).hour == 7 and (#Clock).minute == 0) {
            if ((#Television #Bedroom).switch != "on") {
                (#Television #Bedroom).on()
            }
            if ((#Speaker #Bathroom).switch != "on") {
                (#Speaker #Bathroom).on()
            }
            (#Speaker #Bathroom).play("music.mp3")
        }
    }
}"""
    }],
    [
    {
        "from": "human",
        "value": """Input: Turn on the kitchen TV and play music in the basement at 7:00 AM on weekends.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[Basement,Office]',
'Television': 'Functions : [
    on(),
    off(),
    setTvChannel(tvChannel: int),
    channelUp(),
    channelDown(),
    setVolume(volume: int [0 ~ 100]),
    volumeUp(),
    volumeDown(),
    mute() : void, toggle muteStatus
Values : [
    switch : string {"on"|"off"},
    muteStatus : string {"muted"|"unmuted"},
    tvChannel : int
]
Tags:[Kitchen,Den]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).weekday == "saturday" or (#Clock).weekday == "sunday") {
        if ((#Clock).hour == 7 and (#Clock).minute == 0) {
            if ((#Television #Kitchen).switch != "on") {
                (#Television #Kitchen).on()
            }
            if ((#Speaker #Basement).switch != "on") {
                (#Speaker #Basement).on()
            }
            (#Speaker #Basement).play("music.mp3")
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn off the kitchen refrigerator at 11:00 PM.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Refrigerator': 'Functions : [
    on(),
    off(),
    setRefrigeratorMode(string mode{"RapidCool"|"RapidFreeze"})
]
Values : [
    switch : string {"on"|"off"},
    refrigeratorMode : string {"RapidCool"|"RapidFreeze"}
]
Tags:[Kitchen]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 23 and (#Clock).minute == 0) {
        if ((#Refrigerator #Kitchen).switch != "off") {
            (#Refrigerator #Kitchen).off()
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn off the basement refrigerator at 11:00 PM.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Refrigerator': 'Functions : [
    on(),
    off(),
    setRefrigeratorMode(string mode{"RapidCool"|"RapidFreeze"})
]
Values : [
    switch : string {"on"|"off"},
    refrigeratorMode : string {"RapidCool"|"RapidFreeze"}
]
Tags:[Basement]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 23 and (#Clock).minute == 0) {
        if ((#Refrigerator #Basement).switch != "off") {
            (#Refrigerator #Basement).off()
        }
    }
}"""
    }],[
    {
        "from": "human",
        "value": """Input: Turn off the garage refrigerator at 11:00 PM.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Refrigerator': 'Functions : [
    on(),
    off(),
    setRefrigeratorMode(string mode{"RapidCool"|"RapidFreeze"})
]
Values : [
    switch : string {"on"|"off"},
    refrigeratorMode : string {"RapidCool"|"RapidFreeze"}
]
Tags:[Garage]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 23 and (#Clock).minute == 0) {
        if ((#Refrigerator #Garage).switch != "off") {
            (#Refrigerator #Garage).off()
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the air conditioner in 2 hours.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[LivingRoom,Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """wait until (2 HOUR)
if ((#AirConditioner #LivingRoom).switch != "on") {
    (#AirConditioner #LivingRoom).on()
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn on the office air conditioner in 2 hours.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[LivingRoom,Office,GuestRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """wait until (2 HOUR)
if ((#AirConditioner #Office).switch == "off") {
    (#AirConditioner #Office).on()
}"""
    }],[
    {
        "from": "human",
        "value": """Input: Turn on the kitchen air conditioner in 2 hours.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[Bedroom,GuestRoom,Kitchen]'}"""
    },
    {
        "from": "gpt",
        "value": """wait until (2 HOUR)
if ((#AirConditioner #Kitchen).switch == "off") {
    (#AirConditioner #Kitchen).on()
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Open the livingroom curtain at 7:30 AM.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []', 'Curtain': 'Functions : [
    setCurtainLevel(level: int [0 ~ 100])
]
Values : [
    curtain : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    curtainLevel : int [0 ~ 100]
]
Tags: [Livingroom,Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 7 and (#Clock).minute == 30) {
        if ((#Curtain #Livingroom).switch == "off") {
            (#Curtain #Livingroom).on()
        }
        (#Curtain #Livingroom).open()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Open the kitchen curtain at 7:30 AM.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []', 'Curtain': 'Functions : [
    setCurtainLevel(level: int [0 ~ 100])
]
Values : [
    curtain : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    curtainLevel : int [0 ~ 100]
]
Tags: [Kitchen,Diningroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 7 and (#Clock).minute == 30) {
        if ((#Curtain #Kitchen).switch == "off") {
            (#Curtain #Kitchen).on()
        }
        (#Curtain #Kitchen).open()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Open the bedroom curtain at 7:30 AM.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []', 'Curtain': 'Functions : [
    setCurtainLevel(level: int [0 ~ 100])
]
Values : [
    curtain : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    curtainLevel : int [0 ~ 100]
]
Tags: [Bedroom,Guestroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 7 and (#Clock).minute == 30) {
        if ((#Curtain #Bedroom).switch == "off") {
            (#Curtain #Bedroom).on()
        }
        (#Curtain #Bedroom).open()
    }
}"""
    }
]
,[
    {
        "from": "human",
        "value": """Input: Open the livingroom curtains to 75% at 6pm every day.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Curtain': 'Functions : [
    setCurtainLevel(level: int [0 ~ 100])
]
Values : [
    curtain : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    curtainLevel : int [0 ~ 100]
]
Tags:[LivingRoom,Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop (1 MIN, (#Clock).hour == 18 and (#Clock).minute == 0) {
    if ((#Curtain #LivingRoom).curtainLevel != 75) {
        (#Curtain #LivingRoom).setCurtainLevel(75)
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Open the livingroom curtains to 75% at 6pm every day.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Curtain': 'Functions : [
    setCurtainLevel(level: int [0 ~ 100])
]
Values : [
    curtain : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    curtainLevel : int [0 ~ 100]
]
Tags:[Bedroom,Office,LivingRoom,GuestRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop (1 MIN, (#Clock).hour == 18 and (#Clock).minute == 0) {
    if ((#Curtain #LivingRoom).curtainLevel != 75) {
        (#Curtain #LivingRoom).setCurtainLevel(75)
    }
}"""
    }],[
    {
        "from": "human",
        "value": """Input: Open the livingroom curtains to 75% at 6pm every day.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Curtain': 'Functions : [
    setCurtainLevel(level: int [0 ~ 100])
]
Values : [
    curtain : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    curtainLevel : int [0 ~ 100]
]
Tags:[,Kitchen,LivingRoom,Basement,Attic]'}"""
    },
    {
        "from": "gpt",
        "value": """loop (1 MIN, (#Clock).hour == 18 and (#Clock).minute == 0) {
    if ((#Curtain #LivingRoom).curtainLevel != 75) {
        (#Curtain #LivingRoom).setCurtainLevel(75)
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn off the bedroom humidifier at 5:00 PM if the humidity in the living room is above 55%.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Humidifier': 'Functions : [
    on(),
    off(),
    setHumidiferMode(mode: string {"auto"|"low"|"medium"|"high"})
]
Values : [
    switch : string {"on"|"off"},
    humidifierMode : string {"auto"|"low"|"medium"|"high"}
]
Tags:[Bedroom]', 'HumiditySensor': 'Functions : []
Values : [
    humidity : double[0 ~ 100]
]
Tags:[LivingRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 17 and (#Clock).minute == 0) {
        if ((#HumiditySensor #LivingRoom).humidity > 55.0) {
            if ((#Humidifier #Bedroom).switch == "on") {
                (#Humidifier #Bedroom).off()
            }
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn off the office humidifier at 5:00 PM if the humidity in the basement is above 55%.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Humidifier': 'Functions : [
    on(),
    off(),
    setHumidiferMode(mode: string {"auto"|"low"|"medium"|"high"})
]
Values : [
    switch : string {"on"|"off"},
    humidifierMode : string {"auto"|"low"|"medium"|"high"}
]
Tags:[Office]', 'HumiditySensor': 'Functions : []
Values : [
    humidity : double[0 ~ 100]
]
Tags:[Basement]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 17 and (#Clock).minute == 0) {
        if ((#HumiditySensor #Basement).humidity > 55.0) {
            if ((#Humidifier #Office).switch == "on") {
                (#Humidifier #Office).off()
            }
        }
    }
}"""
    }],[
    {
        "from": "human",
        "value": """Input: Turn off the nursery humidifier at 5:00 PM if the humidity in the attic is above 55%.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Humidifier': 'Functions : [
    on(),
    off(),
    setHumidiferMode(mode: string {"auto"|"low"|"medium"|"high"})
]
Values : [
    switch : string {"on"|"off"},
    humidifierMode : string {"auto"|"low"|"medium"|"high"}
]
Tags:[Nursery]', 'HumiditySensor': 'Functions : []
Values : [
    humidity : double[0 ~ 100]
]
Tags:[Attic]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 17 and (#Clock).minute == 0) {
        if ((#HumiditySensor #Attic).humidity > 55.0) {
            if ((#Humidifier #Nursery).switch == "on") {
                (#Humidifier #Nursery).off()
            }
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn on the livingroom fan.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Fan': 'Functions : [
    on(),
    off(),
    setFanSpeed(speed: int [0 ~ ∞])
]
Values : [
    switch : string {"on"|"off"},
]
Tags:[Livingroom,Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Fan #Livingroom).switch == "off") {
    (#Fan #Livingroom).on()
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn on the bedroom fan.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Fan': 'Functions : [
    on(),
    off(),
    setFanSpeed(speed: int [0 ~ ∞])
]
Values : [
    switch : string {"on"|"off"},
]
Tags:[Bedroom,Office]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Fan #Bedroom).switch == "off") {
    (#Fan #Bedroom).on()
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn on the kitchen fan.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Fan': 'Functions : [
    on(),
    off(),
    setFanSpeed(speed: int [0 ~ ∞])
]
Values : [
    switch : string {"on"|"off"},
]
Tags:[Kitchen,DiningRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Fan #Kitchen).switch == "off") {
    (#Fan #Kitchen).on()
}"""
    }
]
,[
    {
        "from": "human",
        "value": """Input: Set the living room curtains to 40% if the kitchen blinds are at 70%.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []', 'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags: [Kitchen,Bedroom]', 'Curtain': 'Functions : [
    setCurtainLevel(level: int [0 ~ 100])
]
Values : [
    curtain : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    curtainLevel : int [0 ~ 100]
]
Tags: [LivingRoom,Basement]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Blind #Kitchen).blindLevel == 70) {
        (#Curtain #LivingRoom).setCurtainLevel(40)
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Set the dining room curtains to 40% if the office blinds are at 70%.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []', 'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags: [Office,Garage]', 'Curtain': 'Functions : [
    setCurtainLevel(level: int [0 ~ 100])
]
Values : [
    curtain : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    curtainLevel : int [0 ~ 100]
]
Tags: [DiningRoom,Hallway]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Blind #Office).blindLevel == 70) {
        (#Curtain #DiningRoom).setCurtainLevel(40)
    }
}"""
    }],[
    {
        "from": "human",
        "value": """Input: Set the bedroom curtains to 40% if the living room blinds are at 70%.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []', 'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags: [LivingRoom,Attic]', 'Curtain': 'Functions : [
    setCurtainLevel(level: int [0 ~ 100])
]
Values : [
    curtain : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    curtainLevel : int [0 ~ 100]
]
Tags: [Bedroom,Study]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Blind #LivingRoom).blindLevel == 70) {
        (#Curtain #Bedroom).setCurtainLevel(40)
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Change the basement dryer to continuous dehumidification mode.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Basement, LaundryRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """
        if((#Dehumidifier #Basement).switch != "on"){
            (#Dehumidifier #Basement).on()
        }
        if ((#Dehumidifier #Basement).dehumidifierMode != "continuousDehumidifying") {
    (#Dehumidifier #Basement).setDeHumidifierMode("continuousDehumidifying")
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Change the bathroom dryer to continuous dehumidification mode.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Bathroom, LaundryRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """
          if((#Dehumidifier #Bathroom).switch != "on"){
            (#Dehumidifier #Bathroom).on()
        }
        if ((#Dehumidifier #Bathroom).dehumidifierMode != "continuousDehumidifying") {
    (#Dehumidifier #Bathroom).setDeHumidifierMode("continuousDehumidifying")
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Change the attic dryer to continuous dehumidification mode.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Attic, StorageRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """
        if((#Dehumidifier #Attic).switch != "on"){
            (#Dehumidifier #Attic).on()
        }
        if ((#Dehumidifier #Attic).dehumidifierMode != "continuousDehumidifying") {
    (#Dehumidifier #Attic).setDeHumidifierMode("continuousDehumidifying")
}"""
    }# changed code
]
,
[
    {
        "from": "human",
        "value": """Input: Turn on the livingroom air purifier at 6 a.m. every day, and if movement is detected in the hallway at 7 p.m. on weekdays, take a picture and say through the livingroom speaker that movement has been detected.

Services: {
    'Camera': 'Functions : [
        on(),
        off(),
        take() : return binary : storage path for image(photo),
        takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
    ]
    Values : [
        switch : string {"on"|"off"},
        image : binary : the storage path for the most recent image(photo)
    ]
    Tags:[LivingRoom,Office]',

    'MotionSensor': 'Functions : []
    Values : [
        motion : string {"active"|"inactive"}
    ]
    Tags:[Hallway,Garage]',

    'Clock': 'Functions : []
    Values : [
        day : int [1~31],
        hour : int [0~23],
        minute : int [0~59],
        month : int [1~12],
        second : int [0~59],
        weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"},
        year : int [0 ~ 100000],
        isHoliday : bool {true|false},
        timestamp : double : unixTime
    ]
    Tags:[]',

    'AirPurifier': 'Functions : [
        on(),
        off(),
        setAirPurifierFanMode(mode: string {"auto"|"sleep"|"low"|"medium"|"high"|"quiet"|"windFree"|"off"})
    ]
    Values : [
        switch : string {"on"|"off"},
        airPurifierFanMode : string {"auto"|"sleep"|"low"|"medium"|"high"|"quiet"|"windFree"|"off"}
    ]
    Tags:[LivingRoom,Bedroom]',

    'Speaker': 'Functions : [
        on(),
        off(),
        pause(),
        stop(),
        play(source: string),
        speak(text: string)
    ]
    Values : [
        switch : string {"on"|"off"},
        playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
    ]
    Tags:[LivingRoom,Kitchen]'
}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 SEC){
    if((#Clock).hour == 6 and (#Clock).minute == 0 and (#Clock).second == 0){
        if((#AirPurifier #LivingRoom).switch != "on"){
            (#AirPurifier #LivingRoom).on()
        }
    }
    if((#Clock).hour == 19 and (#Clock).minute == 0 and (#Clock).second == 0){
        if((#Clock).weekday == "monday" or (#Clock).weekday == "tuesday" or (#Clock).weekday == "wednesday" or (#Clock).weekday == "thursday" or (#Clock).weekday == "friday"){
            if((#MotionSensor #Hallway).motion == "active"){
                if((#Camera #LivingRoom).switch != "on"){
                    (#Camera #LivingRoom).on()
                }
                (#Camera #LivingRoom).take()
                (#Speaker #LivingRoom).speak("움직임이 감지되었습니다.")
            }
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn on the kitchen air purifier at 6 a.m. every day, and if movement is detected in the backyard at 7 p.m. on weekdays, take a picture and say through the kitchen speaker that movement has been detected.

Services: {
    'Camera': 'Functions : [
        on(),
        off(),
        take() : return binary : storage path for image(photo),
        takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
    ]
    Values : [
        switch : string {"on"|"off"},
        image : binary : the storage path for the most recent image(photo)
    ]
    Tags:[Kitchen,Bedroom]',

    'MotionSensor': 'Functions : []
    Values : [
        motion : string {"active"|"inactive"}
    ]
    Tags:[Backyard,Driveway]',

    'Clock': 'Functions : []
    Values : [
        day : int [1~31],
        hour : int [0~23],
        minute : int [0~59],
        month : int [1~12],
        second : int [0~59],
        weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"},
        year : int [0 ~ 100000],
        isHoliday : bool {true|false},
        timestamp : double : unixTime
    ]
    Tags:[]',

    'AirPurifier': 'Functions : [
        on(),
        off(),
        setAirPurifierFanMode(mode: string {"auto"|"sleep"|"low"|"medium"|"high"|"quiet"|"windFree"|"off"})
    ]
    Values : [
        switch : string {"on"|"off"},
        airPurifierFanMode : string {"auto"|"sleep"|"low"|"medium"|"high"|"quiet"|"windFree"|"off"}
    ]
    Tags:[Kitchen,Office]',

    'Speaker': 'Functions : [
        on(),
        off(),
        pause(),
        stop(),
        play(source: string),
        speak(text: string)
    ]
    Values : [
        switch : string {"on"|"off"},
        playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
    ]
    Tags:[Kitchen,Bathroom]'
}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 SEC){
    if((#Clock).hour == 6 and (#Clock).minute == 0 and (#Clock).second == 0){
        if((#AirPurifier #Kitchen).switch != "on"){
            (#AirPurifier #Kitchen).on()
        }
    }
    if((#Clock).hour == 19 and (#Clock).minute == 0 and (#Clock).second == 0){
        if((#Clock).weekday == "monday" or (#Clock).weekday == "tuesday" or (#Clock).weekday == "wednesday" or (#Clock).weekday == "thursday" or (#Clock).weekday == "friday"){
            if((#MotionSensor #Backyard).motion == "active"){
                if((#Camera #Kitchen).switch != "on"){
                    (#Camera #Kitchen).on()
                }
                (#Camera #Kitchen).take()
                (#Speaker #Kitchen).speak("움직임이 감지되었습니다.")
            }
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn on the bedroom air purifier at 6 a.m. every day, and if movement is detected in the basement at 7 p.m. on weekdays, take a picture and say through the bedroom speaker that movement has been detected.

Services: {
    'Camera': 'Functions : [
        on(),
        off(),
        take() : return binary : storage path for image(photo),
        takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
    ]
    Values : [
        switch : string {"on"|"off"},
        image : binary : the storage path for the most recent image(photo)
    ]
    Tags:[Bedroom,Garage]',

    'MotionSensor': 'Functions : []
    Values : [
        motion : string {"active"|"inactive"}
    ]
    Tags:[Basement,Patio]',

    'Clock': 'Functions : []
    Values : [
        day : int [1~31],
        hour : int [0~23],
        minute : int [0~59],
        month : int [1~12],
        second : int [0~59],
        weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"},
        year : int [0 ~ 100000],
        isHoliday : bool {true|false},
        timestamp : double : unixTime
    ]
    Tags:[]',

    'AirPurifier': 'Functions : [
        on(),
        off(),
        setAirPurifierFanMode(mode: string {"auto"|"sleep"|"low"|"medium"|"high"|"quiet"|"windFree"|"off"})
    ]
    Values : [
        switch : string {"on"|"off"},
        airPurifierFanMode : string {"auto"|"sleep"|"low"|"medium"|"high"|"quiet"|"windFree"|"off"}
    ]
    Tags:[Bedroom,LivingRoom]',

    'Speaker': 'Functions : [
        on(),
        off(),
        pause(),
        stop(),
        play(source: string),
        speak(text: string)
    ]
    Values : [
        switch : string {"on"|"off"},
        playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
    ]
    Tags:[Bedroom,Garage]'
}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 SEC){
    if((#Clock).hour == 6 and (#Clock).minute == 0 and (#Clock).second == 0){
        if((#AirPurifier #Bedroom).switch != "on"){
            (#AirPurifier #Bedroom).on()
        }
    }
    if((#Clock).hour == 19 and (#Clock).minute == 0 and (#Clock).second == 0){
        if((#Clock).weekday == "monday" or (#Clock).weekday == "tuesday" or (#Clock).weekday == "wednesday" or (#Clock).weekday == "thursday" or (#Clock).weekday == "friday"){
            if((#MotionSensor #Basement).motion == "active"){
                if((#Camera #Bedroom).switch != "on"){
                    (#Camera #Bedroom).on()
                }
                (#Camera #Bedroom).take()
                (#Speaker #Bedroom).speak("움직임이 감지되었습니다.")
            }
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: If the outside temperature is lower than 10 degrees, turn on the bedroom air conditioner in heating mode and set it to 22 degrees.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'WeatherProvider': 'Functions : [
    getWeatherInfo(double latitude, double longitude): return string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"}
]
Values : [
    weather : string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"},
    temperature : int celcius,
    humidity : double,
    pressure : double
]
Tags:[]', 'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[Bedroom,LivingRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#WeatherProvider).temperature < 10) {
    if ((#AirConditioner #Bedroom).switch == "off") {
        (#AirConditioner #Bedroom).on()
    }
    (#AirConditioner #Bedroom).setAirConditionerMode("heat")
    (#AirConditioner #Bedroom).setTemperature(22)
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If the outside temperature is lower than 10 degrees, turn on the kitchen air conditioner in heating mode and set it to 22 degrees.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'WeatherProvider': 'Functions : [
    getWeatherInfo(double latitude, double longitude): return string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"}
]
Values : [
    weather : string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"},
    temperature : int celcius,
    humidity : double,
    pressure : double
]
Tags:[]', 'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[Kitchen,Bathroom]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#WeatherProvider).temperature < 10) {
    if ((#AirConditioner #Kitchen).switch == "off") {
        (#AirConditioner #Kitchen).on()
    }
    (#AirConditioner #Kitchen).setAirConditionerMode("heat")
    (#AirConditioner #Kitchen).setTemperature(22)
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If the outside temperature is lower than 10 degrees, turn on the basement air conditioner in heating mode and set it to 22 degrees.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'WeatherProvider': 'Functions : [
    getWeatherInfo(double latitude, double longitude): return string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"}
]
Values : [
    weather : string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"},
    temperature : int celcius,
    humidity : double,
    pressure : double
]
Tags:[]', 'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[Basement,Office]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#WeatherProvider).temperature < 10) {
    if ((#AirConditioner #Basement).switch == "off") {
        (#AirConditioner #Basement).on()
    }
    (#AirConditioner #Basement).setAirConditionerMode("heat")
    (#AirConditioner #Basement).setTemperature(22)
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the livingroom humidifier.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Humidifier': 'Functions : [
    on(),
    off(),
    setHumidiferMode(mode: string {"auto"|"low"|"medium"|"high"})
]
Values : [
    switch : string {"on"|"off"},
    humidifierMode : string {"auto"|"low"|"medium"|"high"}
]
Tags:[Livingroom,Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Humidifier #Livingroom).switch == "off") {
    (#Humidifier #Livingroom).on()
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the kitchen humidifier.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Humidifier': 'Functions : [
    on(),
    off(),
    setHumidiferMode(mode: string {"auto"|"low"|"medium"|"high"})
]
Values : [
    switch : string {"on"|"off"},
    humidifierMode : string {"auto"|"low"|"medium"|"high"}
]
Tags:[Kitchen,Office]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Humidifier #Kitchen).switch == "off") {
    (#Humidifier #Kitchen).on()
}"""
    }],[
    {
        "from": "human",
        "value": """Input: Turn on the bedroom humidifier.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Humidifier': 'Functions : [
    on(),
    off(),
    setHumidiferMode(mode: string {"auto"|"low"|"medium"|"high"})
]
Values : [
    switch : string {"on"|"off"},
    humidifierMode : string {"auto"|"low"|"medium"|"high"}
]
Tags:[Bedroom,Bathroom]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Humidifier #Bedroom).switch == "off") {
    (#Humidifier #Bedroom).on()
}"""
    }
]
,[
      {
        "from": "human",
        "value": """Input: Set the living room robot cleaner to auto mode at 8:00 AM and turn on the kitchen lights if it is raining.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'WeatherProvider': 'Functions : [
    getWeatherInfo(double latitude, double longitude): return string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"}
]
Values : [
    weather : string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"},
    temperature : int celcius,
    humidity : double,
    pressure : double
]
Tags:[]', 'RobotCleaner': 'Functions : [
    on(),
    off(),
    setRobotCleanerCleaningMode(string mode{"auto"|"part"|"repeat"|"manual"|"stop"|"map"})
]
Values : [
    switch : string {"on"|"off"},
    robotCleanerCleaningMode : string {"auto"|"part"|"repeat"|"manual"|"stop"|"map"}
]
Tags:[LivingRoom]', 'Light': 'Functions : [
    on(),
    off(),
    setColor(color: string {"{hue}|{saturation}|{brightness}"})
    setLevel(level int [0 ~ 100])
]
Values : [
    switch : string {"on"|"off"},
    light : double
]
Tags:[Kitchen]'}"""
      },
      {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 8 and (#Clock).minute == 0) {
        if ((#RobotCleaner #LivingRoom).robotCleanerCleaningMode != "auto") {
            (#RobotCleaner #LivingRoom).setRobotCleanerCleaningMode("auto")
        }
        if ((#WeatherProvider).weather == "rain") {
            if (any(#Light #Kitchen).switch != "on") {
                all(#Light #Kitchen).on()
            }
        }
    }
}"""
      }
],
[
      {
        "from": "human",
        "value": """Input: Set the bedroom robot cleaner to auto mode at 8:00 AM and turn on the garage lights if it is raining.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'WeatherProvider': 'Functions : [
    getWeatherInfo(double latitude, double longitude): return string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"}
]
Values : [
    weather : string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"},
    temperature : int celcius,
    humidity : double,
    pressure : double
]
Tags:[]', 'RobotCleaner': 'Functions : [
    on(),
    off(),
    setRobotCleanerCleaningMode(string mode{"auto"|"part"|"repeat"|"manual"|"stop"|"map"})
]
Values : [
    switch : string {"on"|"off"},
    robotCleanerCleaningMode : string {"auto"|"part"|"repeat"|"manual"|"stop"|"map"}
]
Tags:[Bedroom]', 'Light': 'Functions : [
    on(),
    off(),
    setColor(color: string {"{hue}|{saturation}|{brightness}"})
    setLevel(level int [0 ~ 100])
]
Values : [
    switch : string {"on"|"off"},
    light : double
]
Tags:[Garage]'}"""
      },
      {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 8 and (#Clock).minute == 0) {
        if ((#RobotCleaner #Bedroom).robotCleanerCleaningMode != "auto") {
            (#RobotCleaner #Bedroom).setRobotCleanerCleaningMode("auto")
        }
        if ((#WeatherProvider).weather == "rain") {
            if (any(#Light #Garage).switch != "on") {
                all(#Light #Garage).on()
            }
        }
    }
}"""
      }
],
[
      {
        "from": "human",
        "value": """Input: Set the hallway robot cleaner to auto mode at 8:00 AM and turn on the bathroom lights if it is raining.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'WeatherProvider': 'Functions : [
    getWeatherInfo(double latitude, double longitude): return string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"}
]
Values : [
    weather : string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"},
    temperature : int celcius,
    humidity : double,
    pressure : double
]
Tags:[]', 'RobotCleaner': 'Functions : [
    on(),
    off(),
    setRobotCleanerCleaningMode(string mode{"auto"|"part"|"repeat"|"manual"|"stop"|"map"})
]
Values : [
    switch : string {"on"|"off"},
    robotCleanerCleaningMode : string {"auto"|"part"|"repeat"|"manual"|"stop"|"map"}
]
Tags:[Hallway]', 'Light': 'Functions : [
    on(),
    off(),
    setColor(color: string {"{hue}|{saturation}|{brightness}"})
    setLevel(level int [0 ~ 100])
]
Values : [
    switch : string {"on"|"off"},
    light : double
]
Tags:[Bathroom]'}"""
      },
      {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 8 and (#Clock).minute == 0) {
        if ((#RobotCleaner #Hallway).robotCleanerCleaningMode != "auto") {
            (#RobotCleaner #Hallway).setRobotCleanerCleaningMode("auto")
        }
        if ((#WeatherProvider).weather == "rain") {
            if (any(#Light #Bathroom).switch != "on") {
                all(#Light #Bathroom).on()
            }
        }
    }
}"""
      }
]
,
[
    {
        "from": "human",
        "value": """Input: If PM 10 level is above 100 and temperature exceeds 25°C, turn on the living room air conditioner and set it to cool mode. If CO2 level is above 600 ppm, turn off the living room air conditioner.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ ∞] : PM 10 dust level,
    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[LivingRoom,Bedroom,Basement]',
'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[LivingRoom,Bedroom]'}
"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector #LivingRoom).dustLevel > 100.0 and (#AirQualityDetector #LivingRoom).temperature > 25.0) {
        if ((#AirConditioner #LivingRoom).switch == "off") {
            (#AirConditioner #LivingRoom).on()
        }
        if ((#AirConditioner #LivingRoom).airConditionerMode != "cool") {
            (#AirConditioner #LivingRoom).setAirConditionerMode("cool")
        }
    }
    if ((#AirQualityDetector #LivingRoom).carbonDioxide > 600.0) {
        if ((#AirConditioner #LivingRoom).switch == "on") {
            (#AirConditioner #LivingRoom).off()
        }
    }
}"""
    }
]
,[
    {
        "from": "human",
        "value": """Input: If PM 10 level is above 100 and temperature exceeds 25°C, turn on the office air conditioner and set it to cool mode. If CO2 level is above 600 ppm, turn off the office air conditioner.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ ∞] : PM 10 dust level,
    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[Office,Workshop]',
'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[Office,ServerRoom]'}
"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector #Office).dustLevel > 100.0 and (#AirQualityDetector #Office).temperature > 25.0) {
        if ((#AirConditioner #Office).switch == "off") {
            (#AirConditioner #Office).on()
        }
        if ((#AirConditioner #Office).airConditionerMode != "cool") {
            (#AirConditioner #Office).setAirConditionerMode("cool")
        }
    }
    if ((#AirQualityDetector #Office).carbonDioxide > 600.0) {
        if ((#AirConditioner #Office).switch == "on") {
            (#AirConditioner #Office).off()
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: If PM 10 level is above 100 and temperature exceeds 25°C, turn on the basement air conditioner and set it to cool mode. If CO2 level is above 600 ppm, turn off the basement air conditioner.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ ∞] : PM 10 dust level,
    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[Garage,Basement]',
'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[Basement,Attic]'}
"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector #Basement).dustLevel > 100.0 and (#AirQualityDetector #Basement).temperature > 25.0) {
        if ((#AirConditioner #Basement).switch == "off") {
            (#AirConditioner #Basement).on()
        }
        if ((#AirConditioner #Basement).airConditionerMode != "cool") {
            (#AirConditioner #Basement).setAirConditionerMode("cool")
        }
    }
    if ((#AirQualityDetector #Basement).carbonDioxide > 600.0) {
        if ((#AirConditioner #Basement).switch == "on") {
            (#AirConditioner #Basement).off()
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the livingroom humidifier every 30 minutes.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Humidifier': 'Functions : [\n    on(),\n\toff(),\n    setHumidiferMode(mode: string {"auto"|"low"|"medium"|"high"})\n]\nValues : [\n\tswitch : string {"on"|"off"},\n    humidifierMode : string {"auto"|"low"|"medium"|"high"}\n]\nTags:[LivingRoom,Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop (30 MIN) {
        if ((#Humidifier #Livingroom).switch == "off") {
            (#Humidifier #Livingroom).on()
        }

}"""
    } # changed code
],
[
    {
        "from": "human",
        "value": """Input: Turn on the bedroom humidifier every 30 minutes.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Humidifier': 'Functions : [\n    on(),\n\toff(),\n    setHumidiferMode(mode: string {"auto"|"low"|"medium"|"high"})\n]\nValues : [\n\tswitch : string {"on"|"off"},\n    humidifierMode : string {"auto"|"low"|"medium"|"high"}\n]\nTags:[Office,Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop (30 MIN) {
        if ((#Humidifier #Bedroom).switch == "off") {
            (#Humidifier #Bedroom).on()
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn on the office humidifier every 30 minutes.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Humidifier': 'Functions : [\n    on(),\n\toff(),\n    setHumidiferMode(mode: string {"auto"|"low"|"medium"|"high"})\n]\nValues : [\n\tswitch : string {"on"|"off"},\n    humidifierMode : string {"auto"|"low"|"medium"|"high"}\n]\nTags:[Office,Garage]'}"""
    },
    {
        "from": "gpt",
        "value": """loop (30 MIN) {
        if ((#Humidifier #Office).switch == "off") {
            (#Humidifier #Office).on()
        }

}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If PM 10 level is above 100 and temperature exceeds 25°C, turn on the living room air conditioner and set it to cool mode. If CO2 level is above 600 ppm, turn off the living room air conditioner.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ ∞] : PM 10 dust level,
    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[LivingRoom,Bedroom,Basement]',
'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[LivingRoom,Bedroom]'}
"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector #LivingRoom).dustLevel > 100.0 and (#AirQualityDetector #LivingRoom).temperature > 25.0) {
        if ((#AirConditioner #LivingRoom).switch == "off") {
            (#AirConditioner #LivingRoom).on()
        }
        if ((#AirConditioner #LivingRoom).airConditionerMode != "cool") {
            (#AirConditioner #LivingRoom).setAirConditionerMode("cool")
        }
    }
    if ((#AirQualityDetector #LivingRoom).carbonDioxide > 600.0) {
        if ((#AirConditioner #LivingRoom).switch == "on") {
            (#AirConditioner #LivingRoom).off()
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: If PM 10 level is above 100 and temperature exceeds 25°C, turn on the office air conditioner and set it to cool mode. If CO2 level is above 600 ppm, turn off the office air conditioner.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ ∞] : PM 10 dust level,
    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[Office,Workshop]',
'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[Office,ServerRoom]'}
"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector #Office).dustLevel > 100.0 and (#AirQualityDetector #Office).temperature > 25.0) {
        if ((#AirConditioner #Office).switch == "off") {
            (#AirConditioner #Office).on()
        }
        if ((#AirConditioner #Office).airConditionerMode != "cool") {
            (#AirConditioner #Office).setAirConditionerMode("cool")
        }
    }
    if ((#AirQualityDetector #Office).carbonDioxide > 600.0) {
        if ((#AirConditioner #Office).switch == "on") {
            (#AirConditioner #Office).off()
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: If PM 10 level is above 100 and temperature exceeds 25°C, turn on the bedroom air conditioner and set it to cool mode. If CO2 level is above 600 ppm, turn off the bedroom air conditioner.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ ∞] : PM 10 dust level,
    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[Bedroom,LivingRoom]',
'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[Bedroom,GuestRoom]'}
"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector #Bedroom).dustLevel > 100.0 and (#AirQualityDetector #Bedroom).temperature > 25.0) {
        if ((#AirConditioner #Bedroom).switch == "off") {
            (#AirConditioner #Bedroom).on()
        }
        if ((#AirConditioner #Bedroom).airConditionerMode != "cool") {
            (#AirConditioner #Bedroom).setAirConditionerMode("cool")
        }
    }
    if ((#AirQualityDetector #Bedroom).carbonDioxide > 600.0) {
        if ((#AirConditioner #Bedroom).switch == "on") {
            (#AirConditioner #Bedroom).off()
        }
    }
}"""
    }
]
,
[
      {
        "from": "human",
        "value": """Input: If the temperature is above 26 degrees at 8:30 am, turn on the livingroom fan.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Fan': 'Functions : [
    on(),
    off(),
    setFanSpeed(speed: int [0 ~ ∞])
]
Values : [
    switch : string {"on"|"off"}
]
Tags:[LivingRoom,Bedroom]', 'TemperatureSensor': 'Functions : []
Values : [
    temperature: int [-460 ~ 10000]
]
Tags:[LivingRoom,Bathroom]'}"""
      },
      {
        "from": "gpt",
        "value": """wait until((#Clock).hour == 8 && (#Clock).minute == 30)
if((#TemperatureSensor #LivingRoom).temperature >=26){
    if((#Fan #LivingRoom).switch != "on"){
        (#Fan #LivingRoom).on()
    }
}"""
      }
],
[
      {
        "from": "human",
        "value": """Input: If the temperature is above 26 degrees at 8:30 am, turn on the office fan.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Fan': 'Functions : [
    on(),
    off(),
    setFanSpeed(speed: int [0 ~ ∞])
]
Values : [
    switch : string {"on"|"off"}
]
Tags:[Office,StudyRoom]', 'TemperatureSensor': 'Functions : []
Values : [
    temperature: int [-460 ~ 10000]
]
Tags:[Office,Balcony]'}"""
      },
      {
        "from": "gpt",
        "value": """wait until((#Clock).hour == 8 && (#Clock).minute == 30)
if((#TemperatureSensor #Office).temperature >=26){
    if((#Fan #Office).switch != "on"){
        (#Fan #Office).on()
    }
}"""
      }
]
,
[
      {
        "from": "human",
        "value": """Input: If the temperature is above 26 degrees at 8:30 am, turn on the bedroom fan.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Fan': 'Functions : [
    on(),
    off(),
    setFanSpeed(speed: int [0 ~ ∞])
]
Values : [
    switch : string {"on"|"off"}
]
Tags:[Bedroom,GuestRoom]', 'TemperatureSensor': 'Functions : []
Values : [
    temperature: int [-460 ~ 10000]
]
Tags:[Bedroom,Kitchen]'}"""
      },
      {
        "from": "gpt",
        "value": """wait until((#Clock).hour == 8 && (#Clock).minute == 30)
if((#TemperatureSensor #Bedroom).temperature >=26){
    if((#Fan #Bedroom).switch != "on"){
        (#Fan #Bedroom).on()
    }
}"""
      }
],
[
    {
        "from": "human",
        "value": """Input: If the current humidity in the bedroom exceeds 70%, open the livingroom window.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Window': 'Functions : [
    open(),
    close()
]
Values : [
    window : string {"closed"|"open"}
]
Tags:[Livingroom,Office]', 'HumiditySensor': 'Functions : []
Values : [
    humidity : double[0 ~ 100]
]
Tags:[Bedroom,Bathroom]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#HumiditySensor #Bedroom).humidity > 70) {
    if (any(#Window #Livingroom).window == "closed") {
        all(#Window #Livingroom).open()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If the current humidity in the bedroom exceeds 70%, open one livingroom window.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Window': 'Functions : [
    open(),
    close()
]
Values : [
    window : string {"closed"|"open"}
]
Tags:[Livingroom,Office]', 'HumiditySensor': 'Functions : []
Values : [
    humidity : double[0 ~ 100]
]
Tags:[Bedroom,Bathroom]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#HumiditySensor #Bedroom).humidity > 70) {
    if ((#Window #Livingroom).window == "closed") {
        (#Window #Livingroom).open()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If the current humidity in the greenhouse exceeds 70%, open the attic window.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Window': 'Functions : [
    open(),
    close()
]
Values : [
    window : string {"closed"|"open"}
]
Tags:[Attic,Garage]', 'HumiditySensor': 'Functions : []
Values : [
    humidity : double[0 ~ 100]
]
Tags:[Greenhouse,Sauna]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#HumiditySensor #Greenhouse).humidity > 70) {
    if (any(#Window #Attic).window == "closed") {
        all(#Window #Attic).open()
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If the current humidity in the kitchen exceeds 70%, open any bedroom window.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Window': 'Functions : [
    open(),
    close()
]
Values : [
    window : string {"closed"|"open"}
]
Tags:[Bedroom,Livingroom]', 'HumiditySensor': 'Functions : []
Values : [
    humidity : double[0 ~ 100]
]
Tags:[Kitchen,Bathroom]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#HumiditySensor #Kitchen).humidity > 70) {
    if ((#Window #Bedroom).window == "closed") {
        (#Window #Bedroom).open()
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Notifies you of how much gas in kitchen has been used every 10 minutes by living room speaker

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[LivingRoom,Bedroom]', 'GasMeter': 'Functions : []
Values : [
    gasMeter : double,
    gasMeterCalorific : double : amount of heat produced (kJ),
    gasMeterTime : double seconds,
    gasMeterVolume : double
]
Tags:[Basement,Kitchen]'}"""
    },
    {
        "from": "gpt",
        "value": """loop (10 MIN) {
    if ((#Speaker #LivingRoom).switch == "off") {
        (#Speaker #LivingRoom).on()
    }
    (#Speaker #LivingRoom).speak("Gas usage time is " + (#GasMeter #Kitchen).gasMeterTime)
}"""#ok?
    }
],
[
    {
        "from": "human",
        "value": """Input: Notifies you of how much gas in garage has been used every 10 minutes by office speaker.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[Office,Bathroom]', 'GasMeter': 'Functions : []
Values : [
    gasMeter : double,
    gasMeterCalorific : double : amount of heat produced (kJ),
    gasMeterTime : double seconds,
    gasMeterVolume : double
]
Tags:[Garage,Attic]'}"""
    },
    {
        "from": "gpt",
        "value": """loop (10 MIN) {
    if ((#Speaker #Office).switch == "off") {
        (#Speaker #Office).on()
    }
    (#Speaker #Office).speak("Gas usage time is " + (#GasMeter #Garage).gasMeterTime)
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Notifies you of how much gas in garage has been used every 10 minutes by living room speaker.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[Garage,Basement]', 'GasMeter': 'Functions : []
Values : [
    gasMeter : double,
    gasMeterCalorific : double : amount of heat produced (kJ),
    gasMeterTime : double seconds,
    gasMeterVolume : double
]
Tags:[LivingRoom,Bathroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop (10 MIN) {
    if ((#Speaker #Garage).switch == "off") {
        (#Speaker #Garage).on()
    }
    (#Speaker #Garage).speak("Gas usage time is " + (#GasMeter #LivingRoom).gasMeterTime)
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: After 12 minutes, say ‘Hello World’ through the living room speakers.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags: [LivingRoom, Bedroom, Office]'}"""
    },
    {
        "from": "gpt",
        "value": """wait until (12 MIN)
if ((#Speaker #LivingRoom).switch == "off") {
    (#Speaker #LivingRoom).on()
}
(#Speaker #LivingRoom).speak("Hello World")"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: After 12 minutes, say ‘Hello World’ through the bedroom speakers.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags: [Bedroom, Kitchen, Garage]'}"""
    },
    {
        "from": "gpt",
        "value": """wait until (12 MIN)
if ((#Speaker #Bedroom).switch == "off") {
    (#Speaker #Bedroom).on()
}
(#Speaker #Bedroom).speak("Hello World")"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: After 12 minutes, say ‘Hello World’ through the kitchen speakers.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags: [Kitchen, Bathroom, Hallway]'}"""
    },
    {
        "from": "gpt",
        "value": """wait until (12 MIN)
if ((#Speaker #Kitchen).switch == "off") {
    (#Speaker #Kitchen).on()
}
(#Speaker #Kitchen).speak("Hello World")"""
    }
],
[
    {
        "from": "human",
        "value": """Input: After 1 hour, tell the current accumulated basement gas usage time and the amount of gas used by livingroom speaker.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[LivingRoom,Bedroom]', 'GasMeter': 'Functions : []
Values : [
    gasMeter : double,
    gasMeterCalorific : double : amount of heat produced (kJ),
    gasMeterTime : double seconds,
    gasMeterVolume : double
]
Tags:[Basement,Kitchen]'}"""
    },
    {
        "from": "gpt",
        "value": """wait until (1 HOUR)
usage_time = (#GasMeter #Basement).gasMeterTime
usage_amount = (#GasMeter #Basement).gasMeterVolume
(#Speaker #LivingRoom).speak("현재 누적 가스 사용 시간은 " + usage_time)
(#Speaker #LivingRoom).speak("현재 사용된 가스의 양은 " + usage_amount)"""
    }
],
[
    {
        "from": "human",
        "value": """Input: After 1 hour, tell the current accumulated garage gas usage time and the amount of gas used by office speaker.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[Office,Hallway]', 'GasMeter': 'Functions : []
Values : [
    gasMeter : double,
    gasMeterCalorific : double : amount of heat produced (kJ),
    gasMeterTime : double seconds,
    gasMeterVolume : double
]
Tags:[Attic,Garage]'}"""
    },
    {
        "from": "gpt",
        "value": """wait until (1 HOUR)
usage_time = (#GasMeter #Garage).gasMeterTime
usage_amount = (#GasMeter #Garage).gasMeterVolume
(#Speaker #Office).speak("현재 누적 가스 사용 시간은 " + usage_time)
(#Speaker #Office).speak("현재 사용된 가스의 양은 " + usage_amount)"""
    }
],
[
    {
        "from": "human",
        "value": """Input: After 1 hour, tell the current accumulated kitchen gas usage time and the amount of gas used by attic speaker.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[Bathroom,Garage]', 'GasMeter': 'Functions : []
Values : [
    gasMeter : double,
    gasMeterCalorific : double : amount of heat produced (kJ),
    gasMeterTime : double seconds,
    gasMeterVolume : double
]
Tags:[Kitchen,Attic]'}"""
    },
    {
        "from": "gpt",
        "value": """wait until (1 HOUR)
usage_time = (#GasMeter #Kitchen).gasMeterTime
usage_amount = (#GasMeter #Kitchen).gasMeterVolume
(#Speaker #Attic).speak("현재 누적 가스 사용 시간은 " + usage_time)
(#Speaker #Attic).speak("현재 사용된 가스의 양은 " + usage_amount)"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Start watering the garden with 100 ml if the livingroom blinds are open at 7:00 AM.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags:[LivingRoom,Bedroom]', 'Irrigator': 'Functions : [
    on(),
    off(),
    startWatering(),
    setWaterPortion(portion: double [0 ~ 2000], unit: string {"liters"|"milliliters"|"gallons"|"ounces"})
]
Values : [
    switch: string {"on"|"off"}
]
Tags:[Greenhouse,Garden]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 7 and (#Clock).minute == 0) {
        if ((#Blind #LivingRoom).blind == "open") {
            if ((#Irrigator #Garden).switch == "off") {
                (#Irrigator #Garden).on()
            }
            (#Irrigator #Garden).startWatering(100)
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Start watering the balcony with 100 ml if the kitchen blinds are open at 7:00 AM.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags:[Kitchen,Office]', 'Irrigator': 'Functions : [
    on(),
    off(),
    startWatering(),
    setWaterPortion(portion: double [0 ~ 2000], unit: string {"liters"|"milliliters"|"gallons"|"ounces"})
]
Values : [
    switch: string {"on"|"off"}
]
Tags:[Balcony,Patio]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 7 and (#Clock).minute == 0) {
        if ((#Blind #Kitchen).blind == "open") {
            if ((#Irrigator #Balcony).switch == "off") {
                (#Irrigator #Balcony).on()
            }
            (#Irrigator #Balcony).startWatering(100)
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Start watering the terrace with 100 ml if the bedroom blinds are open at 7:00 AM.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags:[Hallway,Bedroom]', 'Irrigator': 'Functions : [
    on(),
    off(),
    startWatering(),
    setWaterPortion(portion: double [0 ~ 2000], unit: string {"liters"|"milliliters"|"gallons"|"ounces"})
]
Values : [
    switch: string {"on"|"off"}
]
Tags:[Backyard,Terrace]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 7 and (#Clock).minute == 0) {
        if ((#Blind #Bedroom).blind == "open") {
            if ((#Irrigator #Terrace).switch == "off") {
                (#Irrigator #Terrace).on()
            }
            (#Irrigator #Terrace).startWatering(100)
        }
    }
}"""
    }
],[
    {
        "from": "human",
        "value": """Input: Turn off the garden irrigation system at 11:00 AM if the livingroom blinds are closed.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags:[Livingroom,Office]',
'Irrigator': 'Functions : [
    on(),
    off(),
    startWatering(),
    setWaterPortion(portion: double [0 ~ 2000], unit: string {"liters"|"milliliters"|"gallons"|"ounces"})
]
Values : [
    switch: string {"on"|"off"}
]
Tags:[Garden,Greenhouse]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 11 and (#Clock).minute == 0) {
        if ((#Blind #Livingroom).blind == "closed") {
            if ((#Irrigator #Garden).switch == "on") {
                (#Irrigator #Garden).off()
            }
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn off the patio irrigation system at 11:00 AM if the bedroom blinds are closed.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags:[Bathroom,Bedroom]',
'Irrigator': 'Functions : [
    on(),
    off(),
    startWatering(),
    setWaterPortion(portion: double [0 ~ 2000], unit: string {"liters"|"milliliters"|"gallons"|"ounces"})
]
Values : [
    switch: string {"on"|"off"}
]
Tags:[Frontyard,Patio]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 11 and (#Clock).minute == 0) {
        if ((#Blind #Bedroom).blind == "closed") {
            if ((#Irrigator #Patio).switch == "on") {
                (#Irrigator #Patio).off()
            }
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn off the rooftop irrigation system at 11:00 AM if the diningroom blinds are closed.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags:[Library,Diningroom]',
'Irrigator': 'Functions : [
    on(),
    off(),
    startWatering(),
    setWaterPortion(portion: double [0 ~ 2000], unit: string {"liters"|"milliliters"|"gallons"|"ounces"})
]
Values : [
    switch: string {"on"|"off"}
]
Tags:[Terrace,Rooftop]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 11 and (#Clock).minute == 0) {
        if ((#Blind #Diningroom).blind == "closed") {
            if ((#Irrigator #Rooftop).switch == "on") {
                (#Irrigator #Rooftop).off()
            }
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Every 7 o'clock, the kitchen smoke detection status is announced through the speaker.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'SmokeDetector': 'Functions : []
Values : [
    smoke : string {"detected"|"not_detected"}
]
Tags:[LivingRoom,Kitchen]',
'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[Bedroom,Office]'}"""
    },
    {
        "from": "gpt",
        "value": """loop (1 MIN, (#Clock).hour == 7 and (#Clock).minute == 0) {
    if ((#Speaker).switch == "off") {
        (#Speaker).on()
    }
    if ((#SmokeDetector #Kitchen).smoke == "detected") {
        (#Speaker).speak("현재 연기가 감지되었습니다. 확인해주세요.")
    }
    if ((#SmokeDetector #Kitchen).smoke == "not_detected") {
        (#Speaker).speak("현재 연기가 감지되지 않았습니다.")
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Every 7 o'clock, the garage smoke detection status is announced through the speaker.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'SmokeDetector': 'Functions : []
Values : [
    smoke : string {"detected"|"not_detected"}
]
Tags:[Basement,Garage]',
'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[Kitchen,DiningRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop (1 MIN, (#Clock).hour == 7 and (#Clock).minute == 0) {
    if ((#Speaker).switch == "off") {
        (#Speaker).on()
    }
    if ((#SmokeDetector #Garage).smoke == "detected") {
        (#Speaker).speak("현재 연기가 감지되었습니다. 확인해주세요.")
    }
    if ((#SmokeDetector #Garage).smoke == "not_detected") {
        (#Speaker).speak("현재 연기가 감지되지 않았습니다.")
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Every 7 o'clock, the bathroom smoke detection status is announced through the speaker.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'SmokeDetector': 'Functions : []
Values : [
    smoke : string {"detected"|"not_detected"}
]
Tags:[Attic,Bathroom]',
'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[LivingRoom,Balcony]'}"""
    },
    {
        "from": "gpt",
        "value": """loop (1 MIN, (#Clock).hour == 7 and (#Clock).minute == 0) {
    if ((#Speaker).switch == "off") {
        (#Speaker).on()
    }
    if ((#SmokeDetector #Bathroom).smoke == "detected") {
        (#Speaker).speak("현재 연기가 감지되었습니다. 확인해주세요.")
    }
    if ((#SmokeDetector #Bathroom).smoke == "not_detected") {
        (#Speaker).speak("현재 연기가 감지되지 않았습니다.")
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Please close the basement gas valve.

Services: {'GasValve': 'Functions : [
    open(),
    close()
]
Values : [
    valve : string {"open"|"closed"}
]
Tags:[Basement,Kitchen]', 'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#GasValve #Basement).valve == "open") {
    (#GasValve #Basement).close()
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Please close the kitchen gas valve.

Services: {'GasValve': 'Functions : [
    open(),
    close()
]
Values : [
    valve : string {"open"|"closed"}
]
Tags:[LaundryRoom,Kitchen]', 'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#GasValve #Kitchen).valve == "open") {
    (#GasValve #Kitchen).close()
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Please close the outdoor gas valve.

Services: {'GasValve': 'Functions : [
    open(),
    close()
]
Values : [
    valve : string {"open"|"closed"}
]
Tags:[Garage,Outdoor]', 'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#GasValve #Outdoor).valve == "open") {
    (#GasValve #Outdoor).close()
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Set the livingroom television channel to 7 in 8 hours.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Television': 'Functions : [
    on(),
    off(),
    setTvChannel(tvChannel: int),
    channelUp(),
    channelDown(),
    setVolume(volume: int [0 ~ 100]),
    volumeUp(),
    volumeDown(),
    mute() : void, toggle muteStatus

Values : [
    switch : string {"on"|"off"}
    muteStatus : string {"muted"|"unmuted"}
    tvChannel : int
]
Tags:[LivingRoom,Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """wait until (8 HOUR)
if ((#Television #LivingRoom).switch == "off") {
    (#Television #LivingRoom).on()
}
(#Television #LivingRoom).setTVChannel(7)"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Set the bedroom television channel to 7 in 8 hours.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Television': 'Functions : [
    on(),
    off(),
    setTvChannel(tvChannel: int),
    channelUp(),
    channelDown(),
    setVolume(volume: int [0 ~ 100]),
    volumeUp(),
    volumeDown(),
    mute() : void, toggle muteStatus

Values : [
    switch : string {"on"|"off"}
    muteStatus : string {"muted"|"unmuted"}
    tvChannel : int
]
Tags:[GuestRoom,Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """wait until (8 HOUR)
if ((#Television #Bedroom).switch == "off") {
    (#Television #Bedroom).on()
}
(#Television #Bedroom).setTVChannel(7)"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Set the kitchen television channel to 7 in 8 hours.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Television': 'Functions : [
    on(),
    off(),
    setTvChannel(tvChannel: int),
    channelUp(),
    channelDown(),
    setVolume(volume: int [0 ~ 100]),
    volumeUp(),
    volumeDown(),
    mute() : void, toggle muteStatus

Values : [
    switch : string {"on"|"off"}
    muteStatus : string {"muted"|"unmuted"}
    tvChannel : int
]
Tags:[LivingRoom,Kitchen]'}"""
    },
    {
        "from": "gpt",
        "value": """wait until (8 HOUR)
if ((#Television #Kitchen).switch == "off") {
    (#Television #Kitchen).on()
}
(#Television #Kitchen).setTVChannel(7)"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the kitchen dishwasher if smoke is detected in the kitchen.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'SmokeDetector': 'Functions : []
Values : [
    smoke : string {"detected"|"not_detected"}
]
Tags:[Kitchen,Basement]', 'Dishwasher': 'Functions : [
    on(),
    off(),
    setDishwasherMode(mode: string {"eco"|"intense"|"auto"|"quick"|"rinse"|"dry"})
]
Values : [
    switch : string {"on"|"off"},
    dishwasherMode : string {"eco"|"intense"|"auto"|"quick"|"rinse"|"dry"}
]
Tags:[Kitchen,LaundryRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#SmokeDetector #Kitchen).smoke == "detected") {
        if ((#Dishwasher #Kitchen).switch == "off") {
            (#Dishwasher #Kitchen).on()
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn on the diningroom dishwasher if smoke is detected in the basement.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'SmokeDetector': 'Functions : []
Values : [
    smoke : string {"detected"|"not_detected"}
]
Tags:[LivingRoom,Basement]', 'Dishwasher': 'Functions : [
    on(),
    off(),
    setDishwasherMode(mode: string {"eco"|"intense"|"auto"|"quick"|"rinse"|"dry"})
]
Values : [
    switch : string {"on"|"off"},
    dishwasherMode : string {"eco"|"intense"|"auto"|"quick"|"rinse"|"dry"}
]
Tags:[Garage,DiningRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#SmokeDetector #Basement).smoke == "detected") {
        if ((#Dishwasher #DiningRoom).switch == "off") {
            (#Dishwasher #DiningRoom).on()
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the utilityroom dishwasher if smoke is detected in the garage.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'SmokeDetector': 'Functions : []
Values : [
    smoke : string {"detected"|"not_detected"}
]
Tags:[Workshop,Garage]', 'Dishwasher': 'Functions : [
    on(),
    off(),
    setDishwasherMode(mode: string {"eco"|"intense"|"auto"|"quick"|"rinse"|"dry"})
]
Values : [
    switch : string {"on"|"off"},
    dishwasherMode : string {"eco"|"intense"|"auto"|"quick"|"rinse"|"dry"}
]
Tags:[Bathroom,UtilityRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#SmokeDetector #Garage).smoke == "detected") {
        if ((#Dishwasher #UtilityRoom).switch == "off") {
            (#Dishwasher #UtilityRoom).on()
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Close the living room curtains completely.

Services: {
    'Clock': 'Functions : []
    Values : [
        day : int [1~31]
        hour : int [0~23]
        minute : int [0~59]
        month : int [1~12]
        second : int [0~59]
        weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
        year : int [0 ~ 100000]
        isHoliday : bool {true|false}
        timestamp : double : unixTime
    ]',
    'Curtain': 'Functions : [
        setCurtainLevel(level: int [0 ~ 100])
    ]
    Values : [
        curtain : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
        curtainLevel : int [0 ~ 100]
    ]
    Tags:[LivingRoom,Bedroom]'
}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Curtain #LivingRoom).curtainLevel > 0) {
    (#Curtain #LivingRoom).setCurtainLevel(0)
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Close the bedroom curtains completely.

Services: {
    'Clock': 'Functions : []
    Values : [
        day : int [1~31]
        hour : int [0~23]
        minute : int [0~59]
        month : int [1~12]
        second : int [0~59]
        weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
        year : int [0 ~ 100000]
        isHoliday : bool {true|false}
        timestamp : double : unixTime
    ]',
    'Curtain': 'Functions : [
        setCurtainLevel(level: int [0 ~ 100])
    ]
    Values : [
        curtain : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
        curtainLevel : int [0 ~ 100]
    ]
    Tags:[Office,Bedroom]'
}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Curtain #Bedroom).curtainLevel > 0) {
    (#Curtain #Bedroom).setCurtainLevel(0)
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Close the office curtains completely.

Services: {
    'Clock': 'Functions : []
    Values : [
        day : int [1~31]
        hour : int [0~23]
        minute : int [0~59]
        month : int [1~12]
        second : int [0~59]
        weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
        year : int [0 ~ 100000]
        isHoliday : bool {true|false}
        timestamp : double : unixTime
    ]',
    'Curtain': 'Functions : [
        setCurtainLevel(level: int [0 ~ 100])
    ]
    Values : [
        curtain : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
        curtainLevel : int [0 ~ 100]
    ]
    Tags:[Kitchen,Office]'
}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Curtain #Office).curtainLevel > 0) {
    (#Curtain #Office).setCurtainLevel(0)
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If the bedroom dehumidifier is in cooling mode at 8:00 PM, set it to finished mode.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Bedroom,Basement]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 20 and (#Clock).minute == 0) {
        if ((#Dehumidifier #Bedroom).dehumidifierMode == "cooling") {
            (#Dehumidifier #Bedroom).setDehumidifierMode("finished")
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: If the garage dehumidifier is in cooling mode at 8:00 PM, set it to finished mode.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Attic,Garage]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 20 and (#Clock).minute == 0) {
        if ((#Dehumidifier #Garage).dehumidifierMode == "cooling") {
            (#Dehumidifier #Garage).setDehumidifierMode("finished")
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If the bathroom dehumidifier is in cooling mode at 8:00 PM, set it to finished mode.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Closet,Bathroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 20 and (#Clock).minute == 0) {
        if ((#Dehumidifier #Bathroom).dehumidifierMode == "cooling") {
            (#Dehumidifier #Bathroom).setDehumidifierMode("finished")
        }
    }
}"""
    }
],
[
      {
        "from": "human",
        "value": """Input: Turn off the livingroom air conditioner at 11:30 PM on the last day of each month.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[LivingRoom,Bedroom]'}"""
      },
      {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).day == 31 and (#Clock).hour == 23 and (#Clock).minute == 30) {
        if ((#AirConditioner #LivingRoom).switch == "on") {
            (#AirConditioner #LivingRoom).off()
        }
    }
}""" # fix?
      }
]
,
[
      {
        "from": "human",
        "value": """Input: Turn off the office air conditioner at 11:30 PM on the last day of each month.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[Garage,Office]'}"""
      },
      {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).day == 31 and (#Clock).hour == 23 and (#Clock).minute == 30) {
        if ((#AirConditioner #Office).switch == "on") {
            (#AirConditioner #Office).off()
        }
    }
}"""
      }
]
,
[
      {
        "from": "human",
        "value": """Input: Turn off the diningroom air conditioner at 11:30 PM on the last day of each month.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirConditioner': 'Functions : [
    on(),
    off(),
    setTemperature(temperature: int),
    setAirConditionerMode(mode: string {"auto"|"cool"|"heat"})
]
Values : [
    switch : string {"on"|"off"},
    airConditionerMode : string {"auto"|"cool"|"heat"}
]
Tags:[Balcony,DiningRoom]'}"""
      },
      {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).day == 31 and (#Clock).hour == 23 and (#Clock).minute == 30) {
        if ((#AirConditioner #DiningRoom).switch == "on") {
            (#AirConditioner #DiningRoom).off()
        }
    }
}"""
      }
]
,
[
    {
        "from": "human",
        "value": """Input: Take time-lapse photos at 10x speed for 3 hours with the garden camera.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Camera': 'Functions : [
    on(),
    off(),
    take() : return binary : storage path for image(photo),
    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
]
Values : [
    switch : string {"on"|"off"},
    image : binary : the storage path for the most recent image(photo)
]
Tags:[Garden,Backyard]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Camera #Garden).switch == "off") {
    (#Camera #Garden).on()
}
(#Camera #Garden).takeTimelapse(3.0, 10.0)"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Take time-lapse photos at 10x speed for 3 hours with the parkinglot camera.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Camera': 'Functions : [
    on(),
    off(),
    take() : return binary : storage path for image(photo),
    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
]
Values : [
    switch : string {"on"|"off"},
    image : binary : the storage path for the most recent image(photo)
]
Tags:[Garage,ParkingLot]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Camera #ParkingLot).switch == "off") {
    (#Camera #ParkingLot).on()
}
(#Camera #ParkingLot).takeTimelapse(3.0, 10.0)"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Take time-lapse photos at 10x speed for 3 hours with the balcony camera.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Camera': 'Functions : [
    on(),
    off(),
    take() : return binary : storage path for image(photo),
    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
]
Values : [
    switch : string {"on"|"off"},
    image : binary : the storage path for the most recent image(photo)
]
Tags:[Roof,Balcony]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Camera #Balcony).switch == "off") {
    (#Camera #Balcony).on()
}
(#Camera #Balcony).takeTimelapse(3.0, 10.0)"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: If VOC level is below 0.03, turn on the livingroom camera and set the bedroom air purifier to low mode.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ ∞] : PM 10 dust level,
    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[Livingroom,Bedroom]', 'AirPurifier': 'Functions : [
    on(),
    off(),
    setAirPurifierFanMode(mode: string {"auto"|"sleep"|"low"|"medium"|"high"|"quiet"|"windFree"|"off"})
]
Values : [
    switch : string {"on"|"off"},
    airPurifierFanMode : string {"auto"|"sleep"|"low"|"medium"|"high"|"quiet"|"windFree"|"off"}
]
Tags:[Bedroom,Office]', 'Camera': 'Functions : [
    on(),
    off(),
    take() : return binary : storage path for image(photo),
    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
]
Values : [
    switch : string {"on"|"off"},
    image : binary : the storage path for the most recent image(photo)
]
Tags:[Livingroom,Basement]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector).tvocLevel < 0.03) {
        if ((#Camera #Livingroom).switch == "off") {
            (#Camera #Livingroom).on()
        }
        if ((#AirPurifier #Bedroom).airPurifierFanMode != "low") {
            (#AirPurifier #Bedroom).setPurifierFanMode("low")
        }
    }
}""" # fixed so that airqualitydetector has no tags
    }
]
,
[
    {
        "from": "human",
        "value": """Input: If VOC level is below 0.03, turn on the hallway camera and set the kitchen air purifier to low mode.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ ∞] : PM 10 dust level,
    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[Livingroom,Kitchen]', 'AirPurifier': 'Functions : [
    on(),
    off(),
    setAirPurifierFanMode(mode: string {"auto"|"sleep"|"low"|"medium"|"high"|"quiet"|"windFree"|"off"})
]
Values : [
    switch : string {"on"|"off"},
    airPurifierFanMode : string {"auto"|"sleep"|"low"|"medium"|"high"|"quiet"|"windFree"|"off"}
]
Tags:[Study,Kitchen]', 'Camera': 'Functions : [
    on(),
    off(),
    take() : return binary : storage path for image(photo),
    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
]
Values : [
    switch : string {"on"|"off"},
    image : binary : the storage path for the most recent image(photo)
]
Tags:[Garage,Hallway]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector).tvocLevel < 0.03) {
        if ((#Camera #Hallway).switch == "off") {
            (#Camera #Hallway).on()
        }
        if ((#AirPurifier #Kitchen).airPurifierFanMode != "low") {
            (#AirPurifier #Kitchen).setPurifierFanMode("low")
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: If VOC level is below 0.03, turn on the garage camera and set the office air purifier to low mode.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ ∞] : PM 10 dust level,
    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[Garage,Office]', 'AirPurifier': 'Functions : [
    on(),
    off(),
    setAirPurifierFanMode(mode: string {"auto"|"sleep"|"low"|"medium"|"high"|"quiet"|"windFree"|"off"})
]
Values : [
    switch : string {"on"|"off"},
    airPurifierFanMode : string {"auto"|"sleep"|"low"|"medium"|"high"|"quiet"|"windFree"|"off"}
]
Tags:[Livingroom,Office]', 'Camera': 'Functions : [
    on(),
    off(),
    take() : return binary : storage path for image(photo),
    takeTimelapse(duration: double [0 ~ ∞], speed: double [0 ~ ∞]) : return binary : storage path for timelapse
]
Values : [
    switch : string {"on"|"off"},
    image : binary : the storage path for the most recent image(photo)
]
Tags:[Bedroom,Garage]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector).tvocLevel < 0.03) {
        if ((#Camera #Garage).switch == "off") {
            (#Camera #Garage).on()
        }
        if ((#AirPurifier #Office).airPurifierFanMode != "low") {
            (#AirPurifier #Office).setPurifierFanMode("low")
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Set the livingroom blinds to 40% if humidity in the basement is below 40%.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []',

'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags: [LivingRoom,Bedroom]',

'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ \u221e] : PM 10 dust level,
    fineDustLevel : int [0 ~ \u221e] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ \u221e] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags: [Basement,Kitchen]'}
"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector #Basement).humidity < 40) {
        (#Blind #LivingRoom).setBlindLevel(40)
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Set the office blinds to 40% if humidity in the attic is below 40%.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []',

'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags: [Library,Office]',

'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ \u221e] : PM 10 dust level,
    fineDustLevel : int [0 ~ \u221e] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ \u221e] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags: [Basement,Attic]'}
"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector #Attic).humidity < 40) {
        (#Blind #Office).setBlindLevel(40)
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Set the kitchen blinds to 40% if humidity in the bathroom is below 40%.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0 ~ 59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []',

'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags: [DiningRoom,Kitchen]',

'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ \u221e] : PM 10 dust level,
    fineDustLevel : int [0 ~ \u221e] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ \u221e] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags: [LaundryRoom,Bathroom]'}
"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector #Bathroom).humidity < 40) {
        (#Blind #Kitchen).setBlindLevel(40)
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: If the bedroom blinds are partially open, close them completely.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags:[Bedroom,LivingRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Blind #Bedroom).blind == "partially") {
    (#Blind #Bedroom).setBlindLevel(0)
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: If the kitchen blinds are partially open, close them completely.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags:[DiningRoom,Kitchen]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Blind #Kitchen).blind == "partially") {
    (#Blind #Kitchen).setBlindLevel(0)
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: If the office blinds are partially open, close them completely.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags:[Library,Office]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Blind #Office).blind == "partially") {
    (#Blind #Office).setBlindLevel(0)
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn off the basement dehumidifier at 11:00 PM if the living room light is on.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Basement]',
'Light': 'Functions : [
    on(),
    off(),
    setColor(color: string {"{hue}|{saturation}|{brightness}"})
    setLevel(level int [0 ~ 100])
]
Values : [
    switch : string {"on"|"off"},
    light : double
]
Tags:[LivingRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 23 and (#Clock).minute == 0) {
        if ((#Light #LivingRoom).switch == "on") {
            if ((#Dehumidifier #Basement).switch == "on") {
                (#Dehumidifier #Basement).off()
            }
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn off the bathroom dehumidifier at 11:00 PM if the kitchen light is on.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Bathroom]',
'Light': 'Functions : [
    on(),
    off(),
    setColor(color: string {"{hue}|{saturation}|{brightness}"})
    setLevel(level int [0 ~ 100])
]
Values : [
    switch : string {"on"|"off"},
    light : double
]
Tags:[Kitchen]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 23 and (#Clock).minute == 0) {
        if ((#Light #Kitchen).switch == "on") {
            if ((#Dehumidifier #Bathroom).switch == "on") {
                (#Dehumidifier #Bathroom).off()
            }
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn off the garage dehumidifier at 11:00 PM if the bedroom light is on.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]',
'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Garage]',
'Light': 'Functions : [
    on(),
    off(),
    setColor(color: string {"{hue}|{saturation}|{brightness}"})
    setLevel(level int [0 ~ 100])
]
Values : [
    switch : string {"on"|"off"},
    light : double
]
Tags:[Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 23 and (#Clock).minute == 0) {
        if ((#Light #Bedroom).switch == "on") {
            if ((#Dehumidifier #Garage).switch == "on") {
                (#Dehumidifier #Garage).off()
            }
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Please tell me the lunch menu at the dormitory cafeteria tomorrow by livingroom speaker.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'MenuProvider': 'Functions : [
    menu(command: string) : command format {"{\uc624\ub298|\ub0b4\uc77c} {\ud559\uc0dd\uc2dd\ub2f9|\uc218\uc758\ub300\uc2dd\ub2f9|\uc804\ub9dd\ub300(3\uc2dd\ub2f9)|\uc608\uc220\uacc4\uc2dd\ub2f9(\uc544\ub984\ub4dc\ub9ac\ub9ac)|\uae30\uc219\uc0ac\uc2dd\ub2f9|\uc544\uc6cc\ud648|\ub3d9\uc6d0\uad00\uc2dd\ub2f9(113\ub3d9)|\uc6f0\uc2a4\ud1a0\ub9ac(220\ub3d9)|\ud22c\uad7f(\uacf5\ub300\uac04\uc774\uc2dd\ub2f9)|\uc790\ud558\uc5f0\uc2dd\ub2f9|301\ub3d9\uc2dd\ub2f9} {\uc544\uce68|\uc810\uc2ec|\uc800\ub141}"}
    todayMenu()
]
Values : []
Tags:[]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[LivingRoom,Office]'}"""
    },
    {
        "from": "gpt",
        "value": """menu_info = (#MenuProvider).menu("내일 기숙사식당 점심")
if ((#Speaker #LivingRoom).switch == "off") {
    (#Speaker #LivingRoom).on()
}
(#Speaker #LivingRoom).speak(menu_info)"""
    }
] # to check
,
[
    {
        "from": "human",
        "value": """Input: Please tell me the lunch menu at the dormitory cafeteria tomorrow by bedroom speaker.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'MenuProvider': 'Functions : [
    menu(command: string) : command format {"{\uc624\ub298|\ub0b4\uc77c} {\ud559\uc0dd\uc2dd\ub2f9|\uc218\uc758\ub300\uc2dd\ub2f9|\uc804\ub9dd\ub300(3\uc2dd\ub2f9)|\uc608\uc220\uacc4\uc2dd\ub2f9(\uc544\ub984\ub4dc\ub9ac\ub9ac)|\uae30\uc219\uc0ac\uc2dd\ub2f9|\uc544\uc6cc\ud648|\ub3d9\uc6d0\uad00\uc2dd\ub2f9(113\ub3d9)|\uc6f0\uc2a4\ud1a0\ub9ac(220\ub3d9)|\ud22c\uad7f(\uacf5\ub300\uac04\uc774\uc2dd\ub2f9)|\uc790\ud558\uc5f0\uc2dd\ub2f9|301\ub3d9\uc2dd\ub2f9} {\uc544\uce68|\uc810\uc2ec|\uc800\ub141}"}
    todayMenu()
]
Values : []
Tags:[Kitchen,Cafeteria]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[]'}"""
    },
    {
        "from": "gpt",
        "value": """menu_info = (#MenuProvider).menu("내일 기숙사식당 점심")
if ((#Speaker #Bedroom).switch == "off") {
    (#Speaker #Bedroom).on()
}
(#Speaker #Bedroom).speak(menu_info)"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Please tell me the lunch menu at the dormitory cafeteria tomorrow by dormroom speaker.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'MenuProvider': 'Functions : [
    menu(command: string) : command format {"{\uc624\ub298|\ub0b4\uc77c} {\ud559\uc0dd\uc2dd\ub2f9|\uc218\uc758\ub300\uc2dd\ub2f9|\uc804\ub9dd\ub300(3\uc2dd\ub2f9)|\uc608\uc220\uacc4\uc2dd\ub2f9(\uc544\ub984\ub4dc\ub9ac\ub9ac)|\uae30\uc219\uc0ac\uc2dd\ub2f9|\uc544\uc6cc\ud648|\ub3d9\uc6d0\uad00\uc2dd\ub2f9(113\ub3d9)|\uc6f0\uc2a4\ud1a0\ub9ac(220\ub3d9)|\ud22c\uad7f(\uacf5\ub300\uac04\uc774\uc2dd\ub2f9)|\uc790\ud558\uc5f0\uc2dd\ub2f9|301\ub3d9\uc2dd\ub2f9} {\uc544\uce68|\uc810\uc2ec|\uc800\ub141}"}
    todayMenu()
]
Values : []
Tags:[]', 'Speaker': 'Functions : [
    on(),
    off(),
    pause(),
    stop(),
    play(source: string),
    speak(text: string)
]
Values : [
    switch : string {"on"|"off"},
    playbackStatus : string {"paused"|"playing"|"stopped"|"fast"|"rewinding"|"buffering"}
]
Tags:[DormRoom,Library]'}"""
    },
    {
        "from": "gpt",
        "value": """menu_info = (#MenuProvider).menu("내일 기숙사식당 점심")
if ((#Speaker #DormRoom).switch == "off") {
    (#Speaker #DormRoom).on()
}
(#Speaker #DormRoom).speak(menu_info)"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn on the basement dehumidifier and set it to internalCare mode at 5:00 PM.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Basement,LivingRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 17 and (#Clock).minute == 0) {
        if ((#Dehumidifier #Basement).switch == "off") {
            (#Dehumidifier #Basement).on()
        }
        if ((#Dehumidifier #Basement).dehumidifierMode != "internalCare") {
            (#Dehumidifier #Basement).setDehumidifierMode("internalCare")
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn on the garage dehumidifier and set it to internalCare mode at 5:00 PM.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Bathroom,Garage]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 17 and (#Clock).minute == 0) {
        if ((#Dehumidifier #Garage).switch == "off") {
            (#Dehumidifier #Garage).on()
        }
        if ((#Dehumidifier #Garage).dehumidifierMode != "internalCare") {
            (#Dehumidifier #Garage).setDehumidifierMode("internalCare")
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn on the bathroom dehumidifier and set it to internalCare mode at 5:00 PM.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Attic,Bathroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 17 and (#Clock).minute == 0) {
        if ((#Dehumidifier #Bathroom).switch == "off") {
            (#Dehumidifier #Bathroom).on()
        }
        if ((#Dehumidifier #Bathroom).dehumidifierMode != "internalCare") {
            (#Dehumidifier #Bathroom).setDehumidifierMode("internalCare")
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Set the bedroom dehumidifier to AIDrying mode at 7:00 PM if the CO2 level in the livingroom is above 600 ppm.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ ∞] : PM 10 dust level,
    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[Livingroom]', 'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 19 and (#Clock).minute == 0) {
        if ((#AirQualityDetector #Livingroom).carbonDioxide > 600.0) {
            if ((#Dehumidifier #Bedroom).switch == "off") {
                (#Dehumidifier #Bedroom).on()
            }
            if ((#Dehumidifier #Bedroom).dehumidifierMode != "AIDrying") {
                (#Dehumidifier #Bedroom).setDehumidifierMode("AIDrying")
            }
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Set the office dehumidifier to AIDrying mode at 7:00 PM if the CO2 level in the kitchen is above 600 ppm.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ ∞] : PM 10 dust level,
    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[Kitchen]', 'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Office]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 19 and (#Clock).minute == 0) {
        if ((#AirQualityDetector #Kitchen).carbonDioxide > 600.0) {
            if ((#Dehumidifier #Office).switch == "off") {
                (#Dehumidifier #Office).on()
            }
            if ((#Dehumidifier #Office).dehumidifierMode != "AIDrying") {
                (#Dehumidifier #Office).setDehumidifierMode("AIDrying")
            }
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Set the basement dehumidifier to AIDrying mode at 7:00 PM if the CO2 level in the diningroom is above 600 ppm.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ ∞] : PM 10 dust level,
    fineDustLevel : int [0 ~ ∞] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ ∞] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[Diningroom]', 'Dehumidifier': 'Functions : [
    on(),
    off(),
    setDehumidifierMode(mode: string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"})
]
Values : [
    switch : string {"on"|"off"},
    dehumidifierMode : string {"cooling"|"delayWash"|"drying"|"finished"|"refreshing"|"weightSensing"|"wrinklePrevent"|"dehumidifying"|"AIDrying"|"sanitizing"|"internalCare"|"freezeProtection"|"continuousDehumidifying"|"thawingFrozenInside"}
]
Tags:[Basement]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 19 and (#Clock).minute == 0) {
        if ((#AirQualityDetector #Diningroom).carbonDioxide > 600.0) {
            if ((#Dehumidifier #Basement).switch == "off") {
                (#Dehumidifier #Basement).on()
            }
            if ((#Dehumidifier #Basement).dehumidifierMode != "AIDrying") {
                (#Dehumidifier #Basement).setDehumidifierMode("AIDrying")
            }
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn on the livingroom light and set it to blue color at 9:00 PM on weekends.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Light': 'Functions : [
    on(),
    off(),
    setColor(color: string {"{hue}|{saturation}|{brightness}"})
    setLevel(level int [0 ~ 100])
]
Values : [
    switch : string {"on"|"off"},
    light : double
]
Tags:[Livingroom,Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).weekday == "saturday" or (#Clock).weekday == "sunday") {
        if ((#Clock).hour == 21 and (#Clock).minute == 0) {
            if ((#Light #Livingroom).switch == "off") {
                all(#Light #Livingroom).on()
            }
            all(#Light #Livingroom).setColor("240|100|100")
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the kitchen light and set it to blue color at 9:00 PM on weekends.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Light': 'Functions : [
    on(),
    off(),
    setColor(color: string {"{hue}|{saturation}|{brightness}"})
    setLevel(level int [0 ~ 100])
]
Values : [
    switch : string {"on"|"off"},
    light : double
]
Tags:[Livingroom,Kitchen,Hallway]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).weekday == "saturday" or (#Clock).weekday == "sunday") {
        if ((#Clock).hour == 21 and (#Clock).minute == 0) {
            if (any(#Light #Kitchen).switch != "on") {
                all(#Light #Kitchen).on()
            }
            all(#Light #Kitchen).setColor("240|100|100")
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn on the bedroom light and set it to blue color at 9:00 PM on weekends.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'Light': 'Functions : [
    on(),
    off(),
    setColor(color: string {"{hue}|{saturation}|{brightness}"})
    setLevel(level int [0 ~ 100])
]
Values : [
    switch : string {"on"|"off"},
    light : double
]
Tags:[Kitchen,Bedroom,Bathroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).weekday == "saturday" or (#Clock).weekday == "sunday") {
        if ((#Clock).hour == 21 and (#Clock).minute == 0) {
            if (any(#Light #Bedroom).switch != "on") {
                all(#Light #Bedroom).on()
            }
            all(#Light #Bedroom).setColor("240|100|100")
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Please turn on the livingroom television.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Television': 'Functions : [\n    on(),\n\toff(),\n\tsetTvChannel(tvChannel: int),\n\tchannelUp(),\n\tchannelDown(),\n    setVolume(volume: int [0 ~ 100]),\n    volumeUp(),\n    volumeDown(),\n\tmute() : void, toggle muteStatus\n\nValues : [\n\tswitch : string {"on"|"off"}\n\tmuteStatus : string {"muted"|"unmuted"}\n\ttvChannel : int\n]\nTags:[LivingRoom,Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Television #Livingroom).switch == "off") {\n\t(#Television #Livingroom).on()\n}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Please turn on the bedroom television.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Television': 'Functions : [\n    on(),\n\toff(),\n\tsetTvChannel(tvChannel: int),\n\tchannelUp(),\n\tchannelDown(),\n    setVolume(volume: int [0 ~ 100]),\n    volumeUp(),\n    volumeDown(),\n\tmute() : void, toggle muteStatus\n\nValues : [\n\tswitch : string {"on"|"off"}\n\tmuteStatus : string {"muted"|"unmuted"}\n\ttvChannel : int\n]\nTags:[Livingroom,Bedroom,GuestRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Television #Bedroom).switch == "off") {\n\t(#Television #Bedroom).on()\n}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Please turn on the kitchen television.\n\nServices: {'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]', 'Television': 'Functions : [\n    on(),\n\toff(),\n\tsetTvChannel(tvChannel: int),\n\tchannelUp(),\n\tchannelDown(),\n    setVolume(volume: int [0 ~ 100]),\n    volumeUp(),\n    volumeDown(),\n\tmute() : void, toggle muteStatus\n\nValues : [\n\tswitch : string {"on"|"off"}\n\tmuteStatus : string {"muted"|"unmuted"}\n\ttvChannel : int\n]\nTags:[Bedroom,Guestroom,Kitchen, DiningRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#Television #Kitchen).switch == "off") {\n\t(#Television #Kitchen).on()\n}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Set the kitchen dishwasher to eco mode at 6:00 PM if the VOC level in the living room is below 0.05.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ \u221e] : PM 10 dust level,
    fineDustLevel : int [0 ~ \u221e] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ \u221e] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[LivingRoom]', 'Dishwasher': 'Functions : [
    on(),
    off(),
    setDishwasherMode(mode: string {"eco"|"intense"|"auto"|"quick"|"rinse"|"dry"})
]
Values : [
    switch : string {"on"|"off"},
    dishwasherMode : string {"eco"|"intense"|"auto"|"quick"|"rinse"|"dry"}
]
Tags:[Kitchen]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 18 and (#Clock).minute == 0) {
        if ((#AirQualityDetector #LivingRoom).tvocLevel < 0.05) {
            if ((#Dishwasher #Kitchen).switch == "off") {
                (#Dishwasher #Kitchen).on()
            }
            if ((#Dishwasher #Kitchen).dishwasherMode != "eco") {
                (#Dishwasher #Kitchen).setDishwaherMode("eco")
            }
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Set the office dishwasher to eco mode at 6:00 PM if the VOC level in the hallway is below 0.05.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ \u221e] : PM 10 dust level,
    fineDustLevel : int [0 ~ \u221e] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ \u221e] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[Livingroom,Basement,Hallway]', 'Dishwasher': 'Functions : [
    on(),
    off(),
    setDishwasherMode(mode: string {"eco"|"intense"|"auto"|"quick"|"rinse"|"dry"})
]
Values : [
    switch : string {"on"|"off"},
    dishwasherMode : string {"eco"|"intense"|"auto"|"quick"|"rinse"|"dry"}
]
Tags:[Livingroom,Kitchen,Office]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 18 and (#Clock).minute == 0) {
        if ((#AirQualityDetector #Hallway).tvocLevel < 0.05) {
            if ((#Dishwasher #Office).switch == "off") {
                (#Dishwasher #Office).on()
            }
            if ((#Dishwasher #Office).dishwasherMode != "eco") {
                (#Dishwasher #Office).setDishwaherMode("eco")
            }
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Set the basement dishwasher to eco mode at 6:00 PM if the VOC level in the garage is below 0.05.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ \u221e] : PM 10 dust level,
    fineDustLevel : int [0 ~ \u221e] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ \u221e] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags:[Garage]', 'Dishwasher': 'Functions : [
    on(),
    off(),
    setDishwasherMode(mode: string {"eco"|"intense"|"auto"|"quick"|"rinse"|"dry"})
]
Values : [
    switch : string {"on"|"off"},
    dishwasherMode : string {"eco"|"intense"|"auto"|"quick"|"rinse"|"dry"}
]
Tags:[Basement]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#Clock).hour == 18 and (#Clock).minute == 0) {
        if ((#AirQualityDetector #Garage).tvocLevel < 0.05) {
            if ((#Dishwasher #Basement).switch == "off") {
                (#Dishwasher #Basement).on()
            }
            if ((#Dishwasher #Basement).dishwasherMode != "eco") {
                (#Dishwasher #Basement).setDishwaherMode("eco")
            }
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Open all the livingroom window every day at 5pm if the weather is clear.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'WeatherProvider': 'Functions : [
    getWeatherInfo(double latitude, double longitude): return string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"}
]
Values : [
    weather : string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"},
    temperature : int celcius,
    humidity : double,
    pressure : double
]
Tags:[]', 'Window': 'Functions : [
    open(),
    close()
]
Values : [
    window : string {"closed"|"open"}
]
Tags:[LivingRoom,Bedroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN){
    if((#Clock).hour == 17 and (#Clock).minute == 0){
        if((#WeatherProvider).weather == "clear"){
            if(all(#Window #LivingRoom).window != "open"){
                all(#Window #LivingRoom).open()
            }
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Open the bedroom window every day at 5pm if the weather is clear.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'WeatherProvider': 'Functions : [
    getWeatherInfo(double latitude, double longitude): return string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"}
]
Values : [
    weather : string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"},
    temperature : int celcius,
    humidity : double,
    pressure : double
]
Tags:[]', 'Window': 'Functions : [
    open(),
    close()
]
Values : [
    window : string {"closed"|"open"}
]
Tags:[Kitchen,Livingroom,Bedroom,Bathroom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN){
    if((#Clock).hour == 17 and (#Clock).minute == 0){
        if((#WeatherProvider).weather == "clear"){
            if(any(#Window #Bedroom).window != "open"){
                all(#Window #Bedroom).open()
            }
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Open a kitchen window every day at 5pm if the weather is clear.

Services: {'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags:[]', 'WeatherProvider': 'Functions : [
    getWeatherInfo(double latitude, double longitude): return string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"}
]
Values : [
    weather : string {"thunderstorm"|"drizzle"|"rain"|"snow"|"mist"|"smoke"|"haze"|"dust"|"fog"|"sand"|"ash"|"squall"|"tornado"|"clear"|"clouds"},
    temperature : int celcius,
    humidity : double,
    pressure : double
]
Tags:[]', 'Window': 'Functions : [
    open(),
    close()
]
Values : [
    window : string {"closed"|"open"}
]
Tags:[Basement,Livingroom,Kitchen,DiningRoom]'}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN){
    if((#Clock).hour == 17 and (#Clock).minute == 0){
        if((#WeatherProvider).weather == "clear"){
            if((#Window #Kitchen).window != "open"){
                (#Window #Kitchen).open()
            }
        }
    }
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn off the smart plug in the living room.\n\nServices: {'SmartPlug': 'Functions : [\n    on(),\n\toff()\n]\nValues : [\n\tswitch : string {"on"|"off"},\n    chargingState : string {"charging"|"discharging"|"stopped"|"fullyCharged"|"error"},\n    voltage : double,\n    current : double\n]\nTags:[LivingRoom,Bedroom,Kitchen]', 'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#SmartPlug #LivingRoom).switch == "on") {
    (#SmartPlug #LivingRoom).off()
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: Turn off the smart plug in the garage.\n\nServices: {'SmartPlug': 'Functions : [\n    on(),\n\toff()\n]\nValues : [\n\tswitch : string {"on"|"off"},\n    chargingState : string {"charging"|"discharging"|"stopped"|"fullyCharged"|"error"},\n    voltage : double,\n    current : double\n]\nTags:[Basement,Garage,Workshop]', 'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#SmartPlug #Garage).switch == "on") {
    (#SmartPlug #Garage).off()
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: Turn off the smart plug in the office.\n\nServices: {'SmartPlug': 'Functions : [\n    on(),\n\toff()\n]\nValues : [\n\tswitch : string {"on"|"off"},\n    chargingState : string {"charging"|"discharging"|"stopped"|"fullyCharged"|"error"},\n    voltage : double,\n    current : double\n]\nTags:[Kitchen,Office,Study]', 'Clock': 'Functions : []\nValues : [\n    day : int [1~31]\n    hour : int [0~23]\n    minute : int [0~59]\n    month : int [1~12]\n    second : int [0~59]\n    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}\n    year : int [0 ~ 100000]\n    isHoliday : bool {true|false}\n    timestamp : double : unixTime\n]\nTags:[]'}"""
    },
    {
        "from": "gpt",
        "value": """if ((#SmartPlug #Office).switch == "on") {
    (#SmartPlug #Office).off()
}"""
    }
],
[
    {
        "from": "human",
        "value": """Input: If PM 10 level is above 150 and VOC level is above 0.1, set the livingroom blinds to 80%. If CO2 level is below 400 ppm, set the bedroom blinds to 0%.

Services: {
'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []',

'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags: [LivingRoom,Bedroom]',

'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ \u221e] : PM 10 dust level,
    fineDustLevel : int [0 ~ \u221e] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ \u221e] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags: [Kitchen,Office]'
}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector).dustLevel > 150.0 and (#AirQualityDetector).tvocLevel > 0.1) {
        if ((#Blind #LivingRoom).blindLevel != 80) {
            (#Blind #LivingRoom).setBlindLevel(80)
        }
    }
    if ((#AirQualityDetector).carbonDioxide < 400.0) {
        if ((#Blind #Bedroom).blindLevel != 0) {
            (#Blind #Bedroom).setBlindLevel(0)
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: If PM 10 level is above 150 and VOC level is above 0.1, set the office blinds to 80%. If CO2 level is below 400 ppm, set the kitchen blinds to 0%.

Services: {
'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []',

'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags: [Office,Kitchen]',

'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ \u221e] : PM 10 dust level,
    fineDustLevel : int [0 ~ \u221e] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ \u221e] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags: [LivingRoom,Bedroom]'
}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector).dustLevel > 150.0 and (#AirQualityDetector).tvocLevel > 0.1) {
        if ((#Blind #Office).blindLevel != 80) {
            (#Blind #Office).setBlindLevel(80)
        }
    }
    if ((#AirQualityDetector).carbonDioxide < 400.0) {
        if ((#Blind #Kitchen).blindLevel != 0) {
            (#Blind #Kitchen).setBlindLevel(0)
        }
    }
}"""
    }
]
,
[
    {
        "from": "human",
        "value": """Input: If PM 10 level is above 150 and VOC level is above 0.1, set the basement blinds to 80%. If CO2 level is below 400 ppm, set the attic blinds to 0%.

Services: {
'Clock': 'Functions : []
Values : [
    day : int [1~31]
    hour : int [0~23]
    minute : int [0~59]
    month : int [1~12]
    second : int [0~59]
    weekday : string {"monday"|"tuesday"|"wednesday"|"thursday"|"friday"|"saturday"|"sunday"}
    year : int [0 ~ 100000]
    isHoliday : bool {true|false}
    timestamp : double : unixTime
]
Tags: []',

'Blind': 'Functions : [
    setBlindLevel(level: int [0 ~ 100])
]
Values : [
    blind : string {"closed"|"closing"|"open"|"opening"|"partially"|"paused"|"unknown"},
    blindLevel : int [0 ~ 100]
]
Tags: [Basement,Attic]',

'AirQualityDetector': 'Functions : []
Values : [
    dustLevel : int [0 ~ \u221e] : PM 10 dust level,
    fineDustLevel : int [0 ~ \u221e] : PM 2.5 finedust level,
    veryFineDustLevel : int [0 ~ \u221e] : PM 1.0 finedust level,
    carbonDioxide : double : CO2 level,
    temperature : int [-460 ~ 10000],
    humidity : double [0 ~ 100],
    tvocLevel : double [0 ~ 1000000] : inert gas concentration
]
Tags: [Garage,Bathroom]'
}"""
    },
    {
        "from": "gpt",
        "value": """loop(1 MIN) {
    if ((#AirQualityDetector).dustLevel > 150.0 and (#AirQualityDetector).tvocLevel > 0.1) {
        if ((#Blind #Basement).blindLevel != 80) {
            (#Blind #Basement).setBlindLevel(80)
        }
    }
    if ((#AirQualityDetector).carbonDioxide < 400.0) {
        if ((#Blind #Attic).blindLevel != 0) {
            (#Blind #Attic).setBlindLevel(0)
        }
    }
}"""
    }
]


]
