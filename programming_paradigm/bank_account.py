class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the account with an optional initial balance.
        Default balance is 0 if not provided.
        """
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        :param amount: The amount to deposit (must be positive).
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if funds are sufficient.
        :param amount: The amount to withdraw.
        :return: True if the transaction was successful, False otherwise.
        """
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current balance: ${self.__account_balance:.2f}")
