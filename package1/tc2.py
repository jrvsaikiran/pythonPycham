import unittest

class SignUp(unittest.TestCase):
    def test_signupemail(self):
        print("email signup")
        self.assertTrue(True)

    def test_signupFacebook(self):
        print("facebook signup")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()