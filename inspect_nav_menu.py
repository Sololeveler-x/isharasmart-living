import re

with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# Find the navigation menu
nav_match = re.search(r'<nav[^>]*class="[^"]*elementor-nav-menu--main[^"]*"[^>]*>.*?</nav>', html, re.DOTALL)
if nav_match:
    print("Found nav menu (len=", len(nav_match.group(0)), ")")
    print(nav_match.group(0)[:2000])
else:
    print("Looking for ul.elementor-nav-menu...")
    ul_match = re.search(r'<ul[^>]*class="[^"]*elementor-nav-menu[^"]*"[^>]*>.*?</ul>', html, re.DOTALL)
    if ul_match:
        print("Found ul.elementor-nav-menu (len=", len(ul_match.group(0)), ")")
        print(ul_match.group(0)[:2000])
