with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Replace remaining showroom / Rajajinagar mentions
html = html.replace('RAJAJINAGAR, ANY WEEKDAY', 'BANGALORE & SHIVAMOGGA, ANY WEEKDAY')
html = html.replace('RAJAJINAGAR SHOWROOM – BENGALURU', 'BANGALORE & SHIVAMOGGA SHOWROOMS — SERVING ALL KARNATAKA')
html = html.replace('RAJAJINAGAR SHOWROOM — BENGALURU', 'BANGALORE & SHIVAMOGGA SHOWROOMS — SERVING ALL KARNATAKA')
html = html.replace('RAJAJINAGAR SHOWROOM', 'BANGALORE & SHIVAMOGGA SHOWROOMS')
html = html.replace('Or come to the showroom in <b>Rajajinagar</b>', 'Or come to our experience centres in <b>Bangalore & Shivamogga</b>')
html = html.replace('in the Rajajinagar showroom', 'in our Bangalore & Shivamogga experience centres')
html = html.replace('our Rajajinagar showroom', 'our Bangalore & Shivamogga experience centres')

# CTA consultation buttons
html = html.replace('href="https://rivasmart.com/book-consultation/"', 'href="https://wa.me/919380792471?text=Hi%20Ishara%20Smart%20Living,%20I%20would%20like%20to%20book%20a%20free%20consultation."')
html = html.replace('href="/book-consultation/"', 'href="https://wa.me/919380792471?text=Hi%20Ishara%20Smart%20Living,%20I%20would%20like%20to%20book%20a%20free%20consultation."')
html = html.replace('href="https://rivasmart.com/contact/"', 'href="https://wa.me/919380792471?text=Hi%20Ishara%20Smart%20Living,%20I%20have%20an%20inquiry."')
html = html.replace('href="/contact/"', 'href="https://wa.me/919380792471?text=Hi%20Ishara%20Smart%20Living,%20I%20have%20an%20inquiry."')

# Replace "Ask us before you buy" link if any
import re
html = re.sub(
    r'<a([^>]*class="[^"]*riva-why-btn[^"]*"[^>]*)href="[^"]*"',
    r'<a\1href="https://wa.me/919380792471?text=Hi%20Ishara%20Smart%20Living,%20I%20need%20expert%20advice%20before%20I%20buy."',
    html
)

with open('home/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finalized showroom text and consultation links.")
