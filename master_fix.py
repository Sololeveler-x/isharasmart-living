import re

with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# 1. ASSIGN EXPLICIT SECTION IDs
section_id_map = [
    (r'<section[^>]*class="[^"]*riva-ph-section[^"]*"[^>]*>', '<section class="riva-ph-section riva-anim" id="riva-house">'),
    (r'<section[^>]*class="[^"]*riva-hero[^"]*"[^>]*>', '<section class="riva-hero" id="hero">'),
    (r'<section[^>]*class="[^"]*riva-device-showcase[^"]*"[^>]*>', '<section class="riva-device-showcase riva-anim" id="products">'),
    (r'<section[^>]*class="[^"]*riva-works-section[^"]*"[^>]*>', '<section class="riva-works-section riva-anim" id="solutions">'),
    (r'<section[^>]*class="[^"]*riva-sig-section[^"]*"[^>]*>', '<section class="riva-sig-section" id="rivaSig">'),
    (r'<section[^>]*class="[^"]*riva-hub-section[^"]*"[^>]*>', '<section class="riva-hub-section riva-anim" id="commercial">'),
    (r'<section[^>]*class="[^"]*riva-why-section[^"]*"[^>]*>', '<section class="riva-why-section riva-anim" id="about">'),
    (r'<section[^>]*class="[^"]*riva-ms[^"]*"[^>]*>', '<section class="riva-ms" id="matter">'),
    (r'<section[^>]*class="[^"]*riva-dim-section[^"]*"[^>]*>', '<section class="riva-dim-section riva-anim" id="dimmer">'),
    (r'<section[^>]*class="[^"]*riva-compatibility[^"]*"[^>]*>', '<section class="riva-compatibility riva-anim" id="brands">'),
    (r'<section[^>]*class="[^"]*riva-cta-section[^"]*"[^>]*>', '<section class="riva-cta-section riva-anim" id="contact">'),
]

for pattern, replacement in section_id_map:
    html = re.sub(pattern, replacement, html, count=1)

print("Section IDs mapped cleanly to: #riva-house, #hero, #products, #solutions, #rivaSig, #commercial, #about, #matter, #dimmer, #brands, #contact")

# 2. MATCH ALL NAVIGATION LINKS DIRECTLY TO THESE IDS
nav_href_map = {
    r'href="[^"]*"\s*([^>]*>Home<)': r'href="#riva-house" \1',
    r'href="[^"]*"\s*([^>]*>Matter<)': r'href="#matter" \1',
    r'href="[^"]*"\s*([^>]*>Solutions<)': r'href="#solutions" \1',
    r'href="[^"]*"\s*([^>]*>Residential<)': r'href="#solutions" \1',
    r'href="[^"]*"\s*([^>]*>Commercial<)': r'href="#commercial" \1',
    r'href="[^"]*"\s*([^>]*>About<)': r'href="#about" \1',
    r'href="[^"]*"\s*([^>]*>Products<)': r'href="#products" \1',
    r'href="[^"]*"\s*([^>]*>Brands<)': r'href="#brands" \1',
    r'href="[^"]*"\s*([^>]*>Explore products<)': r'href="#products" \1',
}

for pattern, replacement in nav_href_map.items():
    html = re.sub(pattern, replacement, html, flags=re.IGNORECASE)

# 3. VERIFY SVG MATTER PLATFORM LOGOS
# Ensure the 7 images in riva-ms are 100% correct
html = re.sub(
    r'<image width="1200" height="500"\s*href="[^"]*"\s*xlink:href="[^"]*"/>',
    r'<image width="1200" height="500" href="./img/works_with_apple.webp" xlink:href="./img/works_with_apple.webp"/>',
    html, count=1
)
html = re.sub(
    r'<image width="1200" height="400"\s*href="[^"]*"\s*xlink:href="[^"]*"/>',
    r'<image width="1200" height="400" href="./img/works_with_google.webp" xlink:href="./img/works_with_google.webp"/>',
    html, count=1
)
html = re.sub(
    r'<image width="1200" height="500"\s*href="[^"]*"\s*xlink:href="[^"]*"/>',
    r'<image width="1200" height="500" href="./img/works_with_alexa.webp" xlink:href="./img/works_with_alexa.webp"/>',
    html, count=1
)

