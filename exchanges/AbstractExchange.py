from exchanges.fees.Fees import Fees
import importlib
import numpy as np
import math

class AbstractExchange(object):
    """
    Abstract class for all the other exchanges.
    """
    def __init__(self):
        """
        Import api and fee class for specific exchange.
        """
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

        :return: fee class with fee structure for specific class.
        """
        fee = Fees(self.__class__.__name__)
        return fee

    def depth(self):
        """
        The main method for this class. Used to make sure abstract classes are called.

        :return: Dictionary with list of ask and bid prices and amounts
        """
        depth_data = self.api.depth() # grab api depth data.
        asks, bids = self.ask_bid_data(depth_data) # grab ask and bid data from dictionary. Puts it in specific format
        cleaned_asks = self.clean_data(asks)
        cleaned_bids = self.clean_data(bids)
        asks_ordered = self.sort_depth(cleaned_asks, False) # calculate the ask price.
        bids_ordered = self.sort_depth(cleaned_bids, True) # calculate the bid price.
        return self.create_dict(asks_ordered, bids_ordered) # add ask and bid prices to a dictionary to return.

    def clean_data_helper(self, asks_or_bids, price_key, amount_key):
        """
        Helper function for cleaning data from ask or bid data.

        :param asks_or_bids: Either a list of bid or ask data. Each list contains prices and amounts.
        :param price_key: key in either dictionary or list to grab price data.
        :param amount_key: key in either dictionary or list to grab amount data.
        :return: Lists containing lists of prices and amounts.
        """
        cleaned_asks_or_bids = []
        for data in asks_or_bids:
            cleaned_asks_or_bids.append([float(data[price_key]), float(data[amount_key])])
        return cleaned_asks_or_bids

    def sort_depth(self, asks_or_bids, rev=False):
        """
        Sorts ask or bid data. Ask data gets sorted ascending.Bid data descending.

        :param asks_or_bids: Either a list of bid or ask data. Each list contains prices and amounts.
        :param rev: Weather data should be sorted ascending or descending.
        :return: Lists with tuples of price and amount.
        :rtype: {'ask': [[price, amount],...,[price, amount]], 'bid': [[price, amount],...,[price, amount]]}
        """
        asks_or_bids.sort(key=lambda data: float(data[0]), reverse=rev)
        return asks_or_bids

    def create_dict(self, ask, bid):
        """
        Create a dictionary of a calculated bid and ask.

        :param bid: Bid price
        :param ask: Ask price
        :return: Dictionary of ask and bid price.
        :rtype: {'ask': [[price, amount],...,[price, amount]], 'bid': [[price, amount],...,[price, amount]]}
        """
        if ask and bid:
            ask_bid_dict = {'ask': ask, 'bid': bid}
            return ask_bid_dict
        else:
            print('Error could not add data to dictionary.')
            return None

    def exchange(self, depth, usd=None, b=None):
        """
        Do an exchange from USD to Bitcoins, or from Bitcoins to USD.
        Creates conversion rate using depth data.
        Multiplies given currency by conversion rates.
        Subtracts fee depending on the exchange.

        :param ask_bid_dict: Dictionary containing depth data.
        :param usd: Amount of USD to convert to Bitcoins.
        :param b: Amount of Bitcoins to convert to USD.
        :return: USD or Bitcoins.
        """
        if (usd and b) or (not usd and not b):
            return None
        depth = self.exchange_depth(depth, usd, b) # grab needed depth data.
        ask_avg = np.average([d[0] for d in depth], weights=[d[1] for d in depth]) # calculate a weighted average from prices and amounts.
        # create conversion rates
        if usd:
            amount = usd
            conversion = 1.0 / ask_avg
        elif b:
            amount = b
            conversion = ask_avg
        total = amount * conversion
        fee = self.fee.calculate_trading_fee(total) # calculate fees.
        total = total - fee # subtract fees from total.
        return total

    def exchange_depth(self, depth, usd=None, b=None):
        """
        Find the total amount of depth needed for a conversion. Used in exchange().

        :param depth: Exchange ask bid depth data.
        :param usd: usd amount.
        :param b: bitcoin amount.
        :return: List of lists that contain price and amounts. Needed depth for conversion.
        """
        if usd:
            amount = usd
            depth = depth['ask']
        elif b:
            amount = b
            depth = depth['bid']
        total = 0.0 # total in usd or bitcoins.
        needed_depth = [] # needed depth information for exchange.
        for ask_or_bid in depth:
            if total >= amount:
                # remove unused bitcoins.
                if usd:
                    needed_depth[-1][1] -= (total - amount) * (1.0 / needed_depth[-1][0]) # convert from usd to
                elif b:
                    needed_depth[-1][1] -= total - amount # subtract bitcoins.
                break
            else:
                if usd:
                    total += ask_or_bid[0] * ask_or_bid[1]
                elif b:
                    total += ask_or_bid[1]
                needed_depth.append([a for a in ask_or_bid]) # add ask data by copying all of its data onto a new list to avoid memory reference to original depth data
        return needed_depth

    #-_-_-_-_-_-_-_-_-_-=
    #- Abstract Methods =
    #-_-_-_-_-_-_-_-_-_-=

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
        :return: List containing lists of prices and amounts.
        """
        raise NotImplementedError( "Should have implemented clean_data" )







