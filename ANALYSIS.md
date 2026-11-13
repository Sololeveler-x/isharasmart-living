# rivasmart.com — Virtual Tour teardown

Source: `https://rivasmart.com/smart-home-virtual-tour/`. The page embeds a WordPress plugin iframe:
`/wp-content/plugins/riva-virtual-room/app/index.html`. It is a single 177 KB HTML file with all CSS and JS inline,
plus 4 assets. There is no backend: every "Matter device" is simulated in the browser.

## Stack
- WordPress + Astra theme + Elementor + LiteSpeed cache, behind Cloudflare (the bot-check beacon was removed in the local copy).
- three.js **0.149.0** (ES module + import map) and `GLTFLoader`. Nothing else.
- 3D model: `confortable_appartment.glb` (5.6 MB, "Confortable appartment" by SofianeLasri, **CC-BY**, so it needs attribution).
- Images: `rivasmart_logo.png`, `rivasmart_logo_reversed.png`, `aqara_fp2.png` (presence sensor texture).
- Everything else is drawn at runtime (sky, skyline, bedspread, curtain folds, TV screen, thermostat, panel screens, fake QR) on `<canvas>`.

## Controls
| Input | Action |
|---|---|
| W A S D / arrows | walk (with collision, step-up ≤ 0.30 m, unstick probes) |
| Mouse (pointer lock) / touch drag | look |
| Shift | run |
| E | open the nearest wall panel or thermostat (within 1.4 m, roughly facing it) |
| V / mic button | voice on/off |
| K | toggle the door you're aiming at |
| P | dev: re-mount the wall panel at your aim |
| Esc | clear alarm → end tour → close panel |

## Devices (all simulated Matter endpoints)
- **Main lights**: on/off, dimming (veil overlay), 6 colour temperatures: Candle 2200K, Warm 2700K, Soft 3000K, Neutral 4000K, Cool 5000K, Daylight 6500K.
- **Cove RGB strip** (18 W): Warm, Cool, Red, Amber, Green, Cyan, Blue, Violet, plus a rainbow cycle. Its path along the cornice is computed by ray-casting from vantage points.
- **Floor lamp** (42 W): absent until you commission it with "Add a device" (scan → BLE → Thread → certificate → room). Pair code `3497-011-2332`.
- **Balcony lantern** (12 W).
- **Curtains**: living room (x = −4.40, glazing) and bedroom (x = 6.49). Motorised and eased, 35 W while moving.
- **TV**: canvas screen that says "Matter cast", 95 W.
- **Doors**: front door smart lock + contact sensor (the magnet swings with the leaf), motorised bedroom and bathroom doors, motorised sliding balcony door + contact sensor.
- **Thermostat**: setpoint in 0.5° steps. Mode Heating / Cooling / Idle at ±0.3°. 1400 W heating, 900 W cooling, 6 W idle.
- **Hob** (2100 W): left on with the kitchen empty for 12 s → smoke.
- **Sensors**: Aqara FP2 presence (bedroom, bathroom), smoke, water leak, contact.
- **Energy view**: live per-device wattage and total.

## Panels
- **S9E-11 wall panel** by the front door. Views: main, room groups (bedroom, bathroom), lights, strip, climate, automations, add-device, tests.
- **Square bedroom panel** at the bed, scoped to that room: its light and its curtains.

## Scenes
| Scene | Effect |
|---|---|
| Good morning | lights 100 % Daylight, curtains open (both), bedroom lights on, 21.5° |
| Movie night | lights 10 % Warm, strip blue, TV on, lamp on, curtains closed, room lights off, 22.0° |
| Leaving home | everything off, doors locked, curtains closed, hob off, 17.0° |

## Automations (each one can be toggled, and shows "last fired")
1. Presence lighting: entering a room brings its lights up, and they hold 3 s after you leave.
2. Unattended hob: hob on and kitchen empty for 12 s → smoke alarm.
3. Fire safe state: smoke → lights up, all doors released, TV off, curtains open.
4. Leak shut-off: water → close the supply valve.
5. Balcony light: follows the balcony door contact.
6. Auto-acknowledge: clears an alarm after a few seconds.

