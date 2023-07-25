# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

# Cria a janela principal
def create_main_window():    
    # Definindo o nosso tema
    sg.theme("DarkTeal6")
    
    layout_tab1 = [
        [
            sg.Text("Isso é um texto"),
            sg.Input("Isso é um input"),
        ],
        [
            sg.Text("Essa é outra linha"),
            sg.Button("Isso é um botão"),
        ],
    ]
    
    layout_tab2 = [
        [
            sg.Text("Eu posso abrir um arquivo"),
            sg.FileBrowse("Abrir"),
        ],
        [
            sg.Text("Uma pasta também"),
            sg.FolderBrowse("Abrir")
        ],
        [
            sg.Text("E por fim, salvar um arquivo"),
            sg.SaveAs("Salvar")
        ]
    ]
    
    layout_tab3 = [
        [
            sg.Text("Eu tenho vários selecionáveis")
        ],
        [
            sg.Radio("Um", 1),
            sg.Radio("Ou outro", 1)
        ],
        [
            sg.Check("Um"),
            sg.Check("E também outro"),
            sg.Check("Ou talves só alguns")
        ]
    ]

    layout_tab4 = [
        [
            sg.Text("Conversor de medidas"),
        ],
        [
            sg.Text("Selecione seu tamanho (cm)"),
            sg.Spin(list(range(100,200)), key=("-CM-"))
        ],
        [
            sg.Button("Converter", key=("-CONVERT-"))
        ],
        [
            sg.Text("Resposta: ", key="-RESULT-")
        ]
    ]
    
    layout_all_tabs = [
        [
            sg.Tab("Conhecimento 1", layout_tab1),
            sg.Tab("Conhecimento 2", layout_tab2),
            sg.Tab("Conhecimento 3", layout_tab3),
            sg.Tab("Conhecimento 4", layout_tab4),
        ]
    ]

    # Definindo nosso layout
    layout = [
        [
            sg.Text("Abas do Aprendizado", font=("Segoi UI", 20)),
        ],
        [
            sg.Text("Coletâneas de alguns dos conteúdos que eu aprendi no curso da ByLearn")
        ],
        [
            sg.TabGroup(layout_all_tabs)
        ]
    ]

    # Definindo o Titulo da janela
    title = "Abas do Aprendizado"

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
    elif event == "-CONVERT-":
        cm = int(values["-CM-"])
        meters = cm / 100
        window['-RESULT-'].update(meters)
        

# Encerrar a janela
window.close()