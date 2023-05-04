import re
from pyfiglet import figlet_format


def morse(plate):
    morse_code = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
                  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

    for char in plate:
        if char in morse_code:
            print(morse_code[char], end=' ')


def ascii(plate):
    print(figlet_format(plate, font="standard"))


def nato(plate):
    nato_alphabet = {
        "A": "ALPHA",
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
        "Z": "ZULU"
    }

    for letter in plate.upper():
        if letter in nato_alphabet:
            word = nato_alphabet[letter]
            print(word, end=' ')


pattern1 = r"[1-9]\b"
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
pattern15 = r"\d-[A-Z]{3}-\d{3}"

forbidden_combination = ['AAP', 'AAS', 'AEL', 'ALA', 'ANE', 'ASS', 'BEB', 'BIT', 'BOM', 'BOY', 'BSP', 'BUB', 'BWP', 'BYT', 'CAP', 'CDF', 'CDH', 'CDV', 'CON', 'CSP', 'CUB', 'CUL', 'CUT', 'CVP', 'DCD', 'DIK', 'DOM', 'FDF', 'FOK', 'FOL', 'FOU', 'FUC', 'FUK', 'GAT', 'GAY', 'GEK', 'GOD', 'HIV', 'HOL', 'JEK', 'KAK', 'KKQ', 'KUL', 'KUT', 'LAF', 'LDD', 'LSP', 'LUL',
                         'MAS', 'MCC', 'MDP', 'MOR', 'MOU', 'MST', 'NIC', 'NIK', 'NIQ', 'NVA', 'PDB', 'PDO', 'PET', 'PFF', 'PIK', 'PIN', 'PIP', 'PIS', 'PJU', 'PKK', 'POT', 'PRL', 'PSB', 'PSC', 'PSL', 'PTB', 'PUE', 'PUT', 'PVV', 'PYK', 'PYN', 'PYP', 'PYS', 'ROM', 'SEX', 'SOA', 'SOT', 'SPA', 'SUL', 'TAK', 'TET', 'TIT', 'TUE', 'VCD', 'VIH', 'VLD', 'VMO', 'VNV', 'ZAC', 'ZAK', 'ZOT']


def is_forbidden(plate):
    for word in forbidden_combination:
        if word in plate:
            return True
    return False


plate = input("Enter license plate: ")
user = plate


