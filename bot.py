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
        parsedlist = []
        for x in msglist:
            parsedlist.append(self.parsemessage(x))
        return(parsedlist)

    def parsemessage(self, m):
        mgrouptype = m['message']['chat']['type']
        mdate = m['message']['date']
        msender = m['message']['from']['first_name'] + " " + m['message']['from']['last_name']
        mtext = m['message']['text']
        mmsgid = m['message']['message_id']
        return dict(msgid=mmsgid, date=mdate, sender=msender, text = mtext, grouptype = mgrouptype)
        

if __name__ == '__main__':
    b = Bot('logs')    
    print(b.messagelist())
