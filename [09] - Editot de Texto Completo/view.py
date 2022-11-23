# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

# Criando o menubar
def menu_bar():
    menu = [
        [
            "&Arquivo",
            ["&Novo Arquivo::new", "A&brir Arquivo::open", "&Salvar Arquivo::save"],
        ],
        [
         "&Editar",
            ["&Fonte",
             [
                 "&Tamanho::size",
                 "&Família::family"
             ],
             "&Tema::theme"],
        ],
        [
             "&Sobre",
            ["&Créditos::credits", "&Versão::version"],
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
                        "Tamanho::size",
                        "Família::family"
                    ],
                "Tema::theme",
            ],
        ],
     ]
    
    return menu



# Cria a janela principal
def create_main_window(title=None, theme="DarkTeal6", size=(1100, 500), font=("Arial", 10), location=(None, None)):    
    # Definindo o nosso tema
    sg.theme(theme)

    # Definindo nosso layout
    layout = [
        [
            sg.MenuBar(menu_bar(), font=("Arial", 10))
        ],
        [
            sg.Multiline(
                right_click_menu=right_click_menu(),
                font=font,
                key='-CONTENT-',
            ),
        ],
        [
            sg.StatusBar(f"Arquivo Atual:  | O arquivo tem um total de YYYY caracteres e ZZZZ linhas | Você está usando o ByEditor de Texto 2.0.0",
                         key="-STATUSBAR-"),
        ],
    ]
    
    # Definindo o titulo da janela
    if title is None:
        title = "ByEditor de Texto 2.0.0 - Novo Arquivo"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(title, layout, size=size, location=location, resizable=True, finalize=True)
    window.find_element("-CONTENT-").expand(True, True, True)
    
    # Ctrl + N ==> Cria Novo
    window.bind("<Control-n>", "::new")
    # Ctrl + O ==> Abre Existente
    window.bind('<Control-o>', '::open')
    # Ctrl + S ==> Salva Atual
    window.bind('<Control-s>', '::save')
    
    
    # Retorna a nossa janela
    return window

