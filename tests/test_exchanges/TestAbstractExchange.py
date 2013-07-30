import unittest
from exchanges.AbstractExchange import AbstractExchange


class TestAbstractExchange(unittest.TestCase):
    """
    Abstract base class for exchanges API. Make sure all the exchanges can access needed data.
    """
    def setUp(self):
        # set up exchange.
        self.ex = AbstractTest()

    def tearDown(self):
        pass

    def test_init(self):
        """
        Test __init__() - make sure class is setup correctly.
        """
        self.assertEqual(self.ex.api, None)

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

    def test_weighted_std(self):
        """
        Test weighted_std() - Calculate standard deviation.
        """
        prices = [1 for i in range(10)]
        amounts = [1 for i in range(10)]
        self.assertEqual(self.ex.weighted_std(prices, amounts), 0.0)

    def test_create_dict(self):
        '''
        Test create_dict() -  Creates a dictionary.
        '''
        ask = 1
        bid = 2
        self.assertEqual(self.ex.create_dict(ask, bid), {'ask': 1, 'bid': 2})

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