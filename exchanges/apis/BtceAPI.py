from exchanges.apis.AbstractExchangeAPI import AbstractExchangeAPI

class BtceAPI(AbstractExchangeAPI):
    '''
    API abstraction for btc-e exchange.
    '''
    def __init__(self):
        baseURL = 'https://btc-e.com/api/2/'
        super(BtceAPI, self).__init__(baseURL)

    def depth(self):
        '''
        Dictionary with bids and asks.

        :return: JSON dictionary with "bids" and "asks".
            bids: Bid list of prices and quantities.
            asks: Ask list of prices and quantities.
        '''
        ext = 'btc_usd/Depth'
        return self.req.get(ext)

if __name__ == '__main__':
    api = BtceAPI()
    print(api.depth())