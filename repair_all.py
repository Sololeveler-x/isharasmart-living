import re

with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# =========================================================================
# 1. FIX MATTER DIAGRAM SVG <image> TAGS (Restore broken logos from Screenshot 1)
# =========================================================================
# In raw/home.html:
# works_with_apple.webp, works_with_google.webp, works_with_alexa.webp,
# works_with_home_assistant.webp, works_with_smartthings.webp, works_with_homey.webp, matter.png

svg_images_replacement = {
    'works_with_apple': './img/works_with_apple.webp',
    'works_with_google': './img/works_with_google.webp',
    'works_with_alexa': './img/works_with_alexa.webp',
    'works_with_home_assistant': './img/works_with_home_assistant.webp',
    'works_with_smartthings': './img/works_with_smartthings.webp',
    'works_with_homey': './img/works_with_homey.webp',
}

# In riva-ms, find all <image ... href="#riva-house" ...> and replace with the real platform logos in order
ms_start = html.find('class="riva-ms"')
ms_end = html.find('</section>', ms_start) if ms_start != -1 else -1

if ms_start != -1 and ms_end != -1:
    ms_section = html[ms_start:ms_end]
    
    # Replace the 6 node images and 1 center image
    # Order in raw:
    # 1. Apple (height 500)
    # 2. Google (height 400)
    # 3. Alexa (height 500)
    # 4. Home Assistant (height 480)
    # 5. SmartThings (height 396)
    # 6. Homey (height 506)
    # 7. Matter (x="452" y="252")
    
    ms_section_new = ms_section
    ms_section_new = re.sub(
        r'<image width="1200" height="500"\s*href="[^"]*"\s*xlink:href="[^"]*"/>',
        r'<image width="1200" height="500" href="./img/works_with_apple.webp" xlink:href="./img/works_with_apple.webp"/>',
        ms_section_new, count=1
    )
    ms_section_new = re.sub(
        r'<image width="1200" height="400"\s*href="[^"]*"\s*xlink:href="[^"]*"/>',
        r'<image width="1200" height="400" href="./img/works_with_google.webp" xlink:href="./img/works_with_google.webp"/>',
        ms_section_new, count=1
    )
    ms_section_new = re.sub(
        r'<image width="1200" height="500"\s*href="[^"]*"\s*xlink:href="[^"]*"/>',
        r'<image width="1200" height="500" href="./img/works_with_alexa.webp" xlink:href="./img/works_with_alexa.webp"/>',
        ms_section_new, count=1
    )
    ms_section_new = re.sub(
        r'<image width="1200" height="480"\s*href="[^"]*"\s*xlink:href="[^"]*"/>',
        r'<image width="1200" height="480" href="./img/works_with_home_assistant.webp" xlink:href="./img/works_with_home_assistant.webp"/>',
        ms_section_new, count=1
    )
    ms_section_new = re.sub(
        r'<image width="1072" height="396"\s*href="[^"]*"\s*xlink:href="[^"]*"/>',
        r'<image width="1072" height="396" href="./img/works_with_smartthings.webp" xlink:href="./img/works_with_smartthings.webp"/>',
        ms_section_new, count=1
    )
    ms_section_new = re.sub(
        r'<image width="1200" height="506"\s*href="[^"]*"\s*xlink:href="[^"]*"/>',
        r'<image width="1200" height="506" href="./img/works_with_homey.webp" xlink:href="./img/works_with_homey.webp"/>',
        ms_section_new, count=1
    )
    ms_section_new = re.sub(
        r'<image x="452" y="252"[^>]*href="[^"]*"[^>]*/>',
        r'<image x="452" y="252" width="96" height="42" preserveAspectRatio="xMidYMid meet" href="./img/matter-logo.png" xlink:href="./img/matter-logo.png"/>',
        ms_section_new, count=1
    )
    
    html = html[:ms_start] + ms_section_new + html[ms_end:]
    print("Fixed Matter diagram SVG platform logo images!")

