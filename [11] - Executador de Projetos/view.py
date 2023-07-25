# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg
import os
import pathlib

def frame_search():
    frame = [
        [
            sg.Text("Selecione a pasta com os projetos:"),
        ],
        [
            sg.Input(key="-FOLDER-", size=(69, None)),
            sg.FolderBrowse('Selecione a Pasta'),
        ],
        [
            sg.Button('Buscar Arquivos', key="-SEARCH-"),
        ],
    ]
    
    return frame



def frame_projects():
    frame = [
        [
            sg.Text("Selecione um projeto:"),
        ],
        [
            sg.Listbox([], size=(85, 11), key="-LIST-")
        ],
        [
            sg.Button('Rodar Código', key="-RUN-"),
        ],
    ]
    
    return frame


def frame_code():
    frame = [
        [
            sg.Multiline("", size=(85, 20), key='-CODE-')
        ]
    ]
    
    return frame



# Cria a janela principal
def create_main_window(title=None, theme="DarkTeal6"):    
    # Definindo o nosso tema
    sg.theme(theme)
    
    column_left = [
        [
            sg.Frame('Buscar projetos', frame_search()),
        ],
        [
            sg.Frame("Selecionar Projeto", frame_projects()),
        ],
    ]
    
    column_right = [
        [
            sg.Frame('Código', frame_code()),
        ],
    ]

    # Definindo nosso layout
    layout = [
        [
            sg.Column(column_left), sg.Column(column_right)
        ]
    ]
    
    # Definindo o titulo da janela
    if title is None:
        title = "Executador de Projetos"
    else:
        title = title
    
    parent_path = str(pathlib.Path(__file__).parent.resolve())
    icon_path = os.path.join(parent_path, "rocket.ico")

    # Criar a janela e deixa ela finalizável
    window = sg.Window(title, layout, icon=icon_path, finalize=True)
    
    # Retorna a nossa janela
    return window

