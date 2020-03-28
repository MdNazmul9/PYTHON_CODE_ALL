import unittest

#get all test from logingTest, signupTest, paymentTest, PaymentReturnTest
from package1.TC_LogingTest import TestLogin
from package1.TC_test_signUp import TestSignup

from Package2.TC_paymentReturnsTest import PaymentReturnTest
from Package2.TC_paymentTest import PaymentTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestSignup)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)

#creating test
sanityTestSuite = unittest.TestSuite([tc1,tc2]) #sanity test suite
functionalTestSuite = unittest.TestSuite([tc3,tc4]) #functional test suite
masterTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4]) #master test suiteS

#unittest.TextTestRunner().run(sanityTestSuite)
#unittest.TextTestRunner().run(functionalTestSuite)
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)