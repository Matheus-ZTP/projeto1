import random
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        self.valores_dados = {
            'D4': 4,
            'D6': 6,
            'D8': 8,
            'D10': 10,
            'D12': 12,
            'D20': 20
        }
        self.dados_jogados = []
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'
        self.layout = [
            [sg.Text('Escolha o tipo de dado:')],
            [sg.Button(dado, key=dado) for dado in self.valores_dados.keys()],
            [sg.Text('Últimos dados jogados:')],
            [sg.Listbox(values=self.dados_jogados, size=(30, 3), key='listbox')]
        ]

    def Iniciar(self):
        self.janela = sg.Window('Simulador de Dado', layout=self.layout)

        while True:
            eventos, valores = self.janela.read()

            if eventos in (None, 'Exit'):
                break

            if eventos in self.valores_dados.keys():
                self.GerarValorDoDado(eventos)
                self.dados_jogados.insert(0, f'{eventos}: {self.ultimo_resultado}')
                self.dados_jogados = self.dados_jogados[:3]
                self.janela['listbox'].update(values=self.dados_jogados)

        self.janela.close()

    def GerarValorDoDado(self, tipo_dado):
        self.ultimo_resultado = random.randint(1, self.valores_dados[tipo_dado])
        print(self.ultimo_resultado)


simulador = SimuladorDeDado()
simulador.Iniciar()
