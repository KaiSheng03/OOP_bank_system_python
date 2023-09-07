#class User
#name,age,gender
#class Bank account
#bank balance

class User:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def showDetails(self):
        print("Name: "+ self.name)
        print(f"Age: {self.age}")
        print("Gender: "+ self.gender)

class Bank:
    def __init__(self,number,balance):
        self.number = number
        self.balance = balance

    def deposit(self,deposit):
        self.balance = self.balance + deposit

    def withdraw(self,withdraw):
        if(self.balance>withdraw):
            self.balance = self.balance - withdraw
        else:
            print("Insufficient amount of balance")

    def showBalance(self):
        print(f"Bank account: {self.number}")
        print(f"Bank balance: {self.balance}")


user1 = User("Kai", 20, "male")
user1 = Bank(1,0)
user1.deposit(2000)
user1.withdraw(1000)
user1.showBalance()

user2 = User("James", 35, "male")
user2.showDetails()
user2 = Bank(2,1000)
user2.deposit(3000)
user2.withdraw(500)
user2.showBalance()