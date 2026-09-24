# Python Bank Management System
 
## Project Overview

The Banking System is a Python-based mini project that simulates basic banking operations. It allows users to create an account, securely log in, and perform various banking activities through a menu-driven application. The project combines Python fundamentals and demonstrates how real-world banking functionalities can be implemented using programming concepts.

---
## Features

### Create Bank Account
- Enter name, phone number, and create a secure 6-digit PIN.
- Generates a unique account number for every user.
- Prevents duplicate account numbers.
- Validates name, phone number, and PIN inputs.

### Login Authentication
- Login using Account Number and PIN.
- Limited login attempts for security.

### Check Account Balance
- Displays the current account balance of the logged-in user.

### Deposit Money
- Enter an amount to deposit into the account.
- Invalid and negative amounts are not accepted.

### Withdraw Money
- Enter an amount to withdraw from the account.
- Checks available balance before processing.

### Transfer Money
- Transfer money between registered accounts.
- Self-transfers are not allowed.
- Transfers are only allowed to existing accounts.

### Transaction History
- Displays deposits, withdrawals, transfers, and PIN changes along with date and time.

### Change PIN
- Allows users to update their security PIN.
- Verifies the old PIN before allowing changes.

### Forgot PIN
- Allows users to reset their PIN using their registered phone number and account number.

### Account Details
- Displays account number, account holder name, phone number, and current balance.

### Logout
- Ends the current session and returns to the main menu.
---
 
## Python Concepts Used
 
- Variables and Data Types
- Conditional Statements
- Loops
- Functions
- Lists and Dictionaries
- String Operations
- Input Validation
- Exception Handling (Future Enhancement)
- Modules
 
---
 
## Technologies Used
 
- Python 3
- Visual Studio Code
- Git
- GitHub
 
---
 
## Modules Used
 
### random
Used to generate unique account numbers for new users.
 
### datetime

Used to record transaction date and time for transaction history.

---
 
## Project Structure

```text
CREATE ACCOUNT
      ↓
ACCOUNT NUMBER + PIN
      ↓
LOGIN
      ↓

┌─────────────────────────┐
│      ACCOUNT MENU       │
├─────────────────────────┤
│ 1. Check Balance        │
│ 2. Deposit              │
│ 3. Withdraw             │
│ 4. Transfer             │
│ 5. Transaction History  │
│ 6. Change PIN           │
│ 7. Account Details      │
│ 8. Logout               │
└─────────────────────────┘

      ↓
LOGOUT
      ↓
MAIN MENU
```

 
---
 
## Project Objective

The main objective of this project is to integrate Python concepts learned during training into a single real-world application. It helps in understanding authentication, account management, transactions, data storage using dictionaries, and modular programming.

---
 
## Real-World Connection

This project demonstrates how programming can be used to model a simplified banking system. The application mimics real banking features such as user authentication, deposits, withdrawals, fund transfers, transaction tracking, and account management.

---
 
## Future Enhancements
 
- JSON File Storage for permanent data saving
- Database Integration (MySQL/SQLite)
- Password Masking using getpass
- Account Deletion Feature
- Interest Calculation
- Email Notifications
- Admin Panel
- Account Locking after multiple failed login attempts
- Statement Generation
 
---
 
## Author
 
Naaz Begum
