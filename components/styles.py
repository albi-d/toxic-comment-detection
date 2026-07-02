HERO_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=DM+Mono:wght@400;500&display=swap');

*, html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

/* PENTING: kembalikan font Material Icons agar tidak render sebagai teks */
[data-testid="stIconMaterial"],
[data-testid="stIconMaterial"] * {
    font-family: 'Material Symbols Rounded', 'Material Icons', sans-serif !important;
}

#MainMenu, footer, header { visibility: hidden; }

/* Remove default streamlit padding */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    max-width: 100% !important;
}

/* ── HERO PAGE ──────────────────────────────── */
.stApp[data-page="hero"] {
    background: #07070f;
}

.hero-section {
    background: linear-gradient(160deg, #07070f 0%, #0d0d1a 50%, #07070f 100%);
    padding: 5rem 2rem 4rem;
    text-align: center;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(99, 102, 241, 0.1);
    border: 1px solid rgba(99, 102, 241, 0.25);
    color: #a5b4fc;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 7px 18px;
    border-radius: 100px;
    margin-bottom: 2rem;
}

.hero-badge-dot {
    width: 6px;
    height: 6px;
    background: #818cf8;
    border-radius: 50%;
    flex-shrink: 0;
}

.hero-title {
    font-size: clamp(2.6rem, 5vw, 3.8rem);
    font-weight: 800;
    line-height: 1.1;
    margin: 0 auto 1.2rem;
    letter-spacing: -0.04em;
    max-width: 640px;
}

.hero-title-white {
    color: #f1f5f9;
    display: block;
}

.hero-title-gradient {
    background: linear-gradient(135deg, #6366f1 0%, #a855f7 55%, #ec4899 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    display: block;
}

.hero-subtitle {
    font-size: 1rem;
    color: #64748b;
    line-height: 1.75;
    max-width: 480px;
    margin: 0 auto 2.5rem;
    font-weight: 400;
}

.hero-subtitle b {
    color: #94a3b8;
    font-weight: 500;
}

.hero-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    justify-content: center;
    margin-bottom: 3rem;
}

.hero-pill {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    color: #64748b;
    font-size: 0.75rem;
    font-weight: 500;
    padding: 6px 14px;
    border-radius: 100px;
}

.hero-divider {
    width: 48px;
    height: 2px;
    background: linear-gradient(90deg, #6366f1, #a855f7);
    border-radius: 2px;
    margin: 0 auto 3rem;
}

.hero-stats-row {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 0;
    margin-bottom: 3.5rem;
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    background: rgba(255,255,255,0.02);
    overflow: hidden;
    max-width: 400px;
    margin-left: auto;
    margin-right: auto;
    margin-bottom: 3.5rem;
}

.hero-stat-item {
    flex: 1;
    padding: 1.25rem 1rem;
    text-align: center;
    border-right: 1px solid rgba(255,255,255,0.07);
}

.hero-stat-item:last-child {
    border-right: none;
}

.hero-stat-val {
    font-size: 1.4rem;
    font-weight: 800;
    color: #f1f5f9;
    letter-spacing: -0.03em;
    line-height: 1;
}

.hero-stat-lbl {
    font-size: 0.68rem;
    color: #475569;
    margin-top: 4px;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

/* ── START BUTTON (Hero) ─── */
.stButton > button[kind="primary"],
.stButton > button {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    letter-spacing: 0.01em !important;
    transition: all 0.2s ease !important;
}

/* ── DETECTION PAGE ─────────────────────────── */
.det-page {
    background: #f8f9fc;
    min-height: 100vh;
    padding: 2rem 1rem 4rem;
}

.det-header {
    text-align: center;
    padding: 1.5rem 1rem 1.75rem;
    border-bottom: 1px solid #e8eaf0;
    margin-bottom: 2rem;
    max-width: 640px;
    margin-left: auto;
    margin-right: auto;
}

.det-badge {
    display: inline-block;
    background: #ede9fe;
    color: #6d28d9;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    padding: 4px 14px;
    border-radius: 100px;
    margin-bottom: 0.75rem;
}

.det-title {
    font-size: 1.6rem;
    font-weight: 700;
    color: #0f172a;
    letter-spacing: -0.02em;
    margin-bottom: 0.35rem;
    line-height: 1.2;
}

.det-desc {
    font-size: 0.85rem;
    color: #94a3b8;
    font-weight: 400;
}

/* Result cards */
.result-toxic {
    background: #fff5f5;
    border: 1.5px solid #fca5a5;
    border-radius: 14px;
    padding: 1.75rem 1.5rem;
    text-align: center;
    margin-bottom: 1rem;
}

.result-nontoxic {
    background: #f0fdf4;
    border: 1.5px solid #86efac;
    border-radius: 14px;
    padding: 1.75rem 1.5rem;
    text-align: center;
    margin-bottom: 1rem;
}

.result-icon { font-size: 2.2rem; margin-bottom: 0.4rem; line-height: 1; }
.result-label-toxic  { font-size: 1.4rem; font-weight: 800; color: #dc2626; margin-bottom: 0.25rem; letter-spacing: -0.01em; }
.result-label-nontoxic { font-size: 1.4rem; font-weight: 800; color: #16a34a; margin-bottom: 0.25rem; letter-spacing: -0.01em; }
.result-desc-toxic   { font-size: 0.82rem; color: #f87171; }
.result-desc-nontoxic { font-size: 0.82rem; color: #4ade80; }

/* Prob pills */
.prob-row {
    display: flex;
    gap: 0.6rem;
    margin-bottom: 1rem;
}

.prob-pill {
    flex: 1;
    background: #ffffff;
    border: 1px solid #e8eaf0;
    border-radius: 12px;
    padding: 0.9rem 0.75rem;
    text-align: center;
}

.prob-value-safe  { font-size: 1.35rem; font-weight: 800; color: #16a34a; letter-spacing: -0.02em; }
.prob-value-toxic { font-size: 1.35rem; font-weight: 800; color: #dc2626; letter-spacing: -0.02em; }
.prob-label { font-size: 0.68rem; color: #94a3b8; margin-top: 3px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.06em; }

/* Empty state */
.empty-state {
    background: #ffffff;
    border: 1.5px dashed #dde1ea;
    border-radius: 14px;
    padding: 3rem 1.5rem;
    text-align: center;
    margin-bottom: 1rem;
}

.empty-icon { font-size: 1.8rem; margin-bottom: 0.5rem; opacity: 0.5; }
.empty-text { font-size: 0.85rem; color: #94a3b8; font-weight: 400; }

/* Preprocessing box */
.preproc-box {
    background: #f8f9fc;
    border: 1px solid #e8eaf0;
    border-radius: 10px;
    padding: 0.85rem 1rem;
    font-family: 'DM Mono', monospace;
    font-size: 0.78rem;
    color: #475569;
    word-break: break-word;
    line-height: 1.6;
}

.preproc-label {
    font-size: 0.68rem;
    font-weight: 700;
    color: #94a3b8;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.35rem;
}

/* Section label */
.section-label {
    font-size: 0.68rem;
    font-weight: 700;
    color: #94a3b8;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 0.75rem;
}

.divider {
    height: 1px;
    background: #f1f3f8;
    margin: 1.25rem 0;
}

/* Stat row CSV */
.stat-row {
    display: flex;
    gap: 0.6rem;
    margin: 1rem 0;
}

.stat-card {
    flex: 1;
    background: #ffffff;
    border: 1px solid #e8eaf0;
    border-radius: 12px;
    padding: 1rem 0.75rem;
    text-align: center;
}

.stat-value       { font-size: 1.5rem; font-weight: 800; color: #0f172a; letter-spacing: -0.03em; }
.stat-value-toxic { font-size: 1.5rem; font-weight: 800; color: #dc2626; letter-spacing: -0.03em; }
.stat-value-safe  { font-size: 1.5rem; font-weight: 800; color: #16a34a; letter-spacing: -0.03em; }
.stat-label { font-size: 0.68rem; color: #94a3b8; font-weight: 600; margin-top: 3px; text-transform: uppercase; letter-spacing: 0.06em; }

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 0 !important;
    background: #f1f3f8 !important;
    border-radius: 10px !important;
    padding: 4px !important;
    margin-bottom: 1.5rem !important;
    border: none !important;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 7px !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    color: #64748b !important;
    padding: 0.45rem 1.1rem !important;
    border: none !important;
}

.stTabs [aria-selected="true"] {
    background: #ffffff !important;
    color: #0f172a !important;
    font-weight: 600 !important;
    box-shadow: 0 1px 4px rgba(0,0,0,0.08) !important;
}

/* Textarea */
.stTextArea textarea {
    border: 1.5px solid #e2e6f0 !important;
    border-radius: 12px !important;
    font-size: 0.88rem !important;
    font-family: 'Inter', sans-serif !important;
    color: #0f172a !important;
    background: #ffffff !important;
    padding: 0.85rem 1rem !important;
    resize: none !important;
}

.stTextArea textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.1) !important;
}

/* Primary/Detect button */
div[data-testid="stVerticalBlock"] .stButton > button {
    background: #0f172a !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 10px !important;
    font-size: 0.86rem !important;
    font-weight: 600 !important;
    padding: 0.7rem 1.5rem !important;
    width: 100% !important;
}

div[data-testid="stVerticalBlock"] .stButton > button:hover {
    background: #1e293b !important;
}

/* Back button */
.back-btn .stButton > button {
    background: transparent !important;
    color: #64748b !important;
    border: 1px solid #e2e6f0 !important;
    border-radius: 8px !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    padding: 0.4rem 1rem !important;
    width: auto !important;
}

.back-btn .stButton > button:hover {
    background: #f8f9fc !important;
    color: #0f172a !important;
}

/* File uploader */
[data-testid="stFileUploader"] section {
    background: #f8f9fc !important;
    border: 1.5px dashed #dde1ea !important;
    border-radius: 12px !important;
}

[data-testid="stFileUploadDropzone"] button {
    background: #0f172a !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    font-size: 0.8rem !important;
    font-weight: 600 !important;
    gap: 0 !important;
}

/* Download button */
.stDownloadButton > button {
    background: #f1f3f8 !important;
    color: #0f172a !important;
    border: 1px solid #e2e6f0 !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 0.83rem !important;
    width: 100% !important;
}

.stDownloadButton > button:hover {
    background: #e8eaf0 !important;
}

/* Sembunyikan teks fallback icon di expander header */
[data-testid="stExpander"] summary [data-testid="stIconMaterial"],
[data-testid="stExpander"] summary svg,
[data-testid="stExpander"] summary [class*="icon"] {
    display: none !important;
}

/* Pastikan label expander tampil normal */
[data-testid="stExpander"] summary p {
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    color: #475569 !important;
}

/* Alert */
.stAlert {
    border-radius: 10px !important;
    font-size: 0.83rem !important;
}

/* Responsive */
@media (max-width: 640px) {
    .hero-title { font-size: 2.2rem; }
    .prob-row { flex-direction: column; }
    .stat-row { flex-direction: column; }
    .hero-stats-row { max-width: 100%; }
}

/* ── Highlight box (fitur 1) ────────────────── */
.highlight-box {
    background: #fff8f8;
    border: 1px solid #fecaca;
    border-radius: 10px;
    padding: 0.85rem 1rem;
    font-size: 0.88rem;
    color: #1e293b;
    line-height: 1.75;
    word-break: break-word;
    margin-bottom: 0.75rem;
}

/* ── Top kata berpengaruh (fitur 5) ─────────── */
.topword-container {
    background: #ffffff;
    border: 1px solid #e8eaf0;
    border-radius: 12px;
    padding: 0.85rem 1rem;
    margin-bottom: 0.75rem;
}

.topword-row {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 0.5rem;
}

.topword-row:last-child { margin-bottom: 0; }

.topword-label {
    font-size: 0.78rem;
    font-weight: 600;
    color: #334155;
    width: 90px;
    flex-shrink: 0;
    font-family: 'DM Mono', monospace;
}

.topword-bar-wrap {
    flex: 1;
    background: #f1f5f9;
    border-radius: 100px;
    height: 6px;
    overflow: hidden;
}

.topword-bar {
    height: 100%;
    border-radius: 100px;
    transition: width 0.4s ease;
}

.topword-score {
    font-size: 0.68rem;
    color: #94a3b8;
    width: 50px;
    text-align: right;
    flex-shrink: 0;
    font-family: 'DM Mono', monospace;
}
</style>
"""
