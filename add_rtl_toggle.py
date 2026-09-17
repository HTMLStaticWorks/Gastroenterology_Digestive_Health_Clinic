import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

rtl_btn = '''        <button id="rtl-toggle" class="theme-toggle" aria-label="Toggle language direction" style="margin-inline-end: 0.5rem;">
          <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="2" y1="12" x2="22" y2="12"></line>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path>
          </svg>
        </button>
'''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if 'id="rtl-toggle"' not in html:
        html = html.replace('<div class="nav-actions">', '<div class="nav-actions">\n' + rtl_btn)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(html)

print('Added RTL toggle to all HTML files')
