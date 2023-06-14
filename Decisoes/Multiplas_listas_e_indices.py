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
    
    resposta=input( "digite \"S\" para realizar a compra de outro produto ou \"N\" para finalizar pedido ") .upper()
   
for indice in range(0,len(inventario)):
    
    print("\nInventario... ",(indice+1))
    print("Nome........... ",inventario(indice))
    print("valor.......... ",valor(indice))
    print("codigo......... ",codigo(indice))
    print("caixa........... ", caixa(indice))

        