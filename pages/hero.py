import streamlit as st
import streamlit.components.v1 as components


def render_hero():
    """Hero section — bagian atas & bawah terpisah, CTA Streamlit native di tengah."""

    st.markdown("""<style>
    .stApp { background: #06060f !important; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    iframe { border: none !important; display: block !important; }
    iframe::-webkit-scrollbar { display: none !important; }
    div[data-testid="stVerticalBlock"] > div { margin-bottom: 0 !important; }
    /* CTA button */
    .cta-wrap { background: #06060f; padding: 1.25rem 1rem 0.5rem; display: flex; justify-content: center; }
    .cta-wrap .stButton > button {
        background: #6366f1 !important; color: #fff !important;
        border: none !important; border-radius: 10px !important;
        font-size: 0.9rem !important; font-weight: 600 !important;
        padding: 0.75rem 2.5rem !important; width: auto !important;
        min-width: 200px !important;
        box-shadow: 0 4px 20px rgba(99,102,241,0.35) !important;
    }
    .cta-wrap .stButton > button:hover { background: #4f46e5 !important; }
    </style>""", unsafe_allow_html=True)

    # ── ATAS: navbar + hero title + stats
    components.html("""<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{box-sizing:border-box;margin:0;padding:0;}
html,body{background:#06060f;font-family:system-ui,-apple-system,sans-serif;
  width:100%;overflow:hidden;}
@keyframes blink{0%,100%{opacity:1;}50%{opacity:0.35;}}
nav{display:flex;align-items:center;justify-content:space-between;
  padding:0.875rem 1.25rem;border-bottom:1px solid rgba(255,255,255,0.06);}
.logo{display:flex;align-items:center;gap:7px;}
.logo-icon{width:26px;height:26px;background:linear-gradient(135deg,#6366f1,#a78bfa);
  border-radius:6px;display:flex;align-items:center;justify-content:center;font-size:13px;}
.logo-name{font-size:0.88rem;font-weight:700;color:#f1f5f9;letter-spacing:-0.02em;}
.nav-links{display:flex;gap:1rem;}
.nav-links a{font-size:0.73rem;color:#475569;font-weight:500;text-decoration:none;cursor:pointer;}
.nav-links a:hover{color:#94a3b8;}
.hero{max-width:540px;margin:0 auto;padding:2.25rem 1.25rem 1.5rem;text-align:center;}
.badge{display:inline-flex;align-items:center;gap:6px;background:rgba(99,102,241,0.1);
  border:1px solid rgba(99,102,241,0.2);color:#a5b4fc;font-size:0.63rem;font-weight:600;
  letter-spacing:0.1em;text-transform:uppercase;padding:5px 14px;border-radius:100px;margin-bottom:1.4rem;}
.dot{width:5px;height:5px;background:#818cf8;border-radius:50%;animation:blink 2s infinite;display:inline-block;}
h1{font-size:clamp(1.85rem,7vw,3rem);font-weight:800;line-height:1.1;
  letter-spacing:-0.04em;margin:0 0 0.9rem;color:#f1f5f9;}
.grad{background:linear-gradient(135deg,#6366f1 0%,#a78bfa 50%,#e879f9 100%);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}
.sub{font-size:0.88rem;color:#64748b;line-height:1.7;max-width:380px;margin:0 auto;}
.sub b{color:#94a3b8;font-weight:500;}
.stats{display:flex;border:1px solid rgba(255,255,255,0.07);border-radius:12px;
  background:rgba(255,255,255,0.02);overflow:hidden;margin-top:1.5rem;}
.stat{flex:1;padding:1rem 0.4rem;text-align:center;border-right:1px solid rgba(255,255,255,0.06);}
.stat:last-child{border-right:none;}
.sv{font-size:1.2rem;font-weight:800;color:#f1f5f9;letter-spacing:-0.04em;line-height:1;}
.sl{font-size:0.55rem;color:#334155;margin-top:4px;font-weight:600;text-transform:uppercase;letter-spacing:0.07em;}
</style><body>
<nav>
  <div class="logo"><div class="logo-icon">&#128737;&#65039;</div><span class="logo-name">ToxicGuard</span></div>
  <div class="nav-links"><a href="#">Fitur</a><a href="#">Cara Kerja</a><a href="#">Contoh</a></div>
</nav>
<div class="hero">
  <div class="badge"><span class="dot"></span>NLP &nbsp;&middot;&nbsp; Bahasa Indonesia &nbsp;&middot;&nbsp; Open Source</div>
  <h1>Deteksi Komentar<br><span class="grad">Toxic Secara Instan</span></h1>
  <p class="sub">Analisis komentar Instagram menggunakan <b>Naive Bayes</b> + <b>TF-IDF</b>. Deteksi 3 level keparahan secara instan.</p>
  <div class="stats">
    <div class="stat"><div class="sv">3</div><div class="sl">Level</div></div>
    <div class="stat"><div class="sv">4</div><div class="sl">Mode</div></div>
    <div class="stat"><div class="sv">NLP</div><div class="sl">Teknologi</div></div>
    <div class="stat"><div class="sv">ID</div><div class="sl">Bahasa</div></div>
  </div>
</div>
</body></html>""", height=390, scrolling=False)

    # ── CTA Button — Streamlit native, tepat di bawah hero
    st.markdown('<div class="cta-wrap">', unsafe_allow_html=True)
    col_l, col_c, col_r = st.columns([1, 1.5, 1])
    with col_c:
        clicked = st.button("Mulai Analisis \u2192", use_container_width=True, key="btn_start")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""<div style="background:#06060f;text-align:center;padding:0.35rem 0 0.5rem;">
        <span style="font-size:0.67rem;color:#334155;letter-spacing:0.04em;">
            Gratis &nbsp;&middot;&nbsp; Tanpa Login &nbsp;&middot;&nbsp; Open Source
        </span>
    </div>""", unsafe_allow_html=True)

    # ── BAWAH: carousel, fitur, cara kerja, footer
    components.html("""<!DOCTYPE html>
