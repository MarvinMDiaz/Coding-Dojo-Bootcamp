
class BankAccount:
    def init(self, int_rate = .05, balance = 5):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if (self.balance < amount):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: {}".format(self.balance))
        return self

    def yield_interest(self):
        if (self.balance > 0):
            self.balance *= self.int_rate
        else:
            print("Insufficent funds")
        return self

checking = BankAccount(4, 900)
# savings = BankAccount(1, 80)

checking.yield_interest()
# savings.deposit(900).deposit(800).withdraw(1000).withdraw(90).withdraw(10).withdraw(5).display_account_info()