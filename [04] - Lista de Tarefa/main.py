# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

# Cria a janela principal
def create_main_window():    
    # Definindo o nosso tema
    sg.theme("DarkTeal6")
    
    tasks = ['Limpar a casa', 'Fazer exercícios de Python', 'Formatar o PC']
    
    task_list = []
    
    for index, task in enumerate(tasks):
        task_list.append(
            [
                sg.Checkbox(task,  key= f'-TASK{index}-', enable_events=True),
            ]
        ) # Adicionar listas dentro de listas

    # Definindo nosso layout
    layout = [
        [
            sg.Text("Minhas Tarefas"),
        ],
        *task_list, # Clocar o * na frente da lista é um recurso chamado Unpacking
        [
            sg.In(key="-NEWTASK-"),
            sg.Button("Adicionar", key="-ADD-"),
        ]
    ]

    # Definindo o Titulo da janela
    title = "Lista de Tarefas"

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
    

# Encerrar a janela
window.close()