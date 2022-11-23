# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg

from view import create_main_window
from popups import create_font_popup, popup_combo


current_theme = "DarkTeal6"
font_family = "Arial"
font_size = 10
file_name = "Novo Arquivo"
full_file_name = file_name
chars = 0
lines = 1

def update_status_bar(content):
    ...


def refresh_window():
    global window
    
    content = values["-CONTENT-"]
    size = window.size
    location = window.current_location()
    window.close()
    
    window = create_main_window(title=f"ByEditor de Texto 2.0.0 - {file_name}", theme=current_theme, size=size,
                                location=location, font=(font_family, font_size))
    
    window["-CONTENT-"].update(content)

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
        
        elif "::new" in event:
            print("Função de criar novo arquivo")
        
        # if event.endswith("::open") pode ser usado quando houver palavras parecidas
        elif "::save" in event:
            file_path = sg.popup_get_file("Como deseja salvar o arquivo", save_as=True)
            print("Função de salvar")
            
        elif "::open" in event:
            file_path = sg.popup_get_file("Selecione um arquivo para abrir")
            print("Função de abrir")
        
        elif "::credits" in event:
            sg.popup_no_buttons("créditos: ByLearn \nAluno: Julio César")
        
        elif "::version" in event:
            sg.popup("Versão: 2.0.0")
        
        elif "::size" in event:
            font_size = create_font_popup("Tamanho da Fonte", "Insira o tamanho da fonte")
            refresh_window()
        
        elif "::family" in event:
            font_family = create_font_popup("Familia da Fonte", "Insira a Familia da fonte")
            # x = sg.popup_get_text() outra forma dr criatr uma popup
            refresh_window()
        
        elif "::theme" in event:
            current_theme = popup_combo(sg.theme_list(), current_theme, "Tema Padrão", "Selecione um Tema")
            refresh_window()
            
        print(event, "==>", values)
        

    # Encerrar a janela
    window.close()