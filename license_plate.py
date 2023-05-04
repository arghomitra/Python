import re
from art import *


def morse(plate):
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

    morse_output = ''
    for char in plate.upper():
        if char in morse_code:
            morse_format = morse_code[char]
            morse_output += morse_format + ' '
    return morse_output.strip()


def ascii(plate):
    ascii_format = text2art(plate)
    return ascii_format


def nato(plate):
    nato_alphabet = {
        "A": "ALFA",
        "B": "BRAVO",
        "C": "CHARLIE",
        "D": "DELTA",
        "E": "ECHO",
        "F": "FOXTROT",
        "G": "GOLF",
        "H": "HOTEL",
        "I": "INDIA",
        "J": "JULIET",
        "K": "KILO",
        "L": "LIMA",
        "M": "MIKE",
        "N": "NOVEMBER",
        "O": "OSCAR",
        "P": "PAPA",
        "Q": "QUEBEC",
        "R": "ROMEO",
        "S": "SIERRA",
        "T": "TANGO",
        "U": "UNIFORM",
        "V": "VICTOR",
        "W": "WHISKEY",
        "X": "XRAY",
        "Y": "YANKEE",
        "Z": "ZULU",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "0": "Zero"
    }
    nato_output = ''
    for letter in plate.upper():
        if letter in nato_alphabet:
            word = nato_alphabet[letter]
            nato_output += word + ' '
    return nato_output.strip()


def forbidden(plate):

    forbidden_combination = ['AAP', 'AAS', 'AEL', 'ALA', 'ANE', 'ASS', 'BEB', 'BIT', 'BOM', 'BOY', 'BSP', 'BUB', 'BWP',
                             'BYT', 'CAP', 'CDF', 'CDH', 'CDV', 'CON', 'CSP', 'CUB', 'CUL', 'CUT', 'CVP', 'DCD', 'DIK',
                             'DOM', 'FDF', 'FOK', 'FOL', 'FOU', 'FUC', 'FUK', 'GAT', 'GAY', 'GEK', 'GOD', 'HIV', 'HOL',
                             'JEK', 'KAK', 'KKQ', 'KUL', 'KUT', 'LAF', 'LDD', 'LSP', 'LUL',
                             'MAS', 'MCC', 'MDP', 'MOR', 'MOU', 'MST', 'NIC', 'NIK', 'NIQ', 'NVA', 'PDB', 'PDO', 'PET',
                             'PFF', 'PIK', 'PIN', 'PIP', 'PIS', 'PJU', 'PKK', 'POT', 'PRL', 'PSB', 'PSC', 'PSL', 'PTB',
                             'PUE', 'PUT', 'PVV', 'PYK', 'PYN', 'PYP', 'PYS', 'ROM', 'SEX', 'SOA', 'SOT', 'SPA', 'SUL',
                             'TAK', 'TET', 'TIT', 'TUE', 'VCD', 'VIH', 'VLD', 'VMO', 'VNV', 'ZAC', 'ZAK', 'ZOT']

    for word in forbidden_combination:
        if word in plate:
            return True
    return False


def main():
    plate = input().strip().upper()

    check_plate = (check(plate))
    print(check_plate)

    if check_plate.startswith('forbidden'):
        exit()

    art = input().strip().lower()
    if art == "morse":
        print(morse(plate))
    elif art == "ascii":
        print(ascii(plate))
    elif art == "nato":
        print(nato(plate).upper())
    else:
        print("Wrong format!")


def check(plate):

    forbi = forbidden(plate)

    if forbi == True:
        a = plate.split('-')
        for i in a:
            if len(i) == 3 and i.isalpha():
                return (f'forbidden plate - {i}')

    pattern1 = r"(?<!\d)[1-9](?!\d)"
    pattern2 = r"\d\d?\b"
    pattern3 = r"A-\d\d?\d?\b"
    pattern4 = r"CD-[A-Z]{2}[1-9]{3}"
    pattern5 = r"G-L[A-Z]{2}-[1-9]{3}"
    pattern6 = r"M-[A-Z]{3}-[0-9]{3}"
    pattern7 = r"O-[A-Z]{3}-[1-9]{3}"
    pattern8 = r"Q-[A-Z]{3}-[0-9]{3}"
    pattern9 = r"T-X[A-Z]{2}-[0-9]{3}"
    pattern10 = r"Y-[A-Z]{3}-[0-9]{3}"
    pattern11 = r"([A-Z]{2})\.\d{3}"
    pattern12 = r"[A-Z]\.\d{3}\.[A-Z]"
    pattern13 = r"(\w+-)?(([A-Z]{3})-\d{3})"
    pattern14 = r"\d{3}-[A-Z]{3}"
    pattern15 = r"^[1-7]-[A-Z]{3}-\d{3}$"

    if re.match(pattern1, plate):
        return ("special plate -  king and queen")

    elif re.match(pattern2, plate):
        return ("special plate -  royal")

    elif re.match(pattern3, plate):
        return ("special plate -  official")

    elif re.match(pattern4, plate):
        return ("special plate - diplomat")

    elif re.match(pattern5, plate):
        return ("special plate - agriculture")

    elif re.match(pattern6, plate):
        return ("special plate - motorcycle")
    elif re.match(pattern7, plate):
        return ("special plate - oldtimer")
    elif re.match(pattern8, plate):
        return ("special plate - trailer")
    elif re.match(pattern9, plate):
        return ("special plate - taxi")
    elif re.match(pattern10, plate):
        return ("special plate - test")
    elif re.match(pattern11, plate):
        return ("standard plate - 1962-1971")
    elif re.match(pattern12, plate):
        return ("standard plate - 1971-1973")
    elif re.match(pattern13, plate):
        return ("standard plate - 1973-2008")
    elif re.match(pattern14, plate):
        return ("standard plate - 2008-2010")
    elif re.match(pattern15, plate):
        return ("standard plate - 2010-now")
    else:
        return 'invalid plate'


if __name__ == "__main__":
    main()
