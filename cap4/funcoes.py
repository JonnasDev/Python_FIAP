def perguntar():
    return input ("O que deseja realizar?\n" + 
               "<I> - Para inserir um usuario\n" + 
               "<P> - Para pesquisar um usuario\n" + 
               "<E> - para excluir um usuario\n" + 
               "<L> - Para listar um usuario").upper()
    
def inserir(dicionario):
    dicionario[input("digite o login: ").upper()] =[input("Digite o nome: "),
                                                    input("Digite a ultima data de acesso: "),
                                                    input("Digite a ultima estação acessada: ").upper()]
    salvar(dicionario)


def salvar (dicionario):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))