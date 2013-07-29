import sys
import json
import numpy
# need to use enthought and python 3.3, so data needs to be pre serialized.
if sys.version[0] == '3':
    from exchanges.MtGox import MtGox
    from exchanges.Bitstamp import Bitstamp
elif sys.version[0] == '2':
    from scipy.optimize import curve_fit
    import matplotlib.pyplot as plt


class BidAskGaussian:
    '''
    Check if bid and ask prices fall into a gausian curve.
    '''
    def __init__(self):
        if sys.version[0] == '3':
            self.exchange = Bitstamp()
        self.file = '/Users/jb/Desktop/python/BitcoinArbitrage/research/data/AskBidSerialized' # file to save serialized ask bid data to.

    def serialize(self):
        # grab ask and bid data from api. Store in a dictionary.
        depth_data = self.exchange.api.depth()
        asks, bids = self.exchange.ask_bid_data(depth_data)
        asks_prices, asks_amounts = self.exchange.extract_prices_amounts(asks)
        bids_prices, bids_amounts = self.exchange.extract_prices_amounts(bids)
        dic = {'asks': asks_prices, 'bids': bids_prices}
        # open a file to store serialized data in.
        output = open(self.file, 'w')
        json.dump(dic, output)
        output.close()
        print('Ask bid data serialized.')


    def deserialize(self):
        file = open(self.file, 'r')
        dic = json.load(file)
        file.close()
        print('Ask bid data deserialized')
        return dic

    def fit_gaussian(self, data):
        data_min = min(data)
        data_max = max(data)
        hist, bin_edges = numpy.histogram(data, bins=numpy.arange(data_min, data_max, 0.25), density=True)
        bin_centres = (bin_edges[:-1] + bin_edges[1:])/2
        print(bin_centres)
        if sys.version[0] == '2':
            plt.plot(bin_centres, hist, 'k', label='Test data')
            plt.show()
        if sys.version[0] == '3':
            pass

    # Define model function to be used to fit to the data above:
    def gauss(x, *p):
        A, mu, sigma = p
        return A*numpy.exp(-(x-mu)**2/(2.*sigma**2))

if __name__ == '__main__':
    g = BidAskGaussian()
    g.serialize()
    data = g.deserialize()
    #print(sorted(data['asks'], key=float))
    print('Ask bins')
    g.fit_gaussian(data['asks'])
    print('Bid bins')
    g.fit_gaussian(data['bids'])