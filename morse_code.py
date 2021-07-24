# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 456.
# Q. 4 Morse Code Converter.

def morse_code(string):
    string = string.upper()
    character = [
        ',', '.', '?', ';', ':', '/',
        '!', '+', '-', '$', '&', '@',
        '(', ')', '0', '1', '2', '3',
        '4', '5', '6', '7', '8', '9',
        'A', 'B', 'C', 'D', 'E', 'F',
        'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z'
    ]
    morse_code_character = [
        '--..--', '.-.-.-', '..--..', '-.-.-.',
        '---...', '-..-.', '-.-.--', '.-.-.',
        '-....-', '...-..-', '.-...', '.--.-.',
        '-.--.', '-.--.-', '-----', '.----',
        '..---', '...--', '....-', '.....',
        '-....', '--...', '---..', '----.',
        '.-', '-...', '-.-.', '-..', '.', '..-.',
        '--.', '....', '..', '.---', '-.-', '.-..',
        '--', '-.', '---', '.--.', '--.-', '.-.',
        '...', '-', '..-', '...-', '.--', '-..-',
        '-.-', '--..']

    for n in range(len(character)):
        string = string.replace(character[n], morse_code_character[n])
    print(string)


string = str(input())
morse_code(string)
