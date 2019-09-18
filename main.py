import requests
testoOriginale=Hook['params']['message']['text']
idChat=Hook['params']['message']['chat']['id']
a=716510924-1
URL='https://api.telegram.org/bot%d:AAH1jYsnJLWy13jfq4rzQITu7A4U_jnDWCc/sendMessage'%a
req=requests.get(URL,verify=False,data={'chat_id':idChat,'text':testoOriginale})
