import zipfile
import os
from pathlib import Path
import re
from datetime import datetime
from math import trunc


zipfile_ = zipfile.ZipFile(Path("HarryPotter.zip"))
zipfile_.extractall()
zipfile_.close()


def calculate_age(birth, death=''):
    today = datetime.now()
    birth = birth.replace(',', '')
    death = death.replace(',', '')

    birthday_date = datetime.strptime(birth, '%d %B %Y')
    if death:
        death_date = datetime.strptime(death, '%d %B %Y')
        age = trunc((death_date - birthday_date).days / 365)

    else:
        age = trunc((today - birthday_date).days / 365)

    return age


# def character(name):
#     today = datetime.now()
#     with open('Characters.csv', 'r', encoding='utf-8') as a:
#         atext = a.readline()
#         while atext:
#             atext = a.readline()
#             word = atext.split(';')
#
#             if len(word) > 1 and name in word[1]:
#
#
#
#                 if word[-2].startswith('Late'):
#                     output = word[1] + '\n' \
#                              + word[4] + '\n' \
#                              + f'{name} died'
#                     print(output)
#                 elif word[14]:#len(word[-2].split())>7 and len(word[-1].split())
#                     bit = word[-2]
#                     det = word[-1]
#                     age = calculate_age(bit, det)
#                     output = word[1] + '\n' \
#                              + word[4] + '\n' \
#                              + f'{name} died at age {age}'
#                     print(output)
#
#                 else:
#                     dob = word[-2].replace(',', '')
#                     try:
#                         birthday_date = datetime.strptime(dob, '%d %B %Y')
#                     except ValueError:
#                         print(f"Error parsing date: {dob}")
#                         return None
#
#                     age = trunc((today - birthday_date).days / 365)
#
#                     output = word[1] + '\n' \
#                              + word[4] + '\n' \
#                              + f'{name} is today {age} years old.'
#                     print(output)
#
# character('Snape')

# file = input()
# spell = input()
# with open (f'Harry Potter {file}.csv','r') as b1:
#     b1Text = b1.read()
# words = b1Text.split()
# punctuation = ",:‘';.!?"
#
# withOutPunctuation_words = []
# for word in words:
#     withOutPunctuation_word = ''
#     for char in word:
#         if char not in punctuation and not char.isspace():
#             withOutPunctuation_word += char
#         elif char in punctuation:
#             withOutPunctuation_word += " "
#     withOutPunctuation_words.append(withOutPunctuation_word)
#
#
# count = 0
#
# spell = input()
#
# pattern = re.compile(fr"\b{spell}\b")
#
# matches = pattern.finditer(b1Text)
#
# for match in matches:
#     count +=1
#
# print(f"{count} apperances of {spell} in book Harry Potter 3.csv")
#
# def mentions(book, text):
#     with open(f"Harry Potter {book}.csv", "r", encoding="utf-8") as file:
#         result = {}
#         lines = file.readlines()
#         for i, line in enumerate(lines):
#             if text in line:
#                 for j in range(max(i-1, 0), min(i+2, len(lines))):
#                     for word in lines[j].strip().split():
#                         if word.istitle():
#                             result.setdefault(word, []).append(j+1)
#         output =  " ".join(f"{character} on line(s) {', '.join(map(str, lines))}." for character, lines in result.items())
#         return output
#
#
#
# v=mentions('1', 'Alohomora')
# def potion(text):
#     potion = text
#     with open('Potions.csv', 'r', encoding='utf-8') as b:
#         line = b.readline()
#         while line:
#             line = b.readline()
#             words = line.split(';')
#
#
#             if len(words) >= 2 and words[0] == potion:
#                 output = 'Name: ' + words[0] + '\n' \
#                          + 'Known ingredients: ' + words[1] + '\n' \
#                          + 'Effect: ' + words[2] + '\n' \
#                          + 'Characteristics: ' + words[3] + '\n' \
#                          + 'Difficulty level: ' + words[4]
#                 print(words[0])
#
# potion('Cure for Boils')

def mentions(book, text):
    spell_potion = text
    with open(f"Harry Potter {book}.csv", "r", encoding='utf-8', errors='ignore') as file:
        lines = file.read().splitlines()

    count = text.count(spell_potion)
    line_numbers = []
    for i, line in enumerate(lines):
        if spell_potion in line:
            line_numbers.append(i + 1)

    if count == 0:
        print( f"No appearances of {spell_potion} in book Harry Potter {book}.csv")
    else:
        print(f"{count} appearances of {spell_potion} in book Harry Potter {book}.csv\n{spell_potion} mentioned on line(s) {', '.join(map(str, line_numbers))}"
    )

mentions('1','Alohomora')