import unittest
from exchanges.apis.BitstampAPI import BitstampAPI


class TestBitstampAPI(unittest.TestCase):
    """
    Abstract base class for exchanges API. Make sure all the exchanges can access needed data.
    """
    def setUp(self):
        self.api = BitstampAPI()

    def tearDown(self):
        pass

    def test_init(self):
        """
        Test __init__() - make sure class is setup correctly.
        """
        pass

    def test_depth(self):
        """
        Test depth() - Make sure it is the correct return structure.
        """
        depth1 = self.api.depth()
        self.assertEqual(type(depth1), dict)
        self.assertTrue(type(depth1['asks']), list)
        self.assertTrue(type(depth1['bids']), list)
        self.assertGreater(len(depth1['asks']), 1)
        self.assertGreater(len(depth1['bids']), 1)
        self.assertEqual(len(depth1['asks'][0]), 2)
        self.assertEqual(len(depth1['bids'][0]), 2)
        depth2 = self.api.depth(ordergrouping=0)
        self.assertEqual(type(depth2), dict)
        self.assertNotEqual(depth1, depth2)


if __name__ == '__main__':
    t = TestBitstampAPI()
    t.main()