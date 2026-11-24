#!/usr/bin/env python3
import json, os, html as htmllib
from datetime import date

reports = json.load(open('./_data/reports.json'))
TODAY = date.today().isoformat()

BLOG_ARTICLES = [
    ('romance-scams', '2026-05-01'),
    ('florida-criminal-records', '2026-05-01'),
    ('rental-scams', '2026-05-01'),
    ('business-scams', '2026-05-01'),
    ('how-to-report-a-scammer-miami', '2026-05-01'),
    ('facebook-marketplace-craigslist-scams-miami', '2026-05-01'),
    ('event-scams-miami', '2026-11-01'),
    ('instagram-scams-miami', '2026-11-01'),
    ('contractor-scams-miami', '2026-11-01'),
    ('online-service-scams-miami', '2026-11-01'),
    ('art-basel-scams', '2026-11-23'),
    ('daniel-sharkey', '2026-11-24'),
]

def e(s): return htmllib.escape(str(s))

CSS = """*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{--bg:#080808;--card:#111;--border:#1e1e1e;--accent:#00c9a7;--red:#ff3b3b;--text:#f0f0f0;--muted:#777;--sub:#aaa}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--text);font-family:'Inter',sans-serif;font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
img{max-width:100%;display:block}
.wrap{max-width:1000px;margin:0 auto;padding:0 24px}
nav{position:fixed;top:0;left:0;right:0;z-index:99;background:rgba(8,8,8,.93);backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}
.nav-inner{max-width:1000px;margin:0 auto;padding:0 24px;height:62px;display:flex;align-items:center;justify-content:space-between}
.logo{font-weight:800;font-size:17px;display:flex;align-items:center;gap:8px}
.logo-dot{width:10px;height:10px;background:var(--accent);border-radius:50%;display:inline-block}
.nav-links{display:flex;gap:28px}
.nav-links a{font-size:14px;color:var(--sub);font-weight:500;transition:color .2s}
.nav-links a:hover{color:var(--text)}
.nav-btn{background:var(--accent);color:#000;border:none;padding:8px 18px;border-radius:8px;font-size:13px;font-weight:700;cursor:pointer;text-decoration:none;display:inline-flex;align-items:center}
.profile-hero{padding:100px 24px 36px;background:linear-gradient(to bottom,#0d0d0d,var(--bg));border-bottom:1px solid var(--border)}
.profile-hero .back{font-size:13px;color:var(--sub);margin-bottom:16px;display:inline-flex;align-items:center;gap:6px}
.profile-hero .back:hover{color:var(--text)}
.profile-hero h1{font-size:clamp(24px,4vw,38px);font-weight:800;letter-spacing:-.5px;margin-bottom:6px}
.profile-hero p{color:var(--sub);font-size:14px}
.profile-wrap{max-width:720px;margin:0 auto;padding:40px 24px 80px}
.card{background:var(--card);border:1px solid var(--border);border-radius:12px;overflow:hidden;margin-bottom:24px}
.card-top{display:flex;align-items:center;justify-content:space-between;padding:14px 18px 0}
.rpt-id{font-size:11px;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.1em}
.badge{display:inline-flex;align-items:center;font-size:10px;font-weight:700;padding:3px 10px;border-radius:100px;text-transform:uppercase;letter-spacing:.06em}
.badge-v{background:rgba(0,201,167,.1);color:var(--accent);border:1px solid rgba(0,201,167,.2)}
.badge-r{background:rgba(255,59,59,.08);color:var(--red);border:1px solid rgba(255,59,59,.18)}
.card-body{display:grid;grid-template-columns:160px 1fr;gap:24px;padding:18px}
.photo{width:150px;height:220px;object-fit:cover;object-position:top;border-radius:9px;border:2px solid var(--border)}
.type-tag{display:inline-block;background:rgba(255,59,59,.07);color:var(--red);border:1px solid rgba(255,59,59,.15);font-size:10px;font-weight:700;padding:3px 9px;border-radius:6px;text-transform:uppercase;letter-spacing:.06em;margin-bottom:12px}
.rpt-name{font-size:22px;font-weight:800;letter-spacing:-.3px;margin-bottom:6px}
.aka{font-size:12px;color:#aaa;margin-bottom:6px}
.meta{display:flex;flex-wrap:wrap;gap:12px;margin-bottom:12px}
.meta-i{font-size:12px;color:var(--sub)}
.desc{font-size:14px;color:var(--sub);line-height:1.75}
.desc p{margin-bottom:10px}
.desc p:last-child{margin-bottom:0}
.record{margin:0 18px 18px;border:1px solid var(--border);border-radius:9px;overflow:hidden}
.record-head{display:flex;align-items:center;justify-content:space-between;padding:9px 14px;background:rgba(255,59,59,.05);border-bottom:1px solid var(--border)}
.record-title{font-size:11px;font-weight:700;color:var(--red);text-transform:uppercase;letter-spacing:.07em}
.record-src{font-size:11px;color:var(--muted)}
.record-ph{padding:16px}
.bullet-row{display:flex;align-items:center;gap:8px;margin-bottom:8px}
.bullet-dot{color:#ff3b3b;font-size:16px;flex-shrink:0}
.bullet-text{font-size:13px;font-weight:600;color:#f0f0f0}
.record-note{font-size:11px;color:#555;line-height:1.5;margin-top:4px}
.card-foot{display:flex;align-items:center;justify-content:space-between;padding:11px 18px;border-top:1px solid var(--border);flex-wrap:wrap;gap:8px}
.foot-date{font-size:12px;color:var(--muted)}
.blog-link-box{background:rgba(0,201,167,.05);border:1px solid rgba(0,201,167,.15);border-radius:10px;padding:16px 20px;margin-bottom:24px}
.blog-link-box p{font-size:13px;color:var(--sub);margin-bottom:8px}
.blog-link-box a{color:var(--accent);font-weight:700;font-size:13px}
.cta-box{background:linear-gradient(135deg,rgba(0,201,167,.07),rgba(0,201,167,.02));border:1px solid rgba(0,201,167,.13);border-radius:14px;padding:36px;text-align:center;margin-bottom:48px}
.cta-box h2{font-size:22px;font-weight:800;letter-spacing:-.3px;margin-bottom:8px}
.cta-box p{color:var(--sub);margin-bottom:20px;font-size:14px}
.btn-a{display:inline-flex;align-items:center;gap:6px;background:var(--accent);color:#000;font-weight:700;font-size:14px;padding:12px 22px;border-radius:9px;border:none;cursor:pointer;text-decoration:none}
footer{border-top:1px solid var(--border);padding:28px 24px}
.foot-inner{max-width:1000px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:14px}
.foot-logo{font-weight:800;font-size:14px;display:flex;align-items:center;gap:7px}
.foot-links{display:flex;gap:20px}
.foot-links a{font-size:12px;color:var(--muted)}
.foot-links a:hover{color:var(--text)}
.foot-copy{font-size:11px;color:var(--muted)}
@media(max-width:680px){
  .card-body{grid-template-columns:90px 1fr;gap:12px}
  .photo{width:90px;height:130px}
  .nav-btn{display:none}
}"""

