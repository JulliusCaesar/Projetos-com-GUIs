import io
import os
import pathlib
# Importando o Pacote do PySimpleGUI
import PySimpleGUI as sg
from PIL import Image

def resize_image(imagepath, size=(100,100)):
    image = Image.open(imagepath)
    image = image.resize(size)
    
    image_bytes = io.BytesIO()
    image.save(image_bytes, format="PNG")
    image_bytes = image_bytes.getvalue()
    
    return image_bytes



# Cria a janela principal
def create_main_window(title=None, theme="DarkTeal9"):    
    # Definindo o nosso tema
    sg.theme(theme)
    
    parent_path = str(pathlib.Path(__file__).parent.resolve())
    image = "math.png"
    
    fullpath = os.path.join(parent_path, image)
    
    image = resize_image(fullpath)
    
    # Definindo nosso layout
    layout = [
        [
            sg.Image(data=image, size=(100, 100)),
        ],
        [
            sg.Text("Calculadora 1990", font=("Calibri", 20, 'bold')),
        ],
        [
            sg.Input(
                "0",
                size=(10, 30),
                font=("Segoi UI", 25),
            )
        ]
    ]
    
    # Definindo o titulo da janela
    if title is None:
        title = "Meu Tiítulo"
    else:
        title = title

    # Criar a janela e deixa ela finalizável
    window = sg.Window(title, layout,element_justification='center', finalize=True)
    
    # Retorna a nossa janela
    return window

