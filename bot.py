#python3
from bottoken import token
import requests
import json
import sqlite3

class Bot:

    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.cur = self.conn.cursor()

    def messagelist(self):
        r = requests.get('https://api.telegram.org/bot' + token + '/getUpdates')
        messages = r.content
        jsonmessages = json.loads(messages.decode('utf-8'))
        msglist = jsonmessages['result']
        return(msglist)

if __name__ == '__main__':
    b = Bot('logs')    
    print(b.messagelist())
