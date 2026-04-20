import unittest
from wallets.wallet import Wallet
from wallets.wallet_internal import InternalWallet
from wallets.wallet_2A_6F import MixerWallet
from wallets.wallet_exchange import WalletExchange

class TestWallets(unittest.TestCase):

    def test_wallet_creation(self):
        wallet = Wallet(balance=100.0, address="TestWallet123")
        self.assertEqual(wallet.get_balance(), 100.0)
        self.assertEqual(wallet.address, "TestWallet123")

    def test_internal_wallet(self):
        wallet = InternalWallet(balance=1000.0)
        self.assertEqual(wallet.get_balance(), 1000.0)
        wallet.deposit(500.0)
        self.assertEqual(wallet.get_balance(), 1500.0)
        wallet.withdraw(200.0)
        self.assertEqual(wallet.get_balance(), 1300.0)

    def test_mixer_wallet(self):
        wallet = MixerWallet(balance=100.0, address="MixerWallet123")
        self.assertEqual(wallet.get_balance(), 100.0)

    def test_wallet_exchange(self):
        internal_wallet = InternalWallet(balance=1000.0)
        mixer_wallet = MixerWallet(balance=0.0, address="MixerWallet123")
        wallet_exchange = WalletExchange(internal_wallet)
        wallet_exchange.exchange_to_external(mixer_wallet, 200.0)
        self.assertEqual(internal_wallet.get_balance(), 800.0)
        self.assertEqual(mixer_wallet.get_balance(), 200.0)

if __name__ == '__main__':
    unittest.main()
