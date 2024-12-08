from appscript import app, k
import time
import os

def fill_remaining_translations():
    try:
        print("Iniciando proceso para llenar traducciones...")
        numbers = app('Numbers')
        
        script_content = '''
        tell application "Numbers"
            tell front document
                tell sheet "Translations Matrix"
                    tell table 1
                        -- Solo columna 6 (fr-FR)
                        set value of cell 1 of column 6 to "fr-FR"
                        set value of cell 2 of column 6 to "Noël"
                        set value of cell 3 of column 6 to "Mignon"
                        set value of cell 4 of column 6 to "Autocollant"
                        set value of cell 5 of column 6 to "Collection"
                    end tell
                end tell
            end tell
        end tell
        '''
        
        script_path = os.path.expanduser('~/Documents/AppStoreStickers/SharedMarketing/numbers_automation/temp_script.scpt')
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        print("Ejecutando script para fr-FR...")
        os.system(f"osascript {script_path}")
        
        print("\n¿Se llenaron correctamente los datos de fr-FR? (si/no)")
        respuesta = input().strip().lower()
        
        if respuesta == "si":
            print("\nPor favor:")
            print("1. Agrega una nueva columna después de fr-FR usando Table > Add Column After")
            print("2. Escribe 'listo' cuando hayas agregado la columna")
            confirmacion = input().strip().lower()
            
            if confirmacion == "listo":
                print("\nAhora intentaremos llenar los datos de de-DE...")
                # Aquí continuaremos con la siguiente columna
        
        os.remove(script_path)
        
    except Exception as e:
        print(f"\nError en la operación: {str(e)}")

if __name__ == "__main__":
    fill_remaining_translations()