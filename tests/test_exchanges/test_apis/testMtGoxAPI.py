import unittest
from exchanges.apis.MtGoxAPI import MtGoxAPI


class TestMtGoxAPI(unittest.TestCase):
    """
    Abstract base class for exchanges API. Make sure all the exchanges can access needed data.
    """
    def setUp(self):
        self.api = MtGoxAPI()

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
        depth = self.api.depth()
        self.assertEqual(type(depth), dict)
        self.assertEqual(len(depth), 2)
        self.assertEqual(type(depth['result']), str)
        self.assertEqual(type(depth['data']), dict)
        self.assertEqual(type(depth['data']['asks']), list)
        self.assertEqual(type(depth['data']['bids']), list)
        self.assertEqual(type(depth['data']['asks'][0]), dict)
        self.assertEqual(type(depth['data']['bids'][0]), dict)
        self.assertEqual(len(depth['data']['asks'][0]), 5)
        self.assertEqual(len(depth['data']['bids'][0]), 5)


if __name__ == '__main__':
    t = TestMtGoxAPI()
    t.main()