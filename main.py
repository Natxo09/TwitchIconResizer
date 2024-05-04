import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class ImageResizerApp:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()  # Oculta la ventana principal temporalmente
        
        # Solicita al usuario que seleccione una imagen
        file_path = filedialog.askopenfilename()
        if file_path:
            self.create_resized_images(file_path)
        self.root.destroy()

    def create_resized_images(self, file_path, sizes=(18, 36, 72)):
        # Carga la imagen original
        original_image = Image.open(file_path)
        
        # Obtiene el nombre de la imagen y crea un directorio para las imágenes redimensionadas
        image_name = os.path.splitext(os.path.basename(file_path))[0]
        directory_path = os.path.join(os.path.dirname(file_path), image_name)
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        # Redimensiona y guarda cada tamaño de imagen
        for size in sizes:
            resized_image = original_image.resize((size, size), Image.LANCZOS)
            resized_image.save(os.path.join(directory_path, f'{size}x{size}.png'))

        # Informa al usuario que las imágenes han sido guardadas
        print(f"Las imágenes redimensionadas se han guardado en: {directory_path}")

if __name__ == '__main__':
    root = tk.Tk()
    app = ImageResizerApp(root)
