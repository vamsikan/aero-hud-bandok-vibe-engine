/**
 * HTML5 Canvas Graphic Card Generator.
 * Creates an ultra-sleek, futuristic 1080x1080 social share card
 * with telemetry gauges, neon grid lines, and high-impact typography.
 */

class HudCardRenderer {
  constructor(canvasId) {
    this.canvas = document.getElementById(canvasId);
    this.ctx = this.canvas ? this.canvas.getContext('2d') : null;
    this.width = 1080;
    this.height = 1080;
  }

  render(quoteData) {
    if (!this.canvas || !this.ctx) return;

    this.canvas.width = this.width;
    this.canvas.height = this.height;
    const ctx = this.ctx;

    const meta = quoteData.card_metadata || {};
    const headline = meta.headline || quoteData.headline || "Aero Telemetry";
    const subtext = meta.subtext || quoteData.subtext || "";
    const dist = meta.distance || "42.0 KM";
    const speed = meta.speed || "31.4 KM/H";
    const elevation = meta.elevation || "240 M";
    const location = meta.location || "Financial District, Hyderabad";
    const bike = meta.bike || "Basso Venta R";
    const vibe = meta.vibe || "Bandók Aero Engine";
    const timestamp = meta.timestamp || "2026 // MORNING PELOTÓN";

    // 1. Deep Space Carbon Background
    const bgGrad = ctx.createLinearGradient(0, 0, this.width, this.height);
    bgGrad.addColorStop(0, '#06080d');
    bgGrad.addColorStop(0.5, '#0a0d17');
    bgGrad.addColorStop(1, '#05070a');
    ctx.fillStyle = bgGrad;
    ctx.fillRect(0, 0, this.width, this.height);

    // 2. Cyber Mesh Grid
    ctx.strokeStyle = 'rgba(0, 245, 212, 0.04)';
    ctx.lineWidth = 1;
    const gridSize = 60;
    for (let x = 0; x < this.width; x += gridSize) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, this.height);
      ctx.stroke();
    }
    for (let y = 0; y < this.height; y += gridSize) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(this.width, y);
      ctx.stroke();
    }

    // 3. Glowing Outer Border & Neon Accents
    ctx.strokeStyle = 'rgba(0, 245, 212, 0.4)';
    ctx.lineWidth = 3;
    ctx.strokeRect(40, 40, this.width - 80, this.height - 80);

    // Corner HUD Brackets
    const bracketSize = 36;
    ctx.strokeStyle = '#00f5d4';
    ctx.lineWidth = 4;

    // Top-Left
    ctx.beginPath();
    ctx.moveTo(40, 40 + bracketSize); ctx.lineTo(40, 40); ctx.lineTo(40 + bracketSize, 40);
    ctx.stroke();
    // Top-Right
    ctx.beginPath();
    ctx.moveTo(this.width - 40 - bracketSize, 40); ctx.lineTo(this.width - 40, 40); ctx.lineTo(this.width - 40, 40 + bracketSize);
    ctx.stroke();
    // Bottom-Left
    ctx.beginPath();
    ctx.moveTo(40, this.height - 40 - bracketSize); ctx.lineTo(40, this.height - 40); ctx.lineTo(40 + bracketSize, this.height - 40);
    ctx.stroke();
    // Bottom-Right
    ctx.beginPath();
    ctx.moveTo(this.width - 40 - bracketSize, this.height - 40); ctx.lineTo(this.width - 40, this.height - 40); ctx.lineTo(this.width - 40, this.height - 40 - bracketSize);
    ctx.stroke();

    // 4. Header Bar
    ctx.fillStyle = 'rgba(0, 245, 212, 0.08)';
    ctx.fillRect(40, 40, this.width - 80, 80);

    // Italian Tricolore Accent on Top
    ctx.fillStyle = '#009246'; ctx.fillRect(60, 56, 16, 6);
    ctx.fillStyle = '#ffffff'; ctx.fillRect(76, 56, 16, 6);
    ctx.fillStyle = '#ce2b37'; ctx.fillRect(92, 56, 16, 6);

    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 24px "Orbitron", "Space Grotesk", sans-serif';
    ctx.fillText(`${bike.toUpperCase()} // AERO DIVISION`, 125, 66);

    ctx.fillStyle = '#00f5d4';
    ctx.font = '14px "JetBrains Mono", monospace';
    ctx.fillText(`HYD FINANCIAL DISTRICT // ${timestamp}`, 125, 94);

    // Bandók Vault Stamp on Right
    ctx.fillStyle = 'rgba(255, 159, 28, 0.9)';
    ctx.font = 'bold 15px "JetBrains Mono", monospace';
    ctx.textAlign = 'right';
    ctx.fillText('⚡ BANDÓK VIBE ENGINE', this.width - 65, 84);
    ctx.textAlign = 'left';

    // 5. Central Quote Block
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 46px "Orbitron", "Space Grotesk", sans-serif';
    const quoteX = 80;
    let currentY = 320;
    const maxTextWidth = this.width - 160;

    // Wrap headline text
    const words = headline.split(' ');
    let line = '';
    for (let n = 0; n < words.length; n++) {
      const testLine = line + words[n] + ' ';
      const metrics = ctx.measureText(testLine);
      if (metrics.width > maxTextWidth && n > 0) {
        ctx.fillText(line, quoteX, currentY);
        line = words[n] + ' ';
        currentY += 64;
      } else {
        line = testLine;
      }
    }
    ctx.fillText(line, quoteX, currentY);

    // Subtext / Punchline
    if (subtext) {
      currentY += 45;
      ctx.fillStyle = '#00f5d4';
      ctx.font = '26px "Inter", sans-serif';
      ctx.fillText(`"${subtext}"`, quoteX, currentY);
    }

    // 6. Telemetry Status Bar (Bottom)
    const telemetryY = this.height - 240;
    ctx.fillStyle = 'rgba(15, 21, 35, 0.9)';
    ctx.strokeStyle = 'rgba(0, 245, 212, 0.25)';
    ctx.lineWidth = 1;
    ctx.strokeRect(60, telemetryY, this.width - 120, 160);
    ctx.fillRect(60, telemetryY, this.width - 120, 160);

    const stats = [
      { label: 'DISTANCE', val: dist, color: '#00f5d4' },
      { label: 'AVG SPEED', val: speed, color: '#39ff14' },
      { label: 'ELEVATION', val: elevation, color: '#ff9f1c' },
      { label: 'SECTOR', val: 'HYD FD', color: '#ffffff' },
    ];

    const colWidth = (this.width - 120) / stats.length;
    stats.forEach((st, i) => {
      const colX = 60 + (i * colWidth) + 24;
      ctx.fillStyle = '#8b9bb4';
      ctx.font = '13px "Orbitron", sans-serif';
      ctx.fillText(st.label, colX, telemetryY + 45);

      ctx.fillStyle = st.color;
      ctx.font = 'bold 32px "JetBrains Mono", monospace';
      ctx.fillText(st.val, colX, telemetryY + 95);

      // Micro Gauge Bar
      ctx.fillStyle = 'rgba(255, 255, 255, 0.1)';
      ctx.fillRect(colX, telemetryY + 115, 120, 4);
      ctx.fillStyle = st.color;
      ctx.fillRect(colX, telemetryY + 115, 85, 4);
    });

    // 7. Route & Footer Signature
    ctx.fillStyle = '#8b9bb4';
    ctx.font = '14px "JetBrains Mono", monospace';
    ctx.fillText(`📍 ${location}`, 80, this.height - 52);

    ctx.textAlign = 'right';
    ctx.fillStyle = 'rgba(0, 245, 212, 0.7)';
    ctx.fillText('#BassoVentaR #Bandók #HydCycling #AeroHUD', this.width - 80, this.height - 52);
    ctx.textAlign = 'left';
  }

  download() {
    if (!this.canvas) return;
    const link = document.createElement('a');
    link.download = `AeroQuote_BassoVentaR_${Date.now()}.png`;
    link.href = this.canvas.toDataURL('image/png');
    link.click();
  }
}
