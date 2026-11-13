import re

with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# 1. Favicon with official logo
favicon_tag = '<link rel="icon" type="image/png" href="./img/ishara-logo.png">'
if '<head>' in html:
    html = html.replace('<head>', '<head>\n' + favicon_tag)

# 2. Update Header Logo to use the official uploaded logo
# Let's inspect the header logo area and replace it cleanly
header_logo_replacement = '''<a href="#riva-house" style="display:inline-flex;align-items:center;gap:12px;text-decoration:none;">
  <img src="./img/ishara-logo-trans.png" alt="Ishara Smart Living" style="height:46px;width:46px;object-fit:contain;filter:drop-shadow(0 2px 6px rgba(0,0,0,0.12));">
  <span style="display:flex;flex-direction:column;text-align:left;">
    <span style="font-family:'Poppins',sans-serif;font-weight:700;font-size:18px;letter-spacing:-0.01em;color:#141413;line-height:1.15;">ISHARA <span style="color:#cfa856;font-weight:600;">SMART LIVING</span></span>
    <span style="font-family:'Open Sans',sans-serif;font-size:9.5px;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;color:#77736c;">Modern Living Made Simple</span>
  </span>
</a>'''

html = re.sub(
    r'<div class="elementor-element elementor-element-bf719e8 elementor-widget elementor-widget-image"[^>]*>.*?</div>\s*</div>',
    f'<div class="elementor-element elementor-element-bf719e8 elementor-widget elementor-widget-image" data-id="bf719e8" data-element_type="widget" data-widget_type="image.default">{header_logo_replacement}</div></div>',
    html,
    flags=re.DOTALL
)

# 3. Update Footer Logo to use the official uploaded logo
footer_logo_replacement = '''<a href="#riva-house" style="display:inline-flex;align-items:center;gap:14px;text-decoration:none;">
  <img src="./img/ishara-logo-trans.png" alt="Ishara Smart Living" style="height:56px;width:56px;object-fit:contain;filter:drop-shadow(0 2px 8px rgba(0,0,0,0.15));">
  <span style="display:flex;flex-direction:column;text-align:left;">
    <span style="font-family:'Poppins',sans-serif;font-weight:700;font-size:22px;letter-spacing:-0.01em;color:#141413;line-height:1.15;">ISHARA <span style="color:#cfa856;font-weight:600;">SMART LIVING</span></span>
    <span style="font-family:'Open Sans',sans-serif;font-size:11px;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;color:#77736c;">Modern Living Made Simple</span>
  </span>
</a>'''

html = re.sub(
    r'<div class="elementor-element elementor-element-381758e elementor-widget elementor-widget-theme-site-logo elementor-widget-image"[^>]*>.*?</div>',
    f'<div class="elementor-element elementor-element-381758e elementor-widget elementor-widget-theme-site-logo elementor-widget-image" data-id="381758e" data-element_type="widget" data-widget_type="theme-site-logo.default">{footer_logo_replacement}</div>',
    html,
    flags=re.DOTALL
)

