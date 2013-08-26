import importlib

class Flow:
    """
    How money flows through the system.
    """
    def __init__(self, exchange_names, usd=None, b=None):
        self.usd = usd
        self.b = b
        self.exchanges = self.create_exchanges(exchange_names)

    def create_exchanges(self, exchange_names):
        """
        Import exchanges and add them to a dictionary.

        :param exchange_names: Exchange names to import exchange packages.
        :return: Dictionary with pairs of exchange names and their associated objects.
        """
        exchanges = {}
        for exchange_name in exchange_names:
            package = 'exchanges.' + exchange_name
            try:
                exchange = importlib.import_module(package)
                exchange_class = getattr(exchange, exchange_name)
                exchanges[exchange_name] = exchange_class()
            except ImportError:
                print('Could not import module')
        return exchanges

    def try_arbitrages(self):
        """
        Try a bunch of different arbitrages between all the different exchanges, and see which one makes you the
        most money.

        :return: List containing tuples of starting exchange, final exchange, starting amount usd, ending amount usd.
        [(exchange1, exchange2, starting usd, final usd)]
        """
        profits = []
        for ex_name_curr in self.exchanges.keys():
            for ex_name_arb in self.exchanges.keys():
                if ex_name_curr != ex_name_arb:
                    usd = self.usd_arbitrage(ex_name_curr, ex_name_arb)
                    profits.append((ex_name_curr, ex_name_arb, self.usd, usd))
        return profits

    def usd_arbitrage(self, exchange1, exchange2):
        """
        Make a arbitrage between two exchanges.
        Go from USD -> Bitcoins -> USD.

        :param exchange1: Exchange name.
        :param exchange2: Exchange name.
        :return: Arbitrage between two different exchanges and return usd.
        """
        usd = self.usd - self.exchanges[exchange1].fee.initial_fee(self.usd)
        b = self.exchanges[exchange1].exchange(self.exchanges[exchange1].depth(), usd=usd)
        usd = self.exchanges[exchange2].exchange(self.exchanges[exchange2].depth(), b=b)
        return usd - self.exchanges[exchange1].fee.final_fee(usd)

    def b_arbitrage(self, exchange1, exchange2):
        """
        Make a arbitrage between two exchanges.
        Go from Bitcoins -> USD -> Bitcoins.

        :param exchange1: Exchange name.
        :param exchange2: Exchange name.
        :return: Arbitrage between two different exchanges and return bitcoins.
        """
        usd = self.exchanges[exchange1].exchange(b=self.b)
        b = self.exchanges[exchange2].exchange(usd=usd)
        return b


