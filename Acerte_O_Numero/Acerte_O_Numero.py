# Objetivo: Criar um algorítimo que gera um valor aleatório e que o usuario tenha que ficar tentando acertar o número
import random
import PySimpleGUI as sg


class TenteUmNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        # layout
        layout = [
            [sg.Text('Sua tentativa', size=(39, 0))],
            [sg.Input(size=(18, 8), key='ValorTentativa')],
            [sg.Button('Jogar')],
            [sg.Output(size=(39, 10))]
        ]
        # Criar uma janela
        self.janela = sg.Window('Tente o numero!', layout=layout)
        # Final valor
        self.GerarNumeroAleatorio()
        try:
            while True:
                # Receber valores
                self.evento, self.valores = self.janela.Read()
                if self.evento == 'Jogar':
                    self.valor_da_tentativa = self.valores['ValorTentativa']
                    while self.tentar_novamente == True:
                        if int(self.valor_da_tentativa) > self.valor_aleatorio:
                            print('Tente um valor mais baixo!')
                            break
                        elif int(self.valor_da_tentativa) < self.valor_aleatorio:
                            print('Tente um valor mais alto!')
                            break
                        if int(self.valor_da_tentativa) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('Boa você acertou👍👍')
                            break

        except:
            print('Favor digitar apenas números!')
            self.Iniciar()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(
            self.valor_minimo, self.valor_maximo)


tente = TenteUmNumero()
tente.Iniciar()
