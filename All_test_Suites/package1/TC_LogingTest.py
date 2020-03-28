import unittest
class TestLogin(unittest.TestCase):
    def test_logingEmail(self):
        print("logging Email")
        self.assertTrue(True)

    def test_logingFacebook(self):
        print("logging Facebook")
        self.assertTrue(True)

    def test_logingTwitter(self):
        print("logging Twitter")
        self.assertTrue(True)


if __name__=="__main__":
    unittest.main()