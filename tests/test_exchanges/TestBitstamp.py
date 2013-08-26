import unittest
from exchanges.Bitstamp import Bitstamp

class TestBitstamp(unittest.TestCase):
    """
    Bitstamp exchange unittest.
    """
    def setUp(self):
        # set up exchange.
        self.ex = Bitstamp()
        self.d = {'asks': [['93.55', '0.83206841'], ['93.58', '8.07300000'], ['93.65', '1.00000000'], ['93.66', '1.00000000']],
                  'bids': [['93.28', '6.43019329'], ['93.09', '3.40800000'], ['93.08', '1.94700000'], ['93.02', '2.79977423']],
                  'timestamp': '1375158220'}

    def tearDown(self):
        pass

    def test_ask_bid_data(self):
        """
        Test ask_bid_data() - Grabs ask and bid data from a dictionary.
        """
        ask, bid = self.ex.ask_bid_data(self.d)
        self.assertEqual(ask, [['93.55', '0.83206841'], ['93.58', '8.07300000'], ['93.65', '1.00000000'], ['93.66', '1.00000000']])
        self.assertEqual(bid, [['93.28', '6.43019329'], ['93.09', '3.40800000'], ['93.08', '1.94700000'], ['93.02', '2.79977423']])

    def test_clean_data(self):
        """
        Test clean_data() - Puts data in the correct format.
        """
        ask, bid = self.ex.ask_bid_data(self.d)
        self.assertEqual(self.ex.clean_data(ask), [[93.55, 0.83206841], [93.58, 8.07300000], [93.65, 1.00000000], [93.66, 1.00000000]])
        self.assertEqual(self.ex.clean_data(bid), [[93.28, 6.43019329], [93.09, 3.40800000], [93.08, 1.94700000], [93.02, 2.79977423]])

if __name__ == '__main__':
    t = TestBitstamp()
    t.main()







