import ollama
import json
import time
import re
import os
import argparse
import time
import requests

'''
from mqtt.mqtt_handler import mqtt_handler
from utility.thing_extract import extract_thing_list, extract_thing_from_thing_list
from utility.servicelist_modify import file_parse 
'''
from .SERVICE_DESCRIPTION_FINAL import description
from .device_verifier import *


THINGS_LIST = """(#AirConditioner)\n(#AirPurifier)\n(#AirQualityDetector)\n(#Blind)\n(#Button)\n(#Calculator)\n(#Camera)\n(#Charger)\n(#Clock)\n(#ContactSensor)\n(#Curtain)\n(#Dehumidifier)\n(#Dishwasher)\n(#DoorLock)\n(#EmailProvider)\n(#Fan)\n(#Feeder)\n(#GasMeter)\n(#GasValve)\n(#Humidifier)\n(#HumiditySensor)\n(#Irrigator)\n(#LeakSensor)\n(#Light)\n(#LightSensor)\n(#MenuProvider)\n(#MotionSensor)\n(#PresenceSensor)\n(#Pump)\n(#Refrigerator)\n(#RobotCleaner)\n(#Shade)\n(#Siren)\n(#SmartPlug)\n(#SmokeDetector)\n(#SoundSensor)\n(#Speaker)\n(#Switch)\n(#Television)\n(#TemperatureSensor)\n(#Valve)\n(#WeatherProvider)\n(#Window)"""
MAPPING_INSTRUCTION_DEVICES =  f"""[INST]와 [/INST] 사이의 행동 강령(CODE OF CONDUCT)을 매우 주의 깊게 읽으세요. 아래 지침을 단계별로 따라가며 작업을 완료해주세요요.
당신은 "SoPIoT"라는 AIoT 시스템의 모듈입니다. SoPIoT의 큰 목표는 사용자의 자연어 요청을 이해하고, 이를 AIoT 시스템이 이해할 수 있는 SoP-Lang 언어로 변환하는 것입니다.

당신의 역할은 사용자 입력을 받아, 그 요청을 수행하기 위해 어떤 디바이스가 필요한지 파악하는 것입니다.
명령을 실행하기 위해 사용할 수 있는 디바이스를 가능한 한 많이 찾아내세요.

당신은 어떤 디바이스를 사용할지 분석하고, 그 목록을 전부 출력하는 책임이 있습니다.

    최종 출력 형식은 반드시 다음과 같이 3줄 형식으로 출력해야 합니다:

    [OUTPUT]
        [Device] : (필요한 디바이스 목록)
    [/OUTPUT]

    예시를 참고해주세요:

    [EXAMPLES]
        예시 1.
        Input: 온도 센서가 18도 이하로 감지되면 에어컨을 난방 모드로 설정해줘.
        value check: 온도 확인
        action: 에어컨 켜기, 에어컨 모드를 난방으로 설정
        [OUTPUT]
            [Device] : (#TemperatureSensor), (#AirConditioner)
        [/OUTPUT]

        예시 2.
        Input: 매 시 50분마다 방의 블라인드를 열고 스피커에서 부드러운 음악을 재생해줘.
        value check: 시간 확인
        action: 블라인드 열기, 스피커에서 음악 재생
        [OUTPUT]
            [Device] : (#Clock), (#TemperatureSensor), (#AirConditioner), (#Blind), (#Speaker)
        [/OUTPUT]

        예시 3.
        Input: 습도가 50을 넘으면 제습기와 공기청정기, 선풍기를 켜줘. 온도가 20도 이상이면 선풍기를 고속 모드로 설정해줘.
        value check: 습도 확인, 온도 확인
        action: 제습기 켜기, 공기청정기 켜기, 선풍기 켜기, 선풍기 고속 모드 설정
        [OUTPUT]
            [Device] : (#HumiditySensor), (#TemperatureSensor), (#Dehumidifier), (#AirPurifier), (#Fan)
        [/OUTPUT]

        예시 4.
        Input: 에어컨을 켜줘
        value check: 없음
        action: 에어컨 켜기
        [OUTPUT]
            [Device] : (#AirConditioner)
        [/OUTPUT]

        예시 5.
        Input: 커피머신을 켜줘
        value check: 없음
        action: 커피머신 켜기
        [OUTPUT]
            [Device] : None
        [/OUTPUT]

        예시 6.
        Input: 온도가 23도 이하이면 에어컨을 켜고 25도 이상이면 꺼줘
        value check: 온도 확인
        action: 에어컨 켜기, 끄기
        [OUTPUT]
            [Device] : (#TemperatureSensor), (#AirConditioner)
        [/OUTPUT]

        예시 7.
        Input: 12시 30분부터 1시까지 음악을 재생하고 블라인드를 50% 열어 햇빛을 들여줘
        value check: 시간 확인
        action: 스피커 켜기, 음악 재생, 블라인드를 50% 열기
        [OUTPUT]
            [Device] : (#Clock), (#Speaker), (#Blind)
        [/OUTPUT]

        예시 8.
        Input: 독서를 시작하면 조명을 자연광 모드로 설정하고 밝기를 60%로 조절해줘
        value check: 없음
        action: 조명 켜기, 조명 밝기 60% 설정
        [OUTPUT]
            [Device] : (#Light)
        [/OUTPUT]
    [/EXAMPLES]

    이외의 형식은 허용되지 않습니다!!!

    다음은 디바이스 목록입니다.
    {THINGS_LIST}
    적절한 값이나 기능을 이 목록에서 반드시 찾아야 합니다. 항상 이 목록에서만 디바이스를 선택해야 합니다.

    각 문장을 확인하고, 목록에 없는 요청이 있다면 파악해주세요.
    명령에서 가능한 한 많은 디바이스를 찾아내야 합니다. 절대 빠뜨리지 마세요! 모든 디바이스를 빠짐없이 찾으세요!

    생각을 단계별로 정리하면서 해결해주세요.
    설명은 출력하지 말고, 오직 결과만 출력해주세요!!!
    ==========
    STEP 1. 디바이스 매핑

    주어진 원래 명령(입력)을 사용하여 명령을 실행하는 데 필요한 정확한 디바이스가 무엇인지 파악합니다. 주어진 디바이스 문자열에 있는 디바이스만 사용해야 합니다. 
    명령의 모든 부분에 해당하는 디바이스를 반환합니다. 명령에 대한 모든 장치를 가능한 한 많이 찾아야 합니다. 입력 명령에서 모든 장치를 모두 찾습니다.
 """

