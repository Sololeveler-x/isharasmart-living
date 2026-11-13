with open('home/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '<image' in line and '#riva-house' in line:
        print(f"Line {i+1}: {line}")
        # also check adjacent lines
        for j in range(max(0, i-2), min(len(lines), i+3)):
            print(f" {j+1}: {lines[j]}")
