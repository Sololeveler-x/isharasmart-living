/**
 * ISHARA SMART LIVING - Interactive Controller Script
 * Handles Smartphone Mockup interaction, Live Sync with House Demo,
 * Energy Calculator, and Direct WhatsApp Quote Generator.
 */
document.addEventListener('DOMContentLoaded', function () {
  // 1. Phone App Mockup Controls & Synchronizer
  const phoneTiles = document.querySelectorAll('.phone-tile');
  const masterPowerBtn = document.querySelector('.phone-power-btn');
  
  phoneTiles.forEach(tile => {
    tile.addEventListener('click', function () {
      const feature = this.dataset.feature;
      const isActive = this.classList.toggle('is-active');
      const statusEl = this.querySelector('.phone-tile-status');
      
      // Update phone tile status label
      if (statusEl) {
        if (feature === 'lights') {
          statusEl.textContent = isActive ? 'On · 80%' : 'All Off';
          // Sync with house demo light switch if available
          const lightSwitch = document.querySelector('[data-toggle="lights"]');
          if (lightSwitch) lightSwitch.click();
        } else if (feature === 'security') {
          statusEl.textContent = isActive ? 'Armed · Active' : 'Disarmed';
          const sensorSwitch = document.querySelector('[data-toggle="sensor"]');
          if (sensorSwitch) sensorSwitch.click();
        } else if (feature === 'curtains') {
          statusEl.textContent = isActive ? 'Open · 100%' : 'Closed';
          const curtainSwitch = document.querySelector('[data-toggle="curtains"]');
          if (curtainSwitch) curtainSwitch.click();
        } else if (feature === 'ac') {
          statusEl.textContent = isActive ? '21.5°C Cooling' : 'Off';
        } else if (feature === 'theatre') {
          statusEl.textContent = isActive ? 'Cinema Mode' : 'Idle';
          // Cinema mode triggers movie scene in demo!
          const movieSceneBtn = document.querySelector('[data-scene="movie"]');
          if (movieSceneBtn && isActive) movieSceneBtn.click();
        } else if (feature === 'gate') {
          statusEl.textContent = isActive ? 'Gate Open' : 'Gate Closed';
          const lockSwitch = document.querySelector('[data-toggle="lock"]');
          if (lockSwitch) lockSwitch.click();
        }
      }
    });
  });

  // Master Power Button
  if (masterPowerBtn) {
    let powerState = true;
    masterPowerBtn.addEventListener('click', function () {
      powerState = !powerState;
      this.style.filter = powerState ? 'brightness(1.15)' : 'grayscale(0.8) opacity(0.7)';
      phoneTiles.forEach(tile => {
        tile.classList.toggle('is-active', powerState);
        const st = tile.querySelector('.phone-tile-status');
        if (st) st.textContent = powerState ? 'Active' : 'Standby';
      });
      // Trigger house scene
      const sceneBtn = document.querySelector(powerState ? '[data-scene="morning"]' : '[data-scene="away"]');
      if (sceneBtn) sceneBtn.click();
    });
  }

  // 2. Interactive Energy Calculator
  const dimSlider = document.getElementById('energy-dim-slider');
  const energyWattVal = document.getElementById('energy-watt-val');
  const energyCostVal = document.getElementById('energy-cost-val');
  const energyCo2Val = document.getElementById('energy-co2-val');

  if (dimSlider) {
    dimSlider.addEventListener('input', function () {
      const level = parseInt(this.value, 10);
      // Base load for a 4BHK luxury villa: ~1400W peak lighting & standby
      const baselineWatts = 1400;
      const currentWatts = Math.round(baselineWatts * (level / 100) * 0.75 + 150);
      const savedWatts = baselineWatts - currentWatts;
      // Approx savings based on 6 hrs/day at ₹8/kWh
      const monthlySavedRs = Math.round((savedWatts * 6 * 30 / 1000) * 8.2);
      const co2SavedKg = ((savedWatts * 6 * 30 / 1000) * 0.82).toFixed(1);

      if (energyWattVal) energyWattVal.textContent = currentWatts + ' W';
      if (energyCostVal) energyCostVal.textContent = '₹' + monthlySavedRs + '/mo saved';
      if (energyCo2Val) energyCo2Val.textContent = co2SavedKg + ' kg/mo';
    });
  }

  // 3. Multi-select Chips in Consultation Form
  const chipButtons = document.querySelectorAll('.chip-select-btn');
  chipButtons.forEach(btn => {
    btn.addEventListener('click', function () {
      this.classList.toggle('is-selected');
    });
  });

  // 4. WhatsApp Direct Quote Generator
  const quoteForm = document.getElementById('ishara-quote-form');
  if (quoteForm) {
    quoteForm.addEventListener('submit', function (e) {
      e.preventDefault();
      
      const name = document.getElementById('quote-name').value.trim();
      const phone = document.getElementById('quote-phone').value.trim();
      const propType = document.getElementById('quote-property').value;
      const city = document.getElementById('quote-city').value.trim();
      
      // Selected services
      const selectedChips = Array.from(document.querySelectorAll('.chip-select-btn.is-selected'))
        .map(el => el.textContent.trim());
      
      const servicesText = selectedChips.length > 0 ? selectedChips.join(', ') : 'All 9 Home Automation Solutions';
      
      // Format message for WhatsApp
      let message = `*NEW INQUIRY - ISHARA SMART LIVING*\n`;
      message += `------------------------------------\n`;
      message += `*Name:* ${name || 'Prospective Client'}\n`;
      message += `*Phone:* ${phone || 'Not provided'}\n`;
      message += `*Property Type:* ${propType}\n`;
      message += `*City/Location:* ${city || 'Karnataka'}\n`;
      message += `*Interested In:* ${servicesText}\n`;
      message += `------------------------------------\n`;
      message += `Kindly share a free consultation, site survey details, and estimate.`;

      const whatsappURL = `https://wa.me/919380792471?text=${encodeURIComponent(message)}`;
      window.open(whatsappURL, '_blank');
    });
  }

  // 5. Mobile Menu Toggle
  const menuToggle = document.querySelector('.nav-mobile-toggle');
  const navLinks = document.querySelector('.nav-links');
  if (menuToggle && navLinks) {
    menuToggle.addEventListener('click', function () {
      const isVisible = navLinks.style.display === 'flex';
      navLinks.style.display = isVisible ? 'none' : 'flex';
      navLinks.style.flexDirection = 'column';
      navLinks.style.position = 'absolute';
      navLinks.style.top = '100%';
      navLinks.style.left = '0';
      navLinks.style.right = '0';
      navLinks.style.background = '#0b0f17';
      navLinks.style.padding = '20px';
      navLinks.style.borderBottom = '1px solid rgba(207, 168, 86, 0.3)';
    });
  }
});
