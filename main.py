from exchanges.Bitstamp import Bitstamp
from exchanges.MtGox import MtGox
from exchanges.Btce import Btce
from research.BidAskGaussian import BidAskGaussian
from Arbitrage.Flow import Flow

def output(arbitrage_data):
    print('Initial Exchange, Final Exchange, Initial Capital, Final Capital')
    for arbitrage in arbitrage_data:
        perc = (arbitrage[3] - arbitrage[2])/ arbitrage[3]
        print(arbitrage[0] + ' -> ' + arbitrage[1] + ': ' + str(arbitrage[2]) + ', ' + str(arbitrage[3]) +  ', percent gain: ' + str(perc))



if __name__ == '__main__':
    '''
    g = BidAskGaussian()
    data = g.deserialize()
    g.fit_gaussian(data['asks'])
    g.fit_gaussian(data['bids'])

    btce = Btce()
    print(btce.depth())

    m = MtGox()
    data = m.depth()
    print(data['ask'][0:5])
    print(data['bid'][0:5])

    b = Bitstamp()
    print(b.exchange_depth(b=20))
    '''
    exchanges = ['MtGox', 'Bitstamp', 'Btce']
    flow = Flow(exchanges, 2500, 5)
    arbitrage_data = flow.try_arbitrages()
    arbitrage_data.sort(key=lambda data: float(data[3]), reverse=True)
    output(arbitrage_data)

