import importlib
import numpy as np
import math

class AbstractExchange(object):
    '''
    Abstract class for all the other exchanges.
    '''
    def __init__(self):
        self.api = self.import_api()

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

    def calculate_bis_ask_prices(self):
        '''
        The main method for this class. Used to make sure abstract classes are called.
        '''
        depth_data = self.api.depth() # grab api depth data.
        asks, bids = self.ask_bid_data(depth_data) # grab ask and bid data from dictionary.
        ask_price = self.calculate_price(asks) # calculate the ask price.
        bid_price = self.calculate_price(bids) # calculate the bid price.
        return self.create_dict(ask_price, bid_price) # add ask and bid prices to a dictionary to return.

    def calculate_price(self, depth_data):
        '''
        Calculate the price of a ask or bid.

        :param depth_data: data from a api depth call from a exchange. Should be either ask or bid data.
            Each of these dictionaries or lists should contain prices and amounts. Data will be initially filtered with extract_prices_amounts.
        :return: Price corresponding to either ask or bid. The price has been filtered for outliers.
        '''
        # extract_prices_amounts is abstract and should be different for each exchange.
        # Makes data usable for this function. Data from API's can be different in each exchange.
        prices, amounts = self.extract_prices_amounts(depth_data)
        std = self.weighted_std(prices, amounts)
        avg = self.weighted_avg(prices, amounts)

        prices_filtered, amounts_filtered = [], []
        for i in range(len(prices)):
            #TODO: What is best to multiply standard deviation by? Should I check prices[i]*amounts[i], or just prices[i]?
            # filter price and amounts, by removing one past a certain threshhold.
            if avg - (std*2) < prices[i]*amounts[i] < avg + (std*2):
                # use standard deviation to remove outliers.
                prices_filtered.append(prices[i])
                amounts_filtered.append(amounts[i])
        price_final = self.weighted_avg(prices_filtered, amounts_filtered) # calculate the final price with the filtered data.
        return price_final

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
        raise NotImplementedError( "Should have implemented bid_ask_prices" )

    def extract_prices_amounts(self, asks_or_bids):
        """
        Abstract
        help extract price and amounts from bids and asks.

        :param ask_or_bids: A list of bid or ask data. Each list at least contains prices and amounts.
            Can also contain time stamp data.
        :raise: Not Implemented Error.
        """
        raise NotImplementedError( "Should have implemented extract_prices_amounts" )







