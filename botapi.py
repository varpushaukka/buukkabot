from bottle import route, run

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
