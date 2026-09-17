import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

old_svg = '''          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
          </svg>'''

new_svg = '''          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M8 3 4 7l4 4"/>
            <path d="M4 7h16"/>
            <path d="m16 21 4-4-4-4"/>
            <path d="M20 17H4"/>
          </svg>'''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if old_svg in html:
        html = html.replace(old_svg, new_svg)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Updated {file}')

print('Done replacing icons')
