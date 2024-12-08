from appscript import app, k
import time

def setup_numbers_document():
    try:
        numbers = app('Numbers')
        
        # Crear nuevo documento
        doc = numbers.make(new=k.document)
        
        # Obtener la primera hoja y tabla
        sheet = numbers.documents.first.sheets.first
        table = sheet.tables.first
        
        # Renombrar las hojas
        sheet_names = [
            "Control Panel",
            "ChristmasStickers",
            "Translations Matrix",
            "Keywords Pool",
            "Validation Rules"
        ]
        
        # Configurar primera hoja
        sheet.name.set(sheet_names[0])
        
        # Crear hojas adicionales
        for name in sheet_names[1:]:
            numbers.documents.first.make(new=k.sheet, with_properties={k.name: name})
        
        print("Documento creado con éxito")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    setup_numbers_document()