# f = open("przyklad.txt","w")
# f.write("powtarzam po zajeciach\ndodalem enter za pomoca\n")
# f.write("""teraz inna forma
# wpisywania
# entera""")
# f.close()
#
# with open("przyklad.txt", "a") as f:
#     f.write("nowal linia")
# dir - komenda w Win w terminalu do sprawdzenia co jest w folderze

# with open ('przyklad.txt') as f:
#     for line in f:
#         print(line)

# class Car:
#     acceleration = 10
#     def __init__(self,registration_numer):
#         self.registration_numer=registration_numer
#         self.in_motion = False
#         self.speed = 0
#
#     def print_info(self):
#         print(f"przyspieszenie jest {self.acceleration}")
#         print(f"numer rejestracyjny to{self.registration_numer}")
#         print(f'czy jest w ruchu {self.in_motion}')
#         print(f'pretkosc jest {self.speed}')
#         print()
#
#     def stop(self):
#         self.in_motion = False
#         self.speed = 0
#
#     def drive(self):
#         self.in_motion = True
#
#     def accelerate(self, przyszpieszenie):
#         if self.in_motion:
#             self.speed += przyszpieszenie
#         else:
#             print("nie mozesz przyspieszac")
#             print()
#
# audi= Car('wpr123')
# volvo= Car("wpr1234")
# mercedes= Car('wpr12345')
#
# audi.accelerate(5)
# audi.drive()
# audi.accelerate(5)
# audi.accelerate(15)
# audi.accelerate(1)
#
# audi.print_info()
# #volvo.print_info()
# #mercedes.print_info()

class Employee:
    rise_amount = 1.04
    def __init__(self,first,last,pay,email):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = email
    def apply_rise(self):
        self.pay = int(self.pay * self.rise_amount)
    def tax(self, prugdochodwy = 85000):
        self.amount_pay=self.pay*12
        if self.amount_pay <= prugdochodwy:
            print(f'twoj podatek to {self.amount_pay*0.17}')
        else:
            print(f"twój podatek to {(self.amount_pay*0.17)+((self.amount_pay-prugdochodwy)*0.32)}")
    @classmethod
    def set_rise_amount(cls,new_rasise_amount):
        cls.rise_amount = new_rasise_amount
    @staticmethod
    def sallary_tax(value):
        print("pierwsza prug podatkowy 17%")
        print(f'Dochod powyzej {value} jest objeta drugim podadkiem dochodowym')
        print("drugi prug podakowy 32%")

Employee.set_rise_amount(1.8)
tomek=Employee("tomek","dominiak",10000,"t.dominiak")
aga=Employee("Aga","pawlinska",10000,"paw@2")
aga.rise_amount =1.1
tomek.apply_rise()
aga.apply_rise()
print(tomek.pay)
print(aga.pay)
tomek.tax()
aga.tax()
aga.tax(1000)
tomek.sallary_tax(8500)

class Developer(Employee):
    rise_amount = 4.5
    def __init__(self,first,last,pay,email,lenguage):
        super().__init__(first,last,pay,email)
        self.lenguage = lenguage

tomek1=Developer("tomek","dominiak",10000,"t.dominiak","phyton")

print(tomek.rise_amount)
print(tomek1.rise_amount)
tomek1.apply_rise()
print(tomek1.pay)
print(tomek1.lenguage)
# class Book:
#     total_numer_of_book = 0
#     def __init__(self,title, author):
#         self.title = title
#         self.author = author
#         Book.total_numer_of_book += 1
#         self.id = Book.total_numer_of_book
# dupa=Book("pizda","cipa")
# fuck=Book("ciota","sierota")
# lolo=Book("marka","dziarka")
#
# print(lolo.id)
# print(lolo.title)





