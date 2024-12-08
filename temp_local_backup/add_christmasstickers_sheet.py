from appscript import app, k
import time
import os

def add_christmasstickers_sheet():
    try:
        print("Iniciando proceso... Fase 1: Creación de hoja y headers")
        numbers = app('Numbers')
        
        script_content = '''
        tell application "Numbers"
            tell front document
                if exists sheet "ChristmasStickers" then
                    delete sheet "ChristmasStickers"
                end if
                
                make new sheet with properties {name:"ChristmasStickers"}
                tell last sheet
                    tell table 1
                        -- Headers
                        set value of cell 1 of column 1 to "Language"
                        set value of cell 1 of column 2 to "Name"
                        set value of cell 1 of column 3 to "Subtitle"
                        set value of cell 1 of column 4 to "Promotional Text"
                        set value of cell 1 of column 5 to "Keywords"
                    end tell
                end tell
            end tell
        end tell
        '''
        
        script_path = os.path.expanduser('~/Documents/AppStoreStickers/SharedMarketing/numbers_automation/temp_script.scpt')
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        print("Ejecutando fase 1...")
        os.system(f"osascript {script_path}")
        
        print("¿Se crearon correctamente los headers? (si/no)")
        respuesta = input()
        
        if respuesta.lower() == 'si':
            print("\nFase 2: Añadiendo datos de en-US...")
            
            script_content = '''
            tell application "Numbers"
                tell front document
                    tell sheet "ChristmasStickers"
                        tell table 1
                            -- Datos para en-US
                            set value of cell 2 of column 1 to "en-US"
                            set value of cell 2 of column 2 to "Kawaii! It is Christmas!"
                            set value of cell 2 of column 3 to "Part of the Kawaii! Collection"
                            set value of cell 2 of column 4 to "Join the Kawaii! Community with our Christmas Collection!"
                            set value of cell 2 of column 5 to "kawaii,christmas,cute,sticker,holiday"
                        end tell
                    end tell
                end tell
            end tell
            '''
            
            with open(script_path, 'w') as f:
                f.write(script_content)
            
            print("Ejecutando fase 2...")
            os.system(f"osascript {script_path}")
            
            print("¿Se añadieron correctamente los datos de en-US? (si/no)")
            respuesta = input()
            
            if respuesta.lower() == 'si':
                print("\nFase 3: Añadiendo placeholders para otros idiomas...")
                
                script_content = '''
                tell application "Numbers"
                    tell front document
                        tell sheet "ChristmasStickers"
                            tell table 1
                                -- Placeholders para otros idiomas
                                set value of cell 3 of column 1 to "ja"
                                set value of cell 4 of column 1 to "zh-Hans"
                                set value of cell 5 of column 1 to "es-ES"
                                set value of cell 6 of column 1 to "fr-FR"
                                set value of cell 7 of column 1 to "de-DE"
                                set value of cell 8 of column 1 to "ko"
                            end tell
                        end tell
                    end tell
                end tell
                '''
                
                with open(script_path, 'w') as f:
                    f.write(script_content)
                
                print("Ejecutando fase 3...")
                os.system(f"osascript {script_path}")
                
                print("\nProceso completo. Por favor verifica que todo esté correcto.")
            else:
                print("Se detuvo el proceso en la fase 2.")
        else:
            print("Se detuvo el proceso en la fase 1.")
        
        os.remove(script_path)
        
    except Exception as e:
        print(f"\nError en la operación: {str(e)}")

if __name__ == "__main__":
    add_christmasstickers_sheet()