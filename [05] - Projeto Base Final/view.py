# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

# Cria a janela principal
def create_main_window(title=None, theme="DarkTeal6"):    
    # Definindo o nosso tema
    sg.theme(theme)

    # Definindo nosso layout
    layout = [
        [
            sg.Text("Olá Mundo!")
        ]
    ]
    
    # Definindo o titulo da janela
    if title is None:
        title = "Meu Tiítulo"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(title, layout, finalize=True)
    
    # Retorna a nossa janela
    return window

