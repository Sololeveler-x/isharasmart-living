with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

# Let's find style tags
import re
styles = re.findall(r'<style[^>]*>(.*?)</style>', raw, re.DOTALL)
print("Total style blocks:", len(styles))

for s in styles:
    if 'header' in s or 'sticky' in s or '1284' in s:
        # split rules
        rules = s.split('}')
        for r in rules:
            if any(k in r for k in ['header-bar', 'header-internal', 'elementor-1284', 'elementor-sticky']):
                print("MATCH:", r.strip())
