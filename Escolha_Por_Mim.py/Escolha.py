# faça uma pergunta para o programa e ele terá que te dar uma resposta.
import random
import PySimpleGUI as sg
class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certezqa, você deve fazer isso!!',
            'Não sei, você que sabe',
            'Não faz isso não!',
            'Acho que tá na hora certa!'
        ]
    
    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(20,10))],
            [sg.Button('Escolha por mim')]
             ]
        # Criar a janela
        self.janela = sg.Window('Escolha por mim!',layout=layout)
        # Ler os valores
        self.eventos, self.valores = self.janela.read()
        # final valores
        if self.eventos == 'Escolha por mim':       
            print(random.choice(self.respostas))
decida = DecidaPorMim()
decida.Iniciar()
