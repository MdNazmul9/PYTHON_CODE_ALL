import unittest
class TestSignup(unittest.TestCase):
    def test_SignupByEmail(self):
        print("SignupBy Email")
        self.assertTrue(True)

    def test_SignupByFacebook(self):
        print("SignupBy Facebook")
        self.assertTrue(True)

    def test_SignupByTwitter(self):
        print("SignupBy Twitter")
        self.assertTrue(True)


if __name__=="__main__":
    unittest.main()