usuarios ={}
emails = ["oioioi@gmail.com", "hihihi@gmail.com"]

tupla = list(enumerate(emails))

for chave in range(0,len(tupla)):
    print("email: ", tupla[chave] [1])
    usuarios[tupla[chave]] = [input("Digite o nome "), input("Digite o nivel ")]
    
for chave, dado in usuarios.items():
    print("usuario.", chave[0])
    print("email...", chave[1])  
    print("nome....", chave[0])  
    print("nivel...", chave[1])      