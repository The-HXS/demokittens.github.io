from appscript import app, k
import time
import os

def create_keywords_pool():
    try:
        print("Iniciando proceso de Keywords Pool...")
        numbers = app('Numbers')
        
        # Primera fase: Crear hoja y headers
        script_content = '''
        tell application "Numbers"
            tell front document
                if exists sheet "Keywords Pool" then
                    delete sheet "Keywords Pool"
                end if
                
                make new sheet with properties {name:"Keywords Pool"}
                tell last sheet
                    tell table 1
                        -- Headers iniciales
                        set value of cell 1 of column 1 to "Keyword"
                        set value of cell 1 of column 2 to "Category"
                        set value of cell 1 of column 3 to "Priority"
                        set value of cell 1 of column 4 to "Used In"
                        set value of cell 1 of column 5 to "Notes"
                    end tell
                end tell
            end tell
        end tell
        '''
        
        script_path = os.path.expanduser('~/Documents/AppStoreStickers/SharedMarketing/numbers_automation/temp_script.scpt')
        with open(script_path, 'w') as f:
            f.write(script_content)
        
        print("Fase 1: Creando estructura básica...")
        os.system(f"osascript {script_path}")
        
        print("¿Se creó correctamente la estructura básica? (si/no)")
        if input().strip().lower() == "si":
            # Segunda fase: Añadir datos base
            script_content = '''
            tell application "Numbers"
                tell front document
                    tell sheet "Keywords Pool"
                        tell table 1
                            -- Datos principales
                            -- Fila 2: kawaii
                            set value of cell 2 of column 1 to "kawaii"
                            set value of cell 2 of column 2 to "Brand"
                            set value of cell 2 of column 3 to "High"
                            set value of cell 2 of column 4 to "All packs"
                            set value of cell 2 of column 5 to "Core brand term"
                            
                            -- Fila 3: christmas
                            set value of cell 3 of column 1 to "christmas"
                            set value of cell 3 of column 2 to "Holiday"
                            set value of cell 3 of column 3 to "High"
                            set value of cell 3 of column 4 to "Christmas packs"
                            set value of cell 3 of column 5 to "Seasonal focus"
                            
                            -- Fila 4: cute
                            set value of cell 4 of column 1 to "cute"
                            set value of cell 4 of column 2 to "Style"
                            set value of cell 4 of column 3 to "High"
                            set value of cell 4 of column 4 to "All packs"
                            set value of cell 4 of column 5 to "Universal appeal"
                            
                            -- Fila 5: sticker
                            set value of cell 5 of column 1 to "sticker"
                            set value of cell 5 of column 2 to "Product"
                            set value of cell 5 of column 3 to "High"
                            set value of cell 5 of column 4 to "All packs"
                            set value of cell 5 of column 5 to "Product category"
                            
                            -- Fila 6: holiday
                            set value of cell 6 of column 1 to "holiday"
                            set value of cell 6 of column 2 to "Season"
                            set value of cell 6 of column 3 to "Medium"
                            set value of cell 6 of column 4 to "Christmas packs"
                            set value of cell 6 of column 5 to "Seasonal term"
                        end tell
                    end tell
                end tell
            end tell
            '''
            
            with open(script_path, 'w') as f:
                f.write(script_content)
            
            print("\nFase 2: Añadiendo datos base...")
            os.system(f"osascript {script_path}")
            
            print("\n¿Se añadieron correctamente los datos? (si/no)")
            if input().strip().lower() == "si":
                print("\n¡Keywords Pool completado!")
                print("\nOpciones disponibles:")
                print("1. Continuar con la siguiente hoja (Validation Rules)")
                print("2. Añadir más keywords a la pool actual")
                print("3. Ajustar formato de la tabla actual")
                print("\n¿Qué prefieres? (1/2/3)")
        
        os.remove(script_path)
        
    except Exception as e:
        print(f"\nError en la operación: {str(e)}")
        print("Tipo de error:", type(e))

if __name__ == "__main__":
    create_keywords_pool()