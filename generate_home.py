import re
import base64

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

print("Original HTML length:", len(html))

# 1. Update CSS bundle link to local ./site.css
old_css_link = 'https://rivasmart.com/wp-content/litespeed/css/6ef5ba9f00fef4ff38c93f5624d5caa8.css?ver=ffe71'
if old_css_link in html:
    html = html.replace(old_css_link, './site.css')
    print("Replaced LiteSpeed CSS link with ./site.css")
else:
    print("CSS link not found directly, searching for litespeed/css...")
    html = re.sub(r'https://rivasmart\.com/wp-content/litespeed/css/[^"\']+\.css(?:\?[^"\']*)?', './site.css', html)

# Also ensure local preload or fallback
html = html.replace('https://rivasmart.com/wp-content/uploads/2026/09/matter.webp', './img/matter.webp')

# 2. Update Script 3 (Photo House) to use local FRAME_BASE = "./img/"
data_scripts = re.findall(r'src="(data:text/javascript;base64,[^"]*)"', html)
print(f"Total data scripts found: {len(data_scripts)}")

# Script 3 is index 2
s3_full = data_scripts[2]
s3_b64 = s3_full.split('data:text/javascript;base64,')[1]
s3_dec = base64.b64decode(s3_b64).decode('utf-8')
if 'FRAME_BASE="https://rivasmart.com/wp-content/uploads/2026/09/";' in s3_dec:
    s3_dec_new = s3_dec.replace('FRAME_BASE="https://rivasmart.com/wp-content/uploads/2026/09/";', 'FRAME_BASE="./img/";')
    s3_b64_new = base64.b64encode(s3_dec_new.encode('utf-8')).decode('utf-8')
    html = html.replace(s3_b64, s3_b64_new)
    print("Updated Script 3 FRAME_BASE to ./img/")

# 3. Update Script 8 (Follow the Signal) to brand stations with Ishara Smart
s8_full = data_scripts[7]
s8_b64 = s8_full.split('data:text/javascript;base64,')[1]
s8_dec = base64.b64decode(s8_b64).decode('utf-8')
if 'RiVa Smart' in s8_dec:
    s8_dec_new = s8_dec.replace('RiVa Smart', 'Ishara Smart')
    s8_b64_new = base64.b64encode(s8_dec_new.encode('utf-8')).decode('utf-8')
    html = html.replace(s8_b64, s8_b64_new)
    print("Updated Script 8 station sub-labels to Ishara Smart")

# 4. Update preload and poster images for Photo House to local ./img/
html = re.sub(
    r'https://rivasmart\.com/wp-content/uploads/2026/09/(Smart-Home-[^"\'\s]+)',
    r'./img/\1',
    html
)
print("Updated Smart-Home photo URLs to ./img/")

# 5. Virtual Home Tour link to our 3D tour
html = html.replace('href="https://rivasmart.com/smart-home-virtual-tour/"', 'href="../tour/index.html"')
html = html.replace('href="/smart-home-virtual-tour/"', 'href="../tour/index.html"')
print("Updated Virtual Tour link to ../tour/index.html")

# 6. Floating WhatsApp icon link
html = html.replace('href="https://wa.link/3yd5bg"', 'href="https://wa.me/919380792471?text=Hi%20Ishara%20Smart%20Living,%20I\'m%20interested%20in%20home%20automation%20solutions."')
print("Updated floating WhatsApp button to 9380792471")

# 7. Update Yoast SEO Title & Meta Description & Schema
html = html.replace('Matter Smart Home Automation in Bengaluru | RiVa Smart', 'Matter Smart Home Automation | Ishara Smart Living – Bangalore & Shivamogga, Karnataka')
html = html.replace('Matter-certified smart home automation in Bengaluru. See it working at our Rajajinagar showroom. We fit and support it. Free consultation.', 'Modern Living Made Simple. Complete Matter smart home automation in Bangalore, Shivamogga & All Karnataka. We design, fit and support it. Call 9380792471.')

# 8. Schema Graph updates
html = html.replace('"name":"RiVa Smart"', '"name":"Ishara Smart Living"')
html = html.replace('"alternateName":["RiVaSmart","Riva Smart","RivaSmart India"]', '"alternateName":["Ishara Smart Living","Ishara Smart","Ishara Automation"]')
html = html.replace('"telephone":"+919902277072"', '"telephone":"+919380792471"')
html = html.replace('"legalName":"Khush Enterprises"', '"legalName":"Ishara Smart Living"')
html = html.replace('"streetAddress":"3rd Floor, Royal Plaza, 15, Dr Rajkumar Road, above ICICI Bank, opposite St Theresa Hospital, A Block, Subramanyanagar, 2nd Stage, Rajajinagar"', '"streetAddress":"Bangalore & Shivamogga Experience Centres | Serving All Karnataka"')
html = html.replace('https://www.instagram.com/rivasmartindia/', 'https://www.instagram.com/isharasmart_living/')
html = html.replace('https://www.facebook.com/rivasmartindia/', 'https://www.instagram.com/isharasmart_living/')

# 9. Phone number in footer address
html = html.replace('+91 99022 77072', '+91 9380792471')
html = html.replace('tel:+919902277072', 'tel:9380792471')
html = html.replace('15, Royal Plaza, 3rd Floor, Rajajinagar, Bengaluru, Karnataka 560010', 'Bangalore & Shivamogga Experience Centres | Serving All Karnataka')

# 10. Footer copyright
html = html.replace('© 2026 RiVa Smart. All Rights Reserved', '© 2026 Ishara Smart Living. All Rights Reserved')
html = html.replace(' 2026 RiVa Smart. All Rights Reserved', '© 2026 Ishara Smart Living. All Rights Reserved')