MAPPING_INSTRUCTION_DEVICES_YG= """
Please read the CODE OF CONDUCT between [INST] and [/INST] very carefully. Go through the following instructions step by step and complete the task.
You are the second module of the AIoT system called "SoPIoT" which stands for Service Oriented Platform for Internet of Things.
The Big Picture of SoPIoT is to understand the user's natural language request and convert it into a SoP-Lang which is a language that the AIoT system can understand.
YOU ARE RESPONSIBLE FOR CHOOSING THE PROPER DEVICE TO GET INFORMATION.

HERE IS AN EXAMPLE OF YOUR TASK:
    [EXAMPLE]
        1. Input: humidity is below 30%
        [OUTPUT]
        [Condition What to do]: get the humidity level is below 30%
        [DEVICE_NAME]: HumiditySensor
        [/OUTPUT]

        3. Input: "light is off", turn on the oven."
        [OUTPUT]
        [Condition What to do]: get the light status is off
        [DEVICE_NAME]: LightSensor
        [/OUTPUT]

        4. Input: "air conditioner is off"
        [OUTPUT]
        [Condition What to do]: get the air conditioner status is off
        [DEVICE_NAME]: AirConditioner
        [/OUTPUT]

        5. Input: "it's snowing outside." 
        [OUTPUT]
        [Condition What to do]: get the weather status is snowing
        [DEVICE_NAME]: WeatherProvider
        [/OUTPUT]
    [/EXAMPLE]


[INST]
1. READ THE DEVICES WE CAN USE IS PROVIED BETWEEN [DEVICE_LIST] and [/DEVICE_LIST] WITH THEIR DESCRIPTIONS.
2. CHOOSE THE DEVICE THAT CAN PROVIDE THE INFORMATION THAT WE NEED BETWEEN [QUESTION] and [/QUESTION].
3. PLEASE ANSWER ONLY IN THE FORMAT BELOW :


[OUTPUT]
    [Condition What to do]: <what_to_do>\n
    [CONDITION_DEVICE_NAME]: <device_name>
[/OUTPUT]
[/INST]
 """

def google_translate(command, api_key = os.environ['GOOGLE_TRANSLATE_KEY']):
    return command
    # url = "https://translation.googleapis.com/language/translate/v2"
    # headers = {
    #     "Content-Type": "application/json"
    # }
    # data = {
    #     "q": command,
    #     "target": "en",
    #     "format": "text"
    # }
    # params = {
    #     "key": api_key
    # }

    # response = requests.post(url, headers=headers, params=params, data=json.dumps(data))

    # if response.status_code == 200:
    #     translation = response.json()["data"]["translations"][0]["translatedText"]
    #     return translation
    # else:
    #     raise Exception(f"Error: {response.status_code}, {response.text}")

    
