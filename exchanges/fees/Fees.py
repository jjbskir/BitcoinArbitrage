class Fees:
    """
    Fees for the differrent exchanges.
    """
    fee_structure = {
        'Bitstamp': {   # exchange
            'trading': 0.005,   # trading percent fee.
            'base': 0.0         # trading base fee.
            },
        'MtGox': {
            'trading': 0.005,
            'base': 0.0
            },
        'Btce': {
            'trading': 0.005,
            'base': 0.0
        }
    }

    def __init__(self):
        pass

    def get_fee(self, key):
        """
        Gets a fee structure for a specific exchange.

        :param key: Key for fee_structure dictionary that corresponds to a specific exchange.
        :return: Fee structure for specific exchange. Contains trading percent and base fee.
            dictionary keys: 'trading', 'base'
        """
        if key in self.fee_structure:
            return self.fee_structure[key]
        print('Exchange does not have a fee structure')
        return None

