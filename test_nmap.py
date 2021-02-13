import unittest
from nmap import validate_url
class SampleTest(unittest.TestCase):
   # return True or False
   def test_urlValidation(self):
      self.assertTrue(validate_url("www.bks-ks.org"))   
      self.assertTrue(validate_url("www.fiek.uni-pr.edu"))
      self.assertTrue(validate_url("http://www.bks-ks.org"))
      self.assertFalse(validate_url("vvv.badurl.de.com.smh"))
      self.assertFalse(validate_url("192.124.1.4.5.2.25.50"))
      self.assertTrue(validate_url("51.254.123.235"))


# running the test
unittest.main()