from exchanges.AbstractExchange import AbstractExchange

class Bitstamp(AbstractExchange):
    '''
    Bitstamp class
    '''
    def __init__(self):
        super(Bitstamp, self).__init__()

    def bid_ask_prices(self, depth_data):
        '''
        Extract bid and ask prices from the JSON data returned from the exchange.

        :param depth_data: Depth data called from the exchange API. Should be a dictionary of bid and ask data.
        :return: Dictionary of average weighted ask and bid price.
        '''
        asks = depth_data['asks']
        bids = depth_data['bids']
        ask_price = self.calculate_price(asks)
        bid_price = self.calculate_price(bids)
        return ask_price, bid_price

    def extract_prices_amounts(self, asks_or_bids):
        '''
        Grabs needed data for calculate_price(). Sorts the data in a way to make it usable for calculate_price().

        :param asks_or_bids: Either a list of bid or ask data. Each list contains prices and amounts.
        :return: Lists for both prices and amounts. return prices, amounts
        '''
        prices, amounts = [], []
        price, amount = 0, 1
        count = 0
        for data in asks_or_bids:
            prices.append(float(data[price]))
            amounts.append(float(data[amount]))
            if count == 400:
                break
            count += 1
        return prices, amounts

if __name__ == '__main__':
    b = Bitstamp()
    print(b.calculate_bis_ask_prices())




