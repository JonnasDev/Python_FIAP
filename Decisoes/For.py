tabuada=int(input("Digite um numero "))
print("Tabuada do numero: ", tabuada)

for valor in range(1,11,1):
    print(str(tabuada) + " X " + str(valor) + " = " + str((tabuada*valor)))