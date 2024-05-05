import unittest
import pandas as pd
from user import App


# из-зи того что у нас граф юзер интерфейс мы не можем так просто протестировать весь функционал 
class TestApp(unittest.TestCase):


    def test_load_App_data(self):
        # Test loading App data from a file
        data = App.load_user_data(App,'user_data.json') # 
        self.assertIsInstance(data, dict) # если все ок то загружаем словать
        self.assertEqual(data['topic'], 'Programming_Vocabulary')
        self.assertEqual(data['timer'], "5")
        self.assertEqual(data['window_position'], '520+390')


    def test_load_words(self):
        df = App.load_words(App, '/Users/togzhandikhan/Documents/Simple-Dimle-English/topics/Medical_Vocabulary.xlsx')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.iat[1, 0], "diagnosis")
        self.assertEqual(df.iat[1, 1], "диагноз")



if __name__ == '__main__':
    unittest.main()
