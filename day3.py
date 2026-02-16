# class BankAccount():
#     private balance
#     def deposit(amount):
#         balance += amount
#     def withdraw(amount):
#         balance -= amount
#     def show_balance():
#         return balance
    
# class SavingsAccount inherits  from BankAccount():
# class bank:
#     name ="Aman Mahato"
#     ifsc ="SBIN0001234"
#     Bank_Name ="State Bank of India"
#     address ="123, MG Road, City"
# a1 = bank()
# bank.name="amit"
# print(a1.name)
# a1.name="rahul"
# print(bank.name)
#Write a Python decorator named my_decorator that prints
# "Function is starting" before a function runs
# and "Function finished" after the function runs.
def my_decorator(func):
    def wrapper():
        print("Function is starting")
        func()
        print("Function finished")
    return wrapper  
@my_decorator
def say_hello():
    print("Hello!")
say_hello()
