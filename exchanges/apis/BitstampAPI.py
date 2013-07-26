from exchanges.Requests import Requests

class BitstampAPI:
    '''
    Bitstamp API.
    '''
    def __init__(self):
        baseURL = 'https://www.bitstamp.net/api/'
        self.req = Requests(baseURL)

    def transactions(self):
        '''
        100 Most recent transactions.
        @return:
        date - unix timestamp date and time
        tid - transaction id
        price - BTC price
        amount - BTC amount
        '''
        ext = 'transactions/'
        params = {'timedelta': 3600}
        return self.req.get(ext, params)

    def depth(self, ordergrouping=1):
        '''
        Dictionary with bids and asks.
        @param: group - group orders with the same price (0 - false; 1 - true). Default: 1.
        @return JSON dictionary with "bids" and "asks".
        Each is a list of open orders and each order is represented as a list of price and amount.
        '''
        ext = 'order_book/'
        params = {"group": ordergrouping}
        return self.req.get(ext, params)

    def ticker(self):
        '''
        Ticker.
        @return:
        last - last BTC price
        high - last 24 hours price high
        low - last 24 hours price low
        volume - last 24 hours volume
        bid - highest buy order
        ask - lowest sell order
        '''
        ext = 'ticker/'
        return self.req.get(ext)

    def eur_usd_conversion(self):
        '''
        Convert from Euero to USD.
        @return Conversion rate
        '''
        ext = 'eur_usd/'
        return self.req.get(ext)

    def get_mean_price(self):
        '''
        TODO: Calculate volume-weighted average.
        http://en.wikipedia.org/wiki/Volume-weighted_average_price
        Calculate the mean transaction price from the transactions.
        @return: mean price.
        '''
        transactions = self.transactions()
        prices = [float(t['price']) for t in transactions]
        mean = sum(prices) / len(prices)
        return mean

    def volume_weighted_avg_price(self):
        '''
        TODO: Calculate volume-weighted average.
        http://en.wikipedia.org/wiki/Volume-weighted_average_price
        Calculate the mean transaction price from the transactions.
        @return: mean price.
        '''
        transactions = self.transactions()
        prices = [float(t['price']) for t in transactions]
        amounts = [float(t['amount']) for t in transactions]
        avg = sum([price*amount for price, amount in zip(prices, amounts)]) / sum(amounts)
        return avg


if __name__ == '__main__':
    api = BitstampAPI()
    print(api.depth())






