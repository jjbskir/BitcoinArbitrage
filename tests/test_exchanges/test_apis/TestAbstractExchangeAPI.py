import unittest
from exchanges.apis.AbstractExchangeAPI import AbstractExchangeAPI


class TestAbstractExchangeAPI(unittest.TestCase):
    """
    Abstract base class for exchanges API. Make sure all the exchanges can access needed data.
    """
    def setUp(self):
        self.api = AbstractTest()

    def tearDown(self):
        pass

    def test_init(self):
        """
        Test __init__() - make sure class is setup correctly.
        """
        self.assertEqual(self.api.req.__class__.__name__, 'Requests')

    def test_depth(self):
        """
        Test depth() -
        """
        # stop error from occuring by creating depth() mathod.
        self.assertEqual(self.api.depth(), None)

class AbstractTest(AbstractExchangeAPI):
    '''
    Test including AbstractExchangeAPI in another class.
    '''
    def __init__(self):
        baseURL = 'https://www.bitstamp.net/api/'
        super(AbstractTest, self).__init__(baseURL)
    def depth(self):
        return None


if __name__ == '__main__':
    t = TestAbstractExchangeAPI()
    t.main()