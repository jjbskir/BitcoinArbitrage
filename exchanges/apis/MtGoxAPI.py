from exchanges.apis.AbstractExchangeAPI import AbstractExchangeAPI
import urllib.parse
import time
import base64
import hmac
import hashlib

class MtGoxAPI(AbstractExchangeAPI):
    """
    Mt. Gox API.
    @note: Mt. Gox's api does not use trailing slashes.
    ext = /<> instead of /<>/
    """
    def __init__(self):
        baseURL = 'https://data.mtgox.com/api/2/'
        super(MtGoxAPI, self).__init__(baseURL)
        self.key = ''
        self.secret = ''

    def ticker(self):
        """
        Ticler information.
        @return:
        vwap: the volume-weighted average price
        last_local: the last trade in your selected auxiliary currency
        last_orig: the last trade (any currency)
        last_all: that last trade converted to the auxiliary currency
        last: the same as last_local
        now: the unix timestamp, but with a resolution of 1 microsecond
        """
        ext = 'BTCUSD/money/ticker'
        return self.req.request(ext)

    def depth(self):
        """
        Get asks and bids.
        Use ext = 'BTCUSD/money/depth/fetch' for 1 day of request.
        Use ext = 'BTCUSD/money/depth/full' for more data.
        @return:
        bids: dictionary of bid price, amount, stamp.
        asks: dictionary of ask price, amount, stamp.
        {"price":93.06545,"amount":0.07284541,"price_int":"9306545","amount_int":"7284541","stamp":"1364769641591046"},
        """
        ext = 'BTCUSD/money/depth/fetch'
        return self.req.request(ext)

    def balance(self):
        """
        Get the user's balance and associated info.

        :return: Dictionary of user's info.
        dict = {'data':
                    'Wallets':
                        'USD':
                            'Balance': {'value': '52.71305', 'currency': 'USD'}
                        'BTC':
                            {'value_int': '0', 'currency': 'BTC', 'display_short': '0.00\xa0BTC', 'display': '0.00000000\xa0BTC', 'value': '0.00000000'}
                    'Login': 'jjbskir',
                    'Rights': ['deposit', 'get_info'], 'Trade_Fee': 0.6}
                'result': 'success'
        """
        ext = 'BTCUSD/money/info'
        header = self._private_header(ext)
        params = {"nonce": self._create_nonce()}
        return self.req.request(ext, params=params, headers=header)

    def _private_header(self, path):
        """
        Create private header that will be added to HTTP request headers. They are the unique identifiers
        for Mt. Gox API. Instead of username and password.
        """
        headers = {  'Rest-Key': self.key,
                     'Rest-Sign': self._sign(path)
        }
        return headers

    def _create_nonce(self):
        """
        Create a nonce. Any number as long as it increases between requests.

        :return: nonce time stamp in the form of a string.
        """
        return str(int(time.time()*1000)) + "000"

    def _sign(self, path):
        """
        Sign the HTTP request in the headers by making this unique signature.

        :param path: Extension of url.
        :return: Signature that is the unhashed secret.
        """
        # create encoded nonce time stamp.
        nonce = {"nonce": self._create_nonce()}
        nonce_encoded = urllib.parse.urlencode(nonce)
        # create unique hash containing path to url, 0, and nonce. Then convert it to bytes.
        api2postdatatohash = (path + chr(0) + nonce_encoded).encode('utf-8')
        # create a secret by unhashing the secret.
        hmac_secret = hmac.new(base64.b64decode(self.secret), api2postdatatohash, hashlib.sha512)
        return base64.b64encode(hmac_secret.digest())



if __name__ == '__main__':
    api = MtGoxAPI()
    print(api.balance())
