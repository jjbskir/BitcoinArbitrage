import importlib

class AbstractExchange:
    '''
    Abstract class for all the other exchanges.
    '''
    def __init__(self):
        pass

    def import_api(self):
        """
        Import API objects.
        :return: api associated with each object.
        """
        class_name = self.__class__.__name__ + 'API'
        package = 'exchanges.apis.' + class_name
        try:
            # create an api variable.
            api = importlib.import_module(package)
            api = getattr(api, class_name)
            api = api()
        except ImportError:
            print('Could not import module')
        if api: return api
        else: return None

    def volume_weighted_avg_price(self, prices, amounts):
        '''
        Calculate the volume weighted average price.
        volume weighted average price = sum(Price[i]*Ammount[i]) / sum(Ammount[i])
        http://en.wikipedia.org/wiki/Volume-weighted_average_price
        :param prices: List of prices.
        :param amounts: List of amounts.
        :return: A volume weighted avg price.
        '''
        avg = sum([price*amount for price, amount in zip(prices, amounts)]) / sum(amounts)
        return avg

    def create_dict(self, ask, bid):
        """
        Create a dictionary of a calculated bid and ask.
        :param bid: Bid price
        :param ask: Ask price
        :return: Dictionary of ask and bid price.
        """
        ask_bid_dict = {'ask': ask, 'bid': bid}
        return ask_bid_dict

    def bid_ask(self):
        """
        Abstract
        Get bid and ask prices.
        :raise: Not Implemented Error.
        """
        raise NotImplementedError( "Should have implemented bid_ask" )

    def extract_price(self):
        """
        Abstract
        help extract price and amounts from bids and asks.
        :raise: Not Implemented Error.
        """
        raise NotImplementedError( "Should have implemented extract_depth" )
