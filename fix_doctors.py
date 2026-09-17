import re

with open('doctors.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add new CSS classes
css_addition = '''    .doctor-profile-reverse {
      grid-template-columns: 2fr 1fr;
    }
    .doctor-profile-reverse .doctor-img-wrapper {
      order: 2;
    }
    .doctor-profile-reverse .doctor-info {
      order: 1;
    }'''
content = content.replace('.doctor-profile {', css_addition + '\n    .doctor-profile {')

mobile_css_addition = '''      .doctor-profile-reverse {
        grid-template-columns: 1fr;
      }
      .doctor-profile-reverse .doctor-img-wrapper,
      .doctor-profile-reverse .doctor-info {
        order: unset;
      }'''
content = content.replace('direction: ltr !important;', 'direction: ltr !important;\n' + mobile_css_addition)

# Update HTML for Dr. Turing
content = content.replace('<div class="doctor-profile" style="direction: rtl;">', '<div class="doctor-profile doctor-profile-reverse">')
content = content.replace('<div class="doctor-img-wrapper" style="direction: ltr;">', '<div class="doctor-img-wrapper">')
content = content.replace('<div class="doctor-info" style="direction: ltr;">', '<div class="doctor-info">')

with open('doctors.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated doctors.html layout hacks')
