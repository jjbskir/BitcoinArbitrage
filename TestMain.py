# exchanges
from tests.test_exchanges.TestRequests import TestRequests
from tests.test_exchanges.TestAbstractExchange import TestAbstractExchange
from tests.test_exchanges.TestBitstamp import TestBitstamp
#apis
from tests.test_exchanges.test_apis.TestAbstractExchangeAPI import TestAbstractExchangeAPI
from tests.test_exchanges.test_apis.TestBistampAPI import TestBitstampAPI
from tests.test_exchanges.test_apis.TestMtGoxAPI import TestMtGoxAPI
# fees
from tests.test_exchanges.test_fees.TestFees import TestFees

if __name__ == '__main__':
    # test exchanges.
    t = TestRequests()
    t.main()
    t = TestAbstractExchange()
    t.main()
    t=TestBitstamp()
    t.main()
    # test apis.
    t=TestAbstractExchangeAPI()
    t.main()
    t=TestBitstampAPI()
    t.main()
    t=TestMtGoxAPI()
    t.main()
    # test fees.
    t=TestFees()
    t.main()
