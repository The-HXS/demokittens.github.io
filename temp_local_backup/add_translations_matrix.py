from appscript import app, k
import time
import os

def add_translations_matrix():
    try:
        print("Iniciando proceso... Fase 1: Creación de hoja y primeras columnas")
        numbers = app('Numbers')
        
        script_content = '''
        tell application "Numbers"
            tell front document
                if exists sheet "Translations Matrix" then
                    delete sheet "Translations Matrix"
                end if
                
                make new sheet with properties {name:"Translations Matrix"}
                tell last sheet
                    tell table 1
                        -- Primera ronda de headers
                        set value of cell 1 of column 1 to "Key Term"
                        set value of cell 1 of column 2 to "en-US"
                        set value of cell 1 of column 3 to "ja"
                        set value of cell 1 of column 4 to "zh-Hans"
                        set value of cell 1 of column 5 to "es-ES"
                        
                        -- Primera palabra clave
                        set value of cell 2 of column 1 to "Christmas"
                        set value of cell 2 of column 2 to "Christmas"
                        set value of cell 2 of column 3 to "クリスマス"
                        set value of cell 2 of column 4 to "圣诞节"
                        set value of cell 2 of column 5 to "Navidad"
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
        
        print("¿Se crearon correctamente las primeras 5 columnas? (si/no)")
        respuesta = input()
        
        if respuesta.lower() == 'si':
            script_content = '''
            tell application "Numbers"
                tell front document
                    tell sheet "Translations Matrix"
                        tell table 1
                            -- Términos adicionales en las columnas existentes
                            set value of cell 3 of column 1 to "Cute"
                            set value of cell 3 of column 2 to "Cute"
                            set value of cell 3 of column 3 to "かわいい"
                            set value of cell 3 of column 4 to "可爱"
                            set value of cell 3 of column 5 to "Lindo"
                            
                            set value of cell 4 of column 1 to "Sticker"
                            set value of cell 4 of column 2 to "Sticker"
                            set value of cell 4 of column 3 to "ステッカー"
                            set value of cell 4 of column 4 to "贴纸"
                            set value of cell 4 of column 5 to "Pegatina"
                            
                            set value of cell 5 of column 1 to "Collection"
                            set value of cell 5 of column 2 to "Collection"
                            set value of cell 5 of column 3 to "コレクション"
                            set value of cell 5 of column 4 to "系列"
                            set value of cell 5 of column 5 to "Colección"
                        end tell
                    end tell
                end tell
            end tell
            '''
            
            with open(script_path, 'w') as f:
                f.write(script_content)
            
            print("\nFase 2: Añadiendo más términos...")
            os.system(f"osascript {script_path}")
            
            print("\nProceso completo. ¿Todo se ve correcto? (si/no)")
            confirmacion = input()
            
            if confirmacion.lower() == 'si':
                print("\nAhora podemos:")
                print("1. Añadir las columnas restantes (fr-FR, de-DE, ko)")
                print("2. Continuar con la siguiente hoja")
                print("¿Qué prefieres? (1/2)")
                siguiente = input()
                return siguiente
            
        os.remove(script_path)
        
    except Exception as e:
        print(f"\nError en la operación: {str(e)}")

if __name__ == "__main__":
    add_translations_matrix()