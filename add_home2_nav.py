import glob

html_files = glob.glob('*.html')
for f in html_files:
    if f in ['dashboard.html', 'login.html', 'signup.html']: continue
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    if '<a href="home2.html" class="nav-link">Home 2</a>' not in content:
        new_content = content.replace('<a href="index.html" class="nav-link">Home</a>', '<a href="index.html" class="nav-link">Home</a>\n      <a href="home2.html" class="nav-link">Home 2</a>')
        
        if content != new_content:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f'Updated {f}')
