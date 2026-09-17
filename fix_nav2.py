import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Change to AURA
    content = re.sub(r'</svg>\s*Aura Digestive</a>', '</svg>\n      AURA</a>', content)
    content = re.sub(r'</svg>\s*Aura Digestive</div>', '</svg>\n      AURA</div>', content)
    content = re.sub(r'</svg>\s*Aura</a>', '</svg>\n      AURA</a>', content)
    content = re.sub(r'</svg>\s*Aura</div>', '</svg>\n      AURA</div>', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated brand names to AURA')
