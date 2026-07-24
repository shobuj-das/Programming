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