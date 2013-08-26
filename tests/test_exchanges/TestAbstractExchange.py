import unittest
from exchanges.AbstractExchange import AbstractExchange
from exchanges.Bitstamp import Bitstamp


class TestAbstractExchange(unittest.TestCase):
    """
    Abstract base class for exchanges API. Make sure all the exchanges can access needed data.
    Test using a fake Abstract test class and Bitstamp exchange class.
    """
    def setUp(self):
        # set up exchange that implements basic abstract.
        self.ex = AbstractTest()
        # implements abstract with actual methods.
        self.bitstamp = Bitstamp()
        # made up small API depth data to test weather abstract exchanges work.
        self.d = {'asks': [['93.55', '0.83206841'], ['93.58', '8.07300000'], ['93.65', '1.00000000'], ['93.66', '1.00000000']],
                  'bids': [['93.28', '6.43019329'], ['93.09', '3.40800000'], ['93.08', '1.94700000'], ['93.02', '2.79977423']],
                  'timestamp': '1375158220'}

    def tearDown(self):
        pass

    def test_init(self):
        """
        Test __init__() - make sure class is setup correctly.
        """
        self.assertEqual(self.ex.api, None)
        self.assertEqual(self.ex.fee.fees, None)
        self.assertEqual(self.bitstamp.api.__class__.__name__, "BitstampAPI")
        self.assertEqual(self.bitstamp.fee.fees,
                         dict(trading=0.005, base=0.0, withdrawal_perc=0.0009, withdrawal_base=0.0, withdrawal_min=15.0,
                              deposit_perc=0.001, deposit_base=0.0, deposit_min=15.0))

    def test_import_api(self):
        """
        Test import_api() - Imports api class for exchange.
        """
        self.assertEqual(self.ex.import_api(), None)
        self.assertEqual(self.bitstamp.import_api().__class__.__name__, "BitstampAPI")

    def test_import_fee(self):
        """
        Test import_fee() - Import fee class.
        """
        fee = self.ex.import_fee()
        self.assertEqual(fee.fees, None)
        fee = self.bitstamp.import_fee()
        self.assertEqual(fee.fees,
                         dict(trading=0.005, base=0.0, withdrawal_perc=0.0009, withdrawal_base=0.0, withdrawal_min=15.0,
                              deposit_perc=0.001, deposit_base=0.0, deposit_min=15.0))

    def test_depth(self):
        """
        Test depth() - calculate a bid and ask depth.
        Not sure how to test because it should be different each time. Uses API data.
        ALl the functions within it have been tested, so it should work fine.
        """
        self.assertEqual(type(self.bitstamp.depth()), dict)

    def test_clean_data_helper(self):
        """
        Test clean_data_helper() -  Cleans data for being sorted.
        Make sure data is in correct format [[price, amount],...,[price, amount]] and is type float.
        """
        asks, bids = self.bitstamp.ask_bid_data(self.d)
        ask_list = self.ex.clean_data_helper(asks, 0, 1)
        self.assertEqual(type(ask_list[0][0]), float)
        self.assertEqual(ask_list, [[93.55, 0.83206841], [93.58, 8.07300000], [93.65, 1.00000000], [93.66, 1.00000000]])
        bid_list = self.ex.clean_data_helper(bids, 0, 1)
        self.assertEqual(bid_list, [[93.28, 6.43019329], [93.09, 3.40800000], [93.08, 1.94700000], [93.02, 2.79977423]])

    def test_sort_depth(self):
        """
        Test sort_depth() - sorts data numerically.
        """
        asks, bids = self.bitstamp.ask_bid_data(self.d)
        ask_list = self.ex.clean_data_helper(asks, 0, 1)
        ask_ordered = self.ex.sort_depth(ask_list, False)
        self.assertNotEqual(ask_ordered, [[93.66, 1.00000000], [93.55, 0.83206841], [93.58, 8.07300000], [93.65, 1.00000000]])
        self.assertEqual(ask_ordered, [[93.55, 0.83206841], [93.58, 8.07300000], [93.65, 1.00000000], [93.66, 1.00000000]]) # sort ask data ascending.
        bid_list = self.ex.clean_data_helper(bids, 0, 1)
        bid_ordered = self.ex.sort_depth(bid_list, True)
        self.assertNotEqual(ask_ordered, [[93.28, 6.43019329], [93.02, 2.79977423], [93.09, 3.40800000], [93.08, 1.94700000]])
        self.assertEqual(bid_ordered, [[93.28, 6.43019329], [93.09, 3.40800000], [93.08, 1.94700000], [93.02, 2.79977423]]) # sort bid data descending.

    def test_create_dict(self):
        '''
        Test create_dict() -  Creates a dictionary.
        '''
        ask = 1
        bid = 2
        self.assertEqual(type(self.ex.create_dict(ask, bid)), dict) # return type is correct.
        self.assertEqual(self.ex.create_dict(ask, bid), {'ask': 1, 'bid': 2}) # data put in correct order.

    def test_exchange(self):
        """
        Exchange from USD -> Bitcoins through a exchange.
        Exchange from Bitcoins -> USD through a exchange.
        """
        depth_data = {'ask': [[93.55, 0.83206841], [93.58, 8.07300000], [93.65, 1.00000000], [93.66, 1.00000000]],
                      'bid': [[93.28, 6.43019329], [93.09, 3.40800000], [93.08, 1.94700000], [93.02, 2.79977423]]}
        # test return types are correct for different scenarios.
        self.assertEqual(self.bitstamp.exchange(depth_data, usd=None, b=None), None)
        self.assertEqual(self.bitstamp.exchange(depth_data, usd=1, b=1), None)
        self.assertNotEqual(type(self.bitstamp.exchange(depth_data, usd=1)), None)
        self.assertNotEqual(type(self.bitstamp.exchange(depth_data, b=1)), None)
        # exchange from USD -> Bitcoins.
        self.assertEqual(self.bitstamp.exchange(depth_data, usd=50), 0.53180117584179587)
        self.assertEqual(self.bitstamp.exchange(depth_data, usd=77.8399997555), 0.82790806794999994)
        self.assertEqual(self.bitstamp.exchange(depth_data, usd=200), 2.1267881731356968)
        # exchange from Bitcoins -> USD.
        self.assertEqual(self.bitstamp.exchange(depth_data, b=0.5), 46.406800000000004)
        self.assertEqual(self.bitstamp.exchange(depth_data, b=10.0),  927.4595180647101)

    def test_exchange_depth(self):
        """
        Test exchange_depth() - Find the needed depth at a exchange in order for a exchange to occur.
        """
        depth_data = {'ask': [[93.55, 0.83206841], [93.58, 8.07300000], [93.65, 1.00000000], [93.66, 1.00000000]],
                      'bid': [[93.28, 6.43019329], [93.09, 3.40800000], [93.08, 1.94700000], [93.02, 2.79977423]]}
        # exchange from USD -> Bitcoins.
        self.assertEqual(self.bitstamp.exchange_depth(depth_data, usd=50), [[93.55, 0.5344735435595938]])
        self.assertEqual(self.bitstamp.exchange_depth(depth_data, usd=77.8399997555), [[93.55, 0.83206841]])
        self.assertEqual(self.bitstamp.exchange_depth(depth_data, usd=200), [[93.55, 0.83206841], [93.58, 1.3054071408901464]])
        # exchange from Bitcoins -> USD.
        self.assertEqual(self.bitstamp.exchange_depth(depth_data, b=0.5), [[93.28, 0.5]])
        self.assertEqual(self.bitstamp.exchange_depth(depth_data, b=10.0),  [[93.28, 6.43019329], [93.09, 3.408], [93.08, 0.16180671000000135]])

    def test_ask_bid_data(self):
        """
        Test depth() - Abstract function.
        stop error from occuring by creating depth() mathod.
        """
        self.assertEqual(self.ex.ask_bid_data(), None)

    def test_clean_data(self):
        """
        Test clean_data() - Abstract function. Stops error from occuring in AbstractTest Class.
        """
        self.assertEqual(self.ex.clean_data(), None)



class AbstractTest(AbstractExchange):
    '''
    Make sure Abstract functions get called.
    '''
    def __init__(self):
        super(AbstractTest, self).__init__()
    def ask_bid_data(self):
        return None
    def clean_data(self):
        return None


if __name__ == '__main__':
    t = TestAbstractExchange()
    t.main()