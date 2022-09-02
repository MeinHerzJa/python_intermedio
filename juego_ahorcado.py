import random

def invalide_value():
    print("Debes ingresar el valor de 1 o 2")
    return repeat()


def repeat():
    try:
        validate = int(input("Deseas repetir el juego: 1. Si  2. No   "))
        assert validate == 1 or validate == 2, invalide_value()
        if validate == 1:
            run()
        if validate == 2:
            return print("Adios")
    except ValueError:
        invalide_value()


def normalize(value):
    replacements = [("á", "a"), ("´é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u")]

    for a, b in replacements:
        value = value.replace(a, b)
    
    return value

def check_letter(print_word, select_word):
    count = 0
    while print_word != select_word:
        print(print_word)
        try:
            input_letter = normalize(input("Ingrese una letra  "))
            assert not input_letter.isnumeric(), "Debes ingresar una letra o palabra"
            if len(input_letter) > 1:
                if input_letter == select_word:
                    return input_letter
                else:
                    print("No es la palabra")
            if input_letter in select_word:
                print_word = list(print_word)
                for i, x in enumerate(select_word):
                    if x == input_letter:
                        print_word[i] = input_letter
                print_word = "".join(print_word)
            else:
                if count < 20:
                    print("Intenta otra vez")
        except ValueError:
            print("Debes ingresar una letra o palabra")
        count += 1
        if count >= 20:
            return "Perdiste"
    return print_word


def run():
    print("Adivina la palabra")
    words = []
    with open('./archivos/data.txt', 'r', encoding="utf-8") as f:
        words = [line.strip("\n") for line in f]
    index_word = random.randint(0, len(words))
    select_word = normalize(words[index_word])
    print_word = (len(select_word)) * "_"
    print_word = check_letter(print_word, select_word)
    if print_word == "Perdiste":
        print(print_word)
        repeat()
    else:
        print(print_word)
        print("\n")
        print("Ganaste")
        repeat()
    

if __name__ == "__main__":
    run()