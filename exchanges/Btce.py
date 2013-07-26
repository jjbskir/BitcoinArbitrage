from exchanges.AbstractExchange import AbstractExchange

class Btce(AbstractExchange):
    '''
    btc-e exchange.
    '''
    def __init__(self):
        super(Btce, self).__init__()

    def bid_ask_prices(self, depth_data):
        """
        Calculate the average ask and bid price.

        :param depth_data: Depth data from btc-e exchange. Dictionary with asks and bids.
            bids: Bid list of prices and quantities.
            asks: Ask list of prices and quantities.
        :return: Ask and bid volume weighted avg prices.
        """
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
        for data in asks_or_bids:
            prices.append(float(data[price]))
            amounts.append(float(data[amount]))
        return prices, amounts


if __name__ == '__main__':
    m = Btce()
    print(m.calculate_bis_ask_prices())