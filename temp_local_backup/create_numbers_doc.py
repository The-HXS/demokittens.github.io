from appscript import app, k
import time

def create_basic_document():
    try:
        # Iniciar Numbers
        numbers = app('Numbers')
        
        # Crear un nuevo documento
        doc = numbers.make(new=k.document)
        time.sleep(2)  # Dar tiempo a Numbers para crear el documento
        
        # Obtener la primera hoja
        sheet = doc.sheets.first
        
        # Renombrar la primera hoja a "Control Panel"
        sheet.name.set("Control Panel")
        
        print("Documento básico creado con éxito")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    create_basic_document()