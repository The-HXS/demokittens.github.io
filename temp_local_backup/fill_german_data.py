from appscript import app, k
import time
import os

def fill_german_data():
    try:
        print("Iniciando proceso para llenar datos en alemán...")
        numbers = app('Numbers')
        
        script_content = '''
        tell application "Numbers"
            tell front document
                tell sheet "Translations Matrix"
                    tell table 1
                        -- Columna 7 (de-DE)
                        set value of cell 1 of column 7 to "de-DE"
                        set value of cell 2 of column 7 to "Weihnachten"
                        set value of cell 3 of column 7 to "Niedlich"
                        set value of cell 4 of column 7 to "Aufkleber"
                        set value of cell 5 of column 7 to "Kollektion"
                    end tell
                end tell
            end tell
        end tell
        '''
        
        script_path = os.path.expanduser('~/Documents/AppStoreStickers/SharedMarketing/numbers_automation/temp_script.scpt')
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        print("Ejecutando script para de-DE...")
        os.system(f"osascript {script_path}")
        
        print("\n¿Se llenaron correctamente los datos de alemán? (si/no)")
        respuesta = input().strip().lower()
        
        if respuesta == "si":
            print("\nPor favor:")
            print("1. Agrega una nueva columna después de de-DE usando Table > Add Column After")
            print("2. Escribe 'listo' cuando hayas agregado la columna para coreano")
            
        os.remove(script_path)
        
    except Exception as e:
        print(f"\nError en la operación: {str(e)}")

if __name__ == "__main__":
    fill_german_data()