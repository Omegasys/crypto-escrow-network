from wallet import Wallet

class MixerWallet(Wallet):
    def __init__(self, balance=0.0, address=None):
        super().__init__(balance, address)

    def mix(self, amount, target_wallet):
        """Mixes a given amount of cryptocurrency and sends it to a target wallet."""
        if self.balance >= amount:
            self.balance -= amount
            target_wallet.balance += amount
            print(f"Mixed {amount} and sent to {target_wallet.address}")
        else:
            print("Insufficient funds to mix!")
