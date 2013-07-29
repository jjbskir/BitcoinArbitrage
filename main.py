from exchanges.Bitstamp import Bitstamp
from exchanges.MtGox import MtGox
from exchanges.Btce import Btce
from research.BidAskGaussian import BidAskGaussian

if __name__ == '__main__':
    '''
    g = BidAskGaussian()
    data = g.deserialize()
    g.fit_gaussian(data['asks'])
    g.fit_gaussian(data['bids'])

    btce = Btce()
    print(btce.calculate_bis_ask_prices())
    '''
    m = MtGox()
    print(m.calculate_bis_ask_prices())

    b = Bitstamp()
    print(b.calculate_bis_ask_prices())
