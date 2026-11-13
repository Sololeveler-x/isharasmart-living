import urllib.request
import os

assets = [
    ('works_with_apple.webp', 'https://rivasmart.com/wp-content/uploads/2026/09/works_with_apple.webp'),
    ('works_with_google.webp', 'https://rivasmart.com/wp-content/uploads/2026/09/works_with_google.webp'),
    ('works_with_alexa.webp', 'https://rivasmart.com/wp-content/uploads/2026/09/works_with_alexa.webp'),
    ('works_with_home_assistant.webp', 'https://rivasmart.com/wp-content/uploads/2026/09/works_with_home_assistant.webp'),
    ('works_with_smartthings.webp', 'https://rivasmart.com/wp-content/uploads/2026/09/works_with_smartthings.webp'),
    ('works_with_homey.webp', 'https://rivasmart.com/wp-content/uploads/2026/09/works_with_homey.webp'),
    ('matter-logo.png', 'https://rivasmart.com/wp-content/uploads/2026/01/matter.png'),
    ('matter-home.webp', 'https://rivasmart.com/wp-content/uploads/2026/09/matter-home.webp'),
    ('bulb-warm.webp', 'https://rivasmart.com/wp-content/uploads/2026/09/bulb-warm.webp'),
    ('bulb-cool.webp', 'https://rivasmart.com/wp-content/uploads/2026/09/bulb-cool.webp'),
    ('bulb-off.webp', 'https://rivasmart.com/wp-content/uploads/2026/09/bulb-off.webp'),
    ('ai-voice-platforms.webp', 'https://rivasmart.com/wp-content/uploads/2026/09/ai-voice-platforms.webp'),
    ('main.webp', 'https://rivasmart.com/wp-content/uploads/2026/09/main.webp')
]

for filename, url in assets:
    target = os.path.join('home', 'img', filename)
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as resp, open(target, 'wb') as f:
            f.write(resp.read())
        print(f"Downloaded: {filename} ({os.path.getsize(target)} bytes)")
    except Exception as e:
        print(f"Error {filename}: {e}")
