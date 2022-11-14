# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

from menu.menu import create_main_window
from registration.first import create_first_window
from registration.second import create_second_window

if __name__ == "__main__":

    # Definindo a janela inicial
    window = create_second_window()

    # Loop da leitura da janela
    while True:
        # Coletar Eventos e Valores atuais
        event, values = window.read()
        
        # Cancelar o loop ao fechar a janela
        if event == sg.WIN_CLOSED:
            break
        
        # Mostrar o evento
        print(event, "==>", values) 
        

    # Encerrar a janela
    window.close()