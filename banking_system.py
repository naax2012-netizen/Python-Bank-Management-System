from random import *
from datetime import *
# storing data
data={}
balance=0

# create bank account
def create_account():
    attempts = 3
    while attempts > 0:
        name = input("Enter your name: ").strip()
        if (
    name
    and "  " not in name
    and all(word.isalpha() for word in name.split())
):
          break
        attempts -= 1
        print(f"Invalid name. Attempts left: {attempts}")
        if attempts == 0:
            print("Too many invalid attempts")
            return
        
    attempts = 3
    while attempts > 0:
        phone_no = input("Enter your phone number: ")
        if len(phone_no) == 10 and phone_no.isdigit() and phone_no[0] in "6789":
            break
        attempts -= 1
        print(f"Invalid phone number. Attempts left: {attempts}")
        if attempts == 0:
            print("Too many invalid attempts")
            return
        
    attempts = 3
    while attempts > 0:
        pin = input("Create your 6-digit security pin: ")
        if len(pin) == 6 and pin.isdigit():
          break
        attempts -= 1
        print(f"Invalid PIN. Attempts left: {attempts}")
        if attempts == 0:
           print("Too many invalid attempts")
           return
    while True:
        acc_no=randint(10000000000,99999999999)
        if acc_no not in data:
            break
    data[acc_no]={
        "name":name,
        "phone_no":phone_no,
        "pin":pin,
        "balance":0,
        "history":[]
    }
    print(f"Your account number is:{acc_no}")
   
def login():
    attempts = 3
    while attempts > 0:
        ac_no = int(input("Enter your account number: "))
        if ac_no in data:
            break
        attempts -= 1
        print(f"Incorrect account number. Attempts left: {attempts}")
        if attempts == 0:
            print("Too many invalid attempts")
            return None
    attempts = 3
    while attempts > 0:
        pass_word = input("Enter your security pin: ")
        if pass_word == data[ac_no]["pin"]:
            print("Successful login")
            return ac_no
        attempts -= 1
        print(f"Wrong PIN. Attempts left: {attempts}")
    print("Account locked. Too many attempts.")
    return None

def check_balance(logged_in):
    print(f"Your account balance is:{data[logged_in]['balance']}")

def deposit_money(logged_in):
    amount=int(input("Enter the amount to be deposited:"))
    if amount<=0:
        print(f"{amount} is invalid amount")
    else:
        data[logged_in]["balance"]+=amount
        data[logged_in]["history"].append(f"{datetime.now()}-Deposited {amount}")
        print(f"Amount deposit on account number {logged_in} successful")
        print(f"Your current balance is {data[logged_in]['balance']}")

def withdraw_money(logged_in):
    amount=int(input("Enter the amount to be withdrawn:"))
    if amount<=0:
        print(f"{amount} is invalid amount")
    elif data[logged_in]["balance"]>=amount:
        data[logged_in]["history"].append(f"{datetime.now()}-Withdrawn {amount}")
        print(f"Amount withdrawn from account number {logged_in} successful")
        data[logged_in]['balance']-=amount
        print(f"Your current balance is {data[logged_in]['balance']}")
    else:
        print("Insufficient balance")

def transfer_money(logged_in):
    receiver_account_number=int(input("Enter receiver account number:"))
    # self transfer is not allowed as it is only single bank and single customer with 1 account number is allowed
    if receiver_account_number == logged_in:
        print("Cannot transfer to the same account")
        return
    # transfer should take place only between registered accounts
    # 1st create 1 account,then create another acoount and log in through it and transfer money to the 1st account which was created
    if receiver_account_number not in data:
        print(f"Receiver account number {receiver_account_number} does not exist in records")
        return
    amount=int(input("Enter the amount to be transferred:"))
    if amount<=0:
        print(f"{amount} is invalid amount")
        return
    if data[logged_in]["balance"]<amount:
        print("Your account has insufficient balance")
    elif data[logged_in]["balance"]>=amount:
        data[logged_in]["balance"]-=amount
        print(f"{amount} Amount deducted from account {logged_in}")
        print(f"Account number {logged_in} your remaining balance is {data[logged_in]['balance']}")
        print(f"{amount} Amount received to account {receiver_account_number}")
        data[receiver_account_number]["balance"]+=amount
        print(f"Account number {receiver_account_number} your remaining balance is {data[receiver_account_number]['balance']}")
        data[logged_in]["history"].append(f"{datetime.now()}-Transferred {amount} to {receiver_account_number}")
        data[receiver_account_number]["history"].append(f"{datetime.now()}-Received {amount} from {logged_in}")

