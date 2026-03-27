class BankAccount: 
  def __init__ (self, account_number, balance=0): 
    self._account_number = account_number 
    self.balance = balance 

  @property
  def account_number(self):
    return self._account_number

  def deposit(self, amount): 
    if amount > 0: 
      self.balance += amount 
      print(f"Deposited {amount}. New balance: {self.balance}")
    else: 
      print("Deposit amount must be positive.")

  def withdraw(self, amount): 
    if amount > self.balance: 
      print("Insufficient funds.")
    elif amount <= 0: 
      print("Withdrawal amount must be positive.")
    else: 
      self.balance -= amount 
      print(f"Withdrew {amount}. New balance: {self.balance}")
  
  def get_balance(self): 
    return self.balance

account1 = BankAccount("123456789", 1000)
print(f"Account Number: {account1.account_number}, Balance: {account1.get_balance
()}")
account1.deposit(500)
account1.withdraw(200)
account1.withdraw(1500)

# Output
# Account Number: 123456789, Balance: 1000
# Deposited 500. New balance: 1500
# Withdrew 200. New balance: 1300