def izogram(word):
    list_of_words = list(word)
    set_of_words = set(list_of_words)
    if len(list_of_words) == len(set_of_words):
        print(f'twoje slowo ({word}) jest izogramem')
    else:
        print(f'twoje slowo ({word}) nie jest izogramem')

if __name__ == "__main__":
        izogram(input("prosze wpisz swoje słowo: "))
