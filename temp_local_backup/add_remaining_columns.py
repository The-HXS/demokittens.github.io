from appscript import app, k
import time
import os

def add_remaining_columns():
    try:
        print("Iniciando proceso de añadir columnas restantes...")
        numbers = app('Numbers')
        
        script_content = '''
        tell application "Numbers"
            tell front document
                tell sheet "Translations Matrix"
                    tell table 1
                        -- Primero intentamos solo la columna fr-FR
                        set value of cell 1 of column 6 to "fr-FR"
                    end tell
                end tell
            end tell
        end tell
        '''
        
        script_path = os.path.expanduser('~/Documents/AppStoreStickers/SharedMarketing/numbers_automation/temp_script.scpt')
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        print("Intentando añadir la columna fr-FR...")
        os.system(f"osascript {script_path}")
        
        print("¿Se añadió correctamente la columna fr-FR? (si/no)")
        respuesta = input().strip().lower()
        
        if respuesta == "no":
            print("\nVamos a intentar un enfoque diferente.")
            print("Por favor:")
            print("1. En Numbers, haz clic en el ícono '+' de la tabla para añadir una columna")
            print("2. Avísame cuando hayas añadido manualmente la columna (listo)")
            confirmacion = input().strip().lower()
            
            if confirmacion == "listo":
                print("\n¿Continuamos con el script para añadir los datos? (si/no)")
                continuar = input().strip().lower()
                if continuar == "si":
                    # Aquí añadiremos el código para los datos
                    print("Preparando el siguiente paso...")
        
        os.remove(script_path)
        
    except Exception as e:
        print(f"\nError en la operación: {str(e)}")

if __name__ == "__main__":
    add_remaining_columns()