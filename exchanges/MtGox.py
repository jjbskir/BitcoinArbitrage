from exchanges.AbstractExchange import AbstractExchange
import time

class MtGox(AbstractExchange):
    '''
    Mt gox class.
    '''
    def __init__(self):
        super(MtGox, self).__init__()

    def bid_ask_prices(self, depth_data):
        """
        Calculate the average ask and bid price.

        :return: Dictionary with ask and bid volume weighted avg price.
        """
        if depth_data['result'] == 'success':
            asks = depth_data['data']['asks']
            bids = depth_data['data']['bids']
            ask_price = self.calculate_price(asks)
            bid_price = self.calculate_price(bids)
            return ask_price, bid_price
        return None

    def extract_prices_amounts(self, asks_or_bids):
        '''
        Grabs needed data for calculate_price(). Sorts the data in a way to make it usable for calculate_price().

        :param asks_or_bids: Either a list of bid or ask data. Each list contains prices and amounts.
        :return: Lists for both prices and amounts.
        '''
        prices, amounts = [], []
        price, amount = 'price', 'amount'
        #TODO: check that time is ok. 3600 * 10^-6 = .0036
        # time since now - .0036 ago.
        time_subtract = 36
        time_current = time.time()
        while len(prices) < 200:
            # Go through the list until at least the 200 prices have been found that have occured in a certain time frame.
            # want the time frame to be as small as possible to get the most current prices.
            t = int((time_current - time_subtract) * 1000000) # seconds
            for data in asks_or_bids:
                if float(data['stamp']) > t:
                    prices.append(data[price])
                    amounts.append(data[amount])
            time_subtract = time_subtract*10 # increase the time frame by multiples of 10.
        return prices, amounts


if __name__ == '__main__':
    m = MtGox()
    print(m.calculate_bis_ask_prices())