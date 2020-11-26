# def greetings(funkcja):
#     def morning (*args, **kwargs):
#         print("good morning,")
#         funkcja(*args, **kwargs)
#         print("ale z ciebie palant")
#     return morning
#
# def cipa(name):
#     print(name)
# @greetings
# def cipa2(name,lala):
#     print(name,lala)
#
# greetings(cipa)("tomek2")
#
# cipa2("Aga","morda")

# def liczba_parzysta(funkcja):
#     def wrapper (liczba):
#         print("Poniższa liczba jest:")
#         if liczba  % 2 == 0 :
#             print(f"parzysta {liczba}")
#         else:
#             print(f"nieparzysta {liczba}")
#     return wrapper
#
# @liczba_parzysta
# def kalkulacja(liczba):
#     print(liczba)
#
# kalkulacja(10)

lista_zarobkow=[10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000,10000]
pensja=sum(lista_zarobkow)
def zarobek(func):
    def wrapper (kwota_podatkowa):
         print(func)
        return wrapper
    return zarobek

@zarobek
def podatek(kwota_podatkowa)
    if pensja > kwota_podatkowa:
        tax = ((pensja-kwota_podatkowa)*0.32)+(kwota_podatkowa*0.17)
        print(f'Twoj podatel to {tax}')
    else:
        print(f'Twoj podatek to {pensja*0.17}')
    return podatek
podatek(85000)



