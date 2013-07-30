import unittest
from exchanges.AbstractExchange import AbstractExchange
from exchanges.Bitstamp import Bitstamp


class TestAbstractExchange(unittest.TestCase):
    """
    Abstract base class for exchanges API. Make sure all the exchanges can access needed data.
    """
    def setUp(self):
        # set up exchange that implements basic abstract.
        self.ex = AbstractTest()
        # implements abstract with actual methods.
        self.bitstamp = Bitstamp()
        self.d = {'asks': [['93.55', '0.83206841'], ['93.58', '8.07300000'],
                               ['93.65', '1.00000000'], ['93.66', '1.00000000']],
                  'bids': [['93.28', '6.43019329'], ['93.09', '3.40800000'],
                                ['93.08', '1.94700000'], ['93.02', '2.79977423']],
                  'timestamp': '1375158220'}

    def tearDown(self):
        pass

    def test_init(self):
        """
        Test __init__() - make sure class is setup correctly.
        """
        self.assertEqual(self.ex.api, None)
        self.assertEqual(self.bitstamp.api.__class__.__name__, "BitstampAPI")

    def test_import_api(self):
        """
        Test import_api() - Imports api class for exchange.
        """
        self.assertEqual(self.ex.import_api(), None)
        self.assertEqual(self.bitstamp.import_api().__class__.__name__, "BitstampAPI")

    def test_ask_bid_data(self):
        """
        Test depth() -
        """
        # stop error from occuring by creating depth() mathod.
        self.assertEqual(self.ex.ask_bid_data(), None)

    def test_extract_prices_amounts(self):
        """
        Test extract_prices_amounts() -
        """
        self.assertEqual(self.ex.extract_prices_amounts(), None)

    def test_weighted_avg(self):
        """
        Test weighted_avg() - Calculate average.
        """
        prices = [1 for i in range(10)]
        amounts = [1 for i in range(10)]
        self.assertEqual(self.ex.weighted_avg(prices, amounts), 1)
        prices = [1.2, 3.5, 2.5, 7.1, 8.9]
        amounts = [0.5, 2.3, 1.2, 4.5, 1.0]
        self.assertEqual(self.ex.weighted_avg(prices, amounts), 5.5263157894736832)
        prices = [0]
        amounts = [0]
        self.assertEqual(self.ex.weighted_avg(prices, amounts), None)
        prices = [93.28, 93.09, 93.08, 93.02]
        amounts = [6.43019329, 3.408, 1.947, 2.79977423]
        self.assertEqual(self.ex.weighted_avg(prices, amounts), 93.158994499138942)
        self.assertEqual(self.bitstamp.weighted_avg(prices, amounts), 93.158994499138942)

    def test_weighted_std(self):
        """
        Test weighted_std() - Calculate standard deviation.
        """
        prices = [1 for i in range(10)]
        amounts = [1 for i in range(10)]
        self.assertEqual(self.ex.weighted_std(prices, amounts), 0.0)
        prices = [93.28, 93.09, 93.08, 93.02]
        amounts = [6.43019329, 3.408, 1.947, 2.79977423]
        self.assertEqual(self.ex.weighted_std(prices, amounts), 0.11004284568677422)
        self.assertEqual(self.bitstamp.weighted_std(prices, amounts), 0.11004284568677422)

    def test_create_dict(self):
        '''
        Test create_dict() -  Creates a dictionary.
        '''
        ask = 1
        bid = 2
        self.assertEqual(self.ex.create_dict(ask, bid), {'ask': 1, 'bid': 2})

    def test_calculate_price(self):
        """
        Test calculate_price() - Calculate the price from a list.
        """
        asks, bids = self.bitstamp.ask_bid_data(self.d)
        ask_price = self.bitstamp.calculate_price(asks)
        bid_price = self.bitstamp.calculate_price(bids)
        self.assertEqual(round(ask_price, 1), 93.599999999999994 )
        self.assertEqual(bid_price, 93.158994499138942 )

    def test_calculate_bis_ask_prices(self):
        """
        Test calculate_bis_ask_prices() - calculate a bid and ask price.
        Not sure how to test because it should be different each time. Uses API data.
        ALl the functions within it have been tested.
        """
        self.assertEqual(type(self.bitstamp.calculate_bis_ask_prices()), dict)

class AbstractTest(AbstractExchange):
    '''
    Test including AbstractExchangeAPI in another class.
    '''
    def __init__(self):
        super(AbstractTest, self).__init__()
    def ask_bid_data(self):
        return None
    def extract_prices_amounts(self):
        return None


if __name__ == '__main__':
    t = TestAbstractExchange()
    t.main()