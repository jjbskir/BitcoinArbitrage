from exchanges.fees.Fees import Fees
import importlib
import numpy as np
import math

class AbstractExchange(object):
    '''
    Abstract class for all the other exchanges.
    '''
    def __init__(self):
        self.api = self.import_api()
        self.fee = self.import_fee()

    def import_api(self):
        """
        Import API objects.

        :return: api associated with each object.
        """
        class_name = self.__class__.__name__ + 'API'
        package = 'exchanges.apis.' + class_name
        api = None
        try:
            # create an api variable.
            api = importlib.import_module(package)
            api = getattr(api, class_name)
            api = api()
        except ImportError:
            print('Could not import module')
        return api

    def import_fee(self):
        """
        Load fee structure for the class.

        :return: fee structure.
        """
        fees = Fees()
        fee = fees.get_fee(self.__class__.__name__)
        return fee

    def depth(self):
        """
        The main method for this class. Used to make sure abstract classes are called.

        :return: Dictionary with list of ask and bid prices and amounts
        """
        depth_data = self.api.depth() # grab api depth data.
        asks, bids = self.ask_bid_data(depth_data) # grab ask and bid data from dictionary. Puts it in specific format
        asks_ordered = self.sort_depth(asks, False) # calculate the ask price.
        bids_ordered = self.sort_depth(bids, True) # calculate the bid price.
        return self.create_dict(asks_ordered, bids_ordered) # add ask and bid prices to a dictionary to return.

    def sort_depth(self, asks_or_bids, rev=False):
        """
        Sorts ask or bid data. Ask data gets sorted ascending.Bid data descending.

        :param asks_or_bids: Either a list of bid or ask data. Each list contains prices and amounts.
        :param rev: Weather data should be sorted ascending or descending.
        :return: Lists with tuples of price and amount.
        """
        asks_or_bids.sort(key=lambda data: float(data[0]), reverse=rev)
        return asks_or_bids

    def weighted_avg(self, prices, amounts):
        '''
        Calculate the volume weighted average price.
        volume weighted average price = sum(Price[i]*Ammount[i]) / sum(Ammount[i])
        http://en.wikipedia.org/wiki/Volume-weighted_average_price

        :param prices: List of prices.
        :param amounts: List of amounts.
        :return: A volume weighted avg price.
        '''
        try:
            avg = np.average(prices, weights=amounts)
            return avg
        except ZeroDivisionError:
            print('Weights sum to zero, cant be normalized in calculating average.')

    def weighted_std(self, values, weights):
        '''
        Calculated the weighted standard deviation.
        weighted standard deviation = sqrt[ (weights[i] * variance[i]) / sum(weights[i]) ]
        variance = (values[i] - average)**2
        http://en.wikipedia.org/wiki/Weighted_arithmetic_mean

        :param values: Values of a list, corresponding to prices.
        :param weights: Values of a list, corresponding to amounts.
        :return: The weighted standard deviation.
        '''
        try:
            avg = self.weighted_avg(values, weights)
            weighted_std = math.sqrt(np.dot(weights, (values-avg)**2)/ sum(weights))
            return weighted_std
        except ZeroDivisionError:
            print('Weights sum to zero, cant be normalized in calculating standard deviation')

    def create_dict(self, ask, bid):
        """
        Create a dictionary of a calculated bid and ask.

        :param bid: Bid price
        :param ask: Ask price
        :return: Dictionary of ask and bid price.
        """
        if ask and bid:
            ask_bid_dict = {'ask': ask, 'bid': bid}
            return ask_bid_dict
        else:
            print('Error could not add data to dictionary.')
            return None

    def exchange(self, usd=None, b=None):
        """
        Do an exchange from USD to Bitcoins, or from Bitcoins to USD.
        Creates conversion rate.
        Multiplies given currency by conversion rates.
        Subtracts fee depending on the exchange.

        :param ask_bid_dict: Dictionary containing depth data.
        :param usd: Amount of USD to convert to Bitcoins.
        :param b: Amount of Bitcoins to convert to USD.
        :return: USD or Bitcoins.
        """
        depth = self.depth()
        if (usd and b) or (not usd and not b):
            return None
        lowest_ask = depth['ask'][0][0]
        if usd:
            amount = usd
            conversion = 1.0 / lowest_ask
        elif b:
            amount = b
            conversion = lowest_ask
        total = amount * conversion
        fee = total * self.fee['trading']
        total = total - fee
        return total


    def ask_bid_data(self, depth_data):
        """
        Abstract
        Get bid and ask data.

        :param depth_data: Data from the exchange API in JSON format.
            Should be a dictionary of bid and ask data.
        :return: Ask and bid data.
            prices, amounts,timestamp.
        :raise: Not Implemented Error.
        """
        raise NotImplementedError( "Should have implemented ask_bid_data" )

    def clean_data(self, asks_or_bids):
        """
        Abstract
        Cleans asks or bids data by putting it in a format that can be used later on.

        :param asks_or_bids: Either a list of bid or ask data. Each list contains prices and amounts.
        :return: Lists containing tuples of prices and amounts.
        """
        raise NotImplementedError( "Should have implemented clean_data" )







