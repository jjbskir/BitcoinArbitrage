class Fees:
    """
    Fees for the differrent exchanges.
    """
    fee_structure = {
        'Bitstamp': {   # exchange
            'trading': 0.005,           # trading percent fee.
            'base': 0.0,                # trading base fee.
            'withdrawal_perc': 0.0009,  # withdrawal percent fees.
            'withdrawal_base': 0.0,     # withdrawal base fee.
            'withdrawal_min': 15.0,     # minimum withdrawl fee.
            'deposit_perc': 0.001,      # deposit percent fees.
            'deposit_base': 0.0,        # base deposit fee.
            'deposit_min': 15.0         # minimum deposit fee
            },
        'MtGox': {
            'trading': 0.005,
            'base': 0.0,
            'withdrawal_perc': 0.0, # withdrawl fees.
            'withdrawal_base': 10.0,
            'deposit_perc': 0.0, # deposit fees.
            'deposit_base': 10.0
            },
        'Btce': {
            'trading': 0.002,
            'base': 0.0,
            'withdrawal_perc': 0.01, # withdrawl fees.
            'withdrawal_base': 0.0,
            'deposit_perc': 0.01, # deposit fees.
            'deposit_base': 0.0
        }
    }

    # fees for your bank.
    my_bank = {
        'withdrawal_base': 45, # withdrawl fees.
        'deposit_base': 18  # deposit fees.
    }

    def __init__(self, class_name):
        """
        Get fees for specific exchange.

        :param class_name: Name of exchange class.
        """
        self.fees = self.get_fees(class_name) # fees for specific exchange.

    def get_fees(self, key):
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

    def calculate_trading_fee(self, amount):
        """
        Calculate trading fee from converting between currencies at a exchange.

        :param amount: Amount of usd or bitcoins.
        :return: Fee amount.
        """
        fee = amount * self.fees['trading'] + self.fees['base']
        return fee

    def initial_fee(self, amount):
        """
        Fee for withdrawing money from bank account and depositing into exchange.

        :param amount: Amount of USD being deposited to exchange.
        :return: Initial fees from wire transfer withdrawing and depositing.
        """
        fee = 0.0
        fee += self.my_bank['withdrawal_base']
        temp_fee = (amount * self.fees['deposit_perc']) + self.fees['deposit_base']
        if 'deposit_min' in self.fees and self.fees['deposit_min'] > temp_fee:
            fee += self.fees['deposit_min']
        else:
            fee += temp_fee
        return fee

    def final_fee(self, amount):
        """
        Fee for withdrawing money from exchange and wiring it to bank account.

        :param amount: Amount of USD being deposited into bank account.
        :return: Final fee for withdrawing money from exchange and wiring to bank account.
        """
        fee = 0.0
        temp_fee = (amount * self.fees['withdrawal_perc']) + self.fees['withdrawal_base']
        if 'withdrawal_min' in self.fees and self.fees['withdrawal_min'] > temp_fee:
            fee += self.fees['withdrawal_min']
        else:
            fee += temp_fee
        fee += self.my_bank['deposit_base']
        return fee







