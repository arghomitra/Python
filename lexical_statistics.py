
with open('sonnets.txt', 'r') as file:
    text = file.read()

words = text.lower().split()
punctuation = ',:‘.!?'

withOutPunctuation_words = []
for word in words:
    withOutPunctuation_word = ''
    for char in word:
        if char not in punctuation and not char.isspace():
            withOutPunctuation_word += char
    withOutPunctuation_words.append(withOutPunctuation_word)

unique = []
numlist =[]
for word in withOutPunctuation_words:
    count = 0
    for word2 in withOutPunctuation_words:
        if word == word2:
            count += 1
    if (word+" "+str(count)) not in unique:
        unique.append(word+" "+str(count))
        numlist.append(count)

numlist.sort()
numlist.reverse()
output=[]
for i in numlist: #490
    for j in unique: #the 490
        num = ''#490
        for k in j: #the 490
            if k.isnumeric(): #490
                num+=k
        if int(num) == i:
            if j not in output:
                output.append(j)
            break
print("The 50 most common words by Shakespeare:\n")
for i in range(50):
    print(output[i])


