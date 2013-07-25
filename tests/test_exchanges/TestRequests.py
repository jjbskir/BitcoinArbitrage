import unittest
import urllib.request
from exchanges.Requests import Requests


class TestRequests(unittest.TestCase):
    '''
    Test HTTP requests for POST and GET.
    '''
    def setUp(self):
        self.req = Requests('https://www.bitstamp.net/api/')

    def tearDown(self):
        pass

    def testJson_decode(self):
        '''
        Test json_decode() - JSON decoder.
        '''
        url = 'https://www.bitstamp.net/api/ticker/'
        json = urllib.request.urlopen(url)
        decode = self.req.json_decode(json)
        self.assertEqual(type(decode), dict)

    def testGet(self):
        '''
        Test get() - HTTP GET request.
        '''
        ext = 'order_book/'
        params = {"group": 0}
        # get request with just extension.
        get1 = self.req.get(ext)
        self.assertEqual(type(get1), dict)
        # get request with extension and parameters. Should give different result then last get.
        get2 = self.req.get(ext, params)
        self.assertEqual(type(get2), dict)
        self.assertNotEqual(get1, get2)
        # bad url extension. Should give warning.
        ext_bad = 'bad/'
        get3 = self.req.get(ext_bad)
        self.assertEqual(get3, None)
        self.assertEqual(self.req.URLError, 'NOT FOUND')

