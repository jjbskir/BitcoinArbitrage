import time
#from exchanges.apis.MtGoxAPI import MtGoxAPI

class MtGox:
    '''
    Mt gox class.
    '''
    def __init__(self):
        """
        init
        """
        self.import_api()

    def bid_ask(self):
        """
        Calculate the average ask and bid price.
        :return: Dictionary with ask and bid volume weighted avg price.
        """
        depth_data = self.api.depth()
        if depth_data['result'] == 'success':
            # ask data
            asks = depth_data['data']['asks']
            asks_prices = self.extract_depth(asks, 'price')
            asks_amounts = self.extract_depth(asks, 'amount')
            ask_volume_weighted_avg_price = self.volume_weighted_avg_price(asks_prices, asks_amounts)
            # bids data
            bids = depth_data['data']['bids']
            bids_prices = self.extract_depth(bids, 'price')
            bids_amounts = self.extract_depth(bids, 'amount')
            bid_volume_weighted_avg_price = self.volume_weighted_avg_price(bids_prices, bids_amounts)
            # add ask and bid volume weighted avg price to dict.
            ask_bid_dict = {'ask': ask_volume_weighted_avg_price, 'bid': bid_volume_weighted_avg_price}
            return ask_bid_dict
        return None

    def extract_depth(self, dict, key):
        """
        :param dict: dictionary of prices and amounts of bitcoins.
        :param key: Key to look for in dictionary.
        :return: List of values from dictionary that were part of a key.
        """
        #TODO: check that time is ok.
        # time since now. 60 minutes ago.
        t = int((time.time() - 36000) * 1000000) # seconds
        list = [d[key] for d in dict if float(d['stamp']) > t]
        return list

    def volume_weighted_avg_price(self, prices, amounts):
        '''
        Calculate the volume weighted average price.
        volume weighted average price = sum(Price[i]*Ammount[i]) / sum(Ammount[i])
        http://en.wikipedia.org/wiki/Volume-weighted_average_price
        :param prices: List of prices.
        :param amounts: List of amounts.
        :return: A volume weighted avg price.
        '''
        avg = sum([price*amount for price, amount in zip(prices, amounts)]) / sum(amounts)
        return avg




if __name__ == '__main__':
    m = MtGox()
    print(m.bid_ask())