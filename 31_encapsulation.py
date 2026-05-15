# Exercise 31: Encapsulation
# Task: Implement encapsulation with private attributes and getter/setter methods.

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            
    def get_balance(self):
        return self.__balance

if __name__ == "__main__":
    acc = BankAccount("Ethan", 1000)
    acc.deposit(250)
    print(f"Account Balance: {acc.get_balance()}")
