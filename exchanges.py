import urllib2


class Bitstamp:
    '''
    Bitstamp exchange API.
    '''
    def __init__(self):
        pass

    def order_book(self):
        req = urllib2.urlopen('https://www.bitstamp.net/api/order_book/')
        orders = req.read()
        return orders

    def transactions(self):
        '''
        100 latest transactions.
        @return: dictionary{date - unix timestamp date and time
                            tid - transaction id
                            price - BTC price
                            amount - BTC amount}
        '''
        params = {}
        req = urllib2.urlopen('https://www.bitstamp.net/api/transactions/', params, None)
        transactions = req.read()
        return transactions

    def conversion_eur_usd(self):
        req = urllib2.urlopen('https://www.bitstamp.net/api/eur_usd/')
        conversion = req.read()
        return conversion

if __name__ == '__main__':
    b = Bitstamp()
    print b.transactions()