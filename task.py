mass = ["Ira", "Tanya", "12", "314", "VladiSlave", "8"]
x = str(input("Vvedit element dlya perevirki(Реєстр важливий): "))
if x in mass:
    print("Такий елемент є, під номером -", mass.index(x))
else:
    print("Такого елемента немає")
