token = 'YOUR_TOKEN'
chat_id = 'YOUR_CHAT_ID'

msg_red = f'''

    💰ENTRADA CONFIRMADA💰

    👉APOSTE NO PRETO ⚫
    👉PROTEÇÃO NO ⚪

    '''

msg_black = f'''

    💰ENTRADA CONFIRMADA💰

    👉APOSTE NO VERELHO 🔴
    👉PROTEÇÃO NO ⚪

    '''

wmsg_red = f'''

    💰RESULTADO DA APOSTA:

    Green✅✅✅✅✅
    ➡️➡️⚫
    '''

wmsg_black = f'''

    💰RESULTADO DA APOSTA:

    Green✅✅✅✅✅
    ➡️➡️🔴

    '''

url_red = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg_red}'
win_red = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={wmsg_red}'
url_black = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg_black}'
win_black = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={wmsg_black}'