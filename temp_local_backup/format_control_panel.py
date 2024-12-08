from appscript import app, k
import time
import os

def format_control_panel():
    try:
        print("Iniciando proceso...")
        numbers = app('Numbers')
        
        script_content = '''
        tell application "Numbers"
            make new document
            tell front document
                tell sheet 1
                    set name to "Control Panel"
                    tell table 1
                        -- Headers
                        set value of cell 1 of column 1 to "Pack"
                        set value of cell 1 of column 2 to "Status"
                        set value of cell 1 of column 3 to "Priority"
                        set value of cell 1 of column 4 to "Target Date"
                        set value of cell 1 of column 5 to "Notes"
                        
                        -- Datos fila 1
                        set value of cell 2 of column 1 to "ChristmasStickers"
                        set value of cell 2 of column 2 to "In Progress"
                        set value of cell 2 of column 3 to "High"
                        set value of cell 2 of column 4 to "2023-12-10"
                        set value of cell 2 of column 5 to "Main Christmas Pack"
                        
                        -- Datos fila 2
                        set value of cell 3 of column 1 to "ChristmasCats"
                        set value of cell 3 of column 2 to "Pending"
                        set value of cell 3 of column 3 to "Medium"
                        set value of cell 3 of column 4 to "2023-12-12"
                        set value of cell 3 of column 5 to "Cat Themed Pack"
                        
                        -- Datos fila 3
                        set value of cell 4 of column 1 to "Axolotls"
                        set value of cell 4 of column 2 to "Planned"
                        set value of cell 4 of column 3 to "Low"
                        set value of cell 4 of column 4 to "2023-12-14"
                        set value of cell 4 of column 5 to "Axolotl Pack"
                    end tell
                end tell
            end tell
        end tell
        '''
        
        script_path = os.path.expanduser('~/Documents/AppStoreStickers/SharedMarketing/numbers_automation/temp_script.scpt')
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        print("Ejecutando AppleScript...")
        os.system(f"osascript {script_path}")
        
        os.remove(script_path)
        print("Proceso completado")
        
        print("\nNOTA: Para dar formato a la tabla:")
        print("1. Selecciona la fila de encabezados")
        print("2. Usa Cmd + B para ponerlos en negrita")
        print("3. Ajusta los anchos de columna manualmente")
        
    except Exception as e:
        print(f"\nError en la operación: {str(e)}")

if __name__ == "__main__":
    format_control_panel()