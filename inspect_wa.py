import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

wa = re.findall(r'<a[^>]*whatsapp[^>]*>.*?(?=</a>)</a>', html, re.DOTALL | re.IGNORECASE)
print(f"WhatsApp <a> tags: {len(wa)}")
for w in wa:
    print("WA:", w)

floating = re.findall(r'<[^>]*elementor-social-icon-whatsapp[^>]*>', html)
print("Floating WA icons:", floating)
for match in re.finditer(r'<a[^>]*elementor-social-icon-whatsapp[^>]*>', html):
    start = max(0, match.start() - 100)
    end = min(len(html), match.end() + 100)
    print("Surrounding:", html[start:end])
