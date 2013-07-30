import unittest
from exchanges.Bitstamp import Bitstamp

class TestBitstamp(unittest.TestCase):
    """
    Bitstamp exchange unittest.
    """
    def setUp(self):
        # set up exchange.
        self.ex = Bitstamp()
        self.d = {'asks': [['93.55', '0.83206841'], ['93.58', '8.07300000'],
                               ['93.65', '1.00000000'], ['93.66', '1.00000000']],
                  'bids': [['93.28', '6.43019329'], ['93.09', '3.40800000'],
                                ['93.08', '1.94700000'], ['93.02', '2.79977423']],
                  'timestamp': '1375158220'}

    def tearDown(self):
        pass

    def test_ask_bid_data(self):
        """
        Test ask_bid_data() - Grabs ask and bid data from a dictionary.
        """
        ask, bid = self.ex.ask_bid_data(self.d)
        self.assertEqual(ask, self.d['asks'])
        self.assertEqual(bid, self.d['bids'])

    def test_extract_prices_amounts(self):
        """
        Test extract_prices_amounts() - extracts price and amounts from bids or asks.
        """
        ask, bid = self.ex.ask_bid_data(self.d)
        prices, amounts = self.ex.extract_prices_amounts(ask)
        self.assertEqual(prices, [93.55, 93.58, 93.65, 93.66])
        self.assertEqual(amounts, [0.83206841, 8.07300000, 1.00000000, 1.00000000])
        prices, amounts = self.ex.extract_prices_amounts(bid)
        self.assertEqual(prices, [93.28, 93.09, 93.08, 93.02])
        self.assertEqual(amounts, [6.43019329, 3.40800000, 1.94700000, 2.79977423])

if __name__ == '__main__':
    t = TestBitstamp()
    t.main()







