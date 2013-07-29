from exchanges.Requests import Requests

class AbstractExchangeAPI(object):
    '''
    Abstract base class for the other exchange API classes.
    '''
    def __init__(self, baseURL):
        # create a request and response object to get data frome exchange api.
        self.req = Requests(baseURL)

    def depth(self):
        '''
        API depth function to get ask and bid prices from exchange.

        :return: HTTP GET request for depth information in JSON format.
        '''
        raise NotImplementedError( "Should have implemented depth" )