def transaction_history(logged_in):
    if len(data[logged_in]["history"])==0:
        print("No deposits,withdrawns,transactions")
        return
    print("Transaction history:\n")
    for transaction in data[logged_in]["history"]:
        print(transaction)

def change_pin(logged_in):
    old_pin=input("Enter your old pin:")
    if old_pin==data[logged_in]["pin"]:
        attempts = 3
        while attempts > 0:
            new_pin = input("Enter  NEW PIN: ")
            if len(new_pin) == 6 and new_pin.isdigit():
                break
            attempts -= 1
            print("PIN must contain exactly 6 digits")
            print(f"Attempts left: {attempts}")
            if attempts == 0:
               print("Too many invalid attempts")
               return
        confirm_pin=input("Re-enter your new pin:")
        if new_pin==confirm_pin:
            print("Pin reset successful")
            data[logged_in]["pin"]=new_pin
            data[logged_in]["history"].append(
    f"{datetime.now()} - PIN Changed"
)
        else:
            print("Pin not matched")
    else:
        print("Wrong pin!")

def forgot_pin():
    acc_no = int(input("Enter your account number: "))
    if acc_no not in data:
        print("Account not found")
        return
    phone_no = input("Enter registered phone number: ")
    if phone_no != data[acc_no]["phone_no"]:
        print("Phone number does not match our records")
        return
    attempts = 3
    while attempts > 0:
        new_pin = input("Enter new 6-digit PIN: ")
        if len(new_pin) == 6 and new_pin.isdigit():
           break
        attempts -= 1
        print(f"Invalid PIN. Attempts left: {attempts}")
        if attempts == 0:
            print("Too many invalid attempts")
            return
    confirm_pin = input("Re-enter new PIN: ")
    if new_pin == confirm_pin:
        data[acc_no]["pin"] = new_pin
        print("PIN reset successful")
    else:
        print("PIN mismatch")

def account_details(logged_in):
    print("\n----- ACCOUNT DETAILS -----")
    print(f"Name           : {data[logged_in]['name']}")
    print(f"Account Number : {logged_in}")
    print(f"Phone Number   : {data[logged_in]['phone_no']}")
    print(f"Balance        : {data[logged_in]['balance']}")

while True:
    print("\n=== MAIN MENU ===")
    print("1. Create Account")
    print("2. Login")
    print("3.Forgot PIN")
    print("4. Exit")
    choice=int(input("Enter your choice:"))
    match(choice):
        case 1:
            create_account()
        case 2:
            logged_in=login()
            if logged_in is not None:
                while True:
                    print("\n-----OPERATIONS------")
                    print("1.Check Balance")
                    print("2.Deposit")
                    print("3.Withdraw")
                    print("4.Transfer")
                    print("5.Transaction History")
                    print("6.Change pin")
                    print("7.Account details")
                    print("8.Log out")
                    ch=int(input("Enter your choice"))
                    match(ch):
                        case 1:
                           check_balance(logged_in)
                        case 2:
                           deposit_money(logged_in)
                        case 3:
                           withdraw_money(logged_in)
                        case 4:
                           transfer_money(logged_in)
                        case 5:
                           transaction_history(logged_in)
                        case 6:
                           change_pin(logged_in)
                        case 7:
                            account_details(logged_in)
                        case 8:
                            print("Logged out successfully")
                            break
                        case _:
                            print("Invalid choice")
        case 3:
            forgot_pin()
        case 4:
            print("Thank you!")
            break
        case _:
            print("Invalid choice")    
