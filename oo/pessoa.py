class Pessoa:

    def __init__(self,*filhos, nome, idade=42):    #eh um metodo de inicializacao de contrucao de objeto
        self.nome = nome                           #o atributo nome existe mas nao tem valor atribuido a ele
        self.idade = idade
        self.filhos = list(filhos)


    def cumprimentar (self):        #metodo cumprimentar
        return 'Ola'

if __name__ == '__main__':          #main eh usado para testar o cod dentro da classe
    andre = Pessoa(nome='Andre')                    # Andre eh filho do Luciano
    luciano = Pessoa(andre, nome='Luciano')         #criacao o objeto p
    print (Pessoa.cumprimentar(andre))
    for filho in luciano.filhos:
        print (filho.nome)


