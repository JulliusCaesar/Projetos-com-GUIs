# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

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
            sg.Radio(".py", group_id="extension", key="-PY-", default=True),
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
    title = "Meu Ptograma Base"

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
    
    # Mostrar o evento
    print(event, "==>", values)
    
    # Cancelar o loop ao fechar a janela
    if event == sg.WIN_CLOSED:
        break 
    

# Encerrar a janela
window.close()