from appscript import app, k
import time
import os

def fill_korean_data():
    try:
        print("Iniciando proceso para llenar datos en coreano...")
        numbers = app('Numbers')
        
        script_content = '''
        tell application "Numbers"
            tell front document
                tell sheet "Translations Matrix"
                    tell table 1
                        -- Columna 8 (ko)
                        set value of cell 1 of column 8 to "ko"
                        set value of cell 2 of column 8 to "크리스마스"
                        set value of cell 3 of column 8 to "귀여운"
                        set value of cell 4 of column 8 to "스티커"
                        set value of cell 5 of column 8 to "컬렉션"
                    end tell
                end tell
            end tell
        end tell
        '''
        
        script_path = os.path.expanduser('~/Documents/AppStoreStickers/SharedMarketing/numbers_automation/temp_script.scpt')
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        print("Ejecutando script para ko...")
        os.system(f"osascript {script_path}")
        
        print("\nProceso completado. ¿Se llenaron correctamente los datos de coreano? (si/no)")
        respuesta = input().strip().lower()
        
        if respuesta == "si":
            print("\n¡Translations Matrix completada!")
            print("\n¿Continuamos con la siguiente hoja (Keywords Pool)? (si/no)")
        
        os.remove(script_path)
        
    except Exception as e:
        print(f"\nError en la operación: {str(e)}")

if __name__ == "__main__":
    fill_korean_data()