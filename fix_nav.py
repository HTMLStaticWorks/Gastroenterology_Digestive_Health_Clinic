import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

hamburger_html = '''      <button id="mobile-menu-toggle" class="hamburger" aria-label="Toggle navigation">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="hamburger-icon-open"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
      </button>'''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Aura to Aura Digestive
    content = re.sub(r'</svg>\s*Aura</a>', '</svg>\n      Aura Digestive</a>', content)
    content = re.sub(r'</svg>\s*Aura</div>', '</svg>\n      Aura Digestive</div>', content)
    
    # 2. Add hamburger menu if missing
    if 'mobile-menu-toggle' not in content:
        theme_toggle_regex = r'(<button id="theme-toggle"[^>]*></button>)'
        if re.search(theme_toggle_regex, content):
            content = re.sub(theme_toggle_regex, r'\1\n' + hamburger_html, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated brand names and hamburger menus across all HTML files.')
