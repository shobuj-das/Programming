# ============================================================
# Day 20 - Bank Account Management System
#
# Difficulty:
# Medium
#
# Concepts:
# - OOP
# - Encapsulation
# - Class Design
# - Exception Handling
# - Transaction History
#
# ------------------------------------------------------------
#
# Problem Statement
#
# Design a simple Bank Account Management System.
#
# Create TWO classes:
#
# 1. BankAccount
# 2. Bank
#
# ------------------------------------------------------------
#
# BankAccount should contain:
#
# - account_number
# - account_holder
# - balance
# - transaction_history
#
# ------------------------------------------------------------
#
# Bank should support:
#
# add_account(account)
#
# remove_account(account_number)
#
# search_account(account_number)
#
# deposit(account_number, amount)
#
# withdraw(account_number, amount)
#
# transfer(from_account, to_account, amount)
#
# display_account(account_number)
#
# display_all_accounts()
#
# ------------------------------------------------------------
#
# Rules
#
# 1. Account number must be unique.
#
# 2. Deposit amount must be greater than zero.
#
# 3. Withdraw amount must be greater than zero.
#
# 4. Cannot withdraw more than the current balance.
#
# 5. Cannot transfer to a non-existing account.
#
# 6. Cannot transfer to the same account.
#
# 7. Every successful operation should be stored in
#    transaction_history.
#
# ------------------------------------------------------------
#
# Bonus
#
# Store every transaction as:
#
# {
#     "type": "Deposit",
#     "amount": 500,
#     "time": datetime.now()
# }
#
# Bonus 2
#
# Add:
#
# display_transaction_history(account_number)
#
# ============================================================

import datetime

class BankAccount:
    def __init__(self, account_number, account_holder):
        self.acc_number = account_number
        self.acc_holder = account_holder
        self.balance = 0

    def __str__(self):
        return(
            f"Account Number: {self.acc_number} |"
            f"Account Holder: {self.acc_holder} |"
            f"Balance: {self.balance}"
        )

class Bank:
    def __init__(self):
        self.acc_list = []
        self.transaction_history = []

    def add_account(self,account):
        self.acc_list.append(account)

    def remove_account(self, account_number):
        acc = self.search_account(account_number)
        if acc is not None:
            self.acc_list.remove(acc)
            print("Account removed succesfully")


    def search_account(self, account_number):
        if self.acc_list is None:
            print("No account found")
            return None
        for account in self.acc_list:
            if account.acc_number == account_number:
                print("Acccount found")
                return account
        print("Account not found")
        return None


    def deposit(self, account_number, amount):
        acc = self.search_account(account_number)
        if acc is not None:
            acc.balance += amount
            print("Deposite Success")
            self.add_transaction_history('deposite',from_acc=account_number,amount=amount)


    def withdraw(self,account_number, amount):
        acc = self.search_account(account_number)
        if acc is not None:
            if acc.balance < amount:
                print("Insufficent balance")
                return
            
            acc.balance -= amount
            print(f"Balance withdraw success\nCurren Balance: {acc.balance}")
            self.add_transaction_history("withdraw", from_acc=account_number, amount=amount)

    def transfer(self, from_account, to_account, amount):
        from_acc = self.search_account(from_account)
        to_acc = self.search_account(to_account)

        if from_acc and to_acc is not None:
            if from_acc.balance < amount:
                print("Insuffiecent balance")
                return
            else:
                from_acc.balance -= amount
                to_acc.balance += amount
                print("Money transfer successful")
                self.add_transaction_history("transfer", from_acc=from_account, to_acc=to_account,amount=amount)

    def display_account(self, account_number):
        acc = self.search_account(account_number=account_number)
        print(acc)


    def display_all_accounts(self):
        for acc in self.acc_list:
            print(acc)

    def add_transaction_history(self, type, from_acc=None, to_acc = None, amount=0):
        
        if type == 'deposite':
            trx = {
                "trx_type" : type,
                "trx_acc_number": from_acc,
                "trx_date_time": datetime.datetime.today(),
                "trx_amount" :amount
            }

            self.transaction_history.append(trx)

        elif type == 'withdraw':
            trx = {
                "trx_type": type,
                "trx_acc_number" : from_acc,
                "trx_date_time" : datetime.datetime.today(),
                "trx_amount" : amount

            }
            self.transaction_history.append(trx)

        elif type == "transfer":
            trx = {
                "trx_type": type,
                "trx_from_acc_number" : from_acc,
                "trx_to_acc_number" : to_acc,
                "trx_date_time" : datetime.datetime.now(),
                "trx_amount" : amount
            }            
            self.transaction_history.append(trx)

    def display_all_transaction_history(self):
        for trx in self.transaction_history:
            print(trx)

if __name__=="__main__":
    acc1 = BankAccount(101, "Alex")
    acc2 = BankAccount(102, "Bob")
    acc3 = BankAccount(103, "Shobuj")

    bank = Bank()
    bank.add_account(acc1)
    bank.add_account(acc2)
    bank.add_account(acc3)

    bank.deposit(101, 2000)
    bank.deposit(103, 5000)

    bank.withdraw(101,10000)

    bank.transfer(101,102,400)

    bank.display_account(101)

    bank.display_all_transaction_history()