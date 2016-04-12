import unittest
import bot

class Testbot(unittest.TestCase):
    tbot = bot.Bot('logs')

    #datastructure = [{sender: x, text: y, type: z, date: d, id: i}, {..}] 
    def test_messagelist(self):
        ml = self.tbot.messagelist()
        self.assertIsInstance(ml, list)
        all(self.assertIsInstance(x, dict) for x in ml)
        all(self.assertIn('sender', x) for x in ml)
        all(self.assertIn('text', x) for x in ml)
        all(self.assertIn('grouptype', x) for x in ml)
        all(self.assertIn('date', x) for x in ml)
        all(self.assertIn('msgid', x) for x in ml)


if __name__ == '__main__':
    unittest.main()
