# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

from view import create_main_window, create_theme_window

if __name__ == "__main__":

    # Definindo a janela inicial
    window = create_main_window() # Caso queira modificar o thema inicial, o programador ja pode modificar por aqui,
                                  # usando dentro dos parenteses theme="tema escolhido"

    # Loop da leitura da janela
    while True:
        # Coletar Eventos e Valores atuais
        event, values = window.read()
        
        # Cancelar o loop ao fechar a janela
        if event == sg.WIN_CLOSED:
            break
        
        if event == "-TRY-":
            window.close()
            window = create_theme_window()
        elif event == "-BACK-":
            window.close()
            window = create_main_window()
        
        # Mostrar o evento
        print(event, "==>", values) 
        

    # Encerrar a janela
    window.close()