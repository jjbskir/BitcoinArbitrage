import unittest
import urllib.request
from exchanges import Requests

class  TestRequests(unittest.TestCase):

    def setUp(self):
        self.req = Requests('https://www.bitstamp.net/api/')

    def tearDown(self):
        pass

    def testJson_decode(self):
        url = 'https://www.bitstamp.net/api/ticker/'
        json = urllib.request.urlopen(url)
        #decode = self.req.json_decode(json)
        #self.assertEqual(type(decode), dict)




if __name__ == "__main__":
    TestRequests.main()