def main():
    def check(plate):
        forbidden = r"(?=AAP|AAS|AEL|ALA|ANE|ASS|BEB|BIT|BOM|BOY|BSP|BUB|BWP|BYT|CAP|CDF|CDH|CDV|CON|CSP|CUB|CUL|CUT|CVP|DCD|DIK|DOM|FDF|FOK|FOL|FOU|FUC|FUK|GAT|GAY|GEK|GOD|HIV|HOL|JEK|KAK|KKQ|KUL|KUT|LAF|LDD|LSP|LUL|MAS|MCC|MDP|MOR|MOU|MST|NIC|NIK|NIQ|NVA|PDB|PDO|PET|PFF|PIK|PIN|PIP|PIS|PJU|PKK|POT|PRL|PSB|PSC|PSL|PTB|PUE|PUT|PVV|PYK|PYN|PYP|PYS|ROM|SEX|SOA|SOT|SPA|SUL|TAK|TET|TIT|TUE|VCD|VIH|VLD|VMO|VNV|ZAC|ZAK|ZOT)"
        forbidden2 = r"\d{3}-(AAP|AAS|AEL|ALA|ANE|ASS|BEB|BIT|BOM|BOY|BSP|BUB|BWP|BYT|CAP|CDF|CDH|CDV|CON|CSP|CUB|CUL|CUT|CVP|DCD|DIK|DOM|FDF|FOK|FOL|FOU|FUC|FUK|GAT|GAY|GEK|GOD|HIV|HOL|JEK|KAK|KKQ|KUL|KUT|LAF|LDD|LSP|LUL|MAS|MCC|MDP|MOR|MOU|MST|NIC|NIK|NIQ|NVA|PDB|PDO|PET|PFF|PIK|PIN|PIP|PIS|PJU|PKK|POT|PRL|PSB|PSC|PSL|PTB|PUE|PUT|PVV|PYK|PYN|PYP|PYS|ROM|SEX|SOA|SOT|SPA|SUL|TAK|TET|TIT|TUE|VCD|VIH|VLD|VMO|VNV|ZAC|ZAK|ZOT)\b"
        forbidden3 = r"\d-(AAP|AAS|AEL|ALA|ANE|ASS|BEB|BIT|BOM|BOY|BSP|BUB|BWP|BYT|CAP|CDF|CDH|CDV|CON|CSP|CUB|CUL|CUT|CVP|DCD|DIK|DOM|FDF|FOK|FOL|FOU|FUC|FUK|GAT|GAY|GEK|GOD|HIV|HOL|JEK|KAK|KKQ|KUL|KUT|LAF|LDD|LSP|LUL|MAS|MCC|MDP|MOR|MOU|MST|NIC|NIK|NIQ|NVA|PDB|PDO|PET|PFF|PIK|PIN|PIP|PIS|PJU|PKK|POT|PRL|PSB|PSC|PSL|PTB|PUE|PUT|PVV|PYK|PYN|PYP|PYS|ROM|SEX|SOA|SOT|SPA|SUL|TAK|TET|TIT|TUE|VCD|VIH|VLD|VMO|VNV|ZAC|ZAK|ZOT)-\d{3}"
        forbidden4 = r"G-(AAP|AAS|AEL|ALA|ANE|ASS|BEB|BIT|BOM|BOY|BSP|BUB|BWP|BYT|CAP|CDF|CDH|CDV|CON|CSP|CUB|CUL|CUT|CVP|DCD|DIK|DOM|FDF|FOK|FOL|FOU|FUC|FUK|GAT|GAY|GEK|GOD|HIV|HOL|JEK|KAK|KKQ|KUL|KUT|LAF|LDD|LSP|LUL|MAS|MCC|MDP|MOR|MOU|MST|NIC|NIK|NIQ|NVA|PDB|PDO|PET|PFF|PIK|PIN|PIP|PIS|PJU|PKK|POT|PRL|PSB|PSC|PSL|PTB|PUE|PUT|PVV|PYK|PYN|PYP|PYS|ROM|SEX|SOA|SOT|SPA|SUL|TAK|TET|TIT|TUE|VCD|VIH|VLD|VMO|VNV|ZAC|ZAK|ZOT)-\d{3}"
        forbidden5 = r"M-(AAP|AAS|AEL|ALA|ANE|ASS|BEB|BIT|BOM|BOY|BSP|BUB|BWP|BYT|CAP|CDF|CDH|CDV|CON|CSP|CUB|CUL|CUT|CVP|DCD|DIK|DOM|FDF|FOK|FOL|FOU|FUC|FUK|GAT|GAY|GEK|GOD|HIV|HOL|JEK|KAK|KKQ|KUL|KUT|LAF|LDD|LSP|LUL|MAS|MCC|MDP|MOR|MOU|MST|NIC|NIK|NIQ|NVA|PDB|PDO|PET|PFF|PIK|PIN|PIP|PIS|PJU|PKK|POT|PRL|PSB|PSC|PSL|PTB|PUE|PUT|PVV|PYK|PYN|PYP|PYS|ROM|SEX|SOA|SOT|SPA|SUL|TAK|TET|TIT|TUE|VCD|VIH|VLD|VMO|VNV|ZAC|ZAK|ZOT)-\d{3}"
        forbidden6 = r"O-(AAP|AAS|AEL|ALA|ANE|ASS|BEB|BIT|BOM|BOY|BSP|BUB|BWP|BYT|CAP|CDF|CDH|CDV|CON|CSP|CUB|CUL|CUT|CVP|DCD|DIK|DOM|FDF|FOK|FOL|FOU|FUC|FUK|GAT|GAY|GEK|GOD|HIV|HOL|JEK|KAK|KKQ|KUL|KUT|LAF|LDD|LSP|LUL|MAS|MCC|MDP|MOR|MOU|MST|NIC|NIK|NIQ|NVA|PDB|PDO|PET|PFF|PIK|PIN|PIP|PIS|PJU|PKK|POT|PRL|PSB|PSC|PSL|PTB|PUE|PUT|PVV|PYK|PYN|PYP|PYS|ROM|SEX|SOA|SOT|SPA|SUL|TAK|TET|TIT|TUE|VCD|VIH|VLD|VMO|VNV|ZAC|ZAK|ZOT)-\d{3}"
        forbidden7 = r"Q-(AAP|AAS|AEL|ALA|ANE|ASS|BEB|BIT|BOM|BOY|BSP|BUB|BWP|BYT|CAP|CDF|CDH|CDV|CON|CSP|CUB|CUL|CUT|CVP|DCD|DIK|DOM|FDF|FOK|FOL|FOU|FUC|FUK|GAT|GAY|GEK|GOD|HIV|HOL|JEK|KAK|KKQ|KUL|KUT|LAF|LDD|LSP|LUL|MAS|MCC|MDP|MOR|MOU|MST|NIC|NIK|NIQ|NVA|PDB|PDO|PET|PFF|PIK|PIN|PIP|PIS|PJU|PKK|POT|PRL|PSB|PSC|PSL|PTB|PUE|PUT|PVV|PYK|PYN|PYP|PYS|ROM|SEX|SOA|SOT|SPA|SUL|TAK|TET|TIT|TUE|VCD|VIH|VLD|VMO|VNV|ZAC|ZAK|ZOT)-\d{3}"
        forbidden9 = r"Y-(AAP|AAS|AEL|ALA|ANE|ASS|BEB|BIT|BOM|BOY|BSP|BUB|BWP|BYT|CAP|CDF|CDH|CDV|CON|CSP|CUB|CUL|CUT|CVP|DCD|DIK|DOM|FDF|FOK|FOL|FOU|FUC|FUK|GAT|GAY|GEK|GOD|HIV|HOL|JEK|KAK|KKQ|KUL|KUT|LAF|LDD|LSP|LUL|MAS|MCC|MDP|MOR|MOU|MST|NIC|NIK|NIQ|NVA|PDB|PDO|PET|PFF|PIK|PIN|PIP|PIS|PJU|PKK|POT|PRL|PSB|PSC|PSL|PTB|PUE|PUT|PVV|PYK|PYN|PYP|PYS|ROM|SEX|SOA|SOT|SPA|SUL|TAK|TET|TIT|TUE|VCD|VIH|VLD|VMO|VNV|ZAC|ZAK|ZOT)-\d{3}"

        if re.match(pattern1, plate):
            print("special plate -  king and queen")
            art = input("Enter format: ")
            if art == "morse":
                morse(plate)
            elif art == "ascii":
                ascii(plate)
            elif art == "nato":
                nato(plate)
            else:
                print("Wrong format!")

        elif re.match(pattern2, plate):
            print("special plate -  royal")
            art = input("Enter format: ")
            if art == "morse":
                morse(plate)
            elif art == "ascii":
                ascii(plate)
            elif art == "nato":
                nato(plate)
            else:
                print("Wrong format!")

        elif re.match(pattern3, plate):
            print("special plate -  official")
            art = input("Enter format: ")
            if art == "morse":
                morse(plate)
            elif art == "ascii":
                ascii(plate)
            elif art == "nato":
                nato(plate)
            else:
                print("Wrong format!")

        elif re.match(pattern4, plate):
            print("special plate - diplomat")
            art = input("Enter format: ")
            if art == "morse":
                morse(plate)
            elif art == "ascii":
                ascii(plate)
            elif art == "nato":
                nato(plate)
            else:
                print("Wrong format!")

        elif re.match(pattern5, plate):
            if is_forbidden(plate):
                for word in forbidden_combination:
                    if word in plate:
                        print(f'forbidden plate - "{word}"')
            else:
                print("special plate - agriculture")
                art = input("Enter format: ")
                if art == "morse":
                    morse(plate)
                elif art == "ascii":
                    ascii(plate)
                elif art == "nato":
                    nato(plate)
                else:
                    print("Wrong format!")

        elif re.match(pattern6, plate):
            if is_forbidden(plate):
                for word in forbidden_combination:
                    if word in plate:
                        print(f'forbidden plate - "{word}"')
            else:
                print("special plate - motorcycle")
                art = input("Enter format: ")
                if art == "morse":
                    morse(plate)
                elif art == "ascii":
                    ascii(plate)
                elif art == "nato":
                    nato(plate)
                else:
                    print("Wrong format!")
        elif re.match(pattern7, plate):
            if is_forbidden(plate):
                for word in forbidden_combination:
                    if word in plate:
                        print(f'forbidden plate - "{word}"')
            else:
                print("special plate - oldtimer")
                art = input("Enter format: ")
                if art == "morse":
                    morse(plate)
                elif art == "ascii":
                    ascii(plate)
                elif art == "nato":
                    nato(plate)
                else:
                    print("Wrong format!")

        elif re.match(pattern8, plate):
            if is_forbidden(plate):
                for word in forbidden_combination:
                    if word in plate:
                        print(f'forbidden plate - "{word}"')
            else:
                print("special plate - trailer")
                art = input("Enter format: ")
                if art == "morse":
                    morse(plate)
                elif art == "ascii":
                    ascii(plate)
                elif art == "nato":
                    nato(plate)
                else:
                    print("Wrong format!")

        elif re.match(pattern9, plate):
            print("special plate -  taxi")
            art = input("Enter format: ")
            if art == "morse":
                morse(plate)
            elif art == "ascii":
                ascii(plate)
            elif art == "nato":
                nato(plate)
            else:
                print("Wrong format!")
        elif re.match(pattern10, plate):
            if is_forbidden(plate):
                for word in forbidden_combination:
                    if word in plate:
                        print(f'forbidden plate - "{word}"')
            else:
                print("special plate - test")
                art = input("Enter format: ")
                if art == "morse":
                    morse(plate)
                elif art == "ascii":
                    ascii(plate)
                elif art == "nato":
                    nato(plate)
                else:
                    print("Wrong format!")

        elif re.match(pattern11, plate):
            print("standard plate - 1962-1971")
            art = input("Enter format: ")
            if art == "morse":
                morse(plate)
            elif art == "ascii":
                ascii(plate)
            elif art == "nato":
                nato(plate)
            else:
                print("Wrong format!")

        elif re.match(pattern12, plate):
            print("standard plate - 1971-1973")

            art = input("Enter format: ")
            if art == "morse":
                morse(plate)
            elif art == "ascii":
                ascii(plate)
            elif art == "nato":
                nato(plate)
            else:
                print("Wrong format!")

        elif re.match(pattern13, plate):
            if is_forbidden(plate):
                for word in forbidden_combination:
                    if word in plate:
                        print(f'forbidden plate - "{word}"')
            else:
                print("standard plate - 1973-2008")
                art = input("Enter format: ")
                if art == "morse":
                    morse(plate)
                elif art == "ascii":
                    ascii(plate)
                elif art == "nato":
                    nato(plate)
                else:
                    print("Wrong format!")

        elif re.match(pattern14, plate):
            if is_forbidden(plate):
                for word in forbidden_combination:
                    if word in plate:
                        print(f'forbidden plate - "{word}"')
            else:
                print("standard plate - 2008-2010")
                art = input("Enter format: ")
                if art == "morse":
                    morse(plate)
                elif art == "ascii":
                    ascii(plate)
                elif art == "nato":
                    nato(plate)
                else:
                    print("Wrong format!")
        elif re.match(pattern15, plate):
            if is_forbidden(plate):
                for word in forbidden_combination:
                    if word in plate:
                        print(f'forbidden plate - "{word}"')
            else:
                print("standard plate - 2010-now")
                art = input("Enter format: ")
                if art == "morse":
                    morse(plate)
                elif art == "ascii":
                    ascii(plate)
                elif art == "nato":
                    nato(plate)
                else:
                    print("Wrong format!")

        else:
            print("invalid plate")

    check(plate)


if __name__ == "__main__":
    main()
