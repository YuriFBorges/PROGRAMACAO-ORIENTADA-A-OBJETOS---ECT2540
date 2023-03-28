class Carro:
    def __init__(self, c):
        self.cor = c
        self.modelo = ''
        self.ano = 0
        print(f'Carro de cor{self.cor}')

    def acelera(self):
        print(f'Acelerando carro de cor {self.cor}')

c1 = Carro('Onix', 'amarelo', 2021)
c2 = Carro('Logan', 'vermelho', 2017)
c3 = Carro('Uno', 'branco', 1998)

c1.acelera()
c2.acelera()
c3.acelera()