class User:

    bank = "Marvins Internation Bank"

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self,amount):
        self.account_balance += amount
        return self
    def make_withdraw(self,amount):
        self.account_balance -= amount
        return self


    def make_transfer(self,account, amount):
        self.account_balance-= amount 
        account.account_balance += amount
        
    def display_account_info(self):
        return self.account_balance



Marvin = User("Marvin", "marvin.miguel.diaz@gmail.com")
Tanjina = User("Tanjina", "Tangerine@gmail.com")
Fahad = User("Fahad", "Gym4Life@gmail.com")

Marvin.make_deposit(100).make_deposit(1000).make_deposit(300).make_withdraw(70)
print(f'Hello, {Marvin.name} your balance is: ${Marvin.account_balance}')

Tanjina.make_deposit(400).make_deposit(200).make_withdraw(100).make_withdraw(50)
print(f'Hello, {Tanjina.name} your balance is: ${Tanjina.account_balance}')

Fahad.make_deposit(1000).make_withdraw(10).make_withdraw(90)
print(f'Hello, {Fahad.name} your balance is: ${Fahad.account_balance}')


Fahad.make_transfer(Tanjina,400000)
print(f'Hello {Fahad.name} you have succesfully transfered money to {Tanjina.name} Your Account Balance is: ${Fahad.account_balance}\n{Tanjina.name}s New Account Balance is: ${Tanjina.account_balance}')

print(f'Hello {Marvin.name}your account balance is: {Marvin.account_balance}')
