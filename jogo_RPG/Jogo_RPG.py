# Importar o módulo Pysimplegui
import PySimpleGUI as sg

# Definir o tema do jogo
sg.theme('DarkBlue')

# Criar uma função para mostrar uma janela com uma mensagem e duas opções


def show_window(message, option1, option2):
    # Criar o layout da janela
    layout = [[sg.Text(message)],
              [sg.Button(option1), sg.Button(option2)]]
    # Criar a janela
    window = sg.Window('A Ilha Perdida', layout)
    # Ler os eventos e valores da janela
    event, values = window.read()
    # Fechar a janela
    window.close()
    # Retornar o evento
    return event


# Criar uma variável para armazenar o final do jogo
ending = ''

# Mostrar a introdução do jogo
intro = 'Você é um explorador que está em busca de um tesouro escondido em uma ilha misteriosa. Você chega à ilha com seu barco e encontra uma trilha que leva ao interior. O que você faz?'
choice1 = show_window(intro, 'Seguir a trilha', 'Ficar no barco')

# Verificar a primeira escolha do jogador
if choice1 == 'Seguir a trilha':
    # Mostrar a segunda janela do jogo
    message = 'Você segue a trilha e encontra uma caverna. Você entra na caverna e vê uma luz no fundo. Você se aproxima da luz e descobre que é uma tocha que ilumina uma porta de pedra com um enigma. O enigma diz: "Para abrir a porta, responda: Qual é o animal que tem quatro patas de manhã, duas ao meio-dia e três à noite?"'
    choice2 = show_window(message, 'Um homem', 'Um leão')

    # Verificar a segunda escolha do jogador
    if choice2 == 'Um homem':
        # Mostrar a terceira janela do jogo
        message = 'Você responde "Um homem" e a porta se abre. Você entra na sala e vê um baú cheio de ouro e joias. Você encontrou o tesouro! Parabéns!'
        ending = 'Você ganhou!'
        show_window(message, 'Fim', 'Sair')
    elif choice2 == 'Um leão':
        # Mostrar a terceira janela do jogo
        message = 'Você responde "Um leão" e a porta não se abre. De repente, você ouve um rugido atrás de você. Você se vira e vê um leão furioso que estava escondido na caverna. Ele pula em cima de você e te devora. Você morreu!'
        ending = 'Você perdeu!'
        show_window(message, 'Fim', 'Sair')
elif choice1 == 'Ficar no barco':
    # Mostrar a segunda janela do jogo
    message = 'Você decide ficar no barco e esperar por um sinal de civilização. Você pega um binóculo e olha ao redor. Você vê um navio pirata se aproximando da ilha. Eles te veem e começam a atirar contra o seu barco. Você tenta fugir, mas é tarde demais. O seu barco explode e você afunda no mar. Você morreu!'
    ending = 'Você perdeu!'
    show_window(message, 'Fim', 'Sair')

# Mostrar uma mensagem final de acordo com o final do jogo
if ending == 'Você ganhou!':
    sg.popup('Parabéns! Você completou o jogo com sucesso!')
elif ending == 'Você perdeu!':
    sg.popup('Que pena! Você não conseguiu completar o jogo!')
