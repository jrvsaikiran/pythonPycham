import  unittest

from package1.tc1 import LoginTest
from  package1.tc2 import SignUp

from package2.tc_payment import PaymentTest
from package2.tc_paymentreturns import PaymentTestReturns

#get all test from all 4 classes

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignUp)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentTestReturns)

#creating testsuits

sanity = unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner(verbosity=2).run(sanity)





