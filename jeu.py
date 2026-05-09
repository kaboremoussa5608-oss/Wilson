import random

print("Je lis dans tes pensées...")
nombre = random.randint(1, 100)
print("J'ai choisi un nombre entre 1 et 100.")

while True:
    essai = int(input("Devine : "))
    if essai == nombre:
        print(f"BOOM ! C'était {nombre}. Je suis trop fort 🤖")
        break
    elif essai < nombre:
        print("Plus grand !")
    else:
        print("Plus petit !")
