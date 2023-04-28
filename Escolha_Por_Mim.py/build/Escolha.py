'''escolha por mim'''
import random
import PySimpleGUI as sg

class DecidaPorMim:
    '''
    class
    '''
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!!',
            'Não sei, você que sabe',
            'Não faz isso não!',
            'Acho que tá na hora certa!'
        ]
        self.janela = None
        self.eventos = None
        self.valores = None

    def iniciar(self):
        '''
        teste
        '''
        # Layout
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(20, 10))],
            [sg.Button('Escolha por mim')]
        ]
        # Criar a janela
        self.janela = sg.Window('Escolha por mim!', layout=layout)
        while True:
            # Ler os valores
            self.eventos, self.valores = self.janela.read()
            # Finalizar valores
            if self.eventos == sg.WINDOW_CLOSED:
                break
            if self.eventos == 'Escolha por mim':
                print(random.choice(self.respostas))


decida = DecidaPorMim()
decida.iniciar()
