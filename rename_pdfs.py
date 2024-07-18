import os
import re
from PyPDF2 import PdfReader


def get_unique_filename(folder_path, base_filename):
    """Genera un nombre de archivo único agregando -1, -2, etc. si es necesario."""
    new_filename = base_filename
    counter = 1
    while os.path.exists(os.path.join(folder_path, new_filename)):
        name, ext = os.path.splitext(base_filename)
        new_filename = f"{name}-{counter}{ext}"
        counter += 1
    return new_filename


def rename_pdfs(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)

            # Leer el PDF
            with open(file_path, 'rb') as file:
                pdf = PdfReader(file)
                first_page = pdf.pages[0]
                text = first_page.extract_text()

            # Buscar el número de Folio Muestra
            match = re.search(r'Folio Muestra:\s*(\d+)', text)
            if match:
                folio_number = match.group(1)

                # Crear el nuevo nombre de archivo
                new_filename = f"{folio_number}.pdf"
                new_filename = get_unique_filename(folder_path, new_filename)
                new_file_path = os.path.join(folder_path, new_filename)

                # Renombrar el archivo
                os.rename(file_path, new_file_path)
                print(f"Renombrado: {filename} -> {new_filename}")
            else:
                print(f"No se encontró Folio Muestra en: {filename}")


# Usa la función
folder_path = r"C:\Users\anton\OneDrive\Escritorio\pruebas"
rename_pdfs(folder_path)
