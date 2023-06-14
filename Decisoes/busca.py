inventario=[]
valor=[]
codigo=[]
caixa=[]
resposta="S"

while resposta=="S":
    inventario.append(input("nome do produto: "))
    codigo.append(int(input("codigo do produto: ")))
    valor.append(float(input("valor do produto: ")))
    caixa.append(int(input("Numero do caixa: ")))
    resposta = input("Digite \"s\" para continuar ")
    
busca = input( "\nDigite o nome do item que deseja procurar: ") .upper()
for indice in range(0,len(inventario)):
    if busca==inventario(indice):
        print("Valor... ",valor(indice))
        print("Codigo... ",codigo(indice))   
   