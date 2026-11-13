with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Remove Google Tag Manager / Analytics / Cooki.co tracking
import re
html = re.sub(r'<script[^>]*googletagmanager\.com[^>]*>.*?</script>', '', html, flags=re.DOTALL)
html = re.sub(r'<script[^>]*id=["\']google_gtagjs-js-after["\'][^>]*>.*?</script>', '', html, flags=re.DOTALL)
html = re.sub(r'<script[^>]*src=["\']https://rivasmart\.com/wp-includes/js/jquery/jquery\.min\.js[^"\']*["\'][^>]*></script>', '<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>', html)
html = re.sub(r'<script[^>]*src=["\']https://rivasmart\.com/wp-content/litespeed/js/[^"\']*["\'][^>]*></script>', '', html)

with open('home/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Cleaned trackers and dead scripts from home/index.html")
