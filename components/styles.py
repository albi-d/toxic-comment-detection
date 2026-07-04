HERO_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,300;0,14..32,400;0,14..32,500;0,14..32,600;0,14..32,700;0,14..32,800;1,14..32,400&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Reset & Base ─────────────────────────── */
*, html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
    box-sizing: border-box;
}

[data-testid="stIconMaterial"],
[data-testid="stIconMaterial"] * {
    font-family: 'Material Symbols Rounded', 'Material Icons', sans-serif !important;
}

#MainMenu, footer, header { visibility: hidden; }

.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    max-width: 100% !important;
}

/* ══════════════════════════════════════════
   HERO PAGE
══════════════════════════════════════════ */

/* ── Tabs ────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {
    gap: 0 !important;
    background: rgba(255,255,255,0.06) !important;
    border-radius: 10px !important;
    padding: 3px !important;
    margin-bottom: 1.5rem !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    overflow-x: auto !important;
    flex-wrap: nowrap !important;
    -webkit-overflow-scrolling: touch !important;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 7px !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    color: #64748b !important;
    padding: 0.42rem 0.9rem !important;
    border: none !important;
    white-space: nowrap !important;
    flex-shrink: 0 !important;
    letter-spacing: 0.01em !important;
}

.stTabs [aria-selected="true"] {
    background: #ffffff !important;
    color: #0f172a !important;
    font-weight: 600 !important;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1) !important;
}

/* ── Textarea ────────────────────────────── */
.stTextArea textarea {
    border: 1.5px solid #e2e8f0 !important;
    border-radius: 10px !important;
    font-size: 0.88rem !important;
    line-height: 1.6 !important;
    color: #1e293b !important;
    background: #ffffff !important;
    padding: 0.85rem 1rem !important;
    resize: none !important;
    transition: border-color 0.15s, box-shadow 0.15s !important;
}

