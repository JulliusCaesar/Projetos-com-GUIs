# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

from select_view import create_main_window
from theme_view import create_theme_window

if __name__ == "__main__":

    current_theme = "DarkTeal6"
    selected_theme = current_theme
    
    # Definindo a janela inicial
    window = create_main_window(theme= current_theme) # Caso queira modificar o thema inicial, o programador ja pode modificar por aqui,
                                  # usando dentro dos parenteses theme="tema escolhido"

    # Loop da leitura da janela
    while True:
        # Coletar Eventos e Valores atuais
        event, values = window.read()
        
        # Cancelar o loop ao fechar a janela
        if event == sg.WIN_CLOSED:
            break
        
        if event == "-TRY-":
            selected_theme = values["-THEME-"]
            window.close()
            window = create_theme_window(theme=selected_theme)
        elif event == "-BACK-":
            window.close()
            window = create_main_window(theme= current_theme)
            window['-THEME-'].update(selected_theme)
        elif event == "-USE-":
            current_theme = values['-THEME-']
            window.close()
            window = create_main_window(theme=current_theme)
        
        # Mostrar o evento
        print(event, "==>", values) 
        

    # Encerrar a janela
    window.close()