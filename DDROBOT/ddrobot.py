import requests
from aip import AipSpeech
from playsound import playsound

""" 你的 APPID AK SK """
APP_ID = '24762487'
API_KEY = 'CEIGfjflnpNHj3VwYEDFcpDn'
SECRET_KEY = 'veD108BrOgeFseCcNM6LoLhNay1K99Pc '

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

print('请输入你想说的：')

while True:
    a=input()
    url='https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s'%a
    te=requests.get(url).json()
    data=te['data']['info']['text']
    print(data)
    result = client.synthesis(data, 'zh', 1, {
        'vol': 8,  # 音量
        'spd': 5,  # 语速
        'pit': 9,  # 语调
        'per': 4,  # 0：女 1：男 3：逍遥 4：小萝莉
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb+') as f:
            f.write(result)

    p = playsound()
    voice_path = r"auido.mp3"
    p.play(voice_path)  # 播放
    p.close()  # 停止

import requests
print('请输入你想说的：')
while True:
    a=input()
    url='https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=%s'%a
    te=requests.get(url).json()
    data=te['data']['info']['text']
    print(data)
