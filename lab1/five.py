import math

def standard(array):
    sumxx = 0
    sum = 0
    for i in range(len(array)):
        sumxx += (array[i]*array[i])
        sum += array[i]
    return (math.sqrt(sumxx / 26 - ((sum / 26) * (sum / 26))))
    
lowerbound = input()
upperbound = input()
ciphertext = ""

while True:
    try:
        line = input()
    except EOFError:
        break
    ciphertext += line

alphabet = []
for i in range(0,26):
    alphabet.append(0)

newtext = ""
for i in range(len(ciphertext)):
    if ciphertext[i].isalpha():
        newtext += ciphertext[i]

maxsum = 0

for i in range(int(lowerbound), (int(upperbound)+1)):
    array = []
    array.clear()
    for j in range(i):
        array.append(alphabet.copy())

    sumStandard = 0
    for j in range(i):
        factor = j
        index = factor
        while index < len(newtext):
            letter = newtext[index]
            if letter.isupper():
                val = ord(letter) - ord('A')
            else:
                val = ord(letter) - ord('a')
            array[j][val] += 1
            factor += i
            index = factor
        sumStandard += standard(array[j])
        #print(standard(array[j]))
    
    if sumStandard > maxsum:
        maxsum = sumStandard
        save = array 
        bound = i
        
    formattedSum = "{:.2f}".format(sumStandard)
    print("The sum of " + str(i) +  " std. devs: " + str(formattedSum))
    sumStandard = 0
    formattedSum = 0

key = ""
for alphabet in save:
    max = 0
    for i in range(len(alphabet)):
        if alphabet[i] > max:
            max = alphabet[i]
            index = i
    index = index - 4
    if index < 0:
        index = index + 26
    key += chr((index)+ord('a'))

print("\nKey guess:\n" + str(key))
