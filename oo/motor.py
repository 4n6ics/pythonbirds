class Motor:

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade) #se negativo, retorna 0. Se positivo, retorna self.velocidade

if __name__ == '__main__':

    motor = Motor()
    print(motor.velocidade)

    motor.acelerar()
    print(motor.velocidade)

    motor.acelerar()
    print(motor.velocidade)

    motor.acelerar()
    print(motor.velocidade)

    motor.frear()
    print(motor.velocidade)

    motor.frear()
    print(motor.velocidade)






