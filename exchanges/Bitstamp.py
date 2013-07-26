from exchanges.AbstractExchange import AbstractExchange

class Bitstamp(AbstractExchange):
    '''
    Bitstamp class
    '''
    def __init__(self):
        super(Bitstamp, self).__init__()
        self.api = self.import_api()

    def bid_ask(self):
        depth_data = self.api.depth()
        asks = depth_data['asks']
        bids = depth_data['bids']
        ask_price = self.extract_price(asks)
        bid_price = self.extract_price(bids)
        return self.create_dict(ask_price, bid_price)

    def extract_price(self, depth_data):
        price, amount = 0, 1
        prices, amounts = [], []
        for data in depth_data:
            prices.append(float(data[price]))
            amounts.append(float(data[amount]))
        price = self.volume_weighted_avg_price(prices, amounts)
        return price


if __name__ == '__main__':
    b = Bitstamp()
    print(b.bid_ask())