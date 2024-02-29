import unittest

class LoginTest(unittest.TestCase):
    def test_loginByEmail(self):
        print("email login")
        self.assertTrue(True)

    def test_loginByFacebook(self):
        print("facebook login")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()