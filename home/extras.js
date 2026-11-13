// RiVa demo extras. Reads the demo's own DOM state (house classes, --night, status line), never its internals.
(function () {
  const sec = document.querySelector('.riva-ph-section'), house = sec && sec.querySelector('#riva-ph-house');
  if (!house) return;
  const status = sec.querySelector('#riva-ph-status-text'), svg = house.querySelector('.riva-ph-overlay');
  const FRAME = { day: './img/Smart-Home-–-Day-Curtains-Open-Lights-On-768x512.webp', night: './img/Smart-Home-–-Night-Curtains-Open-Lights-On-768x512.webp' };
  const isNight = () => getComputedStyle(sec).getPropertyValue('--night').trim() === '1';

  // live front-door camera
  const pip = document.createElement('div'); pip.className = 'rx-pip';
  pip.innerHTML = '<b>LIVE<span> · FRONT DOOR</span></b><u>MOTION</u><i></i>'; house.appendChild(pip);
  const clock = pip.querySelector('i');
  // now playing
  const np = document.createElement('div'); np.className = 'rx-np';
  np.innerHTML = '<span><em></em><em></em><em></em><em></em></span><label>Now playing · Living room</label>'; house.appendChild(np);
  const npLabel = np.querySelector('label');

  // TV glow behind the hallroom window, porch flash at the door (photo pixel space)
  const NS = 'http://www.w3.org/2000/svg';
  const defs = svg.querySelector('defs');
  defs.insertAdjacentHTML('beforeend',
    '<radialGradient id="rxTvG"><stop offset="0%" stop-color="#7fb2ff" stop-opacity=".95"/><stop offset="55%" stop-color="#4f7dff" stop-opacity=".45"/><stop offset="100%" stop-color="#4f7dff" stop-opacity="0"/></radialGradient>' +
    '<radialGradient id="rxPorchG"><stop offset="0%" stop-color="#fff2c4" stop-opacity="1"/><stop offset="100%" stop-color="#ffd27a" stop-opacity="0"/></radialGradient>');
  const ell = (cls, cx, cy, rx, ry, fill) => { const e = document.createElementNS(NS, 'ellipse'); e.setAttribute('class', cls);
    [['cx', cx], ['cy', cy], ['rx', rx], ['ry', ry], ['fill', fill], ['filter', 'url(#rivaSoft)']].forEach(([k, v]) => e.setAttribute(k, v)); svg.insertBefore(e, svg.children[1]); };
  ell('rx-tv', 552, 680, 210, 120, 'url(#rxTvG)');
  ell('rx-porch', 916, 600, 170, 150, 'url(#rxPorchG)');

  function sync() {
    const n = isNight();
    pip.style.backgroundImage = `url("${n ? FRAME.night : FRAME.day}")`;
    pip.classList.toggle('ir', n);
    npLabel.textContent = house.classList.contains('rx-movie') ? 'Movie soundtrack · Sonos' : (n ? 'Evening jazz · Sonos' : 'Morning playlist · Sonos');
  }
  setInterval(() => { clock.textContent = new Date().toLocaleTimeString([], { hour12: false }); }, 1000);

  // movie mode follows the status line, which every scene / chip / voice path writes
  new MutationObserver(() => {
    const t = status.textContent;
    if (/^Movie night/.test(t)) house.classList.add('rx-movie');
    else if (/^(Good morning|Away|Good night|Daytime)|curtains opening|lights on/.test(t)) house.classList.remove('rx-movie');
    sync();
  }).observe(status, { childList: true, characterData: true, subtree: true });
  new MutationObserver(sync).observe(sec, { attributes: true, attributeFilter: ['style'] });
  new MutationObserver(sync).observe(house, { attributes: true, attributeFilter: ['class'] });

  // armed motion sensor: someone walks up every ~12 s
  let motionT = null;
  setInterval(() => {
    if (!house.classList.contains('sense-on') || motionT) return;
    house.classList.add('rx-motion'); pip.classList.add('alert');
    const prev = status.textContent;
    status.textContent = 'Motion at the front door' + (isNight() ? ' — porch light on' : '') + (house.classList.contains('cam-on') ? ', camera recording' : '');
    motionT = setTimeout(() => { house.classList.remove('rx-motion'); pip.classList.remove('alert'); status.textContent = prev; motionT = null; }, 3500);
  }, 12000);
  sec.querySelector('[data-toggle="sensor"]').addEventListener('click', () => setTimeout(() => {
    if (house.classList.contains('sense-on')) status.textContent = 'Motion sensor armed — watching the front door';
  }, 0));

  // ---- boundary: railing fence on a low wall, lantern pillars, arched iron double gate ----
  // photo pixel space (1536×1024). Gate pillars flank the path in front of the steps.
  const GL = 736, GR = 1264, MID = (GL + GR) / 2;
  const arch = x => 772 - 36 * Math.sin(Math.PI * (x - GL) / (GR - GL));     // arched top of the gate
  const spear = (x, t) => `<rect x="${x - 2}" y="${t}" width="4" height="${1004 - t}" fill="url(#rxIron)"/><path d="M${x} ${t - 10}l4.5 10h-9z" fill="#14161a"/>`;
  function leaf(x0, x1) {
    let g = '', pts = [];
    for (let x = x0 + 12; x < x1 - 6; x += 19) g += spear(x, arch(x));
    for (let x = x0; x <= x1; x += 8) pts.push(x + ',' + (arch(x) + 16).toFixed(1));
    return g + `<polyline points="${pts.join(' ')}" fill="none" stroke="#14161a" stroke-width="6"/>` +
      `<rect x="${x0}" y="926" width="${x1 - x0}" height="6" fill="#14161a"/><rect x="${x0}" y="994" width="${x1 - x0}" height="9" fill="#14161a"/>` +
      `<rect x="${x0}" y="${arch(x0) + 10}" width="8" height="${1004 - arch(x0) - 10}" fill="#14161a"/>` +
      `<rect x="${x1 - 8}" y="${arch(x1) + 10}" width="8" height="${1004 - arch(x1) - 10}" fill="#14161a"/>` +
      `<circle cx="${(x0 + x1) / 2}" cy="962" r="17" fill="none" stroke="#14161a" stroke-width="4"/>`;
  }
  function fence(x0, x1) {
    let g = `<rect x="${x0}" y="948" width="${x1 - x0}" height="76" fill="url(#rxWall)"/><rect x="${x0}" y="940" width="${x1 - x0}" height="10" fill="#8d867c"/>`;
    for (let x = x0 + 12; x < x1 - 6; x += 22) g += `<rect x="${x - 1.5}" y="836" width="3" height="104" fill="url(#rxIron)"/><path d="M${x} 828l3.5 8h-7z" fill="#14161a"/>`;
    g += `<rect x="${x0}" y="846" width="${x1 - x0}" height="5" fill="#14161a"/><rect x="${x0}" y="924" width="${x1 - x0}" height="4" fill="#14161a"/>`;
    return g;
  }
  const post = x => `<rect x="${x}" y="808" width="30" height="216" fill="url(#rxWall)"/><rect x="${x - 4}" y="800" width="38" height="10" rx="2" fill="#5f5a53"/>` +
    `<ellipse class="rx-lampglow" cx="${x + 15}" cy="792" rx="34" ry="26" fill="url(#rxPorchG)" filter="url(#rivaSoft)"/><rect class="rx-lamp" x="${x + 8}" y="786" width="14" height="12" rx="3"/>`;
  const pillar = x => `<rect x="${x}" y="702" width="48" height="322" fill="url(#rxWall)"/>` +
    `<rect x="${x}" y="760" width="48" height="2" fill="#b3a893"/><rect x="${x}" y="880" width="48" height="2" fill="#b3a893"/>` +
    `<rect x="${x - 6}" y="690" width="60" height="14" rx="2" fill="#5f5a53"/>` +
    `<ellipse class="rx-lampglow" cx="${x + 24}" cy="664" rx="80" ry="64" fill="url(#rxPorchG)" filter="url(#rivaSoft)"/>` +
    `<path d="M${x + 6} 646h36l-7-11h-22z" fill="#14161a"/><rect x="${x + 10}" y="646" width="28" height="44" rx="3" fill="#14161a"/>` +
    `<rect class="rx-lamp" x="${x + 14}" y="651" width="20" height="34" rx="2"/>`;
  defs.insertAdjacentHTML('beforeend',
    '<linearGradient id="rxWall" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3eee6"/><stop offset="1" stop-color="#cdc3b2"/></linearGradient>' +
    '<linearGradient id="rxIron" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#3a3d43"/><stop offset=".5" stop-color="#1b1d21"/><stop offset="1" stop-color="#0f1013"/></linearGradient>');
  svg.insertAdjacentHTML('beforeend', `<g class="rx-boundary">
    <g class="rx-solid">${fence(0, GL - 48)}${fence(GR + 48, 1536)}${post(210)}${post(452)}${post(1430)}</g>
    <g class="rx-leafL rx-solid">${leaf(GL, MID - 2)}</g>
    <g class="rx-leafR rx-solid">${leaf(MID + 2, GR)}</g>
    <g class="rx-solid">${pillar(GL - 48)}${pillar(GR)}
      <rect x="${GR + 10}" y="890" width="28" height="40" rx="4" fill="#2a2c30"/><circle cx="${GR + 24}" cy="902" r="5" fill="#9aa3ad"/>
      <rect x="${GR + 8}" y="800" width="32" height="18" rx="2" fill="#2a2c30"/><text x="${GR + 24}" y="813" font-size="11" font-family="Inter,system-ui" fill="#e8e2d6" text-anchor="middle">12</text></g>
    <circle class="rx-led" cx="${GR + 24}" cy="920" r="4"/>
  </g>`);
  // control bar under the photo: status line + walk in / walk out, so nothing sits over the gate
  const bar = document.createElement('div'); bar.className = 'rx-bar';
  bar.innerHTML = '<div class="rx-walk-seg" role="group" aria-label="Walk"><button type="button" data-walk="in">Walk in ▸</button><button type="button" data-walk="out" disabled>◂ Walk out</button></div>';
  house.after(bar);
  bar.prepend(house.querySelector('.riva-ph-status'));
  const walkInBtn = bar.querySelector('[data-walk="in"]'), walkOutBtn = bar.querySelector('[data-walk="out"]');

  const gateSw = sec.querySelector('[data-rx-toggle="gate"]'), gateTxt = sec.querySelector('[data-rx-state="gate"]');
  const gateRow = gateSw.closest('.riva-ph-row');
  const AUTO_CLOSE = 10, TRAVEL_MS = 4200;
  let gateOpen = false, moveT = null, countT = null, left = 0;
  function paintGate(txt) {
    gateSw.setAttribute('aria-checked', gateOpen ? 'true' : 'false');
    gateRow.classList.toggle('is-off', !gateOpen);
    gateTxt.textContent = txt;
  }
  function move(open, msg) {
    clearTimeout(moveT); clearInterval(countT);
    gateOpen = open;
    house.classList.toggle('rx-gate-open', open);
    house.classList.add('rx-gate-moving');
    paintGate(open ? 'Opening…' : 'Closing…');
    status.textContent = msg || (open ? 'Gate opening' : 'Gate closing');
    moveT = setTimeout(() => {
      house.classList.remove('rx-gate-moving');
      if (!open) { paintGate('Closed'); status.textContent = 'Gate closed'; return; }
      left = AUTO_CLOSE; paintGate('Open · closes in ' + left + 's');
      countT = setInterval(() => {
        left--;
        if (left > 0) { paintGate('Open · closes in ' + left + 's'); status.textContent = 'Gate open — closing automatically in ' + left + 's'; return; }
        clearInterval(countT); move(false, 'Auto-closing the gate — path clear');
      }, 1000);
    }, TRAVEL_MS);
  }
  const openGate = msg => { if (!gateOpen) move(true, msg); else { left = AUTO_CLOSE; status.textContent = msg || 'Gate already open — timer reset'; } };
  const closeGate = msg => { if (gateOpen || house.classList.contains('rx-gate-moving')) move(false, msg); };
  gateSw.addEventListener('click', () => gateOpen ? closeGate() : openGate());

  // safety beam: someone in the gateway while it closes → back off and reopen
  new MutationObserver(() => {
    if (!walking && house.classList.contains('rx-motion') && !gateOpen && house.classList.contains('rx-gate-moving'))
      move(true, 'Obstacle in the gateway — gate reopening');
  }).observe(house, { attributes: true, attributeFilter: ['class'] });
  // scenes that lock up also shut the gate
  new MutationObserver(() => {
    const t = status.textContent;                       // our own rewrite says "gate": don't react to it again
    if (/^(Away|Good night)/.test(t) && !/gate/.test(t)) closeGate(t + ', gate closing');
  }).observe(status, { childList: true, characterData: true, subtree: true });

  // walk in: gate opens, view glides up the drive to the door and stays; gate closes behind you.
  // walk out: door locks, gate opens, view pulls back to the street, gate closes behind you.
  let walking = false, inside = false, walkTs = [];
  const at = (ms, fn) => walkTs.push(setTimeout(fn, ms));
  const lockBtn = () => sec.querySelector('[data-toggle="lock"]');
  function walkButtons() { walkInBtn.disabled = walking || inside; walkOutBtn.disabled = walking || !inside; }
  function walkIn(unlock) {
    if (walking) return 'Already moving';
    if (inside) return 'You are already at the door';
    walking = true; walkButtons();
    openGate('Gate opening — walking you in');
    at(1800, () => { house.classList.add('rx-walk'); status.textContent = 'Walking up the drive — pillar lanterns, railings, garden lights'; });
    at(7000, () => {
      if (unlock && lockBtn().getAttribute('aria-checked') === 'true') lockBtn().click();
      status.textContent = unlock ? 'At the door — unlocked for you' : 'At the front door';
    });
    at(8500, () => closeGate('Gate closing behind you'));
    at(12800, () => { walking = false; inside = true; walkButtons(); status.textContent = 'Inside the boundary — gate shut behind you'; });
    return unlock ? 'Welcome home — walking you in' : 'Walking you in';
  }
  function walkOut() {
    if (walking) return 'Already moving';
    if (!inside) return 'You are already outside';
    walking = true; walkButtons();
    if (lockBtn().getAttribute('aria-checked') !== 'true') lockBtn().click();
    status.textContent = 'Front door locked — heading out';
    at(1000, () => openGate('Gate opening — walking you out'));
    at(3200, () => { house.classList.remove('rx-walk'); status.textContent = 'Walking down the drive'; });
    at(9000, () => closeGate('Gate closing behind you'));
    at(13400, () => { walking = false; inside = false; walkButtons(); status.textContent = 'Out on the street — gate shut, house locked'; });
    return 'Walking you out';
  }
  walkInBtn.addEventListener('click', () => walkIn(false));
  walkOutBtn.addEventListener('click', walkOut);
  // leaving scenes walk you out if you're inside
  new MutationObserver(() => {
    if (inside && !walking && /^(Away|Good night)/.test(status.textContent)) walkOut();
  }).observe(status, { childList: true, characterData: true, subtree: true });

  window.rxCommand = t => {
    if (/\b(i'?m|i am) (home|back)\b|\barriv(ing|ed)\b|\bwelcome home\b/.test(t)) { walkIn(true); return 'Welcome home — walking you in'; }
    if (/\b(walk|go|step|head|take me)\s*(out|outside)\b|\bleave the house\b|\bexit\b/.test(t)) return walkOut();
    if (/\b(walk|come|take me|let me)\s*(in|inside)\b|\benter\b/.test(t)) return walkIn(false);
    if (!/\bgates?\b/.test(t)) return null;
    if (/\b(close|shut|lock)\b/.test(t)) { closeGate(); return 'Gate closing'; }
    if (/\b(open|unlock|let)\b/.test(t)) { openGate(); return 'Gate opening — auto-closes in ' + AUTO_CLOSE + 's'; }
    gateOpen ? closeGate() : openGate(); return gateOpen ? 'Gate opening' : 'Gate closing';
  };
  sync();
})();
