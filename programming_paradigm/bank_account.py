class BankAccount:

  def _init_(self, account_balance):

    self.account_balance = 0
    self.account_balance = account_balance

  def deposit(self, amount):
    self.account_balance += amount
    
    return amount

  def withdraw(self, amount):

    if self.account_balance > amount:
      self.account_balance -= amount

      return self.account_balance
    
    else:
      return False

  def display_balance(self):
    print(f"Current Balance: ${self.account_balance:.2f}")