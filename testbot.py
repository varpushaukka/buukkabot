import unittest
import bot

class Testbot(unittest.TestCase):
    tbot = bot.Bot('logs')

    #datastructure = [{sender: x, text: y, group: z, date: d, id: i}, {..}] 
    def test_messagelist(self):
        ml = self.tbot.messagelist()
        self.assertIsInstance(ml, list)
        for x in ml: self.assertIsInstance(x, dict)
        self.rightvaluesfound('sender', ml)
        self.rightvaluesfound('text', ml)
        self.rightvaluesfound('group', ml)
        self.rightvaluesfound('date', ml)
        self.rightvaluesfound('msgid', ml)

    def rightvaluesfound(self, field, ml):
        for x in ml: self.assertIn(field, x)

if __name__ == '__main__':
    unittest.main()
