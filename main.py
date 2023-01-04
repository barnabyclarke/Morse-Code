import pandas

morse_alphabet = pandas.read_csv('morse-alphabet.csv', quotechar="#")


def start():
    trans_direction = input("Type '1' to translate from Text to Morse, '2' to translate from Morse to Text, "
                            "or '3' to quit: ")
    if trans_direction == '1':
        into_morse_alphabet()
    elif trans_direction == '2':
        into_text()
    elif trans_direction == '3':
        return quit()
    else:
        print('Please use one of the listed responses (1, 2, or 3).')
        start()


def into_morse_alphabet():
    answer_string = ''
    morse_dictionary = {row.letter: row.morse for (index, row) in morse_alphabet.iterrows()}
    answer = input("Enter text to be converted into morse:\n").upper()
    try:
        answer_in_morse = [morse_dictionary[letter] for letter in answer]
    except KeyError:
        print('Only letters or numbers, please.')
        into_morse_alphabet()
    else:
        for key in answer_in_morse:
            answer_string += f'{key} '
        print(answer_string)

    start()


def into_text():
    answer_string = ''
    morse_dictionary = {row.morse: row.letter for (index, row) in morse_alphabet.iterrows()}
    answer = input("Enter morse code (only using '.', '-', and '/') with a space between each character to be "
                   "converted into text:\n").replace(' ', ',').split(',')
    try:
        answer_in_text = [morse_dictionary[morse] for morse in answer]
    except KeyError:
        print("Only use '.', '-', and '/', please. TIP: Make sure there is no space at the end of the morse code!")
        into_text()
    else:
        for key in answer_in_text:
            answer_string += f'{key}'
        print(answer_string)

    start()


start()
