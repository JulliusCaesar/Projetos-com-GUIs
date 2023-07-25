# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

# Cria a janela principal
def create_main_window(title=None, theme="DarkTeal6"):    
    # Definindo o nosso tema
    sg.theme(theme)
    
    theme_list = sg.theme_list()
    theme_index = theme_list.index(theme)  
    
    # Definindo nosso layout
    layout = [
        [
            sg.Text("Selecione um Tema"),
            sg.Combo(theme_list, theme_list[theme_index], key="-THEME-")
        ],
        [
            sg.Button("Testar Tema", key="-TRY-"),
            sg.Button("Usar Tema", key="-USE-"),
        ]
    ]
    
    # Definindo o titulo da janela
    if title is None:
        title = "Selecionador de Tema"
    else:
        title = title

    # Criar a janela de temas
    window = sg.Window(title, layout, finalize=True)
    
    # Retorna a nossa janela
    return window
