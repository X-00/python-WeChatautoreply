import itchat
import requests
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'   
    data = {
        'key': 'ce697b3fc8b54d5f88c2fa59772cb2cf',  # Tuling Key 
        'info': msg, 
        'userid': 'wechat-robot', 
    }
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return get_response(msg['Text'])
@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)

def print_content(msg):
    return get_response(msg['Text'])
itchat.auto_login(True)
itchat.run()