# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

from menu.menu import create_main_window
from registration.first import create_first_window
from registration.second import create_second_window
from registration.third import create_third_window
from registration.finish import create_finish_window
from visualizer.visualizer import create_visualizer_window

if __name__ == "__main__":

    # Definindo a janela inicial
    window = create_visualizer_window([["Julio", "10/05/1988", "5", "2021", "1000"]])

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