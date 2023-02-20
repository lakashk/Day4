# def add(a,b,c):
#     return a+b+c
#
# print(add(1,2,3))
#
# # lambda a,b,c : a+b+c
# print((lambda a,b,c : a+b+c)(1,2,5))


# def my_fuction(a):
#     print(a)
#
# def my_second_functon():
#     print("Hello")
#     return 10
#
# my_fuction(my_second_functon())
# # my_fuction([1,2,3,4,5])


# def my_fuction(a):
#     print(a())
#
# def my_second_functon():
#     print("Hello")
#     return 10
#
# my_fuction(lambda :10)


#caluclator function to lambda functipn
# a = int(input('Enter any number'))
# b = int(input('Enter any number'))
# def calculator(a):
#     print(a)
#
#
# calculator((lambda a, b: a+b)(a,b))
# calculator((lambda a, b: a-b)(a,b))
# calculator((lambda a, b: a*b)(a,b))
# calculator((lambda a, b: a/b)(a,b))
#
#


#QR code Program
# import qrcode

# img = qrcode.make("My name is Akash")
# img.save("qrocode.png")
#
# data = input("Enter data")
# img = qrcode.make(data)
# img.save("data.png")
#

# add dictionary in input
# data = {
#     "Name": "Akash",
#     "Location":"Pune"
# }
# img = qrcode.make(data)
# img.save("data1.png")
#


#oops concept of pyhton
# Class - A class consist of data members and member function

# class Triptonepal:
#     budget = 5500
#     modeoftransport = "car"
#
#     def eat_something(self , cost):
#         self.budget = self.budget - cost
#
#     def change_mode_of_tansport

# class Calculator:
#
#     def add(self,a , b):
#         print(a+b)
#
#     def sub(self,a , b):
#         print(a-b)
#
#     def mul(self,a , b):
#         print(a*b)
#
#     def div(self,a , b):
#         print(a/b)
#
# cal = Calculator()
# cal.add(10,20)
# cal.sub(20,40)
# cal.mul(30,20)
# cal.div(40,10)


# class Student:
#
#     name =" Harry potter"
#     branch = "Magic"
#     def __init__(self, name , branch):
#         # self.name = name
#         self.branch = branch
#         print(name,self.branch)
#
#     def getdata(self):
#         print(self.name,self.branch)
#
# s1 = Student("Akash","EE")
# s1.getdata()



#wap using class to sreach input in name


# class Student:
#     def __init__(self, name ,usn , branch):
#         self.name = name
#         self.usn = usn
#         self.branch = branch
#
#     def updatebranch(self,newbranch):
#         self.branch = newbranch
#         # print("Updated Branch: ",branch)
#
#     def display_detail(self):
#         print('Student name:', self.name)
#         print('usn :', self.usn)
#         print('branch:', self.branch)
#
# student_db = [
#     Student("Harry Potter", "007", "Magic"),
#     Student("Dobby", "006", "Elf"),
#     Student("Snape", "005", "Dark Arts"),
# ]
#
# search_query = input("Enter your search: ")
# filter_data = [x for x in student_db if x.name.count(search_query) >= 1]
#
# if len(filter_data) >=1:
#     [x.display_detail() for x in filter_data]
# else:
#     print("No data Fount")


#create shape class
#s = shape(10) circle
#s = shape(10,20)
#
# import math
# class Shape:
#
#     def __init__(self,*args):
#         if len(args) == 1:
#             print('Circle')
#             print('area:', math.pi * args[0] * args[0])
#             print("Circumference: ", 2 * math.pi * args[0])
#
#         if len(args) == 2:
#             print("Square")
#             print("Area of Square: ", args[0]*args[1])
#             print("Perimeter: ",2*(args[0]+args[1]))
#
#
# circel= Shape(10)
# rec = Shape(10,20)


#inheritance



# from fastapi import FastAPI
# app = FastAPI()
#
# @app.get("/sample")
# def hello():
#     return{
#         "Name":"Hello",
#         "Address":"World"
#     }


#Atm
#balance,pin,cardnumber
#getdetails,updatepin
#1.withdrwal ,2 deposit 3 update pin 4get balnace

#1 withdrawl >ask pin >enter amt >balance
#2 deposit >entr amt >update balance
#3 update pin >enter current pin >enter new pin


class Atm:
    def __init__(self,balance,pin,card_number):
        self.balance = balance
        self.pin = pin
        self.card_number = card_number


    # def get_detail(self,balance,pin,card_number):
    #     print(balance,pin,card_number)

        if ch == 1:
            print("Withdrwal")
            pin1 = int(input("Enter Your pin"))
            if self.pin == pin1:
                amt = int(input("Enter amount to withdraw: "))
                balance = balance -amt
                self.balance = balance
                print(balance)

            else:
                print("Invalid Pin")

        if ch == 2:
            print("Deposit")
            pin1 = int(input("Enter Your pin"))
            if self.pin == pin1:
                amt = int(input("Enter amount to deposit: "))
                balance = balance + amt
                self.balance = balance
                print(balance)

        if ch ==3:
            print("Update Pin")
            pin1 = int(input("Enter Your current pin"))
            if self.pin == pin1:
                pin2 = int(input("Enter new pin"))
                self.pin =pin2
                print("Updated Pin of card: ",self.pin)



    # def update_pin(self,pin):


ch = int(input(("Enter your choice")))
t = Atm(10000,1234,11112222)