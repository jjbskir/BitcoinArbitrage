class Fees:
    '''
    Fees for the differrent exchanges.
    '''
    fee_structure = {
        'Bitstamp': {
            'trading': 0.005,
            'Base': 0.0
            },
        'MtGox': {
            'trading': 0.005,
            'Base': 0.0
            }
    }

    def __init__(self):
        pass

    def get_fees(self):
        return self.fee_structure

