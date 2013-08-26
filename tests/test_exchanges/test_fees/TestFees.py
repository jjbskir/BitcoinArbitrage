import unittest
from exchanges.fees.Fees import Fees


class TestFees(unittest.TestCase):
    """
    Test fees.
    """
    def setUp(self):
        self.fees_bitstamp = Fees('Bitstamp')

    def tearDown(self):
        pass

    def test_init(self):
        """
        Test __init__() - Test setting up the class.
        """
        fees_empty = Fees(None)
        # make sure fee structure is in place.
        self.assertEqual(type(fees_empty.fee_structure), dict)
        self.assertEqual(type(fees_empty.my_bank), dict)
        self.assertEqual(fees_empty.fees, None)
        self.assertEqual(self.fees_bitstamp.fees, dict(trading=0.005, base=0.0, withdrawal_perc=0.0009, withdrawal_base=0.0, withdrawal_min=15.0,
                                                    deposit_perc=0.001, deposit_base=0.0, deposit_min=15.0))
    def test_get_fees(self):
        """
        Test get_fees() - Test getting fee structure for specific exchange.
        """
        self.assertEqual(self.fees_bitstamp.get_fees('blah'), None) # make a call to the fee structure that does not exist.
        self.assertEqual(self.fees_bitstamp.get_fees('Bitstamp'), dict(trading=0.005, base=0.0, withdrawal_perc=0.0009, withdrawal_base=0.0, withdrawal_min=15.0,
                                                    deposit_perc=0.001, deposit_base=0.0, deposit_min=15.0)) # make call to Bitstamp fee structure.

    def test_calculate_trading_fee(self):
        """
        Test calculate_trading_fee() - Calculates fees for trading.
        """
        self.assertEqual(self.fees_bitstamp.calculate_trading_fee(100), 0.5) # .005 percent of 100
        self.assertEqual(self.fees_bitstamp.calculate_trading_fee(0.5), 0.0025)

    def test_initial_fee(self):
        """
        Test initial_fee() - Calculates initial deposit fees.
        """
        self.assertEqual(self.fees_bitstamp.initial_fee(100), 60) # minimum fee get called for exchange + fee for wire transfer from your bank account.
        self.assertEqual(self.fees_bitstamp.initial_fee(2000), 60)
        self.assertEqual(self.fees_bitstamp.initial_fee(20000), 65) # percent fee gets called + fee for wire transfer from your bank account.
        self.assertEqual(self.fees_bitstamp.initial_fee(20009.15), 65.00915)

    def test_final_fee(self):
        """
        Test final_fee() - Calculates final withdrawl fee.
        """
        self.assertEqual(self.fees_bitstamp.final_fee(100), 33) # minimum fee get called for exchange + fee for wire transfer from your bank account.
        self.assertEqual(self.fees_bitstamp.final_fee(2000), 33)
        self.assertEqual(self.fees_bitstamp.final_fee(20000), 36) # percent fee gets called + fee for wire transfer from your bank account.
        self.assertEqual(self.fees_bitstamp.final_fee(20009.15), 36.008235)
