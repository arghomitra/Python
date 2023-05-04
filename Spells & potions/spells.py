import zipfile
import os
from pathlib import Path
import re
from datetime import datetime
from math import trunc




def mentions(book, text):
    zipfile_ = zipfile.ZipFile(Path("HarryPotter.zip"))
    zipfile_.extractall()
    zipfile_.close()
    file = book
    spell_potion = text

    with open(f"Harry Potter {file}.csv", "r", encoding='utf-8', errors='ignore') as b:
        bText = b.read()
    pattern = re.compile(fr"\b{spell_potion}\b")
    matches = pattern.finditer(bText)
    count = 0
    for match in matches:
        count += 1



    line_counter = 0
    line_dict = {}

    with open(f"Harry Potter {file}.csv", "r", encoding='utf-8', errors='ignore') as file:
        line = file.readline()
        while line:
            line = line.replace(';', ' ')
            splitedLine = line.split()
            if splitedLine:
                line_counter += 1
                if spell_potion in line and splitedLine[0] in line:
                    if splitedLine[0] in line_dict:
                        line_dict[splitedLine[0]].append(line_counter)

                    else:
                        line_dict[splitedLine[0]] = [line_counter]

            line = file.readline()

    # loop through the dictionary and print the output in the desired format
    output = ''
    for key, value in line_dict.items():
        line_numbers = ', '.join(str(x) for x in value)
        output += (f"{key} on line(s) {line_numbers}")+'\n'
    if count == 0:
            return (f"No apperances of {spell_potion} in book Harry Potter {book}.csv" + '\n'
                    + output)
    else:
        return (f"{count} apperances of {spell_potion} in book Harry Potter {book}.csv" + '\n'
                + output)









#
#
def character(name):
    zipfile_ = zipfile.ZipFile(Path("HarryPotter.zip"))
    zipfile_.extractall()
    zipfile_.close()
    today = datetime.now()
    # name = "Hermione"
    name_details = []
    with open('Characters.csv', 'r', encoding='utf-8') as a:
        atext = a.readline()
        while atext:
            atext = a.readline()
            word = atext.split(';')
            if len(word) > 1:
                fullname = word[1]
                if name in fullname:
                    # return (word[1])
                    # return (word[4])

                    if word[-2].startswith('Late'):
                        output = word[1] + '\n' \
                                 + word[4] + '\n' \
                                 + f'{name} died'
                        return output

                    else:
                        dob = word[-2].replace(',', '')
                        birthday_date = datetime.strptime(dob, '%d %B %Y')
                        age = trunc((today - birthday_date).days / 365)


                        output = word[1] + '\n' \
                                 + word[4] + '\n' \
                                 + f'{name} is today {age} years old.'
                        return output



def spell(text):
    zipfile_ = zipfile.ZipFile(Path("HarryPotter.zip"))
    zipfile_.extractall()
    zipfile_.close()
    used_spell = text
    with open('Spells.csv', 'r', encoding='utf-8') as b:
        line = b.readline()
        while line:
            line = b.readline()
            words = line.split(';')

            if len(words) >= 2 and words[1] == used_spell:
                output = 'Name: ' + words[0] + '\n' \
                         + 'Incantation: ' + words[1] + '\n' \
                         + 'Type: ' + words[2] + '\n' \
                         + 'Effect: ' + words[3] + '\n' \
                         + 'Light: ' + words[4]
                return output


def potion(text):
    zipfile_ = zipfile.ZipFile(Path("HarryPotter.zip"))
    zipfile_.extractall()
    zipfile_.close()
    potion = text
    with open('Potions.csv', 'r', encoding='utf-8') as b:
        line = b.readline()
        while line:
            line = b.readline()
            words = line.split(';')

            if len(words) >= 2 and words[0] == potion:
                output = 'Name: ' + words[0] + '\n' \
                         + 'Known ingredients: ' + words[1] + '\n' \
                         + 'Effect: ' + words[2] + '\n' \
                         + 'Characteristics: ' + words[3] + '\n' \
                         + 'Difficulty level: ' + words[4]
                return output


def calculate_age(birth, death=''):
    zipfile_ = zipfile.ZipFile(Path("HarryPotter.zip"))
    zipfile_.extractall()
    zipfile_.close()
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


def main():


    zipfile_ = zipfile.ZipFile(Path("HarryPotter.zip"))
    zipfile_.extractall()
    zipfile_.close()

    file =input().strip()
    input_spell =input().strip()
    if int(file) > 3:
        print("Book not found!")
    else:
        output = mentions(file, input_spell)
        lines = len(output.split('\n')) #number of lines


        lineNumber = 0
        for line in output.split('\n'):
            lineNumber +=1
            print(line)
            if 1<lineNumber<lines:
                line_words = line.split(' ')
                input_name = line_words[0].title()
                name = character(input_name)
                print(name)






    # age = calculate_age('5 October, 2001', '4 March 2015')
    # print(age)

    spells = spell(input_spell)
    if spells:
        print('SPELL '+input_spell)
        print(spells)

    else:
        potion_output = potion(input_spell)
        print('POTION '+input_spell)
        print(potion_output)


if __name__ == "__main__":
    main()
 Missing newline at the end of file.
