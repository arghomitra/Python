import zipfile
import os
from pathlib import Path
import re
from datetime import datetime
from math import trunc

today = datetime.now()

with open('Characters.csv', 'r', encoding='utf-8') as a:
    line = a.readline()
    while line:
        line = a.readline()
        word =line.split(';')
        print(len(word))




# zipfile_ = zipfile.ZipFile(Path("HarryPotter.zip"))
# zipfile_.extractall()
# zipfile_.close()
# file = 1#input("Enter book: ")
# with open(f"Harry Potter {file}.csv", "r") as b:
#     bText = b.read()
# spell = "Alohomora"#input("Enter spell/potion: ")
# pattern = re.compile(fr"\b{spell}\b")
# matches = pattern.finditer(bText)
# count = 0
# for match in matches:
#     count += 1
#
# #print(f"{count} apperances of {spell} in book Harry Potter {file}.csv")


# name = "Hermione"
# name_details = []
# with open('Characters.csv', 'r') as a:
#     atext = a.readline()
#     while atext:
#         atext = a.readline()
#         word = atext.split(';')
#         fname = word[-2]
#         print(fname)
        # if fname.startswith(name):
        #     print('name', word[1])
        #     print('house', word[4])
        #
        # dob = word[-2] #30 January, 1960
        # print(dob)
        #
        #
        # birthday_date = datetime.strptime(dob, '%d %M,"\xa0"%Y')
        # age = today - birthday_date
        # print('age', trunc(age.days / 365))

        # if word[0].startswith(name) == name:
        #     print('name', word[0])
        #     print('house', word[3])
        #     print('DOB', word[4])
        #       # break out of the loop when a match is found

# name = "ron"
# with open('shortversioncharacters.csv', 'r') as a:
#     a_text = a.readline().replace(",", " ")
#     # print(a_text)
#     while a_text:
#         a_text = a.readline()
#         print(a_text)
#         for word in a_text:
#             if word == "ron":
#                 print(a_text)

# print(lines)


# pattern2 = re.compile(fr"\b{spell}(\.|\s)")
# matches = pattern2.finditer(bText)
#
# for match in matches:
#     print(match)
#
#
#
#
# line_dict = {}
#
# with open(f"Harry Potter {file}.csv", "r") as f:
#     line_num = 1
#     line = f.readline()
#     while line:
#         line_dict[line_num] = line.strip()
#         line_num += 1
#         line = f.readline()
#
# #print(line_dict)
#
#
#
# word = "Alohomora"
# word_count = 0
# word_dict = {}
#
# with open(f"Harry Potter {file}.csv", "r") as f:
#     for line_num, line in enumerate(f, start=1):
#         if word in line:
#             word_count += line.count(word)
#             for name in ["harry", "ron", "hermione"]:
#                 if name in line.lower():
#                     if name in word_dict:
#                         word_dict[name].append((line_num, line))
#                     else:
#                         word_dict[name] = [(line_num, line)]
#
# #print(f"The word '{word}' appears {word_count} times in the file.")
# for name, lines in word_dict.items():
#     #print(f"'{name}' used the word '{word}' in the following lines:")
#
#     linesss = ''
#     for line_num1, line in lines:
#         linesss += str(line_num) + ' '
#
#     print(f"{name} on line(s) {linesss}")
