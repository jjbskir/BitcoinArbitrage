from exchanges.Requests import Requests

class MtGoxAPI:
    '''
    Mt. Gox API.
    @note: Mt. Gox's api does not use trailing slashes.
    ext = /<> instead of /<>/
    '''
    def __init__(self):
        baseURL = 'https://data.mtgox.com/api/2/'
        self.req = Requests(baseURL)

    def ticker(self):
        '''
        Ticler information.
        @return:
        vwap: the volume-weighted average price
        last_local: the last trade in your selected auxiliary currency
        last_orig: the last trade (any currency)
        last_all: that last trade converted to the auxiliary currency
        last: the same as last_local
        now: the unix timestamp, but with a resolution of 1 microsecond
        '''
        ext = 'BTCUSD/money/ticker'
        return self.req.get(ext)

    def depth(self):
        '''
        Get asks and bids.
        Use ext = 'BTCUSD/money/depth/fetch' for 1 day of request.
        Use ext = 'BTCUSD/money/depth/full' for more data.
        @return:
        bids: dictionary of bid prices.
        asks: dictionary of ask prices.
        '''
        ext = 'BTCUSD/money/depth/fetch'
        return self.req.get(ext)

    def bid_ask(self):
        '''
        Calculate the average ask and bid price.
        '''
        depth_data = self.depth()
        if depth_data['result'] == 'success':
            # ask data
            asks = depth_data['data']['asks']
            asks_prices = [ask['price'] for ask in asks]
            asks_amounts = [ask['amount'] for ask in asks]
            ask_volume_weighted_avg_price = self.volume_weighted_avg_price(asks_prices, asks_amounts)
            # bids data
            bids = depth_data['data']['bids']
            bids_prices = [bid['price'] for bid in bids]
            bids_amounts = [bid['amount'] for bid in bids]
            bid_volume_weighted_avg_price = self.volume_weighted_avg_price(bids_prices, bids_amounts)
            # add ask and bid volume weighted avg price to dict.
            ask_bid_dict = {'ask': ask_volume_weighted_avg_price, 'bid': bid_volume_weighted_avg_price}
            return ask_bid_dict
        return None


    def avg_price(self):
        '''
        Get volume weighted avg price
        '''
        ticker_data = self.ticker()
        if ticker_data['result'] == 'success':
            return ticker_data['data']['vwap']['value']
        return None

    def volume_weighted_avg_price(self, prices, amounts):
        '''
        Calculate the volume weighted average price.
        volume weighted average price = sum(Price[i]*Ammount[i]) / sum(Ammount[i])
        http://en.wikipedia.org/wiki/Volume-weighted_average_price
        '''
        avg = sum([price*amount for price, amount in zip(prices, amounts)]) / sum(amounts)
        return avg

    def mean(self, data):
        '''
        Calculate mean.
        '''
        return sum(data) / len(data)


if __name__ == '__main__':
    api = MtGoxAPI()
    print(api.ticker())