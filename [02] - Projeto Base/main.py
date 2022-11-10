# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

# Cria a janela principal
def create_main_window():    
    # Definindo o nosso tema
    sg.theme("DarkTeal6")

    # Definindo nosso layout
    layout = [
        [
            sg.Text("Esse projeto foi feito usando o template base"),
        ],
        [
            sg.Text("Digite algo"),
            sg.Input(key="-INPUT-"),
        ],
        [
            sg.Button("OK"),
        ]
    ]

    # Definindo o Titulo da janela
    title = "Ultilizando um template"

    # Criar a janela
    window = sg.Window(title, layout)
    
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
    elif event == "OK":
        sg.popup(f"Você digitou: {values['-INPUT-']}")
        window['-INPUT-'].update("")

# Encerrar a janela
window.close()