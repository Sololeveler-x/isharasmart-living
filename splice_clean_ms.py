import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

m_raw = re.search(r'<section[^>]*riva-ms[^>]*>.*?</section>', raw, re.DOTALL)
if not m_raw:
    print("Error: riva-ms not found in raw")
    exit(1)

clean_ms = m_raw.group(0)

# Replace image URLs with local verified assets
clean_ms = clean_ms.replace('https://rivasmart.com/wp-content/uploads/2026/09/works_with_apple.webp', './img/works_with_apple.webp')
clean_ms = clean_ms.replace('https://rivasmart.com/wp-content/uploads/2026/09/works_with_google.webp', './img/works_with_google.webp')
clean_ms = clean_ms.replace('https://rivasmart.com/wp-content/uploads/2026/09/works_with_alexa.webp', './img/works_with_alexa.webp')
clean_ms = clean_ms.replace('https://rivasmart.com/wp-content/uploads/2026/09/works_with_home_assistant.webp', './img/works_with_home_assistant.webp')
clean_ms = clean_ms.replace('https://rivasmart.com/wp-content/uploads/2026/09/works_with_smartthings.webp', './img/works_with_smartthings.webp')
clean_ms = clean_ms.replace('https://rivasmart.com/wp-content/uploads/2026/09/works_with_homey.webp', './img/works_with_homey.webp')
clean_ms = clean_ms.replace('https://rivasmart.com/wp-content/uploads/2026/01/matter.png', './img/matter-logo.png')

# Ensure ID is intact
clean_ms = clean_ms.replace('<section class="riva-ms">', '<section class="riva-ms" id="riva-matter-scroll">')

with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    current = f.read()

# Replace current riva-ms section with clean_ms
current_new = re.sub(r'<section[^>]*riva-ms[^>]*>.*?</section>', clean_ms, current, flags=re.DOTALL)

with open('home/index.html', 'w', encoding='utf-8') as f:
    f.write(current_new)

print("Spliced clean Matter diagram with all 7 local platform logos!")
