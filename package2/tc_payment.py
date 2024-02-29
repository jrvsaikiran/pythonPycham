import  unittest
class PaymentTest(unittest.TestCase):
    def test_payment(self):
        print("payment in dollor test")
        self.assertTrue(True)

    def test_Payment(self):
        print("payment in rupees")
        self.assertTrue(True)

if __name__=="__main__":
    unittest.main()