.stTextArea textarea::placeholder { color: #cbd5e1 !important; }

.stTextArea textarea:focus {
    border-color: #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.08) !important;
    outline: none !important;
}

/* ── Buttons ─────────────────────────────── */
div[data-testid="stVerticalBlock"] .stButton > button {
    background: #0f172a !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 9px !important;
    font-size: 0.86rem !important;
    font-weight: 600 !important;
    padding: 0.65rem 1.5rem !important;
    width: 100% !important;
    letter-spacing: 0.015em !important;
    transition: background 0.15s !important;
    box-shadow: none !important;
}

div[data-testid="stVerticalBlock"] .stButton > button:hover {
    background: #1e293b !important;
}

/* Back button */
.back-wrap {
    display: flex;
    justify-content: center;
    margin-bottom: 1.5rem;
}

.back-wrap .stButton > button {
    background: #ffffff !important;
    color: #64748b !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 8px !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    padding: 0.42rem 1.1rem !important;
    width: auto !important;
    min-width: 140px !important;
    box-shadow: 0 1px 2px rgba(0,0,0,0.04) !important;
    letter-spacing: 0.01em !important;
}

.back-wrap .stButton > button:hover {
    background: #f8fafc !important;
    color: #334155 !important;
    border-color: #cbd5e1 !important;
}

/* ── File uploader ───────────────────────── */
[data-testid="stFileUploader"] section {
    background: #f8fafc !important;
    border: 1.5px dashed #e2e8f0 !important;
    border-radius: 10px !important;
    padding: 1.25rem !important;
}

[data-testid="stFileUploadDropzone"] button {
    background: #0f172a !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 7px !important;
    font-size: 0.78rem !important;
    font-weight: 600 !important;
}

/* ── Download button ─────────────────────── */
.stDownloadButton > button {
    background: #f1f5f9 !important;
    color: #334155 !important;
    border: 1px solid #e2e8f0 !important;
    border-radius: 9px !important;
    font-weight: 600 !important;
    font-size: 0.84rem !important;
    width: 100% !important;
    letter-spacing: 0.01em !important;
}

.stDownloadButton > button:hover {
    background: #e2e8f0 !important;
}

/* ── Selectbox ───────────────────────────── */
[data-testid="stSelectbox"] > div > div {
    border: 1.5px solid #e2e8f0 !important;
    border-radius: 9px !important;
    font-size: 0.84rem !important;
    background: #ffffff !important;
}

/* ── Expander ────────────────────────────── */
[data-testid="stExpander"] {
    border: 1px solid #e2e8f0 !important;
    border-radius: 10px !important;
    background: #ffffff !important;
}

[data-testid="stExpander"] summary {
    padding: 0.65rem 1rem !important;
    font-size: 0.83rem !important;
    font-weight: 500 !important;
    color: #475569 !important;
}

[data-testid="stExpander"] summary [data-testid="stIconMaterial"],
[data-testid="stExpander"] summary svg {
    display: none !important;
}

/* ── Alert ───────────────────────────────── */
.stAlert {
    border-radius: 9px !important;
    font-size: 0.83rem !important;
    border-left-width: 3px !important;
}

/* ══════════════════════════════════════════
   DETECTION PAGE COMPONENTS
══════════════════════════════════════════ */

/* ── Section label ───────────────────────── */
.section-label {
    font-size: 0.67rem;
    font-weight: 700;
    color: #94a3b8;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
    display: block;
}

.divider {
    height: 1px;
    background: #f1f5f9;
    margin: 1.25rem 0;
}

/* ── Prob pills ──────────────────────────── */
.prob-row {
    display: flex;
    gap: 0.5rem;
    margin-bottom: 0.875rem;
}

.prob-pill {
    flex: 1;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 0.8rem 0.5rem;
    text-align: center;
    min-width: 0;
}

.prob-value-safe  { font-size: 1.25rem; font-weight: 800; color: #16a34a; letter-spacing: -0.02em; line-height: 1; }
.prob-value-toxic { font-size: 1.25rem; font-weight: 800; color: #dc2626; letter-spacing: -0.02em; line-height: 1; }
.prob-label {
    font-size: 0.62rem;
    color: #94a3b8;
    margin-top: 4px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    display: block;
}

/* ── Stat cards ──────────────────────────── */
.stat-row {
    display: flex;
    gap: 0.5rem;
    margin: 0.875rem 0;
}

.stat-card {
    flex: 1;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 0.9rem 0.5rem;
    text-align: center;
    min-width: 0;
}

.stat-value       { font-size: 1.45rem; font-weight: 800; color: #0f172a; letter-spacing: -0.03em; line-height: 1; }
.stat-value-toxic { font-size: 1.45rem; font-weight: 800; color: #dc2626; letter-spacing: -0.03em; line-height: 1; }
.stat-value-safe  { font-size: 1.45rem; font-weight: 800; color: #16a34a; letter-spacing: -0.03em; line-height: 1; }
.stat-label {
    font-size: 0.62rem;
    color: #94a3b8;
    font-weight: 600;
    margin-top: 4px;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    display: block;
}

/* ── Empty state ─────────────────────────── */
.empty-state {
    background: #ffffff;
    border: 1.5px dashed #e2e8f0;
    border-radius: 12px;
    padding: 2.5rem 1.5rem;
    text-align: center;
    margin-bottom: 1rem;
}

.empty-icon { font-size: 1.6rem; margin-bottom: 0.4rem; opacity: 0.4; display: block; }
.empty-text { font-size: 0.83rem; color: #94a3b8; font-weight: 400; line-height: 1.6; }

/* ── Preprocessing box ───────────────────── */
.preproc-box {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 0.75rem 0.9rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.77rem;
    color: #475569;
    word-break: break-word;
    line-height: 1.65;
}

.preproc-label {
    font-size: 0.65rem;
    font-weight: 700;
    color: #94a3b8;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
    display: block;
}

/* ── Highlight box ───────────────────────── */
.highlight-box {
    background: #fefce8;
    border: 1px solid #fde68a;
    border-radius: 9px;
    padding: 0.8rem 0.9rem;
    font-size: 0.87rem;
    color: #1e293b;
    line-height: 1.75;
    word-break: break-word;
    margin-bottom: 0.75rem;
}

/* ── Top words chart ─────────────────────── */
.topword-container {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 0.9rem 1rem;
    margin-bottom: 0.75rem;
}

.topword-row {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 0.55rem;
}

.topword-row:last-child { margin-bottom: 0; }

.topword-label {
    font-size: 0.76rem;
    font-weight: 600;
    color: #334155;
    width: 88px;
    flex-shrink: 0;
    font-family: 'JetBrains Mono', monospace;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.topword-bar-wrap {
    flex: 1;
    background: #f1f5f9;
    border-radius: 100px;
    height: 5px;
    overflow: hidden;
}

.topword-bar {
    height: 100%;
    border-radius: 100px;
}

.topword-score {
    font-size: 0.66rem;
    color: #94a3b8;
    width: 46px;
    text-align: right;
    flex-shrink: 0;
    font-family: 'JetBrains Mono', monospace;
}

/* ── Responsive ──────────────────────────── */
@media (max-width: 640px) {
    .block-container {
        padding-left: 0.75rem !important;
        padding-right: 0.75rem !important;
    }

    .prob-row { flex-wrap: wrap; }
    .prob-pill { min-width: calc(33% - 0.35rem); }

    .stat-row { flex-wrap: wrap; }
    .stat-card { min-width: calc(33% - 0.35rem); }

    .stTabs [data-baseweb="tab"] {
        font-size: 0.74rem !important;
        padding: 0.38rem 0.6rem !important;
    }

    .topword-label { width: 68px; font-size: 0.7rem; }
    .topword-score { width: 40px; font-size: 0.62rem; }
}
</style>
"""
