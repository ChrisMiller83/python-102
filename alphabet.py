alphabet = "abcdefghijklmnopqrstuvwxyz"

print("The first letter is ", alphabet[0])

print("The first three lettters are ", alphabet[:3])

print("Some letters in the middle are ", alphabet[11:16])

print("There are %d letters in the alphabet " % len(alphabet))

alphalist = list(alphabet)

alphabet = "][".join(alphalist)


for letter in alphabet:
    print(letter.upper(), end = ' ')
    
    
