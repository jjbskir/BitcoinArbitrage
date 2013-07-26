from exchanges.Bitstamp import Bitstamp
from exchanges.MtGox import MtGox
from exchanges.Btce import Btce

if __name__ == '__main__':

    btce = Btce()
    print(btce.calculate_bis_ask_prices())

    m = MtGox()
    print(m.calculate_bis_ask_prices())

    b = Bitstamp()
    print(b.calculate_bis_ask_prices())
