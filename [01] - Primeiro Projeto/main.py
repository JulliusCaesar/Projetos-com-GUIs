import PySimpleGUI as sg

layout = [
    [sg.Text('Escolha seu arquivo')],
    [sg.Input(key='-FILE-'), sg.FileBrowse("Selecionar", key='-BROWSE-')],
    [sg.Button("Ok"), sg.Button("Cancel")],
]

window = sg.Window("Meu Primeiro Projeto", layout)

while True:  
    event, values = window.read()
   
    if event == sg.WIN_CLOSED:
        print('A tela foi fechada')
        break
    
    print("Evento: ", event)
    print("-" * 25)
    print("Valor do input:", values["-FILE-"]) # 0 => Chave

window.close()