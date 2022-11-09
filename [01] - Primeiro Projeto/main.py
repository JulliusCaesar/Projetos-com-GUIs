import PySimpleGUI as sg

layout = [
    [sg.Text('Filename')],
    [sg.Input(), sg.FileBrowse()],
    [sg.Button("Ok"), sg.Button("Cancel")],
]

window = sg.Window("Meu Primeiro Projeto", layout)
   
event, values = window.read()

window.close()