import sys
from src.crypto.chaCha20_poly1305 import ChaCha20Poly1305
from src.crypto.aes256 import AES256
from src.crypto.double_ratchet import DoubleRatchet
from src.network.tunnel import establish_tunnel
from src.wallets.wallet import Wallet
from src.escrow.escrow import EscrowSystem

def main():
    # Initialize encryption systems
    chaCha20 = ChaCha20Poly1305()
    aes256 = AES256()
    ratchet = DoubleRatchet()

    # Print basic info on encryption
    print(f"ChaCha20-Poly1305 initialized: {chaCha20}")
    print(f"AES-256 initialized: {aes256}")
    print(f"Double Ratchet initialized: {ratchet}")
    
    # Initialize wallet system
    wallet = Wallet()
    print(f"Wallet Initialized: {wallet}")
    
    # Setup escrow system
    escrow = EscrowSystem(wallet)
    print(f"Escrow system initialized: {escrow}")
    
    # Establish secure communication tunnel (e.g., HTTPS -> SSH -> ChaCha20-Poly1305 -> TCP)
    establish_tunnel()

    # Start the escrow service
    escrow.start_service()

if __name__ == "__main__":
    main()
