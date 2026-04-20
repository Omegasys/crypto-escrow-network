# System Architecture

The system is designed as a secure and decentralized cryptocurrency transfer network utilizing escrow and mixing functionalities. It is built with privacy and security as key goals, ensuring that transactions are anonymous and resistant to attacks.

## Key Components:

### 1. **Network Layer**
   - **HTTPS**: Provides secure communication using SSL/TLS.
   - **SSH**: Provides an additional layer of encryption for secure remote access.
   - **ChaCha20-Poly1305**: Used for authenticated encryption to protect the confidentiality and integrity of data.
   - **TCP**: Reliable transport layer for network communication.

### 2. **Wallets**
   - **Internal Wallet**: Holds the balance of a user (buyer, seller) and facilitates transactions.
   - **Mixer Wallets (2A to 6F)**: Mixes funds to enhance privacy, making it difficult to trace the transaction flow.
   - **Wallet Exchange**: Facilitates the exchange of internal funds between wallets.

### 3. **Mixers**
   - **Mixing Logic**: Implements different mixing strategies across 6 mixers, each having 32 I/O ports. The mixers help in obfuscating transaction amounts, reducing the risk of traceability and increasing privacy.
   - **Time Delays**: Each mixer introduces a delay (1-9 seconds) to thwart timing attacks.

### 4. **Escrow System**
   - **Escrow**: Locks the funds temporarily until both parties agree on the transaction, with mechanisms to handle disputes.
   - **Dispute Resolution**: Resolves issues in case of disagreement between buyer and seller, allowing funds to be returned or released based on the outcome.
   - **Transaction Verification**: Verifies that payments have been made and that goods have been received before releasing funds.

### 5. **Encryption**
   - **ChaCha20-Poly1305**: Used for secure end-to-end communication.
   - **AES-256**: Provides secure encryption for stored and transmitted data.
   - **Double Ratchet**: Ensures forward secrecy and secure communication channels.

## Workflow Overview:
1. **Buyer initiates the escrow**: Funds are locked in the escrow by the buyer.
2. **Funds are mixed**: The buyer's funds are mixed across multiple mixers (2A-6F) to provide privacy.
3. **Seller confirms goods**: Once the goods are received, the seller confirms and the funds are released to them.
4. **Dispute Resolution**: If there is a dispute, the system handles it by allowing the buyer or seller to make a claim.

## Diagram
```plaintext
Buyer Wallet -> Escrow -> Mixer 1 -> Mixer 2 -> Mixer 3 -> ... -> Mixer 6 -> Seller Wallet