# 11. Hero H1 and kicker
html = html.replace(
    'Matter smart home automation in Bengaluru. Come and see it working before you buy.',
    'Complete Matter smart home automation in Karnataka. Come and see it working before you buy.'
)

# 12. Hero copy rail: replace showroom mention with Bangalore | Shivamogga
html = html.replace(
    'Try first — running in the showroom',
    'Try first — live demo in Bangalore & Shivamogga'
)

# 13. Brand logo in sticky header
# In header: <img ... src="https://rivasmart.com/wp-content/uploads/2025/11/rivasmart-logo.webp" ... alt="RiVa Smart" ...>
# Replace with Ishara Smart Living logo
header_logo_old = r'<a href="https://rivasmart\.com/">\s*<img width="430" height="91" src="https://rivasmart\.com/wp-content/uploads/2025/11/rivasmart-logo\.webp"[^>]*alt="RiVa Smart"[^>]*>\s*</a>'
header_logo_new = '''<a href="./" style="display:inline-flex;align-items:center;gap:12px;text-decoration:none;">
  <span style="display:inline-flex;align-items:center;justify-content:center;width:42px;height:42px;border-radius:12px;background:linear-gradient(135deg,#16231a 0%,#0e1911 100%);border:1px solid rgba(207,168,86,0.35);box-shadow:0 4px 12px rgba(0,0,0,0.15);">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#cfa856" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path>
      <polyline points="9 22 9 12 15 12 15 22"></polyline>
    </svg>
  </span>
  <span style="display:flex;flex-direction:column;text-align:left;">
    <span style="font-family:'Poppins',sans-serif;font-weight:700;font-size:19px;letter-spacing:-0.01em;color:#141413;line-height:1.15;">ISHARA <span style="color:#cfa856;font-weight:600;">SMART LIVING</span></span>
    <span style="font-family:'Open Sans',sans-serif;font-size:10px;font-weight:600;letter-spacing:0.18em;text-transform:uppercase;color:#77736c;">Modern Living Made Simple</span>
  </span>
</a>'''
html = re.sub(header_logo_old, header_logo_new, html)

# 14. Footer logo replacement
footer_logo_old = r'<a href="https://rivasmart\.com">\s*<img width="184" height="66" src="https://rivasmart\.com/wp-content/uploads/2025/10/logo-1\.png"[^>]*alt="RivaSmart smart home automation brand logo"[^>]*>\s*</a>'
footer_logo_new = '''<a href="./" style="display:inline-flex;align-items:center;gap:12px;text-decoration:none;">
  <span style="font-family:'Poppins',sans-serif;font-weight:700;font-size:22px;letter-spacing:-0.01em;color:#141413;line-height:1.15;">ISHARA <span style="color:#cfa856;font-weight:600;">SMART LIVING</span></span>
</a>'''
html = re.sub(footer_logo_old, footer_logo_new, html)

# 15. In Photo House header badge:
# Replace RiVa Smart mention in badge
html = html.replace('RiVa Smart — India’s First', 'Ishara Smart Living — Karnataka’s Premier')
html = html.replace('RiVa Smart — India\'s First', 'Ishara Smart Living — Karnataka’s Premier')
html = html.replace('RiVa Smart — India', 'Ishara Smart Living — Karnataka')
html = html.replace('RiVa Smart', 'Ishara Smart Living')

# 16. Add the Top Utility Bar from the flyer right before <header
top_bar = '''<!-- ISHARA SMART LIVING TOP UTILITY BAR (From Flyer) -->
<div style="background:#0f1512;color:#f3efe6;font-family:'Open Sans',sans-serif;font-size:11.5px;padding:8px 16px;border-bottom:1px solid rgba(207,168,86,0.25);position:relative;z-index:9999;">
  <div style="max-width:1360px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;">
    <div style="display:flex;align-items:center;gap:8px;font-weight:600;letter-spacing:0.04em;">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="#cfa856" stroke-width="2.5"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path><circle cx="12" cy="10" r="3"></circle></svg>
      <span>BANGALORE | SHIVAMOGGA &amp; ALL KARNATAKA</span>
    </div>
    <div style="font-weight:700;letter-spacing:0.18em;color:#cfa856;text-transform:uppercase;font-size:10.5px;">
      AUTOMATE &bull; SECURE &bull; ENHANCE
    </div>
    <div style="display:flex;align-items:center;gap:12px;">
      <span style="color:#a7a195;">GET IN TOUCH TODAY:</span>
      <a href="tel:9380792471" style="color:#fae092;font-weight:700;text-decoration:none;display:inline-flex;align-items:center;gap:5px;">
        <svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79a15.053 15.053 0 006.59 6.59l2.2-2.2a1 1 0 011.02-.24 11.72 11.72 0 003.68.59 1 1 0 011 1V20a1 1 0 01-1 1A17 17 0 013 4a1 1 0 011-1h3.5a1 1 0 011 1 11.72 11.72 0 00.59 3.68 1 1 0 01-.24 1.02l-2.23 2.09z"></path></svg>
        9380792471
      </a>
      <a href="https://instagram.com/isharasmart_living" target="_blank" style="color:#cfa856;font-size:11px;text-decoration:none;display:inline-flex;align-items:center;gap:4px;">
        @isharasmart_living
      </a>
    </div>
  </div>
</div>
'''

if '<header' in html:
    html = html.replace('<header', top_bar + '<header', 1)
    print("Injected top utility bar")

# 17. Update CTA WhatsApp action buttons
html = html.replace('href="https://wa.me/919902277072', 'href="https://wa.me/919380792471')

# Write output to home/index.html
with open('home/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Generated home/index.html successfully, size:", len(html))
