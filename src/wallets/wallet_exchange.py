from wallet_internal import InternalWallet
from wallet_2A_6F import MixerWallet

class WalletExchange:
    def __init__(self, internal_wallet: InternalWallet):
        self.internal_wallet = internal_wallet

    def exchange_to_external(self, external_wallet: MixerWallet, amount: float):
        """Transfers funds from the internal wallet to an external wallet (e.g., mixer wallet)."""
        if self.internal_wallet.balance >= amount:
            self.internal_wallet.transfer(external_wallet, amount)
            print(f"Exchanged {amount} from internal wallet to external wallet: {external_wallet.address}")
        else:
            print("Insufficient funds in internal wallet to exchange!")

    def exchange_from_external(self, external_wallet: MixerWallet, amount: float):
        """Transfers funds from an external wallet to the internal wallet."""
        if external_wallet.balance >= amount:
            external_wallet.transfer(self.internal_wallet, amount)
            print(f"Exchanged {amount} from external wallet to internal wallet: {self.internal_wallet.address}")
        else:
            print("Insufficient funds in external wallet to exchange!")

    def display_balances(self):
        """Displays the current balance of both the internal and external wallets."""
        print(f"Internal Wallet balance: {self.internal_wallet.get_balance()}")
        # Assuming you have a list of external wallets (e.g., mixer wallets) that can be checked.
        # Example external wallets (you may loop over or check specific wallets)
        external_wallets = [MixerWallet(address=f"2A-6F Wallet {i}") for i in range(1, 7)]
        for wallet in external_wallets:
            print(f"External Wallet ({wallet.address}) balance: {wallet.get_balance()}")

    def exchange_funds(self, external_wallet: MixerWallet, amount: float, direction: str):
        """
        Exchanges funds between the internal wallet and an external wallet.
        
        Parameters:
        - direction: 'to' for transferring funds from internal wallet to external wallet
                     'from' for transferring funds from external wallet to internal wallet
        """
        if direction == 'to':
            self.exchange_to_external(external_wallet, amount)
        elif direction == 'from':
            self.exchange_from_external(external_wallet, amount)
        else:
            print("Invalid exchange direction. Use 'to' or 'from'.")
