from exchanges.Bitstamp import Bitstamp
from exchanges.MtGox import MtGox
from exchanges.Btce import Btce
from research.BidAskGaussian import BidAskGaussian
from MoneyFlow.Flow import Flow

if __name__ == '__main__':
    '''
    g = BidAskGaussian()
    data = g.deserialize()
    g.fit_gaussian(data['asks'])
    g.fit_gaussian(data['bids'])
    '''
    btce = Btce()
    print(btce.depth())
    '''
    m = MtGox()
    data = m.depth()
    print(data['ask'][0:5])
    print(data['bid'][0:5])

    b = Bitstamp()
    data = b.depth()
    #print(data['ask'][0:5])
    #print(data['bid'][0:5])
    print(b.exchange(data, b=1))

    exchanges = ['MtGox', 'Bitstamp', 'Btce']
    flow = Flow(exchanges, 100, 0)
    print(flow.try_arbitrages())
    '''