# 4. FIX ALL NAV LINKS (Header menu and mobile menu)
link_replacements = {
    'https://rivasmart.com/matter-smart-home-protocol/': '#riva-matter-scroll',
    'https://rivasmart.com/matter-smart-home-protocol': '#riva-matter-scroll',
    'https://rivasmart.com/solutions/residential/': '#riva-works-section',
    'https://rivasmart.com/solutions/commercial/': '#riva-hub-section',
    'https://rivasmart.com/solutions/': '#riva-works-section',
    'https://rivasmart.com/solutions': '#riva-works-section',
    'https://rivasmart.com/about/': '#riva-why-section',
    'https://rivasmart.com/about': '#riva-why-section',
    'https://rivasmart.com/products/': '#riva-device-showcase',
    'https://rivasmart.com/products': '#riva-device-showcase',
    'https://rivasmart.com/products/smartcameras/': '#riva-device-showcase',
    'https://rivasmart.com/products/smartcontrollers/': '#riva-device-showcase',
    'https://rivasmart.com/products/smartcurtains/': '#riva-device-showcase',
    'https://rivasmart.com/products/smartdoorlocks/': '#riva-device-showcase',
    'https://rivasmart.com/products/smarthubs/': '#riva-device-showcase',
    'https://rivasmart.com/products/smartlighting/': '#riva-device-showcase',
    'https://rivasmart.com/products/smartsensors/': '#riva-device-showcase',
    'https://rivasmart.com/products/smartspeakers/': '#riva-device-showcase',
    'https://rivasmart.com/brands/': '#riva-compatibility',
    'https://rivasmart.com/brands': '#riva-compatibility',
    'https://rivasmart.com/brands/aqara/': '#riva-compatibility',
    'https://rivasmart.com/brands/sonos/': '#riva-compatibility',
    'https://rivasmart.com/brands/homey/': '#riva-compatibility',
    'https://rivasmart.com/brands/hikvision/': '#riva-compatibility',
    'https://rivasmart.com/brands/dahua/': '#riva-compatibility',
    'https://rivasmart.com/brands/ubiquiti/': '#riva-compatibility',
    'https://rivasmart.com/brands/yealink/': '#riva-compatibility',
    'https://rivasmart.com/brands/mx-mdr/': '#riva-compatibility',
    'https://rivasmart.com/brands/rivasmart/': '#riva-compatibility',
    'https://rivasmart.com/dealership/': 'https://wa.me/919380792471?text=Hi%20Ishara%20Smart%20Living,%20I%20would%20like%20to%20inquire%20about%20dealership%20and%20experience%20centres.',
    'https://rivasmart.com/dealership': 'https://wa.me/919380792471?text=Hi%20Ishara%20Smart%20Living,%20I%20would%20like%20to%20inquire%20about%20dealership%20and%20experience%20centres.',
    'https://rivasmart.com/contact/': 'https://wa.me/919380792471?text=Hi%20Ishara%20Smart%20Living,%20I%20would%20like%20to%20get%20a%20free%20consultation%20and%20quote.',
    'https://rivasmart.com/contact': 'https://wa.me/919380792471?text=Hi%20Ishara%20Smart%20Living,%20I%20would%20like%20to%20get%20a%20free%20consultation%20and%20quote.',
    'https://rivasmart.com/experience-centre/': 'https://wa.me/919380792471?text=Hi%20Ishara%20Smart%20Living,%20I%20want%20to%20visit%20your%20experience%20centre%20in%20Bangalore%20or%20Shivamogga.',
    'https://rivasmart.com/experience-centre': 'https://wa.me/919380792471?text=Hi%20Ishara%20Smart%20Living,%20I%20want%20to%20visit%20your%20experience%20centre%20in%20Bangalore%20or%20Shivamogga.',
    'https://rivasmart.com/smart-home-automation-india/': '#rivaSig',
    'https://rivasmart.com/smart-home-automation-india': '#rivaSig',
    'https://rivasmart.com/blogs/': '#riva-why-section',
    'https://rivasmart.com/privacy-policy/': '#',
    'https://rivasmart.com/terms-of-use/': '#',
    'https://rivasmart.com/': '#riva-house',
    'https://rivasmart.com': '#riva-house',
}

for old_link, new_link in link_replacements.items():
    html = html.replace(f'href="{old_link}"', f'href="{new_link}"')

# Also catch any remaining /products/... or rivasmart.com links in href
html = re.sub(r'href="https://rivasmart\.com/products/[^"]*"', 'href="#riva-device-showcase"', html)
html = re.sub(r'href="https://rivasmart\.com/[^"]*"', 'href="#riva-house"', html)
print("Replaced all rivasmart.com navigation links!")

