from exchanges.AbstractExchange import AbstractExchange

class MtGox(AbstractExchange):
    """
    Mt gox class.
    """
    def __init__(self):
        super(MtGox, self).__init__()

    def ask_bid_data(self, depth_data):
        """
        Extract bid and ask prices from the JSON data returned from the exchange.

        :param depth_data: Depth data called from the exchange API. Should be a dictionary of bid and ask data.
        :return: Ask and bid data.
        """
        if depth_data['result'] == 'success':
            asks = depth_data['data']['asks']
            bids = depth_data['data']['bids']
            return asks, bids

    def clean_data(self, asks_or_bids):
        """
        Cleans asks or bids data by putting it in a format that can be used later on.

        :param asks_or_bids: Either a list of bid or ask data. Each list contains prices and amounts.
        :return: Lists containing tuples of prices and amounts.
        """
        cleaned_asks_or_bids = []
        for data in asks_or_bids:
            cleaned_asks_or_bids.append((float(data['price']), float(data['amount'])))
        return cleaned_asks_or_bids





if __name__ == '__main__':
    m = MtGox()
    print(m.depth())