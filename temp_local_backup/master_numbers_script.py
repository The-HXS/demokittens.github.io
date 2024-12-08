from appscript import app, k
import time

def format_all_sheets():
    try:
        numbers = app('Numbers')
        doc = numbers.documents.first
        
        # Contenido para cada hoja
        sheet_content = {
            "Control Panel": {
                "headers": ["Pack", "Status", "Priority", "Target Date", "Notes"],
                "data": [
                    ["ChristmasStickers", "In Progress", "High", "2023-12-10", "Main Christmas Pack"],
                    ["ChristmasCats", "Pending", "Medium", "2023-12-12", "Cat Themed Pack"],
                    ["Axolotls", "Planned", "Low", "2023-12-14", "Axolotl Pack"]
                ],
                "column_widths": [150, 100, 80, 100, 250]
            },
            
            "ChristmasStickers": {
                "headers": ["Language", "Name", "Subtitle", "Promotional Text", "Keywords", "Description"],
                "data": [
                    ["en-US", "Kawaii! It is Christmas!", "Part of the Kawaii! Collection", 
                     "Join the Kawaii! Community with our Christmas Collection!", 
                     "kawaii,christmas,cute,sticker,holiday", "Full description here..."],
                    ["ja", "", "", "", "", ""],
                    ["zh-Hans", "", "", "", "", ""],
                    ["es-ES", "", "", "", "", ""],
                    ["fr-FR", "", "", "", "", ""],
                    ["de-DE", "", "", "", "", ""],
                    ["ko", "", "", "", "", ""]
                ],
                "column_widths": [80, 150, 150, 200, 150, 300]
            },
            
            "Translations Matrix": {
                "headers": ["Key Term", "en-US", "ja", "zh-Hans", "es-ES", "fr-FR", "de-DE", "ko"],
                "data": [
                    ["Christmas", "Christmas", "クリスマス", "圣诞节", "Navidad", "Noël", "Weihnachten", "크리스마스"],
                    ["Cute", "Cute", "かわいい", "可爱", "Lindo", "Mignon", "Niedlich", "귀여운"],
                    ["Sticker", "Sticker", "ステッカー", "贴纸", "Sticker", "Autocollant", "Aufkleber", "스티커"]
                ],
                "column_widths": [120, 100, 100, 100, 100, 100, 100, 100]
            },
            
            "Keywords Pool": {
                "headers": ["Keyword", "Category", "Priority", "Used In", "Notes"],
                "data": [
                    ["kawaii", "Brand", "High", "All packs", "Core brand term"],
                    ["christmas", "Holiday", "High", "Christmas packs", "Seasonal"],
                    ["cute", "Style", "High", "All packs", "Universal appeal"]
                ],
                "column_widths": [100, 100, 80, 150, 250]
            },
            
            "Validation Rules": {
                "headers": ["Field", "Max Length", "Required", "Format Rules", "Notes"],
                "data": [
                    ["Name", "30", "Yes", "No special chars", "Keep \"Kawaii!\""],
                    ["Subtitle", "30", "Yes", "No special chars", "Include \"Collection\""],
                    ["Promotional Text", "170", "Yes", "Emojis allowed", "Include \"Community\""],
                    ["Keywords", "100", "Yes", "Comma separated", "No spaces"],
                    ["Description", "4000", "Yes", "Markdown allowed", "Include sections"]
                ],
                "column_widths": [150, 100, 80, 200, 250]
            }
        }
        
        def format_sheet(sheet, content):
            table = sheet.tables.first
            
            # Añadir encabezados
            for col, header in enumerate(content["headers"], 1):
                table.cells[1, col].value.set(header)
                table.cells[1, col].font_weight.set(k.bold)
                table.cells[1, col].background_color.set([0.9, 0.9, 0.9])
            
            # Añadir datos
            for row, data_row in enumerate(content["data"], 2):
                for col, value in enumerate(data_row, 1):
                    table.cells[row, col].value.set(value)
            
            # Ajustar anchos de columna
            for col, width in enumerate(content["column_widths"], 1):
                table.columns[col].width.set(width)
        
        # Formatear cada hoja
        for sheet in doc.sheets():
            sheet_name = sheet.name()
            if sheet_name in sheet_content:
                print(f"Formatting {sheet_name}...")
                format_sheet(sheet, sheet_content[sheet_name])
                
        print("All sheets formatted successfully")
        
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    format_all_sheets()