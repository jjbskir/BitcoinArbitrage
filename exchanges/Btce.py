from exchanges.AbstractExchange import AbstractExchange

class Btce(AbstractExchange):
    """
    btc-e exchange.
    """
    def __init__(self):
        super(Btce, self).__init__()

    def ask_bid_data(self, depth_data):
        """
        Extract bid and ask prices from the JSON data returned from the exchange.

        :param depth_data: Depth data called from the exchange API. Should be a dictionary of bid and ask data.
        :return: Ask and bid lists.
        """
        asks = depth_data['asks']
        bids = depth_data['bids']
        return asks, bids

    def clean_data(self, asks_or_bids):
        """
        Cleans asks or bids data by putting it in a format that can be used later on.

        :param asks_or_bids: Either a list of bid or ask data. Each list contains prices and amounts.
        :return: Lists containing lists of prices and amounts.
        """
        return self.clean_data_helper(asks_or_bids, 0, 1)


if __name__ == '__main__':
    m = Btce()
    print(m.depth())