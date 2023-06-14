inventario=[]
resposta="S"

while resposta=="S":
    inventario.append(input("nome do produto: "))
    inventario.append(int(input("codigo do produto: ")))
    inventario.append(float(input("valor do produto: ")))
    inventario.append(int(input("Numero do caixa: ")))
    
    resposta=input( "digite \"S\" para realizar a compra de outro produto ou \"N\" para finalizar pedido ") .upper()
   
for elemento in inventario:
       print(elemento)

        