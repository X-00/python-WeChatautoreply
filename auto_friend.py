import itchat
import requests
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'   
    data = {
        'key': 'ce697b3fc8b54d5f88c2fa59772cb2cf',  # Tuling Key或者key='fe597ce1cbca442f9f3da027f58ec2a7' 
        'info': msg, 
        'userid': 'wechat-robot', 
    }
    r= requests.post(apiUrl, data=data).json()
    # print(r)
    # print(r.get('text'))
    return r.get('text')

@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return get_response(msg['Text'])

#enableCmdQR=True让二维码显示到命令行上
#扫码登录后，如果想退出程序以后还暂存登录状态，重新执行程序也不用扫码可以添加参数hotReload=True
itchat.auto_login(enableCmdQR=True,hotReload=True)
itchat.run()

'''
2.自动回复相同的别人发给自己的消息
import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text

itchat.auto_login()
itchat.run()
'''



'''
1：给文件传输助手发送hello world
import itchat

itchat.auto_login()     (登录)  
itchat.send_msg("hello world.",  toUserName='filehelper')
'''