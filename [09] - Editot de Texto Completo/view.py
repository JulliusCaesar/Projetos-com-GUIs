# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

def menu_bar():
    menu = [
        [
            "Arquivo",
            ["Novo Arquivo", "Abrir Arquivo", "Salvar Arquivo"],
        ],
        [
         "Editar",
            ["Fonte",
             [
                 "Tamanho",
                 "Família"
             ],
             "Tema"],
        ],
        [
             "Sobre",
            ["Créditos", "Versão"],
        ],
            
    ]
    
    return menu

# Cria a janela principal
def create_main_window(title=None, theme="DarkTeal6"):    
    # Definindo o nosso tema
    sg.theme(theme)

    # Definindo nosso layout
    layout = [
        [
            sg.MenuBar(menu_bar())
        ],
        [
            sg.Multiline(
                size=(190, 10),
                enable_events=True,
                key='-CONTENT-',
            ),
        ],
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