def profile_page(r):
    extra_meta = ''.join(f'\n          <span class="meta-i">{e(m)}</span>' for m in r.get('extraMeta', []))
    desc_html = '\n              '.join(f'<p>{e(p)}</p>' for p in r['desc'])
    if r.get('affiliations'):
        aff_items = ' '.join(
            f'<strong style="color:#f0f0f0">{e(a["name"])}</strong> — {e(a["desc"])}'
            for a in r['affiliations']
        )
        affiliations_html = f'''<div style="margin-top:12px;padding:12px 14px;background:rgba(255,59,59,.04);border:1px solid rgba(255,59,59,.12);border-radius:8px">
          <div style="font-size:10px;font-weight:700;color:#777;text-transform:uppercase;letter-spacing:.08em;margin-bottom:6px">Known Affiliations</div>
          <div style="font-size:13px;color:#ccc;line-height:1.6">{aff_items}</div>
        </div>'''
    else:
        affiliations_html = ''
    bullets_html = '\n'.join(
        f'              <div class="bullet-row"><span class="bullet-dot">&#x25CF;</span><span class="bullet-text">{e(b)}</span></div>'
        for b in r['bullets']
    )
    aka_html = f'<div class="aka">aka {e(r["aka"])}</div>' if r.get('aka') else ''
    fname = e(r['name'].split()[0])

    ld = {
        "@context": "https://schema.org",
        "@type": "ProfilePage",
        "name": r['titleSEO'],
        "url": f"https://miamiscammers.com/profiles/{r['slug']}",
        "description": r['metaDesc'],
        "image": f"https://miamiscammers.com/{r['image']}",
        "mainEntity": {"@type": "Person", "name": r['name'], "description": r['metaDesc']},
        "publisher": {
            "@type": "Organization",
            "name": "Miami Scammers",
            "url": "https://miamiscammers.com",
            "sameAs": ["https://www.instagram.com/miami_scammers/"]
        }
    }

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(r['titleSEO'])}</title>
<meta name="description" content="{e(r['metaDesc'])}">
<link rel="canonical" href="https://miamiscammers.com/profiles/{r['slug']}">
<meta property="og:type" content="profile">
<meta property="og:url" content="https://miamiscammers.com/profiles/{r['slug']}">
<meta property="og:title" content="{e(r['titleSEO'])}">
<meta property="og:description" content="{e(r['metaDesc'])}">
<meta property="og:image" content="https://miamiscammers.com/{r['image']}">
<meta property="og:image:width" content="{r['imageW']}">
<meta property="og:image:height" content="{r['imageH']}">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:secure_url" content="https://miamiscammers.com/{r['image']}">
<meta property="og:site_name" content="Miami Scammers">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(r['titleSEO'])}">
<meta name="twitter:description" content="{e(r['metaDesc'])}">
<meta name="twitter:image" content="https://miamiscammers.com/{r['image']}">
<link rel="manifest" href="/manifest.json">
<meta name="theme-color" content="#00c9a7">
<link rel="apple-touch-icon" href="/icon-192.png">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
<script type="application/ld+json">{json.dumps(ld, indent=2)}</script>
</head>
<body>
<nav>
  <div class="nav-inner">
    <a href="/" class="logo"><span class="logo-dot"></span> Miami Scammers</a>
    <div class="nav-links">
      <a href="/">Reports</a>
      <a href="/scammer-list">Scammer List</a>
      <a href="/blog">Blog</a>
    </div>
    <a href="/#submit" class="nav-btn">+ Submit a Report</a>
  </div>
