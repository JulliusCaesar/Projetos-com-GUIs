# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

# Cria a janela principal
def create_visualizer_window(candidates, title=None, theme="DarkTeal6"):    
    # Definindo o nosso tema
    sg.theme("DarkTeal6")
    
    
    
    # Definindo nosso layout
    layout = [
        [
            sg.Text("Lista de todos os Candidatos:"),
        ],
        [
            sg.Table(candidates, headings=['Nome Completo', 'Data de Nascimento', "Nível de Python",
                                           "Ano Inicial de Python", "Salário Desejado"], size=(40,10))
        ],
        [
            sg.Button("Voltar", key="-BACK-")
        ],
    ]
    
    # Definindo o titulo da janela
    if title is None:
        title = "Visualizaor de Candidatos"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(title, layout, element_justification="center", finalize=True)
    
    # Retorna a nossa janela
    return window