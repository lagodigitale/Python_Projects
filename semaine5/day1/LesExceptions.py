age=input("Entrer ton age")
try:
    age = int(age)
except:
    print("Erreur de type")
    print(age)