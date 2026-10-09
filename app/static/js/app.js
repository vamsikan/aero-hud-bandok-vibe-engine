/**
 * AERO·HUD // Interactive UI Controller
 */

document.addEventListener('DOMContentLoaded', () => {
  // Application State
  const state = {
    activeCategory: null,
    currentQuote: null,
    alternatives: [],
    favorites: JSON.parse(localStorage.getItem('aero_favorites') || '[]'),
    cardRenderer: new HudCardRenderer('socialCanvas'),
  };

  // DOM Elements
  const els = {
    vibeContainer: document.getElementById('vibeContainer'),
    quoteHeadline: document.getElementById('quoteHeadline'),
    quoteSubtext: document.getElementById('quoteSubtext'),
    quoteVibeBadge: document.getElementById('quoteVibeBadge'),
    quoteTagsBadge: document.getElementById('quoteTagsBadge'),
    starBtn: document.getElementById('starBtn'),
    stravaTitlePreview: document.getElementById('stravaTitlePreview'),
    stravaDescPreview: document.getElementById('stravaDescPreview'),
    whatsappStatusPreview: document.getElementById('whatsappStatusPreview'),
    whatsappChatPreview: document.getElementById('whatsappChatPreview'),
    stravaGaugeFill: document.getElementById('stravaGaugeFill'),
    stravaGaugeText: document.getElementById('stravaGaugeText'),
    waGaugeFill: document.getElementById('waGaugeFill'),
    waGaugeText: document.getElementById('waGaugeText'),
    alternativesList: document.getElementById('alternativesList'),
    btnGenerate: document.getElementById('btnGenerate'),
    btnOpenWhatsApp: document.getElementById('btnOpenWhatsApp'),
    btnAudioToggle: document.getElementById('btnAudioToggle'),
    btnSocialCard: document.getElementById('btnSocialCard'),
    cardModal: document.getElementById('cardModal'),
    btnCloseModal: document.getElementById('btnCloseModal'),
    btnDownloadCard: document.getElementById('btnDownloadCard'),
    toast: document.getElementById('hudToast'),
    toastMsg: document.getElementById('toastMsg'),
    
    // Telemetry inputs
    inputDist: document.getElementById('inputDist'),
    inputSpeed: document.getElementById('inputSpeed'),
    inputElev: document.getElementById('inputElev'),
    inputLocation: document.getElementById('inputLocation'),
    inputBike: document.getElementById('inputBike'),
    inputSuffer: document.getElementById('inputSuffer'),
    inputChai: document.getElementById('inputChai'),

    // Custom Quote Elements
    btnOpenCustomModal: document.getElementById('btnOpenCustomModal'),
    customModal: document.getElementById('customModal'),
    btnCloseCustomModal: document.getElementById('btnCloseCustomModal'),
    btnSaveCustomQuote: document.getElementById('btnSaveCustomQuote'),
    customHeadline: document.getElementById('customHeadline'),
    customSubtext: document.getElementById('customSubtext'),
    customCategory: document.getElementById('customCategory'),
  };

  // Audio status indicator
  function updateAudioButton() {
    if (els.btnAudioToggle) {
      els.btnAudioToggle.innerHTML = hudSound.enabled ? '🔊 SFX: ON' : '🔇 SFX: OFF';
    }
  }
  updateAudioButton();

  if (els.btnAudioToggle) {
    els.btnAudioToggle.addEventListener('click', () => {
      const active = hudSound.toggle();
      updateAudioButton();
      showToast(active ? 'Synthesizer SFX Activated' : 'Audio Muted');
    });
  }

  // Toast notification
  function showToast(msg) {
    if (!els.toast || !els.toastMsg) return;
    els.toastMsg.textContent = msg;
    els.toast.classList.add('show');
    setTimeout(() => {
      els.toast.classList.remove('show');
    }, 2400);
  }

  // Clipboard utility
  async function copyToClipboard(text, label = 'Copied') {
    try {
      await navigator.clipboard.writeText(text);
      hudSound.playSuccessConfirm();
      showToast(`✔ ${label} copied to clipboard!`);
    } catch (err) {
      console.error('Clipboard copy failed:', err);
      // Fallback
      const ta = document.createElement('textarea');
      ta.value = text;
      document.body.appendChild(ta);
      ta.select();
      document.execCommand('copy');
      document.body.removeChild(ta);
      hudSound.playSuccessConfirm();
      showToast(`✔ ${label} copied!`);
    }
  }

  // Read current telemetry form
  function getTelemetryPayload() {
    return {
      distance_km: els.inputDist.value ? parseFloat(els.inputDist.value) : null,
      avg_speed_kph: els.inputSpeed.value ? parseFloat(els.inputSpeed.value) : null,
      elevation_m: els.inputElev.value ? parseInt(els.inputElev.value, 10) : null,
      location: els.inputLocation.value || 'Financial District, Hyderabad',
      bike: els.inputBike.value || 'Basso Venta R',
      suffer_score: els.inputSuffer.value ? parseInt(els.inputSuffer.value, 10) : 8,
      chai_consumed: els.inputChai.value ? parseInt(els.inputChai.value, 10) : 1,
    };
  }

  // Load and render categories
  async function loadCategories() {
    try {
      const res = await fetch('/api/categories');
      const data = await res.json();
      if (!els.vibeContainer) return;

      els.vibeContainer.innerHTML = '';
      
      // All vibes pill
      const allPill = document.createElement('button');
      allPill.className = 'vibe-pill active';
      allPill.textContent = '⚡ ALL VIBES';
      allPill.addEventListener('click', () => selectCategory(null, allPill));
      els.vibeContainer.appendChild(allPill);

      data.categories.forEach(cat => {
        const pill = document.createElement('button');
        pill.className = 'vibe-pill';
        pill.textContent = cat.label;
        pill.addEventListener('click', () => selectCategory(cat.id, pill));
        els.vibeContainer.appendChild(pill);
      });
    } catch (err) {
      console.error('Failed to load categories:', err);
    }
  }

  function selectCategory(catId, pillElem) {
    hudSound.playBeep(700, 0.04);
    state.activeCategory = catId;
    document.querySelectorAll('.vibe-pill').forEach(p => p.classList.remove('active'));
    if (pillElem) pillElem.classList.add('active');
    triggerGeneration();
  }

  // Generate quote via API
  async function triggerGeneration() {
    hudSound.playCyberChirp();
    
    // Quick HUD animation
    els.quoteHeadline.style.opacity = '0.4';
    els.quoteHeadline.style.transform = 'translateY(4px)';

    const payload = {
      category: state.activeCategory,
      telemetry: getTelemetryPayload(),
    };

    try {
      const res = await fetch('/api/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      
      state.currentQuote = data.primary;
      state.alternatives = data.alternatives || [];
      
      renderPrimaryQuote(data.primary);
      renderAlternatives(data.alternatives);
    } catch (err) {
      console.error('Generation failed:', err);
      showToast('Engine Error. Using local fallback.');
    } finally {
      els.quoteHeadline.style.opacity = '1';
      els.quoteHeadline.style.transform = 'translateY(0)';
    }
  }

  // Render primary quote
  function renderPrimaryQuote(quote) {
    if (!quote) return;

    els.quoteHeadline.textContent = quote.headline;
    els.quoteSubtext.textContent = quote.subtext || '';
    els.quoteVibeBadge.textContent = quote.source_vibe;
    els.quoteTagsBadge.textContent = (quote.tags || []).map(t => `#${t}`).join(' ');

    // Previews
    els.stravaTitlePreview.textContent = quote.strava_title;
    els.stravaDescPreview.textContent = quote.strava_description;
    els.whatsappStatusPreview.textContent = quote.whatsapp_status;
    els.whatsappChatPreview.textContent = quote.whatsapp_chat;

    // Character metrics
    const stravaLen = quote.strava_title.length;
    const stravaPct = Math.min(100, Math.round((stravaLen / 60) * 100));
    els.stravaGaugeFill.style.width = `${stravaPct}%`;
    els.stravaGaugeText.textContent = `${stravaLen}/60 chars`;

    const waLen = quote.whatsapp_status.length;
    const waPct = Math.min(100, Math.round((waLen / 139) * 100));
    els.waGaugeFill.style.width = `${waPct}%`;
    els.waGaugeText.textContent = `${waLen}/139 chars`;

    // Star state
    updateStarButton();
  }

  // Render alternatives stream
  function renderAlternatives(alts) {
    if (!els.alternativesList) return;
    els.alternativesList.innerHTML = '';

    alts.forEach(alt => {
      const card = document.createElement('div');
      card.className = 'alt-card';
      card.innerHTML = `
        <div class="alt-headline">${alt.headline}</div>
        <div class="alt-meta">${alt.source_vibe} • Click to activate</div>
      `;
      card.addEventListener('click', () => {
        hudSound.playBeep(800, 0.05);
        state.currentQuote = alt;
        renderPrimaryQuote(alt);
        showToast('Selected alternate quote');
      });
      els.alternativesList.appendChild(card);
    });
  }

  // Favorites logic
  function updateStarButton() {
    if (!els.starBtn || !state.currentQuote) return;
    const isSaved = state.favorites.some(f => f.id === state.currentQuote.id);
    if (isSaved) {
      els.starBtn.classList.add('starred');
      els.starBtn.innerHTML = '★';
    } else {
      els.starBtn.classList.remove('starred');
      els.starBtn.innerHTML = '☆';
    }
  }

  if (els.starBtn) {
    els.starBtn.addEventListener('click', () => {
      if (!state.currentQuote) return;
      const idx = state.favorites.findIndex(f => f.id === state.currentQuote.id);
      if (idx >= 0) {
        state.favorites.splice(idx, 1);
        showToast('Removed from favorites');
      } else {
        state.favorites.push(state.currentQuote);
        hudSound.playSuccessConfirm();
        showToast('★ Saved to favorites!');
      }
      localStorage.setItem('aero_favorites', JSON.stringify(state.favorites));
      updateStarButton();
    });
  }

  // Preset Buttons (Hyderabad FD routes)
  document.querySelectorAll('.btn-preset').forEach(btn => {
    btn.addEventListener('click', () => {
      hudSound.playBeep(650, 0.04);
      const dist = btn.dataset.dist;
      const speed = btn.dataset.speed;
      const elev = btn.dataset.elev;
      const loc = btn.dataset.loc;

      if (dist) els.inputDist.value = dist;
      if (speed) els.inputSpeed.value = speed;
      if (elev) els.inputElev.value = elev;
      if (loc) els.inputLocation.value = loc;

      showToast(`Loaded Preset: ${loc}`);
      triggerGeneration();
    });
  });

  // Export copy button event handlers
  document.querySelectorAll('[data-copy-target]').forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.copyTarget;
      let text = '';
      let label = 'Quote';
      if (target === 'strava-title') {
        text = state.currentQuote ? state.currentQuote.strava_title : els.stravaTitlePreview.textContent;
        label = 'Strava Title';
      } else if (target === 'strava-full') {
        text = state.currentQuote ? state.currentQuote.strava_description : els.stravaDescPreview.textContent;
        label = 'Strava Description';
      } else if (target === 'whatsapp-status') {
        text = state.currentQuote ? state.currentQuote.whatsapp_status : els.whatsappStatusPreview.textContent;
        label = 'WhatsApp Status';
      } else if (target === 'whatsapp-chat') {
        text = state.currentQuote ? state.currentQuote.whatsapp_chat : els.whatsappChatPreview.textContent;
        label = 'WhatsApp Broadcast';
      }
      if (text) copyToClipboard(text, label);
    });
  });

  // Direct WhatsApp launch
  if (els.btnOpenWhatsApp) {
    els.btnOpenWhatsApp.addEventListener('click', () => {
      if (!state.currentQuote) return;
      hudSound.playBeep(900, 0.06);
      const text = encodeURIComponent(state.currentQuote.whatsapp_status);
      const url = `https://api.whatsapp.com/send?text=${text}`;
      window.open(url, '_blank');
    });
  }

  // Social Canvas Modal
  if (els.btnSocialCard) {
    els.btnSocialCard.addEventListener('click', () => {
      if (!state.currentQuote) return;
      hudSound.playBeep(1000, 0.06);
      state.cardRenderer.render(state.currentQuote);
      els.cardModal.classList.add('open');
    });
  }

  if (els.btnCloseModal) {
    els.btnCloseModal.addEventListener('click', () => {
      els.cardModal.classList.remove('open');
    });
  }

  if (els.btnDownloadCard) {
    els.btnDownloadCard.addEventListener('click', () => {
      hudSound.playSuccessConfirm();
      state.cardRenderer.download();
      showToast('✔ Image downloaded!');
    });
  }

  // Custom Quote Modal
  if (els.btnOpenCustomModal) {
    els.btnOpenCustomModal.addEventListener('click', () => {
      els.customModal.classList.add('open');
    });
  }

  if (els.btnCloseCustomModal) {
    els.btnCloseCustomModal.addEventListener('click', () => {
      els.customModal.classList.remove('open');
    });
  }

  if (els.btnSaveCustomQuote) {
    els.btnSaveCustomQuote.addEventListener('click', async () => {
      const headline = els.customHeadline.value.trim();
      const subtext = els.customSubtext.value.trim();
      const cat = els.customCategory.value;

      if (!headline) {
        alert('Please enter a quote headline');
        return;
      }

      try {
        const res = await fetch('/api/quotes/custom', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            headline,
            subtext,
            category: cat,
            tags: ['rider-custom', 'peloton']
          })
        });

        const created = await res.json();
        state.currentQuote = created;
        renderPrimaryQuote(created);
        els.customModal.classList.remove('open');
        els.customHeadline.value = '';
        els.customSubtext.value = '';
        hudSound.playSuccessConfirm();
        showToast('✔ Custom quote activated into live pool!');
      } catch (err) {
        console.error('Failed to save custom quote:', err);
      }
    });
  }

  // Main Generator Button
  if (els.btnGenerate) {
    els.btnGenerate.addEventListener('click', () => {
      triggerGeneration();
    });
  }

  // Keyboard shortcut: Spacebar or 'R' rolls a new quote (when not typing in inputs)
  document.addEventListener('keydown', (e) => {
    if (['INPUT', 'TEXTAREA', 'SELECT'].includes(e.target.tagName)) return;
    if (e.code === 'Space' || e.key === 'r' || e.key === 'R') {
      e.preventDefault();
      triggerGeneration();
    }
  });

  // Initial Boot
  loadCategories();
  triggerGeneration();
});
