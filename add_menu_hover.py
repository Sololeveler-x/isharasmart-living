with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

hover_css = '''
/* CSS PURE HOVER FOR DROPDOWNS */
.elementor-nav-menu li.menu-item-has-children {
  position: relative !important;
}

.elementor-nav-menu li.menu-item-has-children:hover > ul.sub-menu,
.elementor-nav-menu li.menu-item-has-children:focus-within > ul.sub-menu {
  display: block !important;
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
  animation: isharaMenuFade 0.22s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
}

@keyframes isharaMenuFade {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
'''

html = html.replace('/* 2. SUBMENU & DROPDOWN GLASSMORPHISM ON HOVER */', hover_css + '\n/* 2. SUBMENU & DROPDOWN GLASSMORPHISM ON HOVER */')

with open('home/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Added pure CSS hover for sub-menus!")
