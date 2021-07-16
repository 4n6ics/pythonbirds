# variaveis com letras maiusculas nao mudam de valor
NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:

    rotacao_a_direita_dict = {NORTE:LESTE,LESTE:SUL,SUL:OESTE,OESTE:NORTE}
    rotacao_a_esquerda_dict = {NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE}

    def __init__(self):
        ''' CODIGO ABAIXO FEITO POR MIM
        self.valor = ['Norte', 'Leste', 'Sul', 'Oeste']
        self.pos = 0
        '''
        self.valor = NORTE

    def girar_a_direita(self):
        ''' CODIGO ABAIXO FEITO POR MIM
        if self.pos == 0:
            self.pos += 1
        elif self.pos < 3:
            self.pos += 1
        else:
            self.pos = 0
        '''
        self.valor = self.rotacao_a_direita_dict [self.valor]

    def girar_a_esquerda(self):
        ''' CODIGO ABAIXO FEITO POR MIM
        if self.pos == 0:
            self.pos -= 1
        elif self.pos < 3:
            self.pos -= 1
        else:
            self.pos = 0
        '''
        self.valor = self.rotacao_a_esquerda_dict[self.valor]

if __name__ == '__main__':

    ''' CODIGO ABAIXO FEITO POR MIM
    direcao = Direcao()
    print(direcao.valor[direcao.pos])

    direcao.girar_a_direita()
    print(direcao.valor[direcao.pos])

    direcao.girar_a_direita()
    print(direcao.valor[direcao.pos])

    direcao.girar_a_direita()
    print(direcao.valor[direcao.pos])

    direcao.girar_a_direita()
    print(direcao.valor[direcao.pos])

    direcao.girar_a_esquerda()
    print(direcao.valor[direcao.pos])

    direcao.girar_a_esquerda()
    print(direcao.valor[direcao.pos])

    direcao.girar_a_esquerda()
    print(direcao.valor[direcao.pos])

    direcao.girar_a_esquerda()
    print(direcao.valor[direcao.pos])
    '''


