## Voice (Web Speech API, `en-GB`, continuous, replies with speechSynthesis)
The wake word "hey/ok RiVa" is optional. Misheard forms reva / rita / viva / river are stripped too. The parser checks commands in this order:
1. **Scenes**: "good morning", "movie / cinema / film", "leaving / away / going out / goodbye".
2. "clear / stop / cancel the alarm". "tour / show me around".
3. **Strip**: "strip/cove/accent/mood" + a colour name, or "rainbow / cycle / party / disco".
4. **Lights**: "N percent", "dim / dimmer / lower" (−20 %), "brighter" (+20 %), a temperature name (candle…daylight), "warmer" / "cooler".
5. **Tests**: "test / simulate / trigger" + "smoke / fire" or "leak / water / flood".
6. **Thermostat**: "temperature / thermostat" + "warmer / colder" (±0.5°) or a number ("set temperature to 22").
7. **Device on/off**: on-words `on open up unlock start raise draw back`, off-words `off close shut down lock stop lower draw`.
   Room words: all/whole house, bedroom, bathroom/shower/toilet, living/lounge/hall, front. Room and device can come in either order.
   Devices: strip, floor lamp, balcony light, lights (default room: all), curtains/blinds (default: living), TV, hob (also accepts hop/mob/mop/stove/cooker), balcony door (inverted), door/lock (default: front, inverted, so "open" means unlock).

Examples: "movie night", "lights off in the bedroom", "dim the lights to 40 percent", "make the strip violet",
"close the curtains", "lock the front door", "set temperature to 22", "test the smoke alarm".

## Guided tour (14 stops)
Welcome → Living room → Curtains & cove → Balcony door → Out on the balcony → Climate → Wall panel → Automations → Front door →
Bedroom presence → Room panel → Bathroom & leak → Hob & energy → Smoke alarm → Add a device → Scenes.

## Local copy (`tour/`)
- `index.original.html`: byte-for-byte download.
- `index.html`: the same file with two changes. three.js is loaded from `vendor/` (works offline), and the Cloudflare beacon is removed.
- Only Google Fonts still loads remotely. Without it the page falls back to system fonts.
- Run: `python3 -m http.server 8765 -d rivasmart-analysis/tour`, then open http://localhost:8765.
  The mic needs Chrome or Edge on localhost or https. Safari/Firefox have no speech recognition, so they show "Not supported".
- `asset_urls.txt`: 895 product images and videos from the WordPress shop pages. These are not part of the tour, so they were not mirrored.

---

# Homepage "Try it yourself" demo (`#riva-house`)

The homepage section uses no 3D. It composites **8 rendered photos** (Day/Night × Lights on / Cool white / Lights off / Curtains closed),
each in 3 sizes (768, 1024, 1500 px), so 24 webp files. One CSS `clip-path` layer is stacked per window (Hallroom, Bedroom, Kitchen),
in the photo's 1536×1024 pixel space. Curtains are two "closed" bands that slide in from each edge. Brightness is the layer opacity,
and colour temperature cross-fades the warm and cool frames. An SVG overlay draws the camera cone, the speaker waves, the motion-sensor arcs, the lock shackle and the night window glow.
- The JS is shipped as a base64 `data:` URI. The CSS is split between an inline `<style>` and the LiteSpeed-combined stylesheet.
  The `.riva-ph-layer` positioning lives **only** in the combined file. Without it every layer collapses, so the curtains, lights and night mode never visibly change.
  That was the "not working" bug in the first local copy. `home/site-demo.css` is the rules extracted from that file.
- State: night, 3 lights + outside (on, brightness, temp), 3 curtains (0–100), lock, camera, speaker, sensor.
- Scenes: Good morning, Movie night (night, 15 % warm, curtains shut, music), Away (locked, sensor armed, outside lights on), Good night.
- Voice: `en-IN`, 8 s listening window, auto-restarts up to 6 times. Room words: bedroom, kitchen, hall/living. Also handles percentages and warm/cool.

