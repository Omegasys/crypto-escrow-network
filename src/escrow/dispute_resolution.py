class DisputeResolution:
    def __init__(self, escrow):
        self.escrow = escrow
        self.resolved = False

    def resolve_dispute(self, winner: str):
        """Resolve a dispute by choosing the winner (buyer or seller) to receive the escrowed funds."""
        if self.escrow.locked:
            if winner == "buyer":
                self.escrow.buyer_wallet.deposit(self.escrow.escrow_balance)
                print(f"Dispute resolved. Funds returned to buyer: {self.escrow.escrow_balance}")
            elif winner == "seller":
                self.escrow.seller_wallet.deposit(self.escrow.escrow_balance)
                print(f"Dispute resolved. Funds released to seller: {self.escrow.escrow_balance}")
            else:
                print("Invalid winner specified. Choose 'buyer' or 'seller'.")
            self.escrow.escrow_balance = 0.0
            self.escrow.locked = False
            self.resolved = True
        else:
            print("No funds are locked in escrow, unable to resolve dispute.")

    def is_resolved(self):
        """Check if the dispute has been resolved."""
        return self.resolved
