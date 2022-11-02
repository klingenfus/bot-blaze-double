import requests
import json
import time
from tele_msg import msg_red, msg_black, wmsg_red, wmsg_black, url_red, win_red, url_black, win_black

while True:
    data = requests.get('https://blaze.com/api/roulette_games/recent')
    result = json.loads(data.content)
    print(result)

    values = [x['color'] for x in result]

    def color(x):
        if x == 0:
            return 'white'
        if x == 1:
            return 'red'
        if x == 2:
            return 'black'

    maps = map(color, values)

    final_color = list(maps)
    print(final_color)

    def send_msg(number):
        if number[0:3] == ['red', 'red', 'red']:
            requests.get(url_red)
            print('🚀sent red')

        elif number[0:3] == ['black', 'black', 'black']:
            requests.get(url_black)
            print('🚀sent black')

        elif number[0:4] == ['black', 'red', 'red', 'red']:
            requests.get(win_red)
            print('🚀sent win red')

        elif number[0:4] == ['red', 'black', 'black', 'black']:
            requests.get(win_black)
            print('🚀sent win black')


    send_msg(final_color)
    time.sleep(30)

