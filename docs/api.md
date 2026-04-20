# API Documentation

This section outlines the API endpoints and methods available for integrating with the cryptocurrency transfer network. The API allows for wallet management, escrow services, transaction handling, and communication with mixers.

## API Endpoints:

### 1. **Create Wallet**
   - **Endpoint**: `POST /api/wallet/create`
   - **Description**: Creates a new wallet for the user.
   - **Request Body**:
     ```json
     {
       "balance": 1000.0,
       "address": "User123"
     }
     ```
   - **Response**:
     ```json
     {
       "status": "success",
       "wallet_address": "User123",
       "balance": 1000.0
     }
     ```

### 2. **Deposit Funds**
   - **Endpoint**: `POST /api/wallet/deposit`
   - **Description**: Deposits funds into the user's wallet.
   - **Request Body**:
     ```json
     {
       "wallet_address": "User123",
       "amount": 500.0
     }
     ```
   - **Response**:
     ```json
     {
       "status": "success",
       "balance": 1500.0
     }
     ```

### 3. **Initiate Escrow**
   - **Endpoint**: `POST /api/escrow/lock`
   - **Description**: Locks funds in escrow for a transaction.
   - **Request Body**:
     ```json
     {
       "buyer_wallet_address": "Buyer123",
       "seller_wallet_address": "Seller123",
       "amount": 300.0
     }
     ```
   - **Response**:
     ```json
     {
       "status": "locked",
       "escrow_balance": 300.0
     }
     ```

### 4. **Release Escrow Funds**
   - **Endpoint**: `POST /api/escrow/release`
   - **Description**: Releases locked funds to the seller.
   - **Request Body**:
     ```json
     {
       "escrow_id": "Escrow123",
       "status": "released"
     }
     ```
   - **Response**:
     ```json
     {
       "status": "success",
       "released_to": "Seller123"
     }
     ```

### 5. **Dispute Resolution**
   - **Endpoint**: `POST /api/escrow/dispute`
   - **Description**: Resolves a dispute in the escrow system, either returning funds to the buyer or releasing them to the seller.
   - **Request Body**:
     ```json
     {
       "escrow_id": "Escrow123",
       "winner": "buyer"
     }
     ```
   - **Response**:
     ```json
     {
       "status": "resolved",
       "funds_returned_to": "Buyer123"
     }
