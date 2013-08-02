from exchanges.AbstractExchange import AbstractExchange

class Bitstamp(AbstractExchange):
    """
    Bitstamp class
    """
    def __init__(self):
        super(Bitstamp, self).__init__()

    def ask_bid_data(self, depth_data):
        """
        Extract bid and ask prices from the JSON data returned from the exchange.

        :param depth_data: Depth data called from the exchange API. Should be a dictionary of bid and ask data.
        :return: Ask and bid lists.
        """
        asks = depth_data['asks']
        bids = depth_data['bids']
        cleaned_asks = self.clean_data(asks)
        cleaned_bids = self.clean_data(bids)
        return cleaned_asks, cleaned_bids

    def clean_data(self, asks_or_bids):
        """
        Cleans asks or bids data by putting it in a format that can be used later on.

        :param asks_or_bids: Either a list of bid or ask data. Each list contains prices and amounts.
        :return: Lists containing tuples of prices and amounts.
        """
        cleanded_asks_or_bids = []
        for data in asks_or_bids:
            cleanded_asks_or_bids.append((float(data[0]), float(data[1])))
        return cleanded_asks_or_bids




if __name__ == '__main__':
    b = Bitstamp()
    print(b.depth())




