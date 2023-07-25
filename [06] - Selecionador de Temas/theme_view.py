# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

def create_theme_window(title=None, theme="DarkTeal6"):    
    # Definindo o nosso tema
    sg.theme(theme)
    
    theme_list = sg.theme_list()
    theme_index = theme_list.index(theme)  
    
    # Definindo nosso layout
    layout = [
        [
            sg.Text("Digite algo:"),
            sg.In(),
        ],
        [
            sg.Text("Você prefere:"),
            sg.Radio("Sorvete", 0),
            sg.Radio("Açai", 0),
        ],
        [
            sg.Button("Voltar", key="-BACK-"),
        ]
    ]
    
    # Definindo o titulo da janela
    if title is None:
        title = "Selecionador de Tema"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(title, layout, finalize=True)
    
    # Retorna a nossa janela
    return window