# =========================================================================
# 2. ADD EXPLICIT IDs TO ALL SECTIONS FOR DIRECT SMOOTH SCROLLING
# =========================================================================
# Replace section tags with explicit IDs
html = html.replace('<section class="riva-hero">', '<section class="riva-hero" id="hero">')
html = html.replace('<section class="riva-works-section">', '<section class="riva-works-section" id="solutions">')
html = html.replace('<section class="riva-works-section riva-anim">', '<section class="riva-works-section riva-anim" id="solutions">')
html = html.replace('<section class="riva-hub-section">', '<section class="riva-hub-section" id="riva-hub-section">')
html = html.replace('<section class="riva-hub-section riva-anim">', '<section class="riva-hub-section riva-anim" id="riva-hub-section">')
html = html.replace('<section class="riva-why-section">', '<section class="riva-why-section" id="about">')
html = html.replace('<section class="riva-why-section riva-anim">', '<section class="riva-why-section riva-anim" id="about">')
html = html.replace('<section class="riva-dim-section">', '<section class="riva-dim-section" id="dimmer">')
html = html.replace('<section class="riva-dim-section riva-anim">', '<section class="riva-dim-section riva-anim" id="dimmer">')
html = html.replace('<section class="riva-compatibility">', '<section class="riva-compatibility" id="brands">')
html = html.replace('<section class="riva-compatibility riva-anim">', '<section class="riva-compatibility riva-anim" id="brands">')
html = html.replace('<section class="riva-cta-section">', '<section class="riva-cta-section" id="contact">')
html = html.replace('<section class="riva-cta-section riva-anim">', '<section class="riva-cta-section riva-anim" id="contact">')

print("Assigned IDs: #solutions, #about, #brands, #contact, #dimmer to sections!")

# =========================================================================
# 3. FIX NAVIGATION MENU LINKS TO EXACT SECTION IDs
# =========================================================================
html = re.sub(r'href="[^"]*"\s*class="elementor-item[^"]*">Solutions', 'href="#solutions" class="elementor-item menu-link">Solutions', html)
html = re.sub(r'href="[^"]*"\s*class="elementor-item[^"]*">About', 'href="#about" class="elementor-item menu-link">About', html)
html = re.sub(r'href="[^"]*"\s*class="elementor-item[^"]*">Matter', 'href="#riva-matter-scroll" class="elementor-item menu-link">Matter', html)
html = re.sub(r'href="[^"]*"\s*class="elementor-item[^"]*">Products', 'href="#riva-device-showcase" class="elementor-item menu-link">Products', html)
html = re.sub(r'href="[^"]*"\s*class="elementor-item[^"]*">Brands', 'href="#brands" class="elementor-item menu-link">Brands', html)

# Submenu links
html = re.sub(r'href="[^"]*"\s*class="elementor-sub-item[^"]*">Residential', 'href="#solutions" class="elementor-sub-item menu-link">Residential', html)
html = re.sub(r'href="[^"]*"\s*class="elementor-sub-item[^"]*">Commercial', 'href="#riva-hub-section" class="elementor-sub-item menu-link">Commercial', html)

# =========================================================================
# 4. FIX HERO COPY: REPLACE REMAINING BENGALURU WITH FLYER DETAILS
# =========================================================================
html = html.replace(
    'BANGALORE & SHIVAMOGGA SHOWROOMS - BENGALURU',
    'BANGALORE | SHIVAMOGGA &amp; ALL KARNATAKA'
)
html = html.replace(
    'BANGALORE & SHIVAMOGGA SHOWROOMS – BENGALURU',
    'BANGALORE | SHIVAMOGGA &amp; ALL KARNATAKA'
)
html = html.replace(
    'BANGALORE & SHIVAMOGGA SHOWROOMS — BENGALURU',
    'BANGALORE | SHIVAMOGGA &amp; ALL KARNATAKA'
)
html = html.replace(
    'Matter smart home\nautomation in\nBengaluru.',
    'Complete Matter smart\nhome automation in\nKarnataka.'
)
html = html.replace(
    'Matter smart home automation in Bengaluru.',
    'Complete Matter smart home automation in Karnataka.'
)
html = html.replace(
    'across Bengaluru\n(Bangalore)',
    'across Bangalore, Shivamogga & all Karnataka'
)
html = html.replace(
    'across Bengaluru (Bangalore)',
    'across Bangalore, Shivamogga & all Karnataka'
)

