import re

with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# 1. Update Header Logo markup: use clean icon mark + brand typography
header_logo_markup = '''<a href="#riva-house" style="display:inline-flex;align-items:center;gap:10px;text-decoration:none;flex-shrink:0;">
  <img src="./img/ishara-icon-trans.png" alt="Ishara Smart Living" style="height:38px;width:auto;object-fit:contain;filter:drop-shadow(0 2px 4px rgba(0,0,0,0.12));">
  <span style="display:flex;flex-direction:column;text-align:left;">
    <span style="font-family:'Poppins',sans-serif;font-weight:700;font-size:16px;letter-spacing:-0.01em;color:#141413;line-height:1.15;white-space:nowrap;">ISHARA <span style="color:#cfa856;font-weight:600;">SMART LIVING</span></span>
    <span style="font-family:'Open Sans',sans-serif;font-size:8.5px;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;color:#77736c;white-space:nowrap;">Modern Living Made Simple</span>
  </span>
</a>'''

html = re.sub(
    r'<div class="elementor-element elementor-element-bf719e8 elementor-widget elementor-widget-image"[^>]*>.*?</div>\s*</div>',
    f'<div class="elementor-element elementor-element-bf719e8 elementor-widget elementor-widget-image" data-id="bf719e8" data-element_type="widget" data-widget_type="image.default">{header_logo_markup}</div></div>',
    html,
    flags=re.DOTALL
)

# 2. Add WhatsApp CTA button right in the header for fast conversion
header_cta = '''<a href="https://wa.me/919380792471?text=Hi%20Ishara%20Smart%20Living,%20I%20would%20like%20to%20get%20a%20free%20consultation." target="_blank" class="header-glass-cta" style="display:inline-flex;align-items:center;gap:6px;padding:7px 16px;border-radius:999px;background:linear-gradient(135deg,rgba(207,168,86,0.25) 0%,rgba(207,168,86,0.10) 100%);border:1px solid rgba(207,168,86,0.45);color:#7d5c18;font-family:'Poppins',sans-serif;font-size:12px;font-weight:600;text-decoration:none;white-space:nowrap;transition:all 0.25s ease;">
  <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M12.031 2C6.502 2 2.012 6.48 2.012 12c0 2.19.71 4.22 1.91 5.88L2 22.25l4.52-1.89c1.6 1.02 3.49 1.64 5.51 1.64 5.53 0 10.02-4.48 10.02-10S17.56 2 12.03 2z"/></svg>
  <span>Get Quote</span>
</a>'''

