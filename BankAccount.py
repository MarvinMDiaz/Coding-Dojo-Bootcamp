


class BankAccount:
    bank_name = "Marvins Bank"
    Balance = 0
    InterestRate = .001
    AllBankAccount = []
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.AllBankAccount.append(self)

    def deposit(self, amount):
        # your code here
        self.balance+= amount
        print(f'{self} you have Deposited ${amount}')
        return self

    def withdraw(self, amount):
        if amount> self.balance:
            print("You do Not have insufficient Funds To Withdraw: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
            print(f'Hello {self}You have withdrawn: ${amount} Your Balance is now ${self.balance}')
        return self
        # your code here
    def display_account_info(self):
        print(f'Hello {self} your Balance is:${self.balance}\n')
        return self.balance
        
        
        # your code here
        # self.account_balance
    def yield_interest(self):
        # your code here
        currentBalance = self.balance
        if (self.balance > 0):
            self.balance *= self.int_rate 
            self.balance+=currentBalance 
            
        else:
            print("insuffiecient Funds")
        return self



class User:
    def __init__ (self,name, email):
        self.name = name
        self.email = email
        self.account= BankAccount(int_rate=0.03, balance=0)


    def deposit(self,amount):
        self.account.balance += amount
        print(f'Hello, {self.name} you have deposited {amount}, Your NEW balance after the deposit is {self.account.balance}' )
        return self
    
    def withdraw(self, amount):
        # amount -= self.account.balance
        self.account.balance -= amount
        print(f'Hello, {self.name} you have withdrawn {amount}, Your New Balance is: {self.account.balance}')
        return self
    def displayAcc(self):
        print(f'Hello, {self.name} after all your transactions your account balance is: {self.account.balance}\n')
        return self



Marvin = User('Marvin', 'marvin@gmail.com').deposit(103).deposit(40).withdraw(89).displayAcc()

Account1 = BankAccount(.001,400).deposit(100).deposit(800).deposit(50).withdraw(300).yield_interest().display_account_info()

Account2 = BankAccount(.003, 100).deposit(500).deposit(30).withdraw(5000).withdraw(10).withdraw(50).withdraw(100).yield_interest().display_account_info()


