
lista={chr(letter): value for letter, value in zip(range(97, 123),range(1, 27))}
print(lista)

def calculate_points(word):
    return sum([lista[letter.lower()] for letter in list(word)])

if __name__ == '__main__':
    while True:
        input_word = input("wpisz slowo ").strip()
        points = calculate_points(input_word)
        print(f"slowo {input_word} ma {points} punktow")
        input_rerun = input('czy chcesz ponownie wpsiać Y/N? ')
        if input_rerun.lower() != "y":
            break

