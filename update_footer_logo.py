import os
import re

directory = r"c:\Users\santi\Downloads\colores"

# Regex to match the footer logo image tag with its style
pattern = re.compile(r'(<img\s+src="\./logos/Logo_footer\.png"\s+alt="Los colores de la guerra"[\s\n]*)style="max-width:\s*180px;"(.*?>)', re.IGNORECASE)

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".html"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            new_content = pattern.sub(r'\1style="max-width: 280px;"\2', content)
            
            if new_content != content:
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated {file}")