<html><head><meta name="viewport" content="width=device-width,initial-scale=1">
<style>
*{box-sizing:border-box;margin:0;padding:0;}
html,body{background:#06060f;font-family:system-ui,-apple-system,sans-serif;
  width:100%;overflow-x:hidden;scrollbar-width:none;}
html::-webkit-scrollbar,body::-webkit-scrollbar{display:none;}
.sec{max-width:540px;margin:2.5rem auto 1.25rem;padding:0 1.25rem;text-align:center;}
.sec-tag{font-size:0.63rem;font-weight:700;color:#6366f1;letter-spacing:0.1em;
  text-transform:uppercase;display:block;margin-bottom:0.4rem;}
.sec h2{font-size:1.2rem;font-weight:700;color:#f1f5f9;letter-spacing:-0.03em;margin:0 0 0.3rem;}
.sec p{font-size:0.77rem;color:#64748b;margin:0;}
.cw{max-width:540px;margin:0 auto;padding:0 1.25rem 0.5rem;width:100%;}
.outer{overflow:hidden;border-radius:13px;width:100%;}
.track{display:flex;transition:transform 0.42s cubic-bezier(0.4,0,0.2,1);width:100%;}
.slide{min-width:100%;width:100%;flex-shrink:0;padding:1.15rem 1rem;
  background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.08);border-radius:13px;}
.r1{display:flex;align-items:flex-start;justify-content:space-between;gap:0.6rem;margin-bottom:0.75rem;}
.cmt{font-size:0.84rem;color:#e2e8f0;line-height:1.6;font-style:italic;flex:1;min-width:0;}
.bdg{font-size:0.57rem;font-weight:700;letter-spacing:0.06em;text-transform:uppercase;
  padding:3px 8px;border-radius:100px;flex-shrink:0;white-space:nowrap;margin-top:2px;}
.ba{background:#dcfce7;color:#15803d;}.bw{background:#fef3c7;color:#b45309;}
.bt{background:#fee2e2;color:#b91c1c;}
.sep{height:1px;background:rgba(255,255,255,0.06);margin:0.65rem 0;}
.mets{display:flex;gap:0.4rem;}
.m{flex:1;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.07);
  border-radius:8px;padding:0.5rem 0.25rem;text-align:center;min-width:0;}
.mv{font-size:0.9rem;font-weight:800;line-height:1;}
.ml{font-size:0.5rem;color:#64748b;margin-top:3px;text-transform:uppercase;letter-spacing:0.06em;display:block;}
.bwrap{background:rgba(255,255,255,0.08);border-radius:100px;height:3px;margin-top:0.6rem;overflow:hidden;}
.bfill{height:100%;border-radius:100px;background:linear-gradient(90deg,#22c55e 0%,#f59e0b 45%,#ef4444 75%);}
.bll{display:flex;justify-content:space-between;font-size:0.49rem;color:#475569;margin-top:2px;}
.navr{display:flex;justify-content:center;gap:0.5rem;margin-top:0.75rem;}
.nb{background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);
  color:#94a3b8;border-radius:8px;width:30px;height:30px;cursor:pointer;
  display:flex;align-items:center;justify-content:center;font-size:0.85rem;}
.nb:hover{background:rgba(99,102,241,0.2);color:#a5b4fc;}
.dots{display:flex;justify-content:center;gap:5px;margin-top:0.6rem;}
.dt{width:5px;height:5px;border-radius:50%;background:rgba(255,255,255,0.15);cursor:pointer;
  transition:background 0.2s,width 0.2s;}
.dt.on{background:#6366f1;width:14px;border-radius:100px;}
.grid{max-width:540px;margin:0 auto;padding:0 1.25rem;display:grid;grid-template-columns:1fr 1fr;gap:0.6rem;}
.card{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);border-radius:11px;padding:0.95rem 0.875rem;}
.card-ico{font-size:1.2rem;margin-bottom:0.45rem;}
.card h3{font-size:0.81rem;font-weight:600;color:#e2e8f0;margin:0 0 0.2rem;}
.card p{font-size:0.71rem;color:#64748b;line-height:1.5;margin:0;}
.pipe{max-width:540px;margin:0 auto;padding:0 1.25rem;}
.step{display:flex;gap:0.75rem;align-items:flex-start;}
.sl2{display:flex;flex-direction:column;align-items:center;flex-shrink:0;}
.sn{width:28px;height:28px;background:rgba(99,102,241,0.12);border:1px solid rgba(99,102,241,0.28);
  border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:0.68rem;font-weight:700;color:#a5b4fc;}
.sc{width:1px;height:1.4rem;background:rgba(255,255,255,0.06);margin:3px 0;}
.sb{padding-top:3px;padding-bottom:0.5rem;}
.sb h4{font-size:0.83rem;font-weight:600;color:#e2e8f0;margin:0 0 0.18rem;}
.sb p{font-size:0.73rem;color:#64748b;line-height:1.55;margin:0;}
.footer{max-width:540px;margin:2.5rem auto 0;padding:1.5rem 1.25rem 2.5rem;
  border-top:1px solid rgba(255,255,255,0.06);text-align:center;}
.fl{display:flex;align-items:center;justify-content:center;gap:7px;margin-bottom:0.5rem;}
.fi{width:20px;height:20px;background:linear-gradient(135deg,#6366f1,#a78bfa);
  border-radius:5px;display:flex;align-items:center;justify-content:center;font-size:10px;}
.fn{font-size:0.85rem;font-weight:700;color:#f1f5f9;letter-spacing:-0.02em;}
.footer p{font-size:0.71rem;color:#334155;margin:0 0 0.4rem;line-height:1.6;}
.footer small{font-size:0.65rem;color:#1e293b;}
</style><body>

<div class="sec"><span class="sec-tag">Contoh Deteksi</span><h2>Lihat Cara Kerjanya</h2>
<p>Contoh komentar nyata dan hasil deteksinya</p></div>
<div class="cw"><div class="outer"><div class="track" id="tr">
  <div class="slide">
    <div class="r1"><div class="cmt">"Selamat ya kak, kerjamu bagus banget! Semangat terus"</div><span class="bdg ba">Aman</span></div>
    <div class="sep"></div>
    <div class="mets">
      <div class="m"><div class="mv" style="color:#16a34a">92%</div><span class="ml">Non-Toxic</span></div>
      <div class="m"><div class="mv" style="color:#dc2626">8%</div><span class="ml">Toxic</span></div>
      <div class="m"><div class="mv" style="color:#16a34a;font-size:0.68rem">AMAN</div><span class="ml">Level</span></div>
    </div>
    <div class="bwrap"><div class="bfill" style="width:8%"></div></div>
    <div class="bll"><span>Aman</span><span>Perlu Perhatian</span><span>Sangat Toxic</span></div>
  </div>
  <div class="slide">
    <div class="r1"><div class="cmt">"Ih males banget sih, ngapain juga upload gitu"</div><span class="bdg bw">Perhatian</span></div>
    <div class="sep"></div>
    <div class="mets">
      <div class="m"><div class="mv" style="color:#16a34a">44%</div><span class="ml">Non-Toxic</span></div>
      <div class="m"><div class="mv" style="color:#dc2626">56%</div><span class="ml">Toxic</span></div>
      <div class="m"><div class="mv" style="color:#d97706;font-size:0.6rem">PERHATIAN</div><span class="ml">Level</span></div>
    </div>
    <div class="bwrap"><div class="bfill" style="width:56%"></div></div>
    <div class="bll"><span>Aman</span><span>Perlu Perhatian</span><span>Sangat Toxic</span></div>
  </div>
  <div class="slide">
    <div class="r1"><div class="cmt">"Dasar bodoh, mending ga usah posting deh!"</div><span class="bdg bt">Sangat Toxic</span></div>
    <div class="sep"></div>
    <div class="mets">
      <div class="m"><div class="mv" style="color:#16a34a">11%</div><span class="ml">Non-Toxic</span></div>
      <div class="m"><div class="mv" style="color:#dc2626">89%</div><span class="ml">Toxic</span></div>
      <div class="m"><div class="mv" style="color:#dc2626;font-size:0.62rem">SGT TOXIC</div><span class="ml">Level</span></div>
    </div>
    <div class="bwrap"><div class="bfill" style="width:89%"></div></div>
    <div class="bll"><span>Aman</span><span>Perlu Perhatian</span><span>Sangat Toxic</span></div>
  </div>
  <div class="slide">
    <div class="r1"><div class="cmt">"Foto nya aesthetic banget kak, filter apa yang dipakai?"</div><span class="bdg ba">Aman</span></div>
    <div class="sep"></div>
    <div class="mets">
      <div class="m"><div class="mv" style="color:#16a34a">97%</div><span class="ml">Non-Toxic</span></div>
      <div class="m"><div class="mv" style="color:#dc2626">3%</div><span class="ml">Toxic</span></div>
      <div class="m"><div class="mv" style="color:#16a34a;font-size:0.68rem">AMAN</div><span class="ml">Level</span></div>
    </div>
    <div class="bwrap"><div class="bfill" style="width:3%"></div></div>
    <div class="bll"><span>Aman</span><span>Perlu Perhatian</span><span>Sangat Toxic</span></div>
  </div>
</div></div>
<div class="navr"><button class="nb" onclick="mv(-1)">&#8592;</button>
<button class="nb" onclick="mv(1)">&#8594;</button></div>
<div class="dots" id="dots"></div></div>

<div class="sec"><span class="sec-tag">Fitur Utama</span><h2>Semua yang Kamu Butuhkan</h2>
<p>Dari satu komentar hingga ribuan data sekaligus</p></div>
<div class="grid">
  <div class="card"><div class="card-ico">&#128172;</div><h3>Deteksi Tunggal</h3>
  <p>Analisis satu komentar dengan highlight kata dan top kata berpengaruh.</p></div>
  <div class="card"><div class="card-ico">&#128203;</div><h3>Deteksi Batch</h3>
  <p>Paste banyak komentar sekaligus, maks 100 baris per sesi.</p></div>
  <div class="card"><div class="card-ico">&#128194;</div><h3>Upload CSV</h3>
  <p>Upload CSV, filter, sort, dan ekspor hasil deteksi lengkap.</p></div>
  <div class="card"><div class="card-ico">&#128202;</div><h3>3 Level Keparahan</h3>
  <p>Aman, Perlu Perhatian, Sangat Toxic dari skor probabilitas.</p></div>
</div>

<div class="sec"><span class="sec-tag">Cara Kerja</span><h2>Pipeline Deteksi</h2></div>
<div class="pipe">
  <div class="step"><div class="sl2"><div class="sn">1</div><div class="sc"></div></div>
  <div class="sb"><h4>Input Teks</h4><p>Masukkan komentar melalui form, batch, atau upload file CSV.</p></div></div>
  <div class="step"><div class="sl2"><div class="sn">2</div><div class="sc"></div></div>
  <div class="sb"><h4>Preprocessing</h4><p>Teks dibersihkan, tokenisasi, stopword removal, dan stemming Bahasa Indonesia.</p></div></div>
  <div class="step"><div class="sl2"><div class="sn">3</div><div class="sc"></div></div>
  <div class="sb"><h4>TF-IDF Vectorization</h4><p>Teks dikonversi menjadi vektor numerik menggunakan bobot TF-IDF.</p></div></div>
  <div class="step"><div class="sl2"><div class="sn">4</div></div>
  <div class="sb"><h4>Naive Bayes Classifier</h4><p>Model memprediksi probabilitas toxic dan menentukan level keparahan.</p></div></div>
</div>

<div class="footer">
  <div class="fl"><div class="fi">&#128737;&#65039;</div><span class="fn">ToxicGuard</span></div>
  <p>Dibangun dengan Naive Bayes + TF-IDF untuk deteksi komentar toxic Bahasa Indonesia.</p>
  <small>Gratis &nbsp;&middot;&nbsp; Tanpa Login &nbsp;&middot;&nbsp; Open Source</small>
</div>

<script>
const tr=document.getElementById('tr'),de=document.getElementById('dots');
const N=tr.children.length;let c=0,tmr;
for(let i=0;i<N;i++){const d=document.createElement('div');
  d.className='dt'+(i===0?' on':'');d.onclick=()=>go(i);de.appendChild(d);}
function go(n){c=(n+N)%N;tr.style.transform='translateX(-'+c*100+'%)';
  document.querySelectorAll('.dt').forEach((d,i)=>d.className='dt'+(i===c?' on':''));
  clearInterval(tmr);tmr=setInterval(()=>go(c+1),4200);}
function mv(d){go(c+d);}
tmr=setInterval(()=>go(c+1),4200);
function sendH(){const h=document.documentElement.scrollHeight;
  window.parent.postMessage({isStreamlitMessage:true,type:'streamlit:setFrameHeight',height:h},'*');}
document.addEventListener('DOMContentLoaded',sendH);
window.addEventListener('load',sendH);
setTimeout(sendH,300);
</script>
</body></html>""", height=1500, scrolling=False)

    return clicked
