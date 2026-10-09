/**
 * Web Audio API synthesizer for futuristic HUD sound design.
 * Pure dynamic audio synthesis - zero external asset dependencies.
 */

class HudAudioEngine {
  constructor() {
    this.ctx = null;
    this.enabled = localStorage.getItem('hud_audio_enabled') !== 'false';
  }

  _initContext() {
    if (!this.ctx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      if (AudioContext) {
        this.ctx = new AudioContext();
      }
    }
    if (this.ctx && this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  toggle() {
    this.enabled = !this.enabled;
    localStorage.setItem('hud_audio_enabled', this.enabled ? 'true' : 'false');
    if (this.enabled) {
      this.playBeep(880, 0.08, 'sine');
    }
    return this.enabled;
  }

  playBeep(freq = 600, duration = 0.05, type = 'sine') {
    if (!this.enabled) return;
    try {
      this._initContext();
      if (!this.ctx) return;

      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = type;
      osc.frequency.setValueAtTime(freq, this.ctx.currentTime);

      gain.gain.setValueAtTime(0.04, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + duration);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start();
      osc.stop(this.ctx.currentTime + duration);
    } catch (e) {
      console.warn('Audio synthesis bypassed:', e);
    }
  }

  playCyberChirp() {
    if (!this.enabled) return;
    try {
      this._initContext();
      if (!this.ctx) return;

      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(440, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(1320, this.ctx.currentTime + 0.08);

      gain.gain.setValueAtTime(0.03, this.ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.0001, this.ctx.currentTime + 0.08);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start();
      osc.stop(this.ctx.currentTime + 0.08);
    } catch (e) {
      console.warn('Audio synthesis bypassed:', e);
    }
  }

  playSuccessConfirm() {
    if (!this.enabled) return;
    try {
      this._initContext();
      if (!this.ctx) return;

      const now = this.ctx.currentTime;
      [587.33, 880].forEach((freq, idx) => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, now + (idx * 0.05));
        gain.gain.setValueAtTime(0.04, now + (idx * 0.05));
        gain.gain.exponentialRampToValueAtTime(0.0001, now + (idx * 0.05) + 0.1);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now + (idx * 0.05));
        osc.stop(now + (idx * 0.05) + 0.1);
      });
    } catch (e) {
      console.warn('Audio synthesis bypassed:', e);
    }
  }
}

const hudSound = new HudAudioEngine();