</nav>

<div class="profile-hero">
  <div class="wrap">
    <a href="/" class="back">← All Reports</a>
    <h1>{e(r['name'])}</h1>
    <p>Report #{r['num']} &middot; Filed {e(r['filed'])} &middot; {e(r['location'])}</p>
  </div>
</div>

<div class="profile-wrap">
  <article class="card">
    <div class="card-top">
      <span class="rpt-id">Report #{r['num']}</span>
      <span class="badge badge-v">&#10003; Verified</span>
    </div>
    <div class="card-body">
      <img class="photo" src="/{r['image']}" alt="{e(r['name'])} Miami scammer report photo" width="{r['imageW']}" height="{r['imageH']}">
      <div>
        <div class="rpt-name">{e(r['name'])}</div>
        {aka_html}
        <div class="meta">
          <span class="meta-i">&#128205; {e(r['location'])}</span>
          <span class="meta-i">&#128197; {e(r['years'])}</span>{extra_meta}
        </div>
        <div class="type-tag">{e(r['typeTag'])}</div>
        <div class="desc">
              {desc_html}
        </div>
        {affiliations_html}
      </div>
    </div>
    <div class="record">
      <div class="record-head">
        <span class="record-title">&#9888; {e(r['recordTitle'])}</span>
        <span class="record-src">{e(r['recordSrc'])}</span>
      </div>
      <div class="record-ph">
{bullets_html}
        <p class="record-note">{e(r['recordNote'])}</p>
      </div>
    </div>
    <div class="card-foot">
      <span class="foot-date">Filed {e(r['filed'])}</span>
    </div>
  </article>

  <div class="blog-link-box">
    <p>&#128218; Want to learn more about this type of scam?</p>
    <a href="{r['blogLink']}">{e(r['blogLabel'])} &#8594;</a>
  </div>

  <div class="cta-box">
    <h2>Know Something About {fname}?</h2>
    <p>Have additional information or evidence? Submit a report and we&#39;ll review it before it goes live.</p>
    <a href="/#submit" class="btn-a">+ Submit a Report</a>
  </div>
</div>

<footer>
  <div class="foot-inner">
    <div class="foot-logo"><span class="logo-dot"></span> Miami Scammers</div>
    <div class="foot-links">
      <a href="/">Reports</a>
      <a href="/blog">Blog</a>
      <a href="/miami-scams">Miami Scams Guide</a>
      <a href="https://www.instagram.com/miami_scammers/" target="_blank" rel="noopener">Instagram</a>
    </div>
    <div class="foot-copy">&copy; 2026 MiamiScammers.com</div>
  </div>
</footer>
</body>
</html>"""

os.makedirs('./profiles', exist_ok=True)
for r in reports:
    out = f"./profiles/{r['slug']}.html"
    open(out, 'w').write(profile_page(r))
    print(f"✓ {out}")

# nick-ruiz backward-compat redirect
open('./profiles/nick-ruiz.html', 'w').write(
    '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>Nicolas Ruiz &#8212; Miami Scammers</title>'
    '<meta property="og:image" content="https://miamiscammers.com/nicolas-ruiz-miami.jpg">'
    '<meta property="og:title" content="Nicolas Ruiz &#8212; Event Fraud Report | Miami Scammers">'
    '</head><body><script>window.location.replace(\'/profiles/nicolas-ruiz\');</script></body></html>'
)
print("✓ profiles/nick-ruiz.html (redirect)")

# sitemap.xml
profile_urls = '\n'.join(
    f'  <url>\n    <loc>https://miamiscammers.com/profiles/{r["slug"]}</loc>\n    <lastmod>{TODAY}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>'
    for r in reports
)
blog_urls = '\n'.join(
    f'  <url>\n    <loc>https://miamiscammers.com/blog/{slug}</loc>\n    <lastmod>{d}</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.8</priority>\n  </url>'
    for slug, d in BLOG_ARTICLES
)
sitemap = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://miamiscammers.com/</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://miamiscammers.com/miami-scams</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://miamiscammers.com/scammer-list</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>https://miamiscammers.com/blog</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.9</priority>
  </url>
{blog_urls}
{profile_urls}
</urlset>"""
open('./sitemap.xml', 'w').write(sitemap)
print("✓ sitemap.xml")

# robots.txt
open('./robots.txt', 'w').write("User-agent: *\nAllow: /\nSitemap: https://miamiscammers.com/sitemap.xml\n")
print("✓ robots.txt")

print(f"\nBuild complete: {len(reports)} profile pages, {len(BLOG_ARTICLES)} blog URLs in sitemap.")