# =========================================================================
# 5. UPGRADE GLASSMORPHISM TO TRUE FIXED FLOATING PILL (VISIBLE AT ALL TIMES)
# =========================================================================
# Replace old glassmorphism style block with comprehensive, bulletproof styles
updated_glass_css = '''
<style id="ishara-glassmorphism-system">
/* ==========================================================================
   ISHARA SMART LIVING — BULLETPROOF GLASSMORPHISM SYSTEM
   ========================================================================== */

html {
  scroll-behavior: smooth !important;
}

/* 1. TOP UTILITY BAR (Fixed above header on load, scrolls off cleanly) */
.ishara-top-bar {
  position: relative !important;
  z-index: 999999 !important;
  background: #0d1310 !important;
  border-bottom: 1px solid rgba(207, 168, 86, 0.3) !important;
}

/* 2. TRUE FLOATING STICKY HEADER PILL (Fixed viewport anchor, stays visible at all depths) */
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
  padding: 0 20px !important;
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
  backdrop-filter: blur(24px) saturate(200%) !important;
  -webkit-backdrop-filter: blur(24px) saturate(200%) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.85) !important;
  border-radius: 999px !important;
  box-shadow: 0 14px 40px rgba(15, 20, 18, 0.12), 0 2px 6px rgba(0, 0, 0, 0.04), inset 0 1px 2px rgba(255, 255, 255, 1) !important;
  padding: 8px 24px !important;
  transition: all 0.35s cubic-bezier(0.22, 0.61, 0.36, 1) !important;
}

#header-bar.is-scrolled .header-internal {
  background: rgba(255, 255, 255, 0.92) !important;
  box-shadow: 0 18px 48px rgba(15, 20, 18, 0.16), inset 0 1px 2px rgba(255, 255, 255, 1) !important;
}

/* 3. PURE CSS HOVER DROPDOWN SUBMENUS WITH GLOWING GLASSMORPHISM */
.elementor-nav-menu li.menu-item-has-children {
  position: relative !important;
}

.elementor-nav-menu li.menu-item-has-children > a {
  cursor: pointer !important;
}

.elementor-nav-menu li.menu-item-has-children:hover > ul.sub-menu,
.elementor-nav-menu li.menu-item-has-children:focus-within > ul.sub-menu {
  display: block !important;
  opacity: 1 !important;
  visibility: visible !important;
  pointer-events: auto !important;
  animation: isharaMenuPop 0.24s cubic-bezier(0.16, 1, 0.3, 1) forwards !important;
}

@keyframes isharaMenuPop {
  from {
    opacity: 0;
    transform: translateY(12px) scale(0.97);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.elementor-nav-menu--main ul.sub-menu,
.elementor-nav-menu--dropdown {
  position: absolute !important;
  top: 100% !important;
  left: 0 !important;
  min-width: 210px !important;
  background: rgba(255, 255, 255, 0.90) !important;
  backdrop-filter: blur(28px) saturate(210%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(210%) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.95) !important;
  border-radius: 20px !important;
  box-shadow: 0 24px 60px rgba(15, 20, 18, 0.16), 0 4px 12px rgba(0,0,0,0.06), inset 0 1px 2px rgba(255, 255, 255, 1) !important;
  padding: 8px !important;
  margin-top: 10px !important;
  z-index: 100000 !important;
}

.elementor-nav-menu--main ul.sub-menu li {
  list-style: none !important;
}

.elementor-nav-menu--main ul.sub-menu li a {
  display: block !important;
  color: #141413 !important;
  font-weight: 600 !important;
  font-size: 13.5px !important;
  padding: 10px 18px !important;
  border-radius: 12px !important;
  transition: all 0.2s ease !important;
  text-decoration: none !important;
}

.elementor-nav-menu--main ul.sub-menu li a:hover {
  background: linear-gradient(90deg, rgba(207, 168, 86, 0.16) 0%, rgba(207, 168, 86, 0.06) 100%) !important;
  color: #8c681f !important;
  transform: translateX(4px) !important;
}

/* 4. CAROUSEL GLASS PUCKS */
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
  background: linear-gradient(165deg, rgba(255, 255, 255, 0.88) 0%, rgba(255, 255, 255, 0.52) 45%, rgba(255, 255, 255, 0.22) 100%) !important;
  backdrop-filter: blur(24px) saturate(190%) !important;
  -webkit-backdrop-filter: blur(24px) saturate(190%) !important;
  border-color: rgba(255, 255, 255, 1) !important;
  box-shadow: 0 32px 70px rgba(90, 86, 78, 0.16), inset 0 1px 3px rgba(255, 255, 255, 1) !important;
  transform: translateX(-50%) translateY(-6px) scale(1.02) !important;
}

/* 5. PHOTO-HOUSE PANELS & STATUS PILL */
.riva-ph-status {
  background: rgba(15, 15, 14, 0.70) !important;
  backdrop-filter: blur(16px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(16px) saturate(150%) !important;
  border: 1px solid rgba(255, 255, 255, 0.30) !important;
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.30) !important;
}

.riva-ph-panel, .riva-ph-voice {
  background: linear-gradient(170deg, rgba(251, 250, 249, 0.90) 0%, rgba(244, 242, 238, 0.80) 100%) !important;
  backdrop-filter: blur(20px) saturate(170%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(170%) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.95) !important;
  box-shadow: 0 18px 45px rgba(30, 28, 24, 0.08), inset 0 1px 2px rgba(255, 255, 255, 0.90) !important;
}

/* 6. DIMMER CALCULATOR GLASS PANEL */
.riva-dim-controls {
  background: linear-gradient(170deg, rgba(251, 250, 249, 0.92) 0%, rgba(244, 242, 238, 0.82) 100%) !important;
  backdrop-filter: blur(20px) saturate(170%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(170%) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.95) !important;
  box-shadow: 0 20px 50px rgba(30, 28, 24, 0.08), inset 0 1px 2px rgba(255, 255, 255, 0.90) !important;
  border-radius: 26px !important;
}

/* 7. HUB EXPLAINER CARD GLASS */
.riva-hub-card {
  background: linear-gradient(170deg, rgba(251, 250, 249, 0.88) 0%, rgba(244, 242, 238, 0.76) 100%) !important;
  backdrop-filter: blur(16px) saturate(160%) !important;
  -webkit-backdrop-filter: blur(16px) saturate(160%) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.90) !important;
  box-shadow: 0 16px 40px rgba(30, 28, 24, 0.07) !important;
}

/* 8. FLOATING WHATSAPP PILL */
.elementor-social-icon-whatsapp {
  box-shadow: 0 10px 30px rgba(37, 211, 102, 0.45) !important;
  backdrop-filter: blur(10px) !important;
  -webkit-backdrop-filter: blur(10px) !important;
  transition: transform 0.35s cubic-bezier(0.34, 1.4, 0.5, 1), box-shadow 0.35s ease !important;
}
.elementor-social-icon-whatsapp:hover {
  transform: scale(1.15) translateY(-4px) !important;
  box-shadow: 0 16px 40px rgba(37, 211, 102, 0.65) !important;
}
</style>

<script>
// Smooth scroll event delegator for all internal anchor links
document.addEventListener('click', function(e) {
  var target = e.target.closest('a');
  if (!target) return;
  var href = target.getAttribute('href');
  if (href && href.startsWith('#') && href.length > 1) {
    var destId = href.substring(1);
    var dest = document.getElementById(destId) || document.querySelector('.' + destId);
    if (dest) {
      e.preventDefault();
      var headerOffset = 90;
      var elementPosition = dest.getBoundingClientRect().top;
      var offsetPosition = elementPosition + window.pageYOffset - headerOffset;
      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    }
  }
});

// Dynamic sticky header elevation on scroll
window.addEventListener('scroll', function() {
  var header = document.getElementById('header-bar');
  if (header) {
    if (window.scrollY > 40) {
      header.classList.add('is-scrolled');
    } else {
      header.classList.remove('is-scrolled');
    }
  }
}, { passive: true });
</script>
'''

# Replace old glassmorphism block
html = re.sub(r'<style id="ishara-glassmorphism-system">.*?</script>', updated_glass_css, html, flags=re.DOTALL)

with open('home/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Repaired Matter diagram images, assigned section IDs, made header fixed-floating, and added smooth scroll delegator!")
