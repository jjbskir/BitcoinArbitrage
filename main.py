from exchanges.exchange import BitstampAPI
from tests.test_exchanges.TestRequests import TestRequests


if __name__ == '__main__':
    #e = BitstampAPI()
    #print(e.get_mean_price())
    t = TestRequests()
    t.main()