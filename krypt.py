#kryptering: Kryptering används för att dölja information från alla som informationen inte är avsedd för. (Oftast med algoritmer.)
#hash: Istället för att lagra lösenord i klartext så kan man spara en hash av lösenordet (oläslig) och sedan jämföra med den när du loggar in. 
#algoritm: Instruktioner för hur problem/beräkningar ska lösas inom ett visst antal steg, på samma sätt varje gång.
#säkerhet: Det är viktigt.

import os, time

word = " "
key = 12
letters = []
crypt = []
meny = 0

while meny !=3:
    try:
        meny = int(input("Kryptera (1) Avkryptera (2)"))
    except:
        print("Du måste ange antingen (1) eller (2)")
    if meny == 1:
        os.system('cls')
        f = open('log.txt', 'a+')
        word = (input("Mata in för kryptering: "))
        f.write(word)
        f.close()
        for letter in word:
            letters.append(ord(letter) + key)
        print(letters)
        time.sleep(2)
        os.system('cls')
        time.sleep(2)
        for letter in letters:
            print(chr(letter)) 
        break

    elif meny == 2:
        os.system('cls')
        f = open('log.txt', 'a+')
        word = (input("Mata in för avkryptering: "))
        f.write(word)
        f.close()
        for l in word:
            crypt.append(ord(l) - key)
        print(crypt)
        time.sleep(2)
        os.system('cls')
        time.sleep(2)
        for l in crypt:
            print(chr(l))
        break