# 5. INJECT COMPREHENSIVE GLASSMORPHISM & SMOOTH SCROLL STYLES
glassmorphism_css = '''
<style id="ishara-glassmorphism-system">
/* ==========================================================================
   ISHARA SMART LIVING — PREMIUM GLASSMORPHISM DESIGN SYSTEM
   ========================================================================== */

/* Smooth page scrolling for anchor navigation */
html {
  scroll-behavior: smooth !important;
}

/* 1. STICKY HEADER GLASSMORPHISM (Always active & lush) */
#header-bar {
  position: sticky !important;
  top: 12px !important;
  z-index: 9999 !important;
  padding: 0 16px !important;
}

#header-bar .header-internal {
  background: rgba(255, 255, 255, 0.76) !important;
  backdrop-filter: blur(20px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
  border: 1px solid rgba(255, 255, 255, 0.70) !important;
  border-radius: 999px !important;
  box-shadow: 0 10px 32px rgba(20, 20, 18, 0.08), inset 0 1px 2px rgba(255, 255, 255, 0.9) !important;
  padding: 10px 28px !important;
  transition: all 0.35s cubic-bezier(0.22, 0.61, 0.36, 1) !important;
}

#header-bar.is-scrolled .header-internal {
  background: rgba(255, 255, 255, 0.88) !important;
  box-shadow: 0 16px 40px rgba(20, 20, 18, 0.12), inset 0 1px 2px rgba(255, 255, 255, 1) !important;
}

/* 2. SUBMENU & DROPDOWN GLASSMORPHISM ON HOVER */
.elementor-nav-menu--main ul.sub-menu,
.elementor-nav-menu--dropdown {
  background: rgba(255, 255, 255, 0.86) !important;
  backdrop-filter: blur(24px) saturate(190%) !important;
  -webkit-backdrop-filter: blur(24px) saturate(190%) !important;
  border: 1px solid rgba(255, 255, 255, 0.85) !important;
  border-radius: 18px !important;
  box-shadow: 0 20px 50px rgba(20, 20, 18, 0.14) !important;
  overflow: hidden !important;
  padding: 8px 0 !important;
  margin-top: 8px !important;
}

.elementor-nav-menu--main ul.sub-menu li a,
.elementor-nav-menu--dropdown li a {
  color: #141413 !important;
  font-weight: 500 !important;
  padding: 10px 22px !important;
  transition: background 0.2s ease, color 0.2s ease, transform 0.2s ease !important;
}

.elementor-nav-menu--main ul.sub-menu li a:hover,
.elementor-nav-menu--dropdown li a:hover {
  background: rgba(207, 168, 86, 0.12) !important;
  color: #111111 !important;
  transform: translateX(4px) !important;
}

/* 3. DEVICE SHOWCASE GLASS PUCKS */
.riva-card-glass {
  background: linear-gradient(165deg, rgba(255, 255, 255, 0.65) 0%, rgba(255, 255, 255, 0.35) 45%, rgba(255, 255, 255, 0.10) 100%) !important;
  backdrop-filter: blur(16px) saturate(160%) !important;
  -webkit-backdrop-filter: blur(16px) saturate(160%) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.85) !important;
  border-bottom-color: rgba(255, 255, 255, 0.35) !important;
  box-shadow: 0 20px 45px rgba(90, 86, 78, 0.08), inset 0 1px 2px rgba(255, 255, 255, 0.9) !important;
}

.riva-device-card:hover .riva-card-glass {
  background: linear-gradient(165deg, rgba(255, 255, 255, 0.82) 0%, rgba(255, 255, 255, 0.48) 45%, rgba(255, 255, 255, 0.18) 100%) !important;
  backdrop-filter: blur(20px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(180%) !important;
  box-shadow: 0 30px 65px rgba(90, 86, 78, 0.14), inset 0 1px 3px rgba(255, 255, 255, 1) !important;
}

/* 4. PHOTO-HOUSE PANELS & STATUS PILL GLASS */
.riva-ph-status {
  background: rgba(15, 15, 14, 0.65) !important;
  backdrop-filter: blur(14px) saturate(140%) !important;
  -webkit-backdrop-filter: blur(14px) saturate(140%) !important;
  border: 1px solid rgba(255, 255, 255, 0.25) !important;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25) !important;
}

.riva-ph-tag {
  background: rgba(15, 15, 14, 0.52) !important;
  backdrop-filter: blur(10px) !important;
  -webkit-backdrop-filter: blur(10px) !important;
  border: 1px solid rgba(255, 255, 255, 0.20) !important;
}

.riva-ph-panel, .riva-ph-voice {
  background: linear-gradient(170deg, rgba(251, 250, 249, 0.88) 0%, rgba(244, 242, 238, 0.78) 100%) !important;
  backdrop-filter: blur(18px) saturate(160%) !important;
  -webkit-backdrop-filter: blur(18px) saturate(160%) !important;
  border: 1px solid rgba(255, 255, 255, 0.90) !important;
  box-shadow: 0 16px 40px rgba(30, 28, 24, 0.06), inset 0 1px 2px rgba(255, 255, 255, 0.85) !important;
}

/* 5. DIMMER CALCULATOR CONTROLS GLASS */
.riva-dim-controls {
  background: linear-gradient(170deg, rgba(251, 250, 249, 0.90) 0%, rgba(244, 242, 238, 0.80) 100%) !important;
  backdrop-filter: blur(16px) saturate(160%) !important;
  -webkit-backdrop-filter: blur(16px) saturate(160%) !important;
  border: 1px solid rgba(255, 255, 255, 0.90) !important;
  box-shadow: 0 16px 40px rgba(30, 28, 24, 0.06), inset 0 1px 2px rgba(255, 255, 255, 0.85) !important;
  border-radius: 24px !important;
}

.riva-dim-badge {
  background: rgba(15, 15, 14, 0.65) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
}

/* 6. HUB EXPLAINER CARD GLASS */
.riva-hub-card {
  background: linear-gradient(170deg, rgba(251, 250, 249, 0.85) 0%, rgba(244, 242, 238, 0.72) 100%) !important;
  backdrop-filter: blur(14px) saturate(150%) !important;
  -webkit-backdrop-filter: blur(14px) saturate(150%) !important;
  border: 1px solid rgba(255, 255, 255, 0.85) !important;
  box-shadow: 0 14px 34px rgba(30, 28, 24, 0.06) !important;
}

/* 7. FLOATING WHATSAPP BUTTON GLASS & GLOW */
.elementor-social-icon-whatsapp {
  box-shadow: 0 8px 26px rgba(37, 211, 102, 0.45) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  transition: transform 0.35s cubic-bezier(0.34, 1.4, 0.5, 1), box-shadow 0.35s ease !important;
}
.elementor-social-icon-whatsapp:hover {
  transform: scale(1.12) translateY(-3px) !important;
  box-shadow: 0 14px 34px rgba(37, 211, 102, 0.60) !important;
}
</style>

<script>
// Sticky header dynamic scroll state
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

if '</head>' in html:
    html = html.replace('</head>', glassmorphism_css + '\n</head>')

with open('home/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied official logo, removed all external riva links, and added glassmorphism!")
