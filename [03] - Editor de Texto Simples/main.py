# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg
import os
import pathlib

# Cria a janela principal
def create_main_window():    
    # Definindo o nosso tema
    sg.theme("DarkTeal6")

    # Definindo nosso layout
    layout = [
        [
            sg.Text("Bem vindo ao nosso editor de texto")
        ],
        [
            sg.Text("Nome do arquivo:"),
            sg.Input(key="-NAME-"),
            sg.Radio(".py", group_id="extension", default=True, key="-PY-"),
            sg.Radio(".txt", group_id="extension", key="-TXT-"),
        ],
        [
            sg.Multiline(size=(150,30), key="-CONTENT-"), # Horizontal, vertical
        ],
        [
            sg.Button("Salvar Arquivo", key="-SAVE-", size=(133, None))
        ]
    ]

    # Definindo o Titulo da janela
    title = "Editor de Texto Simples"

    # Criar a janela
    window = sg.Window(title, layout, element_justification="center")
    
    # Retorna a nossa janela
    return window

# Definindo a janela inicial
window = create_main_window()

# Loop da leitura da janela
while True:
    # Coletar Eventos e Valores atuais
    event, values = window.read()
    
    if event == '-SAVE-':
        if values['-PY-']:
            extension = ".py"
        else:
            extension = ".txt"
        
        filename = values['-NAME-'] + extension
        content = values["-CONTENT-"]
        
        folder = "Arquivos Salvos"
        
        parent_path = pathlib.Path(__file__).parent.resolve()
        path = os.path.join(parent_path, folder)
        
        if not os.path.isdir(path):
            os.makedirs(path)
        
        full_path = os.path.join(path, filename)
        
        with open(full_path, 'w', encoding='utf-8') as file:
            file.write(content) 
    
    
    
    # Cancelar o loop ao fechar a janela
    if event == sg.WIN_CLOSED:
        break 
    
    # Mostrar o evento
    print(event, "==>", values)

# Encerrar a janela
window.close()