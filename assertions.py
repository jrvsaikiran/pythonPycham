import  unittest
from selenium import webdriver


class Test(unittest.TestCase):
    def testName(self):


       # driver=webdriver.Chrome(executable_path="F:\pycharm\drivers\chromedriver.exe")
       # driver.get("https://www.google.com/")
       # webtitle=driver.title

        #asserts
       # self.assertEqual("Google",webtitle,"webtitle is not same")
        #self.assertNotEqual("Google2",webtitle,"webtitle is same")
        #self.assertTrue(webtitle=="Google")
        #self.assertFalse(webtitle=="Google")
        #self.assertIsNone(webtitle)
        #self.assertIsNotNone(webtitle)


        # list ={"sai","jrv","kiran"}
        # self.assertIn("jrv",list)
        # self.assertNotIn("jrv",list)

        self.assertGreater(10,2)
        self.assertLess(2,4)
        self.assertGreaterEqual(2,2)
        self.assertLessEqual(20,20)




if __name__=="__main__":
    unittest.main()