# 3. Master Glassmorphism & Header Layout CSS
true_glassmorphism_css = '''
<style id="ishara-true-glassmorphism">
/* ==========================================================================
   ISHARA SMART LIVING — OPTICALLY AUTHENTIC FROSTED GLASS SYSTEM
   ========================================================================== */

html {
  scroll-behavior: smooth !important;
}

/* Ensure Photo House has breathing room under the fixed header */
.riva-ph-section {
  padding-top: 110px !important;
  background: linear-gradient(180deg, #f8f6f0 0%, #ffffff 320px) !important;
}

/* 1. FIXED FLOATING HEADER PILL (True 40% Frosted Glassmorphism) */
header.elementor-location-header {
  position: fixed !important;
  top: 12px !important;
  left: 0 !important;
  right: 0 !important;
  width: 100% !important;
  z-index: 999999 !important;
  pointer-events: none !important;
  display: flex !important;
  justify-content: center !important;
  padding: 0 16px !important;
  box-sizing: border-box !important;
}

#header-bar {
  width: 100% !important;
  max-width: 1280px !important;
  background: transparent !important;
  pointer-events: none !important;
}

#header-bar .e-con-inner {
  max-width: 100% !important;
  padding: 0 !important;
}

#header-bar .header-internal {
  pointer-events: auto !important;
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: nowrap !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 16px !important;
  height: 58px !important;
  max-height: 58px !important;
  /* 38% TRANSLUCENT FROSTED GLASS */
  background: rgba(255, 255, 255, 0.38) !important;
  backdrop-filter: blur(20px) saturate(190%) contrast(92%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(190%) contrast(92%) !important;
  border: 1px solid rgba(255, 255, 255, 0.65) !important;
  border-top: 1.5px solid rgba(255, 255, 255, 0.95) !important;
  border-radius: 999px !important;
  box-shadow: 0 16px 42px rgba(15, 20, 18, 0.09), 
              0 2px 6px rgba(0, 0, 0, 0.03), 
              inset 0 1px 1px rgba(255, 255, 255, 1),
              inset 0 -1px 1px rgba(255, 255, 255, 0.4) !important;
  padding: 0 20px !important;
  transition: all 0.35s cubic-bezier(0.22, 0.61, 0.36, 1) !important;
}

#header-bar.is-scrolled .header-internal {
  background: rgba(255, 255, 255, 0.58) !important;
  box-shadow: 0 20px 50px rgba(15, 20, 18, 0.14), inset 0 1px 2px rgba(255, 255, 255, 1) !important;
}

/* Prevent nav menu from wrapping into two lines */
.elementor-element.elementor-element-aad36e5 {
  flex: 1 1 auto !important;
  display: flex !important;
  justify-content: center !important;
}

.elementor-nav-menu--main {
  width: auto !important;
}

.elementor-nav-menu--main .elementor-nav-menu {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: nowrap !important;
  align-items: center !important;
  gap: 2px !important;
  margin: 0 !important;
  padding: 0 !important;
}

.elementor-nav-menu--main .elementor-nav-menu > li {
  position: relative !important;
  white-space: nowrap !important;
}

.elementor-nav-menu--main .elementor-nav-menu > li > a {
  border-radius: 999px !important;
  padding: 7px 13px !important;
  font-size: 13.5px !important;
  font-weight: 600 !important;
  color: #1a1a18 !important;
  white-space: nowrap !important;
  transition: all 0.22s ease !important;
  text-decoration: none !important;
}

.elementor-nav-menu--main .elementor-nav-menu > li > a:hover {
  background: rgba(255, 255, 255, 0.65) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  color: #8c681f !important;
  box-shadow: 0 3px 12px rgba(0,0,0,0.06), inset 0 1px 1px #fff !important;
  transform: translateY(-1px) !important;
}

/* 2. DROPDOWN SUBMENU (Frosted Glass Container with 55% Opacity) */
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
  min-width: 210px !important;
  background: rgba(255, 255, 255, 0.55) !important;
  backdrop-filter: blur(28px) saturate(220%) contrast(92%) !important;
  -webkit-backdrop-filter: blur(28px) saturate(220%) contrast(92%) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.85) !important;
  border-radius: 18px !important;
  box-shadow: 0 24px 60px rgba(15, 20, 18, 0.16), 0 4px 12px rgba(0,0,0,0.06), inset 0 1.5px 2px rgba(255, 255, 255, 1) !important;
  padding: 8px !important;
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
  padding: 9px 15px !important;
  border-radius: 12px !important;
  transition: all 0.2s ease !important;
  text-decoration: none !important;
}

.elementor-nav-menu--main ul.sub-menu li a:hover {
  background: rgba(207, 168, 86, 0.18) !important;
  color: #7d5c18 !important;
  transform: translateX(4px) !important;
  box-shadow: inset 0 1px 1px #fff, 0 2px 6px rgba(0,0,0,0.04) !important;
}

/* 3. CAROUSEL PUCK GLASSMORPHISM */
.riva-card-glass {
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.45) 0%, rgba(255, 255, 255, 0.20) 45%, rgba(255, 255, 255, 0.08) 100%) !important;
  backdrop-filter: blur(20px) saturate(180%) contrast(92%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(180%) contrast(92%) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.85) !important;
  border-bottom-color: rgba(255, 255, 255, 0.35) !important;
  box-shadow: 0 24px 50px rgba(90, 86, 78, 0.10), inset 0 1.5px 2px rgba(255, 255, 255, 0.95) !important;
  transition: all 0.4s cubic-bezier(0.22, 0.61, 0.36, 1) !important;
}

.riva-device-card:hover .riva-card-glass {
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.65) 0%, rgba(255, 255, 255, 0.35) 45%, rgba(255, 255, 255, 0.15) 100%) !important;
  backdrop-filter: blur(26px) saturate(210%) !important;
  -webkit-backdrop-filter: blur(26px) saturate(210%) !important;
  border-color: rgba(255, 255, 255, 1) !important;
  box-shadow: 0 32px 70px rgba(90, 86, 78, 0.16), inset 0 2px 4px rgba(255, 255, 255, 1) !important;
  transform: translateX(-50%) translateY(-8px) scale(1.03) !important;
}

/* 4. PHOTO HOUSE PANELS (Translucent Glass with 55% Opacity) */
.riva-ph-panel, .riva-ph-voice {
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.60) 0%, rgba(246, 243, 237, 0.40) 100%) !important;
  backdrop-filter: blur(20px) saturate(180%) contrast(92%) !important;
  -webkit-backdrop-filter: blur(20px) saturate(180%) contrast(92%) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.85) !important;
  box-shadow: 0 18px 45px rgba(30, 28, 24, 0.08), inset 0 1.5px 2px rgba(255, 255, 255, 0.95) !important;
}

.riva-ph-status {
  background: rgba(15, 15, 14, 0.60) !important;
  backdrop-filter: blur(16px) saturate(160%) !important;
  -webkit-backdrop-filter: blur(16px) saturate(160%) !important;
  border: 1px solid rgba(255, 255, 255, 0.30) !important;
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.30) !important;
}

/* 5. DIMMER CALCULATOR GLASS */
.riva-dim-controls {
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.60) 0%, rgba(246, 243, 237, 0.40) 100%) !important;
  backdrop-filter: blur(22px) saturate(180%) !important;
  -webkit-backdrop-filter: blur(22px) saturate(180%) !important;
  border: 1.5px solid rgba(255, 255, 255, 0.85) !important;
  box-shadow: 0 20px 50px rgba(30, 28, 24, 0.08), inset 0 1.5px 2px rgba(255, 255, 255, 0.95) !important;
  border-radius: 26px !important;
}
</style>

<script>
// Capture phase click delegator for instant, unblockable smooth scrolling
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
      e.stopPropagation();
      e.stopImmediatePropagation();
      var headerOffset = 80;
      var elementPosition = target.getBoundingClientRect().top;
      var offsetPosition = elementPosition + window.pageYOffset - headerOffset;
      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
      try { history.pushState(null, null, '#' + id); } catch(err) {}
    }
  }
}, true);

// Header dynamic elevation
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

# Replace previous style blocks
html = re.sub(r'<style id="ishara-[^"]*">.*?</script>', true_glassmorphism_css, html, flags=re.DOTALL)

with open('home/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Applied authentic 40% frosted glassmorphism and compact single-line header pill!")
