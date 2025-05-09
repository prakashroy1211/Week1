class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    # deposit function
    def deposit(self, amount):
        if amount > 0:  # Deposit amount should be a positive number
            self.balance += amount
            print(f"Deposited: Rs{amount}")
        else:
            print("Invalid deposit amount")
    # withdraw function
    def withdraw(self, amount):
        if 0 < amount <= self.balance:  # The amount to withdraw should be less than the balance in the account
            self.balance -= amount
            print(f"Withdraw: Rs{amount}")
        else:
            print("Insufficient funds or invalid amount")

    # balance checking
    def display_balance(self):
        print(f"{self.owner}'s Balance: Rs{self.balance}")


# Example
account = BankAccount("Prakash", 1000) # Initially 1000 was the balance
account.deposit(500)                   # Added 500, so 1500
account.withdraw(200)                  # Withdraw 200, so balance will be 1500 - 200 = 1300
account.display_balance()