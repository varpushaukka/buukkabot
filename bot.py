#python3
from bottoken import token
import requests
import json
import sqlite3
import time

class Bot:

    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.cur = self.conn.cursor()

    def messagelist(self):
        while True:
            r = requests.get('https://api.telegram.org/bot' + token + '/getUpdates')
            messages = r.content
            jsonmessages = json.loads(messages.decode('utf-8'))
            msglist = jsonmessages['result']
            parsedlist = []
            for x in msglist:
                parsedlist.append(self.parsemessage(x))
            time.sleep(3)
            return(parsedlist)

    def parsemessage(self, m):
        mgroup = m['message']['chat']['type']
        mdate = m['message']['date']
        msender = m['message']['from']['first_name'] + " " + m['message']['from']['last_name']
        mtext = m['message']['text']
        mmsgid = m['message']['message_id']
#        self.cur.execute('INSERT into messages VALUES (%i, %s, %i, %s, %s)', (mmsgid, mgroup, mdate, msender, mtext))
#        self.conn.commit()
        return dict(msgid=mmsgid, date=mdate, sender=msender, text = mtext, group = mgroup)
        

if __name__ == '__main__':
    b = Bot('logs')    
    print(b.messagelist())
