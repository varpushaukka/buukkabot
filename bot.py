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
        self.offset = 0

    def getupdatestolist(self):
        if self.offset == 0: r = requests.get('https://api.telegram.org/bot' + token + '/getUpdates')
        else: r = requests.get('https://api.telegram.org/bot' + token + '/getUpdates?offset=' +  str(self.offset))
        messages = r.content
        jsonmessages = json.loads(messages.decode('utf-8'))
        msglist = jsonmessages['result']
        if msglist == []: offset = 0      
        else: self.offset = msglist[-1]['update_id'] + 1
        return msglist

    def messagelist(self):
        msglist = self.getupdatestolist()
        parsedlist = []
        for x in msglist:
            parsedlist.append(self.parsemessage(x))
        return(parsedlist)

    def grouptitle(self, m):
        if m['message']['chat']['type'] == 'private': return 'private'
        else: return m['message']['chat']['title']

    def parsemessage(self, m):
        ms = m['message']
        mgroup = self.grouptitle(m)
        mdate = ms['date']
        msender = ms['from']['first_name'] + " " + ms['from']['last_name']
        mtext = ms['text']
        mmsgid = ms['message_id']
        return dict(msgid=mmsgid, date=mdate, sender=msender, text = mtext, group = mgroup)

    def savetodatabase(self, msg):
        self.cur.execute('INSERT into messages VALUES (?, ?, ?, ?, ?)', (msg['msgid'], msg['group'], msg['date'], msg['sender'], msg['text']))
        self.conn.commit()
        
    def runbot(self):
        while True:
            messages = self.messagelist()            
            if messages:
                for message in messages:
                    self.savetodatabase(message)
                    print(message)
            time.sleep(3)

if __name__ == '__main__':
    b = Bot('logs')
    b.runbot()    
    print(b.messagelist())
