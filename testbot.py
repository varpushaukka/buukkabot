import unittest
import bot

class Testbot(unittest.TestCase):
    tbot = bot.Bot('logs')

    #datastructure = [{sender: x, text: y, group: z, date: d}, {..}] 
    def test_messagelist(self):
        ml = self.tbot.messagelist()
        self.assertIsInstance(ml, list)
        all(self.assertIsInstance(x, dict) for x in ml)
        all(self.assertIn('sender', x) for x in ml)
        all(self.assertIn('text', x) for x in ml)
        all(self.assertIn('group', x) for x in ml)
        all(self.assertIn('date', x) for x in ml)


if __name__ == '__main__':
    unittest.main()
