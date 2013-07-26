from exchanges.Requests import Requests

class MtGoxAPI:
    '''
    Mt. Gox API.
    @note: Mt. Gox's api does not use trailing slashes.
    ext = /<> instead of /<>/
    '''
    def __init__(self):
        baseURL = 'https://data.mtgox.com/api/2/'
        self.req = Requests(baseURL)

    def ticker(self):
        '''
        Ticler information.
        @return:
        vwap: the volume-weighted average price
        last_local: the last trade in your selected auxiliary currency
        last_orig: the last trade (any currency)
        last_all: that last trade converted to the auxiliary currency
        last: the same as last_local
        now: the unix timestamp, but with a resolution of 1 microsecond
        '''
        ext = 'BTCUSD/money/ticker'
        return self.req.get(ext)

    def depth(self):
        '''
        Get asks and bids.
        Use ext = 'BTCUSD/money/depth/fetch' for 1 day of request.
        Use ext = 'BTCUSD/money/depth/full' for more data.
        @return:
        bids: dictionary of bid price, amount, stamp.
        asks: dictionary of ask price, amount, stamp.
        {"price":93.06545,"amount":0.07284541,"price_int":"9306545","amount_int":"7284541","stamp":"1364769641591046"},
        '''
        ext = 'BTCUSD/money/depth/fetch'
        return self.req.get(ext)

if __name__ == '__main__':
    api = MtGoxAPI()
    print(api.ticker())