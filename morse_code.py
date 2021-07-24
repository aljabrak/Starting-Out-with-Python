# Starting Out with Python (4th Edition).
# Tony Gaddis.
# Page 456.
# Q. 4 Morse Code Converter.

def morse_code(string):
    string = string.upper()
    characters = [',', '.', '?']
    morse_code_characters = ['--..--', '.-.-.-', '..--..']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    morse_code_numbers = ['-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.']
    alpahbets = [
        'A', 'B', 'C', 'D', 'E', 'F',
        'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R',
        'S', 'T', 'U', 'V', 'W', 'X',
        'Y', 'Z'
    ]
    morse_code_alpahbets = [
        '.-', '-...', '-.-.', '-..', '.', '..-.',
        '--.', '....', '..', '.---', '-.-', '.-..',
        '--', '-.', '---', '.--.', '--.-', '.-.',
        '...', '-', '..-', '...-', '.--', '-..-',
        '-.-', '--..'
    ]

    for n in range(len(numbers)):
        string = string.replace(numbers[n], morse_code_numbers[n])

    for n in range(len(characters)):
        string = string.replace(characters[n], morse_code_characters[n])
    
    for n in range(len(alpahbets)):
        string = string.replace(alpahbets[n], morse_code_alpahbets[n])

    print(string)


string = str(input())
morse_code(string)
