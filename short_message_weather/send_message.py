from twilio.rest import Client
from weather import get_weather
import time

account = 'ACbd65e496ac7e704b2935678763448e1f'
token = '9e63d8fd3c3e6b592f886628380836e1'


def send_message(location):
    client = Client(account, token)
    weather_message = get_weather(location)
    message = client.messages.create(
        from_='+12085475915',
        to='+8615990184749',
        body=weather_message
    )
    print(message.sid)


if __name__ == '__main__':
    print('running...')
    while True:
        hour = time.strftime('%H', time.localtime())
        if hour == '6' or hour == '06':
            print('{} 短信正在发送...'.format(time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())))
            send_message('淳安')
            print('{} 短信发送成功...'.format(time.strftime('%Y/%m/%d %H:%M:%S',time.localtime())))
        time.sleep(3600)
