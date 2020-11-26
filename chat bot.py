list1={("czesc","hej",'siema'):"cześc jak sie masz",
       ("dobrze","wspaniale","kapitalnie"):"spoko, jak ci moge pomuc",
       ("źle","słabo",'okropnie'): 'szkoda, jak ci poprawic humor',
       ("kawal","coś smiesznego"): "co robi 9 złotych w portfelu, ledwo dycha"}

def conversation_with_bot(human_input):
    for key, value in list1.items():
        if human_input in key:
            return value
    return "sory nie wiem o co chodzi zmnień słowo"

if __name__ == '__main__':

    while True:
        input_word = input("wpisz slowo: ").lower()
        zwrot= conversation_with_bot(input_word)
        print(zwrot)
        input_rerun = input('czy chcesz ponownie wpsiać Y/N? ')
        if input_rerun.lower() != "y":
            break