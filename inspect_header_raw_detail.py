with open('raw/home.html', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

pos = 183550
print("--- PRECEDING 1000 CHARS BEFORE id='header-bar' ---")
print(raw[pos-1000:pos])

print("--- FOLLOWING 2000 CHARS AFTER id='header-bar' ---")
print(raw[pos:pos+2000])
