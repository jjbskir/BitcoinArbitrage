from exchanges.Bitstamp import Bitstamp
from exchanges.MtGox import MtGox

if __name__ == '__main__':

    m = MtGox()
    print(m.calculate_bis_ask_prices())
    b = Bitstamp()
    print(b.calculate_bis_ask_prices())
