class Pessoa:

    def __init__(self,idade=42): #eh um metodo de inicializacao de contrucao de objeto
        self.nome = None #o atributo nome existe mas nao tem valor atribuido a ele
        self.idade = idade


    def cumprimentar (self): #metodo cumprimentar
        return 'Ola'

if __name__ == '__main__': #main eh usado para testar o cod dentro da classe
    p = Pessoa() #criacao o objeto p
    print (p.cumprimentar())
    p.nome ='Flamengo' #atribui o nome Flamengo ao objeto
    print (f'Nome: {p.nome}')
    print (f'Idade: {p.idade}')

