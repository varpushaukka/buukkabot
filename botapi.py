from bottle import route, run, request
import sqlite3

class BotApi:
    
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.cur = self.conn.cursor()

    @route('/searchlogs')
    def search_from_log_data(self):
        param = self.request.decode()
        return 'foo'    
    
if __name__ == '__main__':
    a = BotApi('logs')
    run(host='localhost', port=8080)
