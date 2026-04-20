import unittest
from escrow.escrow import Escrow
from wallet_internal import InternalWallet
from wallet_2A_6F import MixerWallet

class TestEscrow(unittest.TestCase):

    def test_lock_funds(self):
        buyer_wallet = InternalWallet(balance=1000.0)
        seller_wallet = InternalWallet(balance=500.0)
        escrow = Escrow(buyer_wallet, seller_wallet)
        escrow.lock_funds(300.0)
        self.assertEqual(buyer_wallet.get_balance(), 700.0)
        self.assert
