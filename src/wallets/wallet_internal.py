from wallet import Wallet

class InternalWallet(Wallet):
    def __init__(self, balance=0.0, address="1A2b3C4d5E6f7G8h9I0j1K2L3M4n5P6q7R8S9T0"):
        super().__init__(balance, address)

    def deposit(self, amount):
        """Deposits funds into the internal wallet."""
        self.balance += amount
        print(f"Deposited {amount} into internal wallet. New balance: {self.balance}")

    def withdraw(self, amount):
        """Withdraws funds from the internal wallet."""
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} from internal wallet. New balance: {self.balance}")
        else:
            print("Insufficient funds in internal wallet!")
