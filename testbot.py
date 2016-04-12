import unittest
import bot

class Testbot(unittest.TestCase):
    
    #datastructure = [{sender: x, messagetext: y, group: z, date: d}, {..}] 
    def messagelisttest(self):
        testbot = bot.Bot('logs')
        ml = self.testbot.messagelist()
        self.assertIsInstance(ml, list)

if __name__ == '__main__':
    unittest.main()
