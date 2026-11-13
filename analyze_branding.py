import re

with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# 1. Phone numbers
phones = re.findall(r'(?:\+91[\s-]?)?[6-9]\d{9}', html)
print("Phones found:", set(phones))

# 2. Addresses / Locations
rajajinagar = re.findall(r'.{0,50}(?:Rajajinagar|Royal Plaza|Subramanyanagar).{0,50}', html, re.IGNORECASE)
print(f"Location mentions ({len(rajajinagar)}):")
for r in rajajinagar[:5]:
    print(" -", r.strip())

# 3. Riva Smart mentions (case insensitive)
riva_text = re.findall(r'(?i)(.{0,40}riva\s*smart.{0,40})', html)
print(f"RiVa Smart brand mentions: {len(riva_text)}")
for r in set(riva_text[:10]):
    print(" -", r.strip())

# 4. WhatsApp links
wa_links = re.findall(r'href="([^"]*(?:wa\.me|whatsapp)[^"]*)"', html, re.IGNORECASE)
print("WhatsApp links:", set(wa_links))

# 5. Virtual tour button / link
tour_matches = re.findall(r'.{0,50}(?:tour|hotspot|virtual).{0,50}', html, re.IGNORECASE)
print(f"Tour mentions ({len(tour_matches)}):")
for t in set(tour_matches[:5]):
    print(" -", t.strip())
