from bottle import route, run
import sqlite3

class BotApi:
    
    def __init__(self, dbname):
        self.conn = sqlite3.connect(dbname)
        self.cur = self.conn.cursor()

    @route('/searchbyuser/<user>')    
    def search_by_user(user):
        return 'foo'
    
    @route('/searchbydate/<date>')
    def search_by_date(date):
        return 'foo'

    @route('/searchbygroup/<group>')
    def search_by_group(group):
        return 'foo'

    @route('searchbyword/<word>')
    def search_by_word(word):
        return 'foo'

if __name__ == '__main__':
    a = BotApi('logs')
    run(host='localhost', port=8080)
