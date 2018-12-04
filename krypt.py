#kryptering:
#hash:
#algoritm:
#säkerhet:

word = "test"
key = 12
letters = []
crypt = []



for letter in word:
    letters.append(ord(letter) + key)

print(letters)

for l in letters:
    crypt.append(chr(l -key))

print(crypt)
