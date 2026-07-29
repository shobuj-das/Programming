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


class BankAccount:
    def __int__(self, account_number, account_holder, balance, transaction_history):
        self.acc_number = account_number
        self.acc_holder = self.acc_holder
        self.balance = balance
        self.acc_transaction_history = transaction_history

    def __str__(self):
        return(
            f"Account Number: {self.acc_number} |"
            f"Account Holder: {self.acc_holder} |"
            f"Balance: {self.balance}"
        )

class Bank:
    def __init__(self):
        self.acc_list = []

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
