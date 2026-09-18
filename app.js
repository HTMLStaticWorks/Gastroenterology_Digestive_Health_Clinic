document.addEventListener('DOMContentLoaded', () => {
  // Theme Toggle Logic
  const themeToggle = document.getElementById('theme-toggle');
  const body = document.documentElement;
  
  // Check for saved theme preference or system preference
  const savedTheme = localStorage.getItem('theme');
  const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  if (savedTheme) {
    body.setAttribute('data-theme', savedTheme);
  } else if (systemPrefersDark) {
    body.setAttribute('data-theme', 'dark');
  }
  
  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const currentTheme = body.getAttribute('data-theme');
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      body.setAttribute('data-theme', newTheme);
      localStorage.setItem('theme', newTheme);
      
      // Update icon if using lucide or SVG
      updateThemeIcon(newTheme);
    });
  }
  
  function updateThemeIcon(theme) {
    if(themeToggle) {
        themeToggle.innerHTML = theme === 'dark' 
            ? '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.2 4.2l1.4 1.4M18.4 18.4l1.4 1.4M1 12h2M21 12h2M4.2 19.8l1.4-1.4M18.4 5.6l1.4-1.4"/></svg>' 
            : '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>';
    }
  }

  // Initialize theme icon
  updateThemeIcon(body.getAttribute('data-theme') || 'light');

  // Back to Top Logic
  const backToTopBtn = document.getElementById('back-to-top');
  
  if (backToTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });
    
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // Mobile Menu Logic
  const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
  const navLinks = document.querySelector('.nav-links');
  const navActions = document.querySelector('.nav-actions');
  
  if (mobileMenuToggle && navLinks) {
    const actionBtn = document.querySelector('.nav-actions .btn') || document.querySelector('.nav-links .btn');
    
    function handleMenuResize() {
      if (window.innerWidth <= 900) {
        if (actionBtn && actionBtn.parentElement !== navLinks) {
          navLinks.appendChild(actionBtn);
        }
      } else {
        if (actionBtn && navActions && actionBtn.parentElement !== navActions) {
          navActions.appendChild(actionBtn);
        }
      }
    }
    
    window.addEventListener('resize', handleMenuResize);
    handleMenuResize(); // initialize on load

    mobileMenuToggle.addEventListener('click', () => {
      navLinks.classList.toggle('active');
      
      // Toggle icon between hamburger and close (X)
      if (navLinks.classList.contains('active')) {
        mobileMenuToggle.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="hamburger-icon-close"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>';
      } else {
        mobileMenuToggle.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="hamburger-icon-open"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>';
      }
    });
  }
});


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
