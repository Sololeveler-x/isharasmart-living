import re
with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

# Check if raw/home.html has any top bar or phone or Bengaluru
print("Searching raw/home.html:")
for term in ["BANGALORE", "Shivamogga", "97411", "top-bar", "topbar", "announcement"]:
    m = [match.start() for match in re.finditer(re.escape(term), raw, re.IGNORECASE)]
    print(f"Term '{term}': {len(m)} occurrences")

with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    home = f.read()

print("\nSearching home/index.html for top-bar:")
for m in re.finditer(r'top-bar', home):
    pos = m.start()
    print(home[max(0, pos-100):min(len(home), pos+200)])
