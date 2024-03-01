from datetime import datetime
from time import sleep
import requests


def print_message(message):
    t = message['time']
    dt = datetime.fromtimestamp(t)
    print(dt.strftime('%Y-%m-%d %H:%M:%S'), message['name'])
    print(message['text'])


def help():
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'bot')
    print('''Проект для дз номер 3 \n
    __________\n
    Проект состоит из 3 основных частей:  \n
    - server — сервер, который хранит наш мессенджер и поддерживает 
    браузерные странички /index, /status\n
    - sender — файл, поддерживающий отправку сообщений от некоторго польователя\n
    - reciver — файл, который обеспечивает прием и вывод сообщений \n 
    \n
    Чтобы запстить весь проект целиком, нужно исполнить в командной строке  
    python server.py  \n
    Далее  в любом порядке нужно запустить остальные 2 файла  
    python sender.py\n
    python reciver.py  \n
    \n
    Так же если отправить команду /help в reciver.py,
    то это сообщение будет выведено
    ''')


if __name__ == "__main__":
    after = 0
    while True:
        response = requests.get('http://127.0.0.1:5000/messages', params={'after': after})
        messages = response.json()['messages']

        for message in messages:
            print_message(message)
            if message['text'] == '/help':

                help()
            print(" ")
        after = message['time']
        sleep(1)
