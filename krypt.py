#kryptering: Kryptering används för att dölja information från alla som informationen inte är avsedd för. (Oftast med algoritmer.)
#hash: Istället för att lagra lösenord i klartext så kan man spara en hash av lösenordet (oläslig) och sedan jämföra med den när du loggar in. 
#algoritm: 
#säkerhet:

word = " "
key = 12
letters = []
crypt = []
meny = 0

while meny !=3:
    try:
        meny = int(input("Inmatning (1) Utmatning (2)"))
    except:
        print("Du måste ange antingen (1) eller (2)")
    if meny == 1:
        word = (input("Mata in för kryptering: "))
        for letter in word:
            letters.append(ord(letter) + key)
        print(letters)
        break

for l in letters:
    crypt.append(chr(l -key))

print(crypt)
