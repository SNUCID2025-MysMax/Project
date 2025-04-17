grammar = '''
SoPLang Grammar Specification
-------------------------------------------------------------------------------

1. Lexical Rules (Token Definitions)
-------------------------------------
Literals:
  - Integer:             [+-]?[0-9]+              => INTEGER
  - Floating-point:      [-+]?([0-9]*\.[0-9]+|[0-9]+) => DOUBLE
  - String literal:      ".*?"                    => STRING_LITERAL
  - Identifier:          [a-zA-Z][_a-zA-Z0-9]*    => IDENTIFIER

Keywords:
  "wait until" => WAIT_UNTIL
  "loop"       => LOOP
  "if"         => IF
  "else"       => ELSE
  "not"        => NOT
  "all"        => ALL
  "or"         => OR
  "and"        => AND

Operators and Punctuation:
  >=  => GE        <= => LE        == => EQ         != => NE
   =  => ASSIGN     : => COLON      , => COMMA       ; => SEMICOLON
   [  => LBRACKET   ] => RBRACKET   . => DOT         # => HASH
   +  => PLUS       - => MINUS      * => MULT        / => DIV

Time Units:
  MSEC, SEC, MIN, HOUR, DAY

Line Terminators and Comments:
  // comment until newline
  "\n", "\r\n" as line breaks


2. Grammar Rules (BNF-style)
-----------------------------

scenario            ::= statement_list

statement_list      ::= statement
                      | statement blank statement_list

statement           ::= action_behavior
                      | if_statement
                      | loop_statement
                      | wait_statement
                      | compound_statement

compound_statement  ::= '{' blank statement_list blank '}'

action_behavior     ::= function_call
                      | value_read
                      | function_call_with_output

function_call       ::= '(' device_id ')' DOT skill_function_name '(' argument_list ')'
value_read          ::= '(' device_id ')' DOT skill_value_name
function_call_with_output ::= IDENTIFIER ASSIGN '(' device_id ')' DOT skill_function_name '(' argument_list ')'

device_id        ::= HASH IDENTIFIER        
device_id_list   ::= device_id

skill_function_name ::= IDENTIFIER UNDERSCORE IDENTIFIER    // e.g., airConditionerMode_setAirConditionerMode
skill_value_name    ::= IDENTIFIER UNDERSCORE IDENTIFIER    // e.g., airConditionerMode_airConditionerMode

argument_list       ::= empty
                      | argument
                      | argument_list blank COMMA blank argument

argument            ::= primary_expression

primary_expression  ::= IDENTIFIER
                      | INTEGER
                      | DOUBLE
                      | STRING_LITERAL
                      | STRING_LITERAL PLUS STRING_LITERAL

if_statement        ::= IF '(' condition_list ')' blank statement blank else_clause
else_clause         ::= empty
                      | ELSE blank statement

condition_list      ::= condition
                      | '(' condition_list ')'
                      | condition_list blank OR blank condition_list
                      | condition_list blank AND blank condition_list
                      | NOT condition blank

condition           ::= '(' device_id ')' DOT skill_function_name '(' ')' EQ expression_value
                      | '(' device_id ')' DOT skill_value_name comparison_operator expression_value

expression_value    ::= INTEGER | DOUBLE | STRING_LITERAL | IDENTIFIER

comparison_operator ::= EQ | NE | GE | LE | '>' | '<'

loop_statement      ::= LOOP '(' loop_condition ')' blank statement
loop_condition      ::= empty
                      | period_time COMMA condition_list
                      | period_time
                      | condition_list

period_time         ::= INTEGER time_unit
time_unit           ::= MSEC | SEC | MIN | HOUR | DAY

wait_statement      ::= WAIT_UNTIL '(' condition_list ')'
                      | WAIT_UNTIL '(' period_time ')'


3. Semantic Notes
------------------

- All service accesses use full skill prefix: skill_function_name = skillId_functionId
- Value reads must use full skill prefix: skill_value_name = skillId_valueId
- Action calls cannot be assigned to variables unless explicitly allowed (e.g., output assignment is only syntactic, not semantic unless device allows).
- No arbitrary assignment like `x = (#Device).skill_value` is permitted.
- No method chaining; only one function/value call per action.
- Concatenation is allowed in argument expressions: "a" + "b"
- Output device like Speaker must be used explicitly to produce output: e.g., `(#Speaker).speak("a" + "b")`

4. Example Usage
-----------------

Valid:
  (#AirConditioner).airConditionerMode_setAirConditionerMode("auto")
  (#AirConditioner).airConditionerMode_setTemperature(26)
  (#Speaker).speak("현재 온도는 " + "26도입니다")
  loop(5000 MSEC, (#Button).buttonStatus_isPressed()) { (#Light).lightControl_blink("green") }

Invalid:
  x = (#AirConditioner).airConditionerMode_airConditionerMode       // assignment not allowed
  (#Device).skillId.functionId()                                     // wrong format
  (#Speaker).speak("온도: " + (#Sensor).temperature_getValue())      // function call as expression not allowed

'''

