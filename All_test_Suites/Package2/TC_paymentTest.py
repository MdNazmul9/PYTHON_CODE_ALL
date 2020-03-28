import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentDolar(self):
        print("This is test payment by dolar")
        self.assertTrue(True)

    def test_paymentTk(self):
        print("This is test payment by TK")
        self.assertTrue(True)


if __name__=="__main__":
    unittest.main()