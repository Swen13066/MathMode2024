from datetime import datetime
from time import sleep
import requests


def print_message(message):
    t = message['time']
    dt = datetime.fromtimestamp(t)
    print(dt.strftime('%Y-%m-%d %H:%M:%S'), message['name'])
    print(message['text'])


def help():
    print('smt useful')


after = 0
while True:
    response = requests.get('http://127.0.0.1:5000/messages', params={'after': after})
    messages = response.json()['messages']

    for message in messages:
        print_message(message)
        if '/help' in message['text']:
            help()
        print(" ")
    after = message['time']
    sleep(1)