services = r'''
{
  "AirConditioner": {
    "skills": [
      {
        "info": "Allows for the control of the air conditioner.",
        "val": {
          "airConditionerMode": {
            "info": "Current mode of the air conditioner",
            "type": "ENUM",
            "format": "airConditionerModeEnum"
          },
          "supportedAcModes": {
            "info": "Supported states for this air conditioner to be in",
            "type": "LIST",
            "format": "list[airConditionerModeEnum]"
          },
          "targetTemperature": {
            "info": "Current temperature status of the air conditioner",
            "type": "INTEGER"
          }
        },
        "fun": {
          "setAirConditionerMode": {
            "info": "Set the air conditioner mode",
            "args": {
              "mode": {
                "info": "Set the air conditioner mode",
                "type": "ENUM",
                "format": "airConditionerModeEnum"
              }
            },
            "ret": "VOID"
          },
          "setTemperature": {
            "info": "Set the air conditioner temperature",
            "args": {
              "temperature": {
                "info": "Set the air conditioner temperature",
                "type": "INTEGER"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {
          "airConditionerModeEnum": {
            "auto": "The fan is on auto",
            "cool": "The fan is in sleep mode to reduce noise",
            "heat": "The fan is on low"
          }
        }
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "AirPurifier": {
    "skills": [
      {
        "info": "Maintains and sets the state of an air purifier's fan",
        "val": {
          "airPurifierFanMode": {
            "info": "The current mode of the air purifier fan, an enum of auto, low, medium, high, sleep, quiet or windFree",
            "type": "ENUM",
            "format": "airPurifierFanModeEnum"
          },
          "supportedAirPurifierFanModes": {
            "info": "Supported states for this air purifier fan to be in",
            "type": "LIST",
            "format": "list[airPurifierFanModeEnum]"
          }
        },
        "fun": {
          "setAirPurifierFanMode": {
            "info": "Set the air purifier fan's mode",
            "args": {
              "mode": {
                "info": "Set the air purifier fan's mode",
                "type": "ENUM",
                "format": "airPurifierFanModeEnum"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {
          "airPurifierFanModeEnum": {
            "auto": "The fan is on auto",
            "sleep": "The fan is in sleep mode to reduce noise",
            "low": "The fan is on low",
            "medium": "The fan is on medium",
            "high": "The fan is on high",
            "quiet": "The fan is on quiet mode to reduce noise",
            "windFree": "The fan is on wind free mode to reduce the feeling of cold air",
            "off": "The fan is off"
          }
        }
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "AirQualityDetector": {
    "skills": [
      {
        "info": "Measure total volatile organic compound levels",
        "val": {
          "tvocLevel": {
            "info": "The level of total volatile organic compounds detected",
            "type": "DOUBLE"
          }
        },
        "fun": {},
        "enum": {}
      },
      {
        "info": "Measure carbon dioxide levels",
        "val": {
          "carbonDioxide": {
            "info": "The level of carbon dioxide detected",
            "type": "DOUBLE"
          }
        },
        "fun": {},
        "enum": {}
      },
      {
        "info": "Gets the reading of the dust sensor.",
        "val": {
          "dustLevel": {
            "info": "Current dust level -- also refered to as PM10, measured in micrograms per cubic meter",
            "type": "INTEGER"
          },
          "fineDustLevel": {
            "info": "Current level of fine dust -- also refered to as PM2.5, measured in micrograms per cubic meter",
            "type": "INTEGER"
          },
          "veryFineDustLevel": {
            "info": "Current level of fine dust -- also refered to as PM1.0, measured in micrograms per cubic meter",
            "type": "INTEGER"
          }
        },
        "fun": {},
        "enum": {}
      },
      {
        "info": "Allow reading the relative humidity from devices that support it",
        "val": {
          "humidity": {
            "info": "A numerical representation of the relative humidity measurement taken by the device",
            "type": "DOUBLE"
          }
        },
        "fun": {},
        "enum": {}
      },
      {
        "info": "Get the temperature from a Device that reports current temperature",
        "val": {
          "temperature": {
            "info": "A number that usually represents the current temperature",
            "type": "DOUBLE"
          },
          "temperatureRange": {
            "info": "Constraints on the temperature value",
            "type": "DICT"
          }
        },
        "fun": {},
        "enum": {}
      }
    ]
  },
  "Alarm": {
    "skills": [
      {
        "info": "The Alarm skill allows for interacting with devices that serve as alarms",
        "val": {
          "alarm": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "alarmEnum"
          },
          "alarmVolume": {
            "info": "A string representation of the volume of the alarm",
            "type": "ENUM",
            "format": "alarmVolumeEnum"
          }
        },
        "fun": {
          "both": {
            "info": "Strobe and sound the alarm",
            "args": {},
            "ret": "VOID"
          },
          "off": {
            "info": "Turn the alarm (siren and strobe) off",
            "args": {},
            "ret": "VOID"
          },
          "setAlarmVolume": {
            "info": "Set the volume of the alarm",
            "args": {
              "alarmVolume": {
                "info": "Set the volume of the alarm to \"mute\", \"low\", \"medium\", or \"high\"",
                "type": "ENUM",
                "format": "alarmVolumeEnum"
              }
            },
            "ret": "VOID"
          },
          "siren": {
            "info": "Sound the siren on the alarm",
            "args": {},
            "ret": "VOID"
          },
          "strobe": {
            "info": "Strobe the alarm",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "alarmVolumeEnum": {
            "both": "if the alarm is strobing and sounding the alarm",
            "off": "if the alarm is turned off",
            "siren": "if the alarm is sounding the siren",
            "strobe": "if the alarm is strobing"
          }
        }
      },
      {
        "info": "Defines that the device has a battery",
        "val": {
          "battery": {
            "info": "An indication of the status of the battery",
            "type": "INTEGER"
          }
        },
        "fun": {},
        "enum": {}
      }
    ]
  },
  "Blind": {
    "skills": [
      {
        "info": "Allows for the control of the level of a blind.",
        "val": {
          "blindLevel": {
            "info": "A number that represents the current level as a function of being open, ``0-100`` in percent; 0 representing completely closed, and 100 representing completely open.",
            "type": "INTEGER"
          }
        },
        "fun": {
          "setBlindLevel": {
            "info": "Set the blind level to the given value.",
            "args": {
              "blindLevel": {
                "info": "The level to which the blind should be set, ``0-100`` in percent; 0 representing completely closed, and 100 representing completely open.",
                "type": "INTEGER"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {}
      },
      {
        "info": "Allows for the control of the blind.",
        "val": {
          "blind": {
            "info": "A string representation of whether the blind is open or closed",
            "type": "ENUM",
            "format": "blindEnum"
          }
        },
        "fun": {
          "close": {
            "info": "Close the blind",
            "args": {},
            "ret": "VOID"
          },
          "open": {
            "info": "Open the blind",
            "args": {},
            "ret": "VOID"
          },
          "pause": {
            "info": "Pause opening or closing the blind",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "blindEnum": {
            "closed": "closed",
            "closing": "closing…",
            "open": "open",
            "opening": "opening…",
            "partially open": "partially open",
            "unknown": "unknown"
          }
        }
      }
    ]
  },
  "Button": {
    "skills": [
      {
        "info": "A device with one or more buttons",
        "val": {
          "button": {
            "info": "The state of the buttons",
            "type": "ENUM",
            "format": "buttonEnum"
          },
          "numberOfButtons": {
            "info": "The number of buttons on the device",
            "type": "INTEGER"
          },
          "supportedButtonValues": {
            "info": "List of valid button attribute values",
            "type": "LIST",
            "format": "list[buttonEnum]"
          }
        },
        "fun": {},
        "enum": {
          "buttonEnum": {
            "pushed": "The value if the button is pushed",
            "held": "The value if the button is held",
            "double": "The value if the button is pushed twice",
            "pushed_2x": "The value if the button is pushed twice",
            "pushed_3x": "The value if the button is pushed three times",
            "pushed_4x": "The value if the button is pushed four times",
            "pushed_5x": "The value if the button is pushed five times",
            "pushed_6x": "The value if the button is pushed six times",
            "down": "The value if the button is clicked down",
            "down_2x": "The value if the button is clicked down twice",
            "down_3x": "The value if the button is clicked down three times",
            "down_4x": "The value if the button is clicked down four times",
            "down_5x": "The value if the button is clicked down five times",
            "down_6x": "The value if the button is clicked down six times",
            "down_hold": "The value if the button is clicked down and held",
            "up": "The value if the button is clicked up",
            "up_2x": "The value if the button is clicked up twice",
            "up_3x": "The value if the button is clicked up three times",
            "up_4x": "The value if the button is clicked up four times",
            "up_5x": "The value if the button is clicked up five times",
            "up_6x": "The value if the button is clicked up six times",
            "up_hold": "The value if the button is clicked up and held",
            "swipe_up": "The value if the button is swiped up from botton to top",
            "swipe_down": "The value if the button is swiped down from top to bottom",
            "swipe_left": "The value if the button is swiped from right to left",
            "swipe_right": "The value if the button is swiped from left to right"
          }
        }
      }
    ]
  },
  "Buttonx4": {
    "skills": [
      {
        "info": "A device with four buttons",
        "val": {
          "button1": {
            "info": "The state of the button1",
            "type": "ENUM",
            "format": "buttonEnum"
          },
          "button2": {
            "info": "The state of the button2",
            "type": "ENUM",
            "format": "buttonEnum"
          },
          "button3": {
            "info": "The state of the button3",
            "type": "ENUM",
            "format": "buttonEnum"
          },
          "button4": {
            "info": "The state of the button4",
            "type": "ENUM",
            "format": "buttonEnum"
          },
          "numberOfButtons": {
            "info": "The number of buttons on the device",
            "type": "INTEGER"
          },
          "supportedButtonValues": {
            "info": "List of valid button attribute values",
            "type": "LIST",
            "format": "list[buttonEnum]"
          }
        },
        "fun": {},
        "enum": {
          "buttonEnum": {
            "pushed": "The value if the button is pushed",
            "held": "The value if the button is held",
            "double": "The value if the button is pushed twice",
            "pushed_2x": "The value if the button is pushed twice",
            "pushed_3x": "The value if the button is pushed three times",
            "pushed_4x": "The value if the button is pushed four times",
            "pushed_5x": "The value if the button is pushed five times",
            "pushed_6x": "The value if the button is pushed six times",
            "down": "The value if the button is clicked down",
            "down_2x": "The value if the button is clicked down twice",
            "down_3x": "The value if the button is clicked down three times",
            "down_4x": "The value if the button is clicked down four times",
            "down_5x": "The value if the button is clicked down five times",
            "down_6x": "The value if the button is clicked down six times",
            "down_hold": "The value if the button is clicked down and held",
            "up": "The value if the button is clicked up",
            "up_2x": "The value if the button is clicked up twice",
            "up_3x": "The value if the button is clicked up three times",
            "up_4x": "The value if the button is clicked up four times",
            "up_5x": "The value if the button is clicked up five times",
            "up_6x": "The value if the button is clicked up six times",
            "up_hold": "The value if the button is clicked up and held",
            "swipe_up": "The value if the button is swiped up from botton to top",
            "swipe_down": "The value if the button is swiped down from top to bottom",
            "swipe_left": "The value if the button is swiped from right to left",
            "swipe_right": "The value if the button is swiped from left to right"
          }
        }
      }
    ]
  },
  "Calculator": {
    "skills": [
      {
        "info": "Provides calculation services",
        "val": {},
        "fun": {
          "add": {
            "info": "Add two numbers",
            "args": {
              "a": {
                "info": "The first number to add",
                "type": "DOUBLE"
              },
              "b": {
                "info": "The second number to add",
                "type": "DOUBLE"
              }
            },
            "ret": "DOUBLE"
          },
          "div": {
            "info": "Divide two numbers",
            "args": {
              "a": {
                "info": "The first number to add",
                "type": "DOUBLE"
              },
              "b": {
                "info": "The second number to add",
                "type": "DOUBLE"
              }
            },
            "ret": "DOUBLE"
          },
          "mod": {
            "info": "Modulo two numbers",
            "args": {
              "a": {
                "info": "The first number to add",
                "type": "DOUBLE"
              },
              "b": {
                "info": "The second number to add",
                "type": "DOUBLE"
              }
            },
            "ret": "DOUBLE"
          },
          "mul": {
            "info": "Multiply two numbers",
            "args": {
              "a": {
                "info": "The first number to add",
                "type": "DOUBLE"
              },
              "b": {
                "info": "The second number to add",
                "type": "DOUBLE"
              }
            },
            "ret": "DOUBLE"
          },
          "sub": {
            "info": "Subtract two numbers",
            "args": {
              "a": {
                "info": "The first number to add",
                "type": "DOUBLE"
              },
              "b": {
                "info": "The second number to add",
                "type": "DOUBLE"
              }
            },
            "ret": "DOUBLE"
          }
        },
        "enum": {}
      }
    ]
  },
  "Camera": {
    "skills": [
      {
        "info": "Allows for the control of a camera device",
        "val": {
          "image": {
            "info": "The latest image captured by the camera",
            "type": "BINARY"
          },
          "video": {
            "info": "The latest video captured by the camera",
            "type": "BINARY"
          }
        },
        "fun": {
          "take": {
            "info": "Take a picture with the camera - Return the image as binary data",
            "args": {},
            "ret": "BINARY"
          },
          "takeTimelapse": {
            "info": "Take a picture with the camera - Return the video as binary data",
            "args": {
              "duration": {
                "info": "The duration of the timelapse in seconds",
                "type": "DOUBLE"
              },
              "speed": {
                "info": "The speed of the timelapse",
                "type": "DOUBLE"
              }
            },
            "ret": "BINARY"
          }
        },
        "enum": {}
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "Charger": {
    "skills": [
      {
        "info": "The current status of battery charging",
        "val": {
          "chargingState": {
            "info": "The current charging state of the device",
            "type": "ENUM",
            "format": "chargingStateEnum"
          },
          "supportedChargingStates": {
            "info": "The list of charging states that the device supports. Optional, defaults to all states if not set.",
            "type": "LIST",
            "format": "list[chargingStateEnum]"
          }
        },
        "fun": {},
        "enum": {
          "chargingStateEnum": {
            "charging": "charging",
            "discharging": "discharging",
            "stopped": "stopped",
            "fullyCharged": "fully charged",
            "error": "error"
          }
        }
      },
      {
        "info": "Get the value of voltage measured from devices that support it",
        "val": {
          "voltage": {
            "info": "A number representing the current voltage measured",
            "type": "DOUBLE"
          }
        },
        "fun": {},
        "enum": {}
      },
      {
        "info": "Get the value of electrical current measured from a device.",
        "val": {
          "current": {
            "info": "A number representing the current measured.",
            "type": "DOUBLE"
          }
        },
        "fun": {},
        "enum": {}
      }
    ]
  },
  "Clock": {
    "skills": [
      {
        "info": "Provide current date and time",
        "val": {
          "date": {
            "info": "Current date as double number - format: YYYYMMdd",
            "type": "DOUBLE"
          },
          "datetime": {
            "info": "Current date and time as double number - format: YYYYMMddhhmm",
            "type": "DOUBLE"
          },
          "day": {
            "info": "Current day",
            "type": "INTEGER"
          },
          "hour": {
            "info": "Current hour",
            "type": "INTEGER"
          },
          "isHoliday": {
            "info": "today is holiday or not",
            "type": "BOOL"
          },
          "minute": {
            "info": "Current minute",
            "type": "INTEGER"
          },
          "month": {
            "info": "Current month",
            "type": "INTEGER"
          },
          "second": {
            "info": "Current second",
            "type": "INTEGER"
          },
          "time": {
            "info": "Current time as double number - format: hhmm",
            "type": "DOUBLE"
          },
          "timestamp": {
            "info": "Current timestamp (return current unix time - unit: seconds with floating point)",
            "type": "DOUBLE"
          },
          "weekday": {
            "info": "Current weekday",
            "type": "ENUM",
            "format": "weekdayEnum"
          },
          "year": {
            "info": "Current year",
            "type": "INTEGER"
          }
        },
        "fun": {
          "delay": {
            "info": "delay for a given amount of time",
            "args": {
              "hour": {
                "info": "hour",
                "type": "INTEGER"
              },
              "minute": {
                "info": "minute",
                "type": "INTEGER"
              },
              "second": {
                "info": "second",
                "type": "INTEGER"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {
          "weekdayEnum": {}
        }
      }
    ]
  },
  "ContactSensor": {
    "skills": [
      {
        "info": "Allows reading the value of a contact sensor device",
        "val": {
          "contact": {
            "info": "The current state of the contact sensor",
            "type": "ENUM",
            "format": "contactEnum"
          }
        },
        "fun": {},
        "enum": {
          "contactEnum": {
            "closed": "The value if closed",
            "open": "The value if open"
          }
        }
      }
    ]
  },
  "Curtain": {
    "skills": [
      {
        "info": "Allows for the control of the curtain.",
        "val": {
          "curtain": {
            "info": "A string representation of whether the curtain is open or closed",
            "type": "ENUM",
            "format": "curtainEnum"
          },
          "supportedCurtainCommands": {
            "info": "Curtain commands supported by this instance of Curtain",
            "type": "LIST",
            "format": "list[curtainEnum]"
          }
        },
        "fun": {
          "close": {
            "info": "Close the curtain",
            "args": {},
            "ret": "VOID"
          },
          "open": {
            "info": "Open the curtain",
            "args": {},
            "ret": "VOID"
          },
          "pause": {
            "info": "Pause opening or closing the curtain",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "curtainEnum": {
            "closed": "closed",
            "closing": "closing…",
            "open": "open",
            "opening": "opening…",
            "partially open": "partially open",
            "unknown": "unknown"
          }
        }
      }
    ]
  },
  "Dehumidifier": {
    "skills": [
      {
        "info": "Allows for the control of the dehumidifier mode.",
        "val": {
          "dehumidifierMode": {
            "info": "Current mode of the dehumidifier",
            "type": "ENUM",
            "format": "dehumidifierModeEnum"
          }
        },
        "fun": {
          "setDehumidifierMode": {
            "info": "Set the dehumidifier mode",
            "args": {
              "mode": {
                "info": "Set the dehumidifier mode",
                "type": "ENUM",
                "format": "dehumidifierModeEnum"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {
          "dehumidifierModeEnum": {}
        }
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "Dishwasher": {
    "skills": [
      {
        "info": "Allows for the control of the dishwasher mode.",
        "val": {
          "dishwasherMode": {
            "info": "Current mode of the dishwasher",
            "type": "ENUM",
            "format": "dishwasherModeEnum"
          }
        },
        "fun": {
          "setDishwasherMode": {
            "info": "Set the dishwasher mode",
            "args": {
              "mode": {
                "info": "Set the dishwasher mode to \"eco\", \"intense\", \"auto\", \"quick\", \"rinse\", or \"dry\" mode",
                "type": "ENUM",
                "format": "dishwasherModeEnum"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {
          "dishwasherModeEnum": {
            "eco": "The dishwasher is in \"eco\" mode",
            "intense": "The dishwasher is in \"intense\" mode",
            "auto": "The dishwasher is in \"auto\" mode",
            "quick": "The dishwasher is in \"quick\" mode",
            "rinse": "The dishwasher is in \"rinse\" mode",
            "dry": "The dishwasher is in \"dry\" mode"
          }
        }
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "DoorLock": {
    "skills": [
      {
        "info": "Allow for the control of a door",
        "val": {
          "door": {
            "info": "The current state of the door",
            "type": "ENUM",
            "format": "doorEnum"
          }
        },
        "fun": {
          "close": {
            "info": "Close the door",
            "args": {},
            "ret": "VOID"
          },
          "open": {
            "info": "Open the door",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "doorEnum": {
            "closed": "The door is closed",
            "closing": "The door is closing",
            "open": "The door is open",
            "opening": "The door is opening",
            "unknown": "The current state of the door is unknown"
          }
        }
      }
    ]
  },
  "EmailProvider": {
    "skills": [
      {
        "info": "Provides email services",
        "val": {},
        "fun": {
          "sendMail": {
            "info": "Send an email",
            "args": {
              "toAddress": {
                "info": "The email address of the recipient",
                "type": "STRING"
              },
              "title": {
                "info": "The title of the email",
                "type": "STRING"
              },
              "text": {
                "info": "The text of the email",
                "type": "STRING"
              }
            },
            "ret": "VOID"
          },
          "sendMailWithFile": {
            "info": "Send an email with an attachment",
            "args": {
              "toAddress": {
                "info": "The email address of the recipient",
                "type": "STRING"
              },
              "title": {
                "info": "The title of the email",
                "type": "STRING"
              },
              "text": {
                "info": "The text of the email",
                "type": "STRING"
              },
              "file": {
                "info": "The path to the file to be attached",
                "type": "BINARY"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {}
      }
    ]
  },
  "Fan": {
    "skills": [
      {
        "info": "Allows for the control of the fan.",
        "val": {
          "fanSpeed": {
            "info": "The current fan speed represented as a integer value. - unit: RPM",
            "type": "INTEGER"
          },
          "percent": {
            "info": "The current fan speed represented as a percent value.",
            "type": "INTEGER"
          }
        },
        "fun": {
          "setFanSpeed": {
            "info": "Set the fan speed",
            "args": {
              "speed": {
                "info": "Set the fan to this speed",
                "type": "INTEGER"
              }
            },
            "ret": "VOID"
          },
          "setPercent": {
            "info": "Set the fan speed percent.",
            "args": {
              "percent": {
                "info": "The percent value to set the fan speed to.",
                "type": "INTEGER"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {}
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "Feeder": {
    "skills": [
      {
        "info": "Allows for the control of a feeder device.",
        "val": {
          "feederOperatingState": {
            "info": "The current state of the feeder.",
            "type": "ENUM",
            "format": "feederOperatingStateEnum"
          }
        },
        "fun": {
          "startFeeding": {
            "info": "Begin the feeding process.",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "feederOperatingStateEnum": {
            "idle": "idle",
            "feeding": "feeding",
            "error": "error"
          }
        }
      },
      {
        "info": "Allows for the portion control of a feeder device.",
        "val": {
          "feedPortion": {
            "info": "A number that represents the portion (in grams, pounds, ounces, or servings) that will dispense.",
            "type": "DOUBLE"
          }
        },
        "fun": {
          "setFeedPortion": {
            "info": "Set the portion (in grams, pounds, ounces, or servings) that the feeder will dispense.",
            "args": {
              "portion": {
                "info": "The portion (in grams, pounds, ounces, or servings) to dispense.",
                "type": "DOUBLE"
              },
              "unit": {
                "info": "",
                "type": "ENUM",
                "format": "unitEnum"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {
          "unitEnum": {}
        }
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "GasMeter": {
    "skills": [
      {
        "info": "Read the gas consumption of an energy metering device",
        "val": {
          "gasMeter": {
            "info": "the gas energy reported by the metering device. unit: kWh",
            "type": "DOUBLE"
          },
          "gasMeterCalorific": {
            "info": "a measure of the available heat energy, used as part of the calculation to convert gas volume to gas energy. - unit: kcal",
            "type": "DOUBLE"
          },
          "gasMeterTime": {
            "info": "The cumulative gas use time reported by the metering device. - unit: seconds",
            "type": "DOUBLE"
          },
          "gasMeterVolume": {
            "info": "the cumulative gas volume reported by the metering device. - unit: cubic meters",
            "type": "DOUBLE"
          }
        },
        "fun": {},
        "enum": {}
      }
    ]
  },
  "GasValve": {
    "skills": [
      {
        "info": "Read the gas consumption of an energy metering device",
        "val": {
          "gasMeter": {
            "info": "the gas energy reported by the metering device. unit: kWh",
            "type": "DOUBLE"
          },
          "gasMeterCalorific": {
            "info": "a measure of the available heat energy, used as part of the calculation to convert gas volume to gas energy. - unit: kcal",
            "type": "DOUBLE"
          },
          "gasMeterTime": {
            "info": "The cumulative gas use time reported by the metering device. - unit: seconds",
            "type": "DOUBLE"
          },
          "gasMeterVolume": {
            "info": "the cumulative gas volume reported by the metering device. - unit: cubic meters",
            "type": "DOUBLE"
          }
        },
        "fun": {},
        "enum": {}
      },
      {
        "info": "Allows for the control of a valve device",
        "val": {
          "valve": {
            "info": "A string representation of whether the valve is open or closed",
            "type": "ENUM",
            "format": "valveEnum"
          }
        },
        "fun": {
          "close": {
            "info": "Close the valve",
            "args": {},
            "ret": "VOID"
          },
          "open": {
            "info": "Open the valve",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "valveEnum": {
            "closed": "The value of the ``valve`` attribute if the valve is closed",
            "open": "The value of the ``valve`` attribute if the valve is open"
          }
        }
      }
    ]
  },
  "Humidifier": {
    "skills": [
      {
        "info": "Maintains and sets the state of an humidifier",
        "val": {
          "humidifierMode": {
            "info": "Current mode of the humidifier",
            "type": "ENUM",
            "format": "humidifierModeEnum"
          }
        },
        "fun": {
          "setHumidifierMode": {
            "info": "Set the humidifier mode",
            "args": {
              "mode": {
                "info": "Set the humidifier mode to \"auto\", \"low\", \"medium\", or \"high\" mode",
                "type": "ENUM",
                "format": "humidifierModeEnum"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {
          "humidifierModeEnum": {}
        }
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "HumiditySensor": {
    "skills": [
      {
        "info": "Allow reading the relative humidity from devices that support it",
        "val": {
          "humidity": {
            "info": "A numerical representation of the relative humidity measurement taken by the device",
            "type": "DOUBLE"
          }
        },
        "fun": {},
        "enum": {}
      }
    ]
  },
  "Irrigator": {
    "skills": [
      {
        "info": "Allows for the control of a irrigator device.",
        "val": {
          "irrigatorOperatingState": {
            "info": "The current state of the irrigator.",
            "type": "ENUM",
            "format": "irrigatorOperatingStateEnum"
          }
        },
        "fun": {
          "startWatering": {
            "info": "Begin the watering process.",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "irrigatorOperatingStateEnum": {
            "idle": "idle",
            "watering": "watering",
            "error": "error"
          }
        }
      },
      {
        "info": "Allows for the portion control of a irrigator device.",
        "val": {
          "waterPortion": {
            "info": "A number that represents the portion (in liters, milliliters, gallons, or ounces) that will dispense.",
            "type": "DOUBLE"
          }
        },
        "fun": {
          "setWaterPortion": {
            "info": "Set the portion (in liters, milliliters, gallons, or ounces) that the irrigator will dispense.",
            "args": {
              "portion": {
                "info": "The portion (in grams, pounds, ounces, or servings) to dispense.",
                "type": "DOUBLE"
              },
              "unit": {
                "info": "",
                "type": "ENUM",
                "format": "unitEnum"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {
          "unitEnum": {}
        }
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "LeakSensor": {
    "skills": [
      {
        "info": "A Device that senses water leakage",
        "val": {
          "leakage": {
            "info": "Whether or not water leakage was detected by the Device",
            "type": "ENUM",
            "format": "presenceEnum"
          }
        },
        "fun": {},
        "enum": {
          "presenceEnum": {
            "detected": "water leak is detected",
            "not detected": "no leak"
          }
        }
      }
    ]
  },
  "Light": {
    "skills": [
      {
        "info": "Allows for control of a color changing device by setting its hue, saturation, and color values",
        "val": {
          "color": {
            "info": "``{\"hue\":\"0-100 (percent)\", \"saturation\":\"0-100 (percent)\"}``",
            "type": "STRING"
          },
          "hue": {
            "info": "``0-100`` (percent)",
            "type": "DOUBLE"
          },
          "saturation": {
            "info": "``0-100`` (percent)",
            "type": "DOUBLE"
          }
        },
        "fun": {
          "setColor": {
            "info": "Sets the color based on the values passed in with the given map",
            "args": {
              "color": {
                "info": "The color map supports the following key/value pairs:",
                "type": "DICT"
              }
            },
            "ret": "VOID"
          },
          "setHue": {
            "info": "Set the hue value of the color",
            "args": {
              "hue": {
                "info": "A number in the range ``0-100`` representing the hue as a value of percent",
                "type": "DOUBLE"
              }
            },
            "ret": "VOID"
          },
          "setSaturation": {
            "info": "Set the saturation value of the color",
            "args": {
              "saturation": {
                "info": "A number in the range ``0-100`` representing the saturation as a value of percent",
                "type": "DOUBLE"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {}
      },
      {
        "info": "Allows for the control of the level of a device like a light or a dimmer switch.",
        "val": {
          "level": {
            "info": "A number that represents the current level, usually ``0-100`` in percent",
            "type": "INTEGER"
          },
          "levelRange": {
            "info": "Constraints on the level value",
            "type": "DICT"
          }
        },
        "fun": {
          "alert": {
            "info": "Alert with dimming",
            "args": {},
            "ret": "VOID"
          },
          "setLevel": {
            "info": "Set the level to the given value. If the device supports being turned on and off then it will be turned on if ``level`` is greater than 0 and turned off if ``level`` is equal to 0.",
            "args": {
              "level": {
                "info": "The level value, usually ``0-100`` in percent",
                "type": "INTEGER"
              },
              "rate": {
                "info": "The rate at which to change the level",
                "type": "INTEGER"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {}
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "LightSensor": {
    "skills": [
      {
        "info": "A numerical representation of the brightness intensity",
        "val": {
          "light": {
            "info": "brightness intensity (Unit: lux)",
            "type": "DOUBLE"
          }
        },
        "fun": {},
        "enum": {}
      }
    ]
  },
  "MenuProvider": {
    "skills": [
      {
        "info": "Provides menu information services",
        "val": {},
        "fun": {
          "menu": {
            "info": "Get the menu - Return the menu list",
            "args": {
              "command": {
                "info": "The command to get the menu - format: [오늘|내일] [학생식당|수의대식당|전망대(3식당)|예술계식당(아름드리)|기숙사식당|아워홈|동원관식당(113동)|웰스토리(220동)|투굿(공대간이식당)|자하연식당|301동식당] [아침|점심|저녁]",
                "type": "STRING"
              }
            },
            "ret": "STRING"
          },
          "todayMenu": {
            "info": "Get today's menu randomly - Return the menu list",
            "args": {},
            "ret": "STRING"
          },
          "todayPlace": {
            "info": "Get today's restaurant randomly - Return the restaurant name",
            "args": {},
            "ret": "STRING"
          }
        },
        "enum": {}
      }
    ]
  },
  "MotionSensor": {
    "skills": [
      {
        "info": "• active - The value when motion is detected\n• inactive - The value when no motion is detected",
        "val": {
          "motion": {
            "info": "The current state of the motion sensor",
            "type": "ENUM",
            "format": "motionEnum"
          }
        },
        "fun": {},
        "enum": {
          "motionEnum": {}
        }
      }
    ]
  },
  "PresenceSensor": {
    "skills": [
      {
        "info": "The ability to see the current status of a presence sensor device",
        "val": {
          "presence": {
            "info": "The current state of the presence sensor",
            "type": "ENUM",
            "format": "presenceEnum"
          }
        },
        "fun": {},
        "enum": {
          "presenceEnum": {
            "present": "The device is present",
            "not present": "left"
          }
        }
      }
    ]
  },
  "Pump": {
    "skills": [
      {
        "info": "Allows for the control of a pump device",
        "val": {
          "pump": {
            "info": "A string representation of whether the pump is open or closed",
            "type": "ENUM",
            "format": "pumpEnum"
          }
        },
        "fun": {
          "close": {
            "info": "Close the pump",
            "args": {},
            "ret": "VOID"
          },
          "open": {
            "info": "Open the pump",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "pumpEnum": {
            "closed": "The value of the ``pump`` attribute if the pump is closed",
            "open": "The value of the ``pump`` attribute if the pump is open"
          }
        }
      },
      {
        "info": "Allows for setting the operation mode on a pump.",
        "val": {
          "currentOperationMode": {
            "info": "The current effective operation mode of the pump",
            "type": "ENUM",
            "format": "pumpOperationModeEnum"
          },
          "operationMode": {
            "info": "The operation mode of the pump",
            "type": "ENUM",
            "format": "pumpOperationModeEnum"
          },
          "supportedOperationModes": {
            "info": "Supported operation modes for this device to be in",
            "type": "LIST",
            "format": "list[pumpOperationModeEnum]"
          }
        },
        "fun": {
          "setOperationMode": {
            "info": "Set the operation mode",
            "args": {
              "operationMode": {
                "info": "The operation mode to set the device to",
                "type": "ENUM",
                "format": "pumpOperationModeEnum"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {
          "pumpOperationModeEnum": {
            "normal": "The pump is controlled by a setpoint.",
            "minimum": "This value sets the pump to run at the minimum possible speed it can without being stopped.",
            "maximum": "This value sets the pump to run at its maximum possible speed.",
            "localSetting": "This value sets the pump to run with the local settings of the pump."
          }
        }
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "Refrigerator": {
    "skills": [
      {
        "info": "Allows for the control of the refrigeration.",
        "val": {
          "defrost": {
            "info": "Status of the defrost",
            "type": "ENUM",
            "format": "defrostEnum"
          },
          "rapidCooling": {
            "info": "Status of the rapid cooling",
            "type": "ENUM",
            "format": "rapidCoolingEnum"
          },
          "rapidFreezing": {
            "info": "Status of the rapid freezing",
            "type": "ENUM",
            "format": "rapidFreezingEnum"
          }
        },
        "fun": {
          "setDefrost": {
            "info": "Sets the defrost on or off",
            "args": {
              "defrost": {
                "info": "The on or off value for the defrost",
                "type": "ENUM",
                "format": "defrostEnum"
              }
            },
            "ret": "VOID"
          },
          "setRapidCooling": {
            "info": "Sets the rapid cooling on or off",
            "args": {
              "rapidCooling": {
                "info": "The on or off value for the rapid cooling",
                "type": "ENUM",
                "format": "rapidCoolingEnum"
              }
            },
            "ret": "VOID"
          },
          "setRapidFreezing": {
            "info": "Sets the rapid freezing on or off",
            "args": {
              "rapidFreezing": {
                "info": "The on or off value for the rapid freezing",
                "type": "ENUM",
                "format": "rapidFreezingEnum"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {
          "rapidFreezingEnum": {
            "on": "The value of the ``defrost``, ``rapidCooling``, ``rapidFreezing`` attribute if the defrost, rapidCooling, rapidFreezing is on",
            "off": "The value of the ``defrost``, ``rapidCooling``, ``rapidFreezing`` attribute if the defrost, rapidCooling, rapidFreezing is off"
          }
        }
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "RobotCleaner": {
    "skills": [
      {
        "info": "Allows for the control of the robot cleaner cleaning mode.",
        "val": {
          "robotCleanerCleaningMode": {
            "info": "Current status of the robot cleaner cleaning mode",
            "type": "ENUM",
            "format": "robotCleanerCleaningModeEnum"
          }
        },
        "fun": {
          "setRobotCleanerCleaningMode": {
            "info": "Set the robot cleaner cleaning mode",
            "args": {
              "mode": {
                "info": "Set the robot cleaner cleaning mode, to \"auto\", \"part\", \"repeat\", \"manual\" or \"stop\" modes",
                "type": "ENUM",
                "format": "robotCleanerCleaningModeEnum"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {
          "robotCleanerCleaningModeEnum": {
            "auto": "The robot cleaner cleaning mode is in \"auto\" mode",
            "part": "The robot cleaner cleaning mode is in \"part\" mode",
            "repeat": "The robot cleaner cleaning mode is in \"repeat\" mode",
            "manual": "The robot cleaner cleaning mode is in \"manual\" mode",
            "stop": "The robot cleaner cleaning mode is in \"stop\" mode",
            "map": "The robot cleaner cleaning mode is in \"map\" mode"
          }
        }
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "Shade": {
    "skills": [
      {
        "info": "Allows for the control of the level of a window shade.",
        "val": {
          "shadeLevel": {
            "info": "A number that represents the current level as a function of being open, ``0-100`` in percent; 0 representing completely closed, and 100 representing completely open.",
            "type": "INTEGER"
          }
        },
        "fun": {
          "setShadeLevel": {
            "info": "Set the shade level to the given value.",
            "args": {
              "shadeLevel": {
                "info": "The level to which the shade should be set, ``0-100`` in percent; 0 representing completely closed, and 100 representing completely open.",
                "type": "INTEGER"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {}
      },
      {
        "info": "Allows for the control of the window shade.",
        "val": {
          "supportedWindowShadeCommands": {
            "info": "Window shade commands supported by this instance of Window Shade",
            "type": "LIST",
            "format": "list[windowShadeEnum]"
          },
          "windowShade": {
            "info": "A string representation of whether the window shade is open or closed",
            "type": "ENUM",
            "format": "windowShadeEnum"
          }
        },
        "fun": {
          "close": {
            "info": "Close the window shade",
            "args": {},
            "ret": "VOID"
          },
          "open": {
            "info": "Open the window shade",
            "args": {},
            "ret": "VOID"
          },
          "pause": {
            "info": "Pause opening or closing the window shade",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "windowShadeEnum": {
            "closed": "closed",
            "closing": "closing…",
            "open": "open",
            "opening": "opening…",
            "partially open": "partially open",
            "unknown": "unknown"
          }
        }
      }
    ]
  },
  "Siren": {
    "skills": [
      {
        "info": "Allows for the control of the siren.",
        "val": {
          "sirenMode": {
            "info": "Current mode of the siren",
            "type": "ENUM",
            "format": "sirenModeEnum"
          }
        },
        "fun": {
          "setSirenMode": {
            "info": "Set the siren mode",
            "args": {
              "mode": {
                "info": "Set the siren mode",
                "type": "ENUM",
                "format": "sirenModeEnum"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {
          "sirenModeEnum": {}
        }
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "SmartPlug": {
    "skills": [
      {
        "info": "Get the value of voltage measured from devices that support it",
        "val": {
          "voltage": {
            "info": "A number representing the current voltage measured",
            "type": "DOUBLE"
          }
        },
        "fun": {},
        "enum": {}
      },
      {
        "info": "Allows for reading the power consumption from devices that report it",
        "val": {
          "power": {
            "info": "A number representing the current power consumption. Check the device documentation for how this value is reported - unit: Watts",
            "type": "DOUBLE"
          },
          "powerConsumption": {
            "info": "energy and power consumption during specific time period - unit: Wh",
            "type": "DICT"
          }
        },
        "fun": {},
        "enum": {}
      },
      {
        "info": "Get the value of electrical current measured from a device.",
        "val": {
          "current": {
            "info": "A number representing the current measured.",
            "type": "DOUBLE"
          }
        },
        "fun": {},
        "enum": {}
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "SmokeDetector": {
    "skills": [
      {
        "info": "A device that detects the presence or absence of smoke.",
        "val": {
          "smoke": {
            "info": "The state of the smoke detection device",
            "type": "ENUM",
            "format": "smokeEnum"
          }
        },
        "fun": {},
        "enum": {
          "smokeEnum": {
            "clear": "No smoke detected",
            "detected": "Smoke detected",
            "tested": "Smoke detector test button was activated"
          }
        }
      }
    ]
  },
  "SoilMoistureSensor": {
    "skills": [
      {
        "info": "Allow reading the soil humidity from devices that support it",
        "val": {
          "soilHumidity": {
            "info": "A numerical representation of the soil humidity measurement taken by the device",
            "type": "DOUBLE"
          }
        },
        "fun": {},
        "enum": {}
      }
    ]
  },
  "SoundSensor": {
    "skills": [
      {
        "info": "Gets the value of the sound pressure level.",
        "val": {
          "soundPressureLevel": {
            "info": "Level of the sound pressure",
            "type": "DOUBLE"
          }
        },
        "fun": {},
        "enum": {}
      },
      {
        "info": "A Device that senses sound",
        "val": {
          "sound": {
            "info": "Whether or not sound was detected by the Device",
            "type": "ENUM",
            "format": "soundEnum"
          }
        },
        "fun": {},
        "enum": {
          "soundEnum": {
            "detected": "Sound is detected",
            "not detected": "no sound"
          }
        }
      }
    ]
  },
  "Speaker": {
    "skills": [
      {
        "info": "Allows for the control of the media playback.",
        "val": {
          "playbackStatus": {
            "info": "Status of the media playback",
            "type": "ENUM",
            "format": "mediaPlaybackEnum"
          },
          "supportedPlaybackCommands": {
            "info": "Media playback commands which are supported",
            "type": "LIST",
            "format": "list[mediaPlaybackEnum]"
          }
        },
        "fun": {
          "fastForward": {
            "info": "Fast forward the media playback",
            "args": {},
            "ret": "VOID"
          },
          "pause": {
            "info": "Pause the media playback",
            "args": {},
            "ret": "VOID"
          },
          "play": {
            "info": "Play the media playback",
            "args": {
              "source": {
                "info": "The source of the media playback",
                "type": "STRING"
              }
            },
            "ret": "VOID"
          },
          "rewind": {
            "info": "Rewind the media playback",
            "args": {},
            "ret": "VOID"
          },
          "setPlaybackStatus": {
            "info": "Set the playback status",
            "args": {
              "status": {
                "info": "Set the playback status to \"paused\", \"playing\", \"stopped\", \"fast forwarding\" or \"rewinding\" state.",
                "type": "ENUM",
                "format": "mediaPlaybackEnum"
              }
            },
            "ret": "VOID"
          },
          "speak": {
            "info": "TTS feature",
            "args": {
              "text": {
                "info": "The text to be spoken",
                "type": "STRING"
              }
            },
            "ret": "VOID"
          },
          "stop": {
            "info": "Stop the media playback",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "mediaPlaybackEnum": {
            "paused": "Media playback is in a \"paused\" state",
            "playing": "Media playback is in a \"playing\" state",
            "stopped": "Media playback is in a \"stopped\" state",
            "fast forwarding": "Media playback is in a \"fast forwarding\" state",
            "rewinding": "Media playback is in a \"rewinding\" state",
            "buffering": "Media playback is in a \"buffering\" state"
          }
        }
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "Recorder": {
    "skills": [
      {
        "info": "Record audio",
        "val": {
          "recordStatus": {
            "info": "The current status of the audio recorder",
            "type": "ENUM",
            "format": "recordStatusEnum"
          }
        },
        "fun": {
          "record": {
            "info": "Record audio",
            "args": {
              "file": {
                "info": "The file to record to",
                "type": "STRING"
              },
              "duration": {
                "info": "The duration to record for",
                "type": "DOUBLE"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {
          "recordStatusEnum": {
            "idle": "The audio recorder is idle",
            "recording": "The audio recorder is recording"
          }
        }
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "Switch": {
    "skills": [
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "Television": {
    "skills": [
      {
        "info": "Allows for the control of audio mute.",
        "val": {
          "muteStatus": {
            "info": "Current status of the audio mute",
            "type": "ENUM",
            "format": "muteEnum"
          }
        },
        "fun": {
          "mute": {
            "info": "Set the audio to mute state",
            "args": {},
            "ret": "VOID"
          },
          "setMute": {
            "info": "Set the state of the audio mute",
            "args": {
              "state": {
                "info": "Set the audio mute state to \"muted\" or \"unmuted\"",
                "type": "ENUM",
                "format": "muteEnum"
              }
            },
            "ret": "VOID"
          },
          "unmute": {
            "info": "Set the audio to unmute state",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "muteEnum": {
            "muted": "The audio is in \"muted\" state",
            "unmuted": "The audio is in \"unmuted\" state"
          }
        }
      },
      {
        "info": "Allows for the control of the TV channel.",
        "val": {
          "tvChannel": {
            "info": "Current status of the TV channel",
            "type": "INTEGER"
          },
          "tvChannelName": {
            "info": "Current status of the TV channel name",
            "type": "STRING"
          }
        },
        "fun": {
          "channelDown": {
            "info": "Move the TV channel down",
            "args": {},
            "ret": "VOID"
          },
          "channelUp": {
            "info": "Move the TV channel up",
            "args": {},
            "ret": "VOID"
          },
          "setTvChannel": {
            "info": "Set the TV channel",
            "args": {
              "tvChannel": {
                "info": "",
                "type": "INTEGER"
              }
            },
            "ret": "VOID"
          },
          "setTvChannelName": {
            "info": "Set the TV channel Name",
            "args": {
              "tvChannelName": {
                "info": "",
                "type": "STRING"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {}
      },
      {
        "info": "Allows for the control of audio volume.",
        "val": {
          "volume": {
            "info": "The current volume setting of the audio",
            "type": "INTEGER"
          }
        },
        "fun": {
          "setVolume": {
            "info": "Set the audio volume level",
            "args": {
              "volume": {
                "info": "A value to which the audio volume level should be set",
                "type": "INTEGER"
              }
            },
            "ret": "VOID"
          },
          "volumeDown": {
            "info": "Turn the audio volume down",
            "args": {},
            "ret": "VOID"
          },
          "volumeUp": {
            "info": "Turn the audio volume up",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {}
      },
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "TemperatureSensor": {
    "skills": [
      {
        "info": "Get the temperature from a Device that reports current temperature",
        "val": {
          "temperature": {
            "info": "A number that usually represents the current temperature",
            "type": "DOUBLE"
          },
          "temperatureRange": {
            "info": "Constraints on the temperature value",
            "type": "DICT"
          }
        },
        "fun": {},
        "enum": {}
      }
    ]
  },
  "TestDevice": {
    "skills": [
      {
        "info": "testSkill",
        "val": {
          "testSkillValue": {
            "info": "testSkillValue",
            "type": "STRING"
          }
        },
        "fun": {
          "testSkillFunction": {
            "info": "testSkillFunction",
            "args": {
              "testArgument": {
                "info": "testArgument",
                "type": "STRING"
              }
            },
            "ret": "STRING"
          }
        },
        "enum": {
          "testSkillEnum": {}
        }
      }
    ]
  },
  "Valve": {
    "skills": [
      {
        "info": "Allows for the control of a valve device",
        "val": {
          "valve": {
            "info": "A string representation of whether the valve is open or closed",
            "type": "ENUM",
            "format": "valveEnum"
          }
        },
        "fun": {
          "close": {
            "info": "Close the valve",
            "args": {},
            "ret": "VOID"
          },
          "open": {
            "info": "Open the valve",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "valveEnum": {
            "closed": "The value of the ``valve`` attribute if the valve is closed",
            "open": "The value of the ``valve`` attribute if the valve is open"
          }
        }
      }
    ]
  },
  "WeatherProvider": {
    "skills": [
      {
        "info": "Provides weather information",
        "val": {
          "humidityWeather": {
            "info": "Current humidity level",
            "type": "DOUBLE"
          },
          "pm10Weather": {
            "info": "Current pm10 level",
            "type": "DOUBLE"
          },
          "pm25Weather": {
            "info": "Current pm25 level",
            "type": "DOUBLE"
          },
          "pressureWeather": {
            "info": "Current pressure level",
            "type": "DOUBLE"
          },
          "temperatureWeather": {
            "info": "Current temperature level",
            "type": "DOUBLE"
          },
          "weather": {
            "info": "Current weather condition",
            "type": "ENUM",
            "format": "weatherEnum"
          }
        },
        "fun": {
          "getWeatherInfo": {
            "info": "Get the current weather information - Return whole weather information, format: \"temperature, humidity, pressure, pm25, pm10, weather, weather_string, icon_id, location\"",
            "args": {
              "lat": {
                "info": "The latitude of the location",
                "type": "DOUBLE"
              },
              "lon": {
                "info": "The longitude of the location",
                "type": "DOUBLE"
              }
            },
            "ret": "STRING"
          }
        },
        "enum": {
          "weatherEnum": {
            "thunderstorm": "thunderstorm",
            "drizzle": "drizzle",
            "rain": "rain",
            "snow": "snow",
            "mist": "mist",
            "smoke": "smoke",
            "haze": "haze",
            "dust": "dust",
            "fog": "fog",
            "sand": "sand",
            "ash": "ash",
            "squall": "squall",
            "tornado": "tornado",
            "clear": "clear",
            "clouds": "clouds"
          }
        }
      }
    ]
  },
  "Window": {
    "skills": [
      {
        "info": "Allows for the control of the window shade.",
        "val": {
          "window": {
            "info": "A string representation of whether the window is open or closed",
            "type": "ENUM",
            "format": "windowEnum"
          }
        },
        "fun": {
          "close": {
            "info": "Close the window",
            "args": {},
            "ret": "VOID"
          },
          "open": {
            "info": "Open the window",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "windowEnum": {
            "closed": "closed",
            "open": "open",
            "unknown": "unknown"
          }
        }
      }
    ]
  },
  "FallDetector": {
    "skills": [
      {
        "info": "Detects if a fall has occurred",
        "val": {
          "fall": {
            "info": "Whether or not a fall was detected",
            "type": "ENUM",
            "format": "fallEnum"
          }
        },
        "fun": {},
        "enum": {
          "fallEnum": {
            "fall": "fall detected",
            "normal": "no fall detected"
          }
        }
      }
    ]
  },
  "FaceRecognizer": {
    "skills": []
  },
  "CloudServiceProvider": {
    "skills": []
  },
  "NewsProvider": {
    "skills": []
  },
  "OccupancySensor": {
    "skills": [
      {
        "info": "The ability to see the current status of a presence sensor device",
        "val": {
          "presence": {
            "info": "The current state of the presence sensor",
            "type": "ENUM",
            "format": "presenceEnum"
          }
        },
        "fun": {},
        "enum": {
          "presenceEnum": {
            "present": "The device is present",
            "not present": "left"
          }
        }
      }
    ]
  },
  "Relay": {
    "skills": [
      {
        "info": "Allows for the control of a switch device",
        "val": {
          "switch": {
            "info": "A string representation of whether the switch is on or off",
            "type": "ENUM",
            "format": "switchEnum"
          }
        },
        "fun": {
          "off": {
            "info": "Turn a switch off",
            "args": {},
            "ret": "VOID"
          },
          "on": {
            "info": "Turn a switch on",
            "args": {},
            "ret": "VOID"
          },
          "toggle": {
            "info": "Toggle a switch",
            "args": {},
            "ret": "VOID"
          }
        },
        "enum": {
          "switchEnum": {
            "on": "The value of the ``switch`` attribute if the switch is on",
            "off": "The value of the ``switch`` attribute if the switch is off"
          }
        }
      }
    ]
  },
  "Timer": {
    "skills": [
      {
        "info": "The Timer allows for interacting with devices that serve as timers",
        "val": {},
        "fun": {
          "add": {
            "info": "Add a timer",
            "args": {
              "name": {
                "info": "The time name",
                "type": "STRING"
              },
              "timeout": {
                "info": "The time at which the timer should expire",
                "type": "DOUBLE"
              }
            },
            "ret": "VOID"
          },
          "isExist": {
            "info": "Check if a timer is exist",
            "args": {
              "name": {
                "info": "The time name",
                "type": "STRING"
              }
            },
            "ret": "BOOL"
          },
          "isSet": {
            "info": "Check if a timer is set",
            "args": {
              "name": {
                "info": "The time name",
                "type": "STRING"
              }
            },
            "ret": "BOOL"
          },
          "reset": {
            "info": "Reset a timer",
            "args": {
              "name": {
                "info": "The time name",
                "type": "STRING"
              }
            },
            "ret": "VOID"
          },
          "set": {
            "info": "Set a timer",
            "args": {
              "name": {
                "info": "The time name",
                "type": "STRING"
              },
              "timeout": {
                "info": "The time at which the timer should expire",
                "type": "DOUBLE"
              }
            },
            "ret": "VOID"
          },
          "start": {
            "info": "Start a timer",
            "args": {
              "name": {
                "info": "The time name",
                "type": "STRING"
              }
            },
            "ret": "VOID"
          }
        },
        "enum": {}
      }
    ]
  },
  "ManagerThing": {
    "skills": [
      {
        "info": "Allow Manager Thing's features",
        "val": {},
        "fun": {
          "add_thing": {
            "info": "Add staff thing - Return error string",
            "args": {
              "parameter": {
                "info": "Staff thing's parameter",
                "type": "STRING"
              },
              "client_id": {
                "info": "Requester's client id",
                "type": "STRING"
              },
              "name": {
                "info": "Staff thing's name",
                "type": "STRING"
              }
            },
            "ret": "STRING"
          },
          "delete_thing": {
            "info": "Delete staff thing - Return error string",
            "args": {
              "name": {
                "info": "Staff thing's name",
                "type": "STRING"
              },
              "client_id": {
                "info": "Requester's client id",
                "type": "STRING"
              }
            },
            "ret": "STRING"
          },
          "discover": {
            "info": "Discover local devices - Return device list with json format",
            "args": {},
            "ret": "STRING"
          }
        },
        "enum": {}
      }
    ]
  },
  "SuperThing": {
    "skills": []
  },
  "Undefined": {
    "skills": []
  }
}
'''