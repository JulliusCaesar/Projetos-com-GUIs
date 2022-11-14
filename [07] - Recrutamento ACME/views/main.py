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
    window = create_main_window()
    
    current_window = "main"
    next_window = {
        "first": "second",
        "second": "third",
        "third": "finish",
        "finish": "main"
    }
    
    all_candidates = [
        ["Julio", "10/05/1988", "5", "2021", "1000"],
        ["Felipe", "01/01/2000", "7", "2019", "3000"],
        ["José", "09/02/2002", "10", "1992", "10000"]
        ]
    
    candidate = []

    # Loop da leitura da janela
    while True:
        # Coletar Eventos e Valores atuais
        event, values = window.read()
        
        # Cancelar o loop ao fechar a janela
        if event == sg.WIN_CLOSED:
            break
        
        if event == "-REGISTER-":
            window.close()
            window = create_first_window()
            current_window = "first"
            
        elif event == "-SHOW-":
            window.close()
            window = create_visualizer_window(all_candidates)
            current_window = "visualizer"
        
        elif event == "-BACK-":
            window.close()
            window = create_main_window()
            current_window = "main"
        
        elif event == "-NEXT-":
            window.close()
            
            # Primeira Janela
            if next_window[current_window] == 'second':
                candidate.append(values["-NAME-"])
                candidate.append(values["-BIRTHDAY-"])
                window = create_second_window()
            
            # Segunda Janela    
            elif next_window[current_window] == 'third':
                candidate.append(values["-LEVEL-"])
                candidate.append(values["-YEARPYTHON-"])
                window = create_third_window()
            
            # Terceira Janela    
            elif next_window[current_window] == 'finish':
                candidate.append(values["-SALARY-"])
                window = create_finish_window()
            
            # Janela Final
            else:
                all_candidates.append(candidate) 
                candidate = []
                window = create_main_window()
            
            # 
            current_window = next_window[current_window]
             
        
            
            
        # Mostrar o evento
        print(event, "==>", values) 
        
        
        

    # Encerrar a janela
    window.close()