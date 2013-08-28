from exchanges.apis.AbstractExchangeAPI import AbstractExchangeAPI

class BitstampAPI(AbstractExchangeAPI):
    '''
    Bitstamp API.
    '''
    def __init__(self):
        baseURL = 'https://www.bitstamp.net/api/'
        super(BitstampAPI, self).__init__(baseURL)

    """
    Public Functions
    """

    def depth(self, ordergrouping=1):
        """
        Dictionary with bids and asks.

        :param: group - group orders with the same price (0 - false; 1 - true). Default: 1.
        :return: JSON dictionary with "bids" and "asks".
            Each is a list of open orders and each order is represented as a list of price and amount.
        """
        ext = 'order_book/'
        params = {"group": ordergrouping}
        return self.req.request(ext, params)

    def eur_usd_conversion(self):
        '''
        Convert from Euero to USD.

        :return: Conversion rate
        '''
        ext = 'eur_usd/'
        return self.req.get(ext)

    """
    Private Functions
    """

    def balance(self, user, password):
        ext = 'balance/'
        params = {'user': user, 'password': password}
        return self.req.request(ext, params)


if __name__ == '__main__':
    api = BitstampAPI()
    print(api.depth())
    print(api.balance('07274', 'G3qsqqNtv4qEOx'))