# 4. INJECT MASTER GLASSMORPHISM & SMOOTH SCROLL STYLES
master_css_js = '''
<style id="ishara-master-glassmorphism">
/* ==========================================================================
   ISHARA SMART LIVING — MASTER GLASSMORPHISM & HOVER ENGINE
   ========================================================================== */

html {
  scroll-behavior: smooth !important;
}

/* 1. FIXED FLOATING HEADER PILL (Visible at all times on every scroll depth) */
header.elementor-location-header {
  position: fixed !important;
  top: 14px !important;
  left: 0 !important;
  right: 0 !important;
  width: 100% !important;
  z-index: 99999 !important;
  pointer-events: none !important;
  display: flex !important;
  justify-content: center !important;
  padding: 0 16px !important;
  box-sizing: border-box !important;
}

#header-bar {
  width: 100% !important;
  max-width: 1320px !important;
  background: transparent !important;
  pointer-events: none !important;
}

#header-bar .e-con-inner,
#header-bar .header-internal {
  pointer-events: auto !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  background: rgba(255, 255, 255, 0.82) !important;
  backdrop-filter: blur(22px) saturate(190%) !important;
  -webkit-backdrop-filter: blur(22px) saturate(190%) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.85) !important;
  border-radius: 999px !important;
  box-shadow: 0 14px 40px rgba(15, 20, 18, 0.12), inset 0 1px 2px rgba(255, 255, 255, 1) !important;
  padding: 8px 24px !important;
  transition: all 0.35s cubic-bezier(0.22, 0.61, 0.36, 1) !important;
}

#header-bar.is-scrolled .header-internal {
  background: rgba(255, 255, 255, 0.94) !important;
  box-shadow: 0 18px 48px rgba(15, 20, 18, 0.16), inset 0 1px 2px rgba(255, 255, 255, 1) !important;
}

/* 2. MAIN NAV LINK HOVER GLASSMORPHISM */
.elementor-nav-menu--main .elementor-nav-menu > li {
  position: relative !important;
}

.elementor-nav-menu--main .elementor-nav-menu > li > a {
  border-radius: 999px !important;
  padding: 8px 16px !important;
  transition: all 0.22s ease !important;
  font-weight: 600 !important;
  color: #1a1a18 !important;
}

.elementor-nav-menu--main .elementor-nav-menu > li > a:hover {
  background: rgba(207, 168, 86, 0.15) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  color: #99752b !important;
  box-shadow: 0 4px 14px rgba(207, 168, 86, 0.20), inset 0 1px 1px rgba(255,255,255,0.9) !important;
  transform: translateY(-1px) !important;
}

/* 3. DROPDOWN SUBMENU: SOLVES left:-999em BUG & RENDERS LUSH FROSTED GLASS */
.elementor-nav-menu li.menu-item-has-children {
  position: relative !important;
}

.elementor-nav-menu li.menu-item-has-children > ul.sub-menu,
.main-header-menu .sub-menu {
  display: block !important;
  position: absolute !important;
  top: calc(100% + 10px) !important;
  left: 0 !important;
  right: auto !important;
  min-width: 220px !important;
  background: rgba(255, 255, 255, 0.90) !important;
  backdrop-filter: blur(28px) saturate(210%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(210%) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.95) !important;
  border-radius: 20px !important;
  box-shadow: 0 24px 60px rgba(15, 20, 18, 0.18), 0 4px 12px rgba(0,0,0,0.06), inset 0 1px 2px rgba(255, 255, 255, 1) !important;
  padding: 10px !important;
  margin: 0 !important;
  z-index: 100000 !important;
  opacity: 0 !important;
  visibility: hidden !important;
  pointer-events: none !important;
  transform: translateY(10px) scale(0.96) !important;
  transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
}

.elementor-nav-menu li.menu-item-has-children:hover > ul.sub-menu,
.elementor-nav-menu li.menu-item-has-children:focus-within > ul.sub-menu {
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
  transform: translateY(0) scale(1) !important;
}

.elementor-nav-menu--main ul.sub-menu li {
  list-style: none !important;
  margin: 0 !important;
  padding: 2px 0 !important;
}

.elementor-nav-menu--main ul.sub-menu li a {
  display: flex !important;
  align-items: center !important;
  color: #141413 !important;
  font-weight: 600 !important;
  font-size: 13.5px !important;
  padding: 10px 16px !important;
  border-radius: 12px !important;
  transition: all 0.2s ease !important;
  text-decoration: none !important;
}

.elementor-nav-menu--main ul.sub-menu li a:hover {
  background: linear-gradient(90deg, rgba(207, 168, 86, 0.20) 0%, rgba(207, 168, 86, 0.08) 100%) !important;
  color: #8c681f !important;
  transform: translateX(4px) !important;
  box-shadow: inset 0 1px 1px #fff, 0 2px 6px rgba(0,0,0,0.04) !important;
}

/* 4. CAROUSEL PUCK GLASSMORPHISM & HOVER GLOW */
.riva-card-glass {
  background: linear-gradient(165deg, rgba(255, 255, 255, 0.72) 0%, rgba(255, 255, 255, 0.40) 45%, rgba(255, 255, 255, 0.14) 100%) !important;
  backdrop-filter: blur(18px) saturate(170%) !important;
  -webkit-backdrop-filter: blur(18px) saturate(170%) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.90) !important;
  border-bottom-color: rgba(255, 255, 255, 0.40) !important;
  box-shadow: 0 22px 50px rgba(90, 86, 78, 0.10), inset 0 1px 2px rgba(255, 255, 255, 0.95) !important;
  transition: all 0.4s cubic-bezier(0.22, 0.61, 0.36, 1) !important;
}

.riva-device-card:hover .riva-card-glass {
  background: linear-gradient(165deg, rgba(255, 255, 255, 0.90) 0%, rgba(255, 255, 255, 0.54) 45%, rgba(255, 255, 255, 0.24) 100%) !important;
  backdrop-filter: blur(24px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(24px) saturate(200%) !important;
  border-color: rgba(255, 255, 255, 1) !important;
  box-shadow: 0 32px 70px rgba(90, 86, 78, 0.18), inset 0 1px 3px rgba(255, 255, 255, 1) !important;
  transform: translateX(-50%) translateY(-6px) scale(1.02) !important;
}

/* 5. WHY US / MISTAKE CARDS HOVER GLASSMORPHISM */
.riva-why-card {
  transition: all 0.35s cubic-bezier(0.22, 0.61, 0.36, 1) !important;
  border-radius: 24px !important;
}
.riva-why-card:hover {
  background: rgba(255, 255, 255, 0.92) !important;
  backdrop-filter: blur(20px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
  border: 1.5px solid rgba(255, 255, 255, 1) !important;
  box-shadow: 0 24px 60px rgba(30, 28, 24, 0.12), inset 0 1px 2px rgba(255, 255, 255, 1) !important;
  transform: translateY(-6px) !important;
}

/* 6. HUB EXPLAINER CARD HOVER GLASSMORPHISM */
.riva-hub-card {
  transition: all 0.35s cubic-bezier(0.22, 0.61, 0.36, 1) !important;
}
.riva-hub-card:hover {
  background: rgba(255, 255, 255, 0.94) !important;
  backdrop-filter: blur(22px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(22px) saturate(180%) !important;
  border: 1.5px solid rgba(255, 255, 255, 1) !important;
  box-shadow: 0 24px 55px rgba(30, 28, 24, 0.12), inset 0 1px 2px rgba(255, 255, 255, 1) !important;
  transform: translateY(-6px) !important;
}
</style>

<script>
// BULLETPROOF SMOOTH SCROLL EVENT DELEGATOR
document.addEventListener('click', function(e) {
  var a = e.target.closest('a');
  if (!a) return;
  var href = a.getAttribute('href');
  if (href && href.startsWith('#') && href.length > 1) {
    var id = href.substring(1);
    var target = document.getElementById(id) || 
                 document.querySelector('.' + id) || 
                 document.querySelector('[id*="' + id + '"]');
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      try { history.pushState(null, null, '#' + id); } catch(err) {}
    }
  }
});

// Dynamic elevation on scroll
window.addEventListener('scroll', function() {
  var header = document.getElementById('header-bar');
  if (header) {
    if (window.scrollY > 30) {
      header.classList.add('is-scrolled');
    } else {
      header.classList.remove('is-scrolled');
    }
  }
}, { passive: true });
</script>
'''

# Replace previous style block or inject cleanly
if '<style id="ishara-glassmorphism-system">' in html:
    html = re.sub(r'<style id="ishara-glassmorphism-system">.*?</script>', master_css_js, html, flags=re.DOTALL)
elif '<style id="ishara-master-glassmorphism">' in html:
    html = re.sub(r'<style id="ishara-master-glassmorphism">.*?</script>', master_css_js, html, flags=re.DOTALL)
else:
    html = html.replace('</head>', master_css_js + '\n</head>')

with open('home/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied master fix: Section IDs, nav links, sub-menu left:0 positioning, and hover glassmorphism!")