## Local additions (`home/extras.js`, `home/extras.css`, plus a voice patch in `home/index.html`)
- Movie night: a flickering blue TV glow behind the living-room curtains, and a "Movie soundtrack" now-playing chip.
- Camera: a live front-door picture-in-picture with a REC dot and clock. It switches to an infrared look at night.
- Speaker: a now-playing chip with an animated equaliser.
- Motion sensor: when armed, it "detects" someone every 12 s. The porch light flashes, the camera border goes red with a MOTION tag, and the status line updates.
- Voice: "daylight", "night time", "night mode", "evening" and "night light" are now handled as time of day. The original sent them to the plain light toggle. There are 7 new one-tap phrase chips.

## 3D tour simplifications (`tour/index.html`)
- No pointer lock: drag to look, and the cursor stays visible.
- Double-click or double-tap: front, bedroom and bathroom doors, the balcony slider (including glass in its bay), the living and bedroom curtains, and the TV.
- Double-click or double-tap the floor: auto-turn and walk there. WASD or the joystick cancels it, and it stops on furniture.

## Boundary wall + automatic gate (added 3 Nov 2026)
- An SVG compound wall across the front of the photo: plaster panels with joints, dark stone coping, a plinth, two pillars with lamps (they glow at night) and a status LED.
  The wall and gate darken with `--night`.
- Sliding gate with 12 slats. It slides behind the left wall over 3.4 s. It **auto-closes after 10 s** with a live countdown in the panel row and the status line.
  Safety beam: if the motion sensor fires while the gate is closing, it reopens.
- Controls: a "Gate" switch in the panel. Voice: "open/close the gate"; "I'm home" / "welcome home" opens the gate and unlocks the front door. The Away and Good night scenes close it.
- Fixes in this round:
  - On phone width, the one-row phrase strip forced its grid column to ~956 px (`min-width:auto`).
  - The camera label wrapped over the picture.
  - Assets were served stale from cache; they now load as `?v=` versioned links.
  - Away / Good night froze the page in an infinite observer loop (the gate's own status rewrite re-triggered itself).

## Iron gate + walk-in (replaces the low wall, 3 Nov 2026)
- The boundary is now:
  - a railing fence on a low plaster wall, with 3 lit posts
  - two white gate pillars with black lanterns (glowing at night), an intercom, a house number and a status LED
  - an **arched black iron double gate** with spear-top bars, rails and ring details
- The gate leaves swing open from their hinges (scaleX, 4.2 s) and auto-close after 10 s.
- **Walk in** (photo button, or voice "walk in" / "enter"; "I'm home" also unlocks the door), about 13 s:
  1. The gate opens.
  2. The view glides up the drive to the door: the photo stack scales 1.6×, and the boundary scales faster and fades as you pass it.
  3. The gate closes behind you.
  4. The view pulls back out to show it shut.
- `serve.py` serves with `Cache-Control: no-store` and sends `Clear-Site-Data: "cache"` on page loads.
  The old `python -m http.server` let Chrome keep a stale `index.html`, so updates never showed up.

## Ishara landing page merge + layout pass (3 Nov 2026)
- Imported the Ishara Smart Living landing page from the 23 Oct zip as `home/index.html`. The standalone demo is now `home/demo.html`.
  The landing page's house section now runs the patched demo script (wake words "Ishara" and "RiVa"), with the gate row, the chips and `extras.*`.
- All 164 fonts, images and videos from rivasmart.com are now local under `home/assets/`. The fonts had been CORS-blocked, and a theme font was a 404. The Cloudflare beacon is removed.
- A control bar under the photo now holds the status line and **Walk in / Walk out**, so nothing covers the gate or the fence.
  - Walk in: you stay at the door, and the gate shuts behind you.
  - Walk out: the door locks, the gate opens, the view pulls back to the street, and the gate shuts.
  - Away / Good night walk you out if you're inside. Voice: "walk out", "step outside", "exit".
- Phone fixes:
  - Panel names no longer split ("Lig/hts").
  - The header ☰ menu toggle had wrapped into an off-screen column, making the page 470 px wide.
  - The WhatsApp bubble is smaller, and the footnote is kept clear of it.
  - No section overflows at 375 px.
- Still pointing at rivasmart.com: the SEO schema JSON-LD (url, logo) and two WordPress helper scripts (hooks, i18n).
