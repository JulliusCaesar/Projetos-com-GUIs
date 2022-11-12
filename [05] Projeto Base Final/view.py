# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

# Cria a janela principal
def create_main_window():    
    # Definindo o nosso tema
    sg.theme("DarkTeal6")

    # Definindo nosso layout
    layout = [
        [
            sg.Text("Olá Mundo!")
        ]
    ]

    # Definindo o Titulo da janela
    title = "Meu Ptograma Base"

    # Criar a janela e deixa ela finalizável
    window = sg.Window(title, layout, finalize=True)
    
    # Retorna a nossa janela
    return window
