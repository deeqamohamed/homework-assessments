import mock
import unittest
from unittest import TestCase, main
from Q3_code import verify_pin,log_in,set_start_balance,run_atm

class AccountsAtm(TestCase):

    @mock.patch('Q3_code.verify_pin')
    def test_verify_pin(self, mock_verify_pin):
        pin = 2684
        mock_verify_pin.return_value = pin
        self.assertEqual(pin,mock_verify_pin.return_value)

    @mock.patch('Q3_code.log_in')
    def test_log_in(self, mock_log_in):
        verify_pin != 2684
        mock_log_in.return_value = verify_pin
        self.assertEqual(verify_pin, mock_log_in.return_value)

    @mock.patch('Q3_code.set_start_balance')
    def test_starting_balance(self,mock_set_start_balance):
        set_start_balance = 100
        mock_set_start_balance.return_value = set_start_balance
        self.assertEqual(set_start_balance,mock_set_start_balance.return_value)

    @mock.patch('Q3_code.run_atm')
    def test_run_atm(self, mock_run_atm):
        amount = 123
        set_balance = 100
        balance = set_balance - amount
        mock_run_atm.return_value = balance
        self.assertEqual(balance, mock_run_atm.return_value)

if __name__ == '__main__':
    main()
