import glob

# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

from view import create_main_window

if __name__ == "__main__":

    # Definindo a janela inicial
    window = create_main_window()

    # Loop da leitura da janela
    while True:
        # Coletar Eventos e Valores atuais
        event, values = window.read()
        
        # Cancelar o loop ao fechar a janela
        if event == sg.WIN_CLOSED:
            break
        
        elif event == "-SEARCH-":
            path = values["-FOLDER-"]
            full_path = glob.escape(path) + "/**/main.py"
            all_projects = glob.glob(full_path, recursive=True)
            
            # all_projects = [project.replace(path, "")[1:] for project in all_projects]
            
            all_projects = [project.replace(path, "")[1:].replace("\main.py", '') for project in all_projects]
            
            window['-LIST-'].update(values=all_projects) # Recomendado usar values para o listbox
            
            
        # Mostrar o evento
        print(event, "==>", values) 
        

    # Encerrar a janela
    window.close()