def extract_output_sections(input_text):
    lines = input_text.split('\n')
    
    # [output]과 [/output] 사이의 내용을 모을 리스트를 초기화합니다.
    output_lines = []
    
    # [output]과 [/output] 사이의 내용을 추출하기 위한 플래그와 카운터 초기화
    inside_output = False

    for line in lines:
        if '[output]' in line.lower():
            inside_output = True
            continue
        if '[/output]' in line.lower():
            inside_output = False
            continue
        if inside_output:
            output_lines.append(line)

    # 모든 내용을 합친 후 스페이스와 쉼표 기준으로 분리합니다.
    combined_text = ' '.join(output_lines)
    words = re.split(r'[,\s]+', combined_text)

    # 빈 문자열은 제거
    words = [re.sub(r'[\(\)#]', '', word) for word in words if re.sub(r'[\(\)#]', '', word).isalpha()]

    return words

    
def Device_Mapping(command, services, model='finetune0606-3',temperature=0,max_try=5,verbose=False,seed=123):
      chat_result = ollama.chat(
      model=model,
      messages=[{'role': 'user', 'content': 'Device_Limitations :'  + MAPPING_INSTRUCTION_DEVICES+ '\n=======\nUser input: '+ command }], #services   + "\n=======\n"
      options=dict(temperature=0)
        )
      #give the result to mapping_verifier to modify wrong device names
      step1_map_result = Mapping_Verifier(chat_result['message']['content'])
      step1_map_result.device_verify()
      final_device_mapping = " ".join(extract_output_sections(step1_map_result.input_text))
      #find more devices using mapping verifier
      every_device_list = Mapping_Verifier(command)
      more_devices = every_device_list.device_mapping()
      #이미 생성한 중복 device 제거
      for more_device in more_devices[:]:
          if (more_device in final_device_mapping):
              more_devices.remove(more_device)
      if (len(more_devices)>0):
          final_device_mapping = final_device_mapping + " " + " ".join(more_devices)
      return final_device_mapping.split()
     
      
'''
def mqtt_process():
    global STRING_THING_LIST 
    global DICT_THING_LIST
    # Uncomment mqtt_handler for get information from middleware
    print(f"{BOLD}{MAGENTA}[MAIN/MQTT]{RESET}{BOLD} MQTT Communication...{RESET}")
    mqtt_handler()
    print(f"{BOLD}{MAGENTA}[MAIN/MQTT]{RESET}{BOLD} MQTT Communication Done{RESET}\n")

    # get thing list
    print(f"{BOLD}{MAGENTA}[MAIN/DATA]{RESET}{BOLD} Extracting thing list...{RESET}")
    extract_thing_list()
    #generate_thing_description_list()
    string_thing_list = extract_thing_from_thing_list()
    STRING_THING_LIST = string_thing_list
    parsed_service_list = file_parse()
    #print(string_thing_list)
    
    thing_dictionary = [device.strip() for device in STRING_THING_LIST.split(",")]
    #print(f"{BOLD}{MAGENTA}[MAIN/DATA]{RESET}{BOLD} Generating thing summary...{RESET}")
    #generate_thing_summary()
    print(f"{BOLD}{MAGENTA}[MAIN/DATA]{RESET}{BOLD} Data Processing Done{RESET}\n")

    return string_thing_list, thing_dictionary, parsed_service_list
'''
def process():
    while True:
       #step 0 : translate
       #format_instruction()
       #translated_input = google_translate(input())
       translated_input = input()
       start = time.time()
       mapping_result = Device_Mapping(translated_input, services)
       print("\n---------------------------------------------------\n")
       print("STEP 1 DEVICE Mapping result:\n\n" ,mapping_result)
       print("\n---------------------------------------------------\n")
      
       end = time.time()
       print("time: ",end-start)

if __name__ == '__main__':
    '''
    global STRING_THING_LIST
    global DICT_THING_LIST

    parser = argparse.ArgumentParser(description="Process some requests.")
    parser.add_argument(
        "-t", "--test", action="store_true", help="Run predefined test inputs"
    )
    parser.add_argument(
        "-m", "--mqtt", action="store_true", help="Run mqtt_process function"
    )
    args = parser.parse_args()
    # 100% Working.

    # Execute functions based on arguments
    if args.mqtt:
        # Step 0
        STRING_THING_LIST, DICT_THING_LIST, PARSED_THING_LIST = mqtt_process()

    else:
        # Add the logic for test inputs here
        with open('data/parsed_servicelist.json',  encoding='utf-8') as f:
            devices_json = json.load(f)
        with open('testcase.txt',  encoding='utf-8') as f: 
            testcases = f.readlines()
            '''
    services = str(description)
    process()