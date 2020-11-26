# def kalkulatro_bmi(waga,wzrots):
#     bmi = waga / wzrots ** 2
#     if bmi < 18.5:
#         wynik = "niedowaga"
#     elif bmi > 25:
#         wynik = "nadwaga"
#     else:
#         wynik = "norma"
#     return wynik
# if __name__ == "__main__":
#     wzrost = float(input("twoj wzrost to: "))
#     wagga = float(input("twoja waga to: "))
#     waga= kalkulatro_bmi(wagga,wzrost)
#     print(f"twoja waga to {waga}")
#
# def imie(imie):
#     print(imie)
#
# imie("tomek")
#
# def ojeden(liczba):
#     return liczba + 1
# wieksza = int(input("podaj licze: "))
# wiekszaa = ojeden(wieksza)
# print(f'liczba wieksza o 1 od {wieksza} to {wiekszaa}')
#
# tomek = 1
# tomek += 1
# print(tomek)
#
# def max(sewuence):
#     najwieksza = 0
#     for element in sewuence:
#         if element > najwieksza:
#             najwieksza = element
#     return najwieksza
# lista=[1,10,3,4,5,6,7,8,9]
# print(max(lista))
#
# def pukanie(name):
#     for x in range(10):
#         print(f'{name}!!!!!!!')
#
# pukanie("aga")

# def odliczanie(numer):
#     while numer:
#         print(numer)
#         numer-= 1
#     print("koniec !!!")
# odliczanie(10)

# def odliczanie1(numer):
#     while numer:
#         print(numer)
#         numer-= 1
#         if numer == 5:
#             break
#     print("koniec !!!")
# odliczanie1(10)

# def odliczanie2(numer):
#     while numer:
#         numer-= 1
#         if numer % 2:
#             continue
#         print(numer)
#
#     print("koniec !!!")
# odliczanie2(10)

# def isogram(slowo):
#     litery=set()
#     for litera in slowo.lower():
#         if litera in litery:
#             return False
#         litery.add(litera)
#     return True
#
# if __name__ == "__main__":
#     while True:
#         slowoo= input("podaj imie ").strip()
#         odp= "jest" if isogram(slowoo) else "nie jest"
#         print(f'Slowo {slowoo} {odp} isogramem\n')
#         czyconti = input("czy chcesz kontynowac y/n? ")
#         if czyconti.lower() != "y":
#             break

# def isogram2(word):
#     lista1= len(word.lower())
#     lista2= len(set(word.lower()))
#     if lista1 == lista2:
#         print(f'Slowo "{word}" jest izogramem')
#     else:
#         print(f'Slowo "{word}" nie jest izogramem')
#
# if __name__ == "__main__":
#
#     isogram2(input("prosze wprowadz slowo: ").strip())

# def count_letters(word):
#     return_dict = {}
#     for letter in list(word.lower()):
#         tmp_counter = return_dict.get(letter, 0)
#         return_dict[letter] = tmp_counter + 1
#
#     return return_dict
#
#
# if __name__ == '__main__':
#     while True:
#         input_word = input('Provide word: ')
#         points = count_letters(input_word)
#         print(f'Word "{input_word}": {points}')
#         input_rerun = input('Do you want to rerun application [y]/n: ')
#         if input_rerun != 'y':
#             break

# punktacja = {chr(x) : y for x, y in zip(range(97, 123), range(1, 27))}
# # print(punktacja)
# def scrabble(slowo):
#      return sum(punktacja[x.lower()] for x in list(slowo))
#
# print(scrabble("tomek"))
