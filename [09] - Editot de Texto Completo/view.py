# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

# Criando o menubar
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


def right_click_menu():
    menu = [
        [], # No click do botao do mouse esse primeiro menu não aparece, não importa o que escreva!!
        [
            "Editar",
            [
                    "Fonte",
                    [
                        "Tamanho",
                        "Família"
                    ],
                "Tema",
            ],
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
                right_click_menu=right_click_menu(),
                key='-CONTENT-',
            ),
        ],
        [
            sg.StatusBar(f"Arquivo Atual: XXXX | O arquivo tem um total de YYYY caracteres e ZZZZ linhas | Você está usando o ByEditor de Texto 2.0.0",
                         key="-STATUSBAR-"),
        ],
    ]
    
    # Definindo o titulo da janela
    if title is None:
        title = "ByEditor de Texto 2.0.0"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(title, layout, finalize=True)
    
    
    # Retorna a nossa janela
    return window

