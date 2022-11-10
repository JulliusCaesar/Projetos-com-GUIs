import PySimpleGUI as sg

# sg.theme_previewer() # DarjTeal6
# print(sg.theme_list())
sg.theme("DarkTeal6")

layout = [
    [
        sg.Text('Escolha seu arquivo')
    ],
    [
        sg.Input(key='-FILE-'), 
        sg.FileBrowse("Selecionar", key='-BROWSE-')
    ],
    [
        sg.Button("Ok", button_color=("black on grey"), key='-BTNOK-'), 
        sg.Button("Cancel", button_color=("black on grey"))
    ],
]

# button_color = ("cor do texto", "Cor de fundo")
# button_color = ("blue", "white")
# button_color = ("blue on white")
# button_color = ("#00FF6C", "#FFFF00")

window = sg.Window("Meu Primeiro Projeto", layout)

def update_input():
    window["-FILE-"].update("")

while True:  
    event, values = window.read()
   
    if event == sg.WIN_CLOSED:
        print('A tela foi fechada')
        break
    elif event == "-BTNOK-":
        # print("Valor do input:", values["-FILE-"]) # 0 => Chave
        sg.popup(f'O arquivo escolhido foi: {values["-FILE-"]}', title= "Arquivo Escolhido")
        update_input()
    print("Evento: ", event)
    
    

window.close()