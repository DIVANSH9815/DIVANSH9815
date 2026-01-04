#Q1️⃣ Encapsulation & Privacy

class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number      # public
        self.holder_name = holder_name              # public
        self.__balance = balance                    # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

account1 = BankAccount(2230760, "Divansh", 50000)

account1.deposit(5000)
account1.withdraw(45000)

print("    ---------This Your Balance---------     ")
print("Current Balance:", account1.get_balance())

    
