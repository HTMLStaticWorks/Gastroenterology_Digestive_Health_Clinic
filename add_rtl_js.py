import os

with open('app.js', 'r', encoding='utf-8') as f:
    js = f.read()

if 'rtlToggle' not in js:
    js += '''

// RTL Toggle functionality
document.addEventListener('DOMContentLoaded', () => {
  const rtlToggle = document.getElementById('rtl-toggle');
  
  // Check for saved preference
  const savedRtl = localStorage.getItem('rtl') === 'true';
  if (savedRtl) {
    document.documentElement.setAttribute('dir', 'rtl');
    document.documentElement.setAttribute('lang', 'ar');
  } else {
    document.documentElement.setAttribute('dir', 'ltr');
    document.documentElement.setAttribute('lang', 'en');
  }

  if (rtlToggle) {
    rtlToggle.addEventListener('click', () => {
      const isRtl = document.documentElement.getAttribute('dir') === 'rtl';
      if (isRtl) {
        document.documentElement.setAttribute('dir', 'ltr');
        document.documentElement.setAttribute('lang', 'en');
        localStorage.setItem('rtl', 'false');
      } else {
        document.documentElement.setAttribute('dir', 'rtl');
        document.documentElement.setAttribute('lang', 'ar');
        localStorage.setItem('rtl', 'true');
      }
    });
  }
});
'''
    with open('app.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print('Added RTL JS logic to app.js')
else:
    print('RTL logic already exists')
