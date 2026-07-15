import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

root_new = '''/* ===========================
   VITO LOCKS — Dark Charcoal + Rose Gold Theme
   =========================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Montserrat:wght@600;700;800&display=swap');

/* ——— CSS Variables ——— */
:root {
  --primary:         #c9956b;
  --primary-light:   #d4a574;
  --primary-glass:   rgba(201,149,107,0.12);
  --accent:          #b76e79;
  --accent-light:    #d4a574;
  --accent-pale:     rgba(201,149,107,0.08);
  --neutral-dark:    #f0e6dc;
  --neutral-mid:     #a89b8c;
  --neutral-soft:    #7a6f63;
  --neutral-light:   #1e1e2f;
  --bg:              #0f0f1a;
  --border:          rgba(201,149,107,0.15);
  --border-light:    rgba(201,149,107,0.08);
  --glass-bg:        rgba(30,30,47,0.70);
  --glass-bg-card:   rgba(30,30,47,0.78);
  --glass-bg-nav:    rgba(15,15,26,0.92);
  --glass-blur:      blur(18px);
  --glass-shadow:    0 4px 24px rgba(0,0,0,0.3);
  --shadow:          0 2px 16px rgba(0,0,0,0.25);
  --radius:          14px;
  --radius-sm:       8px;
  --font-body:       'Inter', sans-serif;
  --font-head:       'Playfair Display', 'Montserrat', serif;
  --transition:      0.26s ease;
}'''
css = re.sub(r'/\* ===========================.*?--transition:\s*0\.26s ease;\n\}', root_new, css, count=1, flags=re.DOTALL)

bg_new = '''  background:
    radial-gradient(ellipse at 0% 0%,   rgba(201,149,107,0.05) 0%, transparent 55%),
    radial-gradient(ellipse at 100% 15%, rgba(183,110,121,0.08) 0%, transparent 50%),
    radial-gradient(ellipse at 50% 80%,  rgba(201,149,107,0.05) 0%, transparent 60%),
    var(--bg);'''
css = re.sub(r'  background:\n    radial-gradient[^;]+;', bg_new, css, count=1)

hero_bg_new = '''background: linear-gradient(110deg, rgba(15,15,26,0.92) 38%, rgba(30,30,47,0.75) 100%);'''
css = re.sub(r'background: linear-gradient\(110deg, rgba\(18,55,105,0.88\).*?;', hero_bg_new, css, count=1)

hero_tag_new = '''  background: rgba(201,149,107,0.15);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  border: 1px solid rgba(201,149,107,0.4);
  color: #d4a574;'''
css = re.sub(r'  background: rgba\(255,255,255,0.15\);\n  backdrop-filter: blur\(8px\);\n  -webkit-backdrop-filter: blur\(8px\);\n  border: 1px solid rgba\(255,255,255,0.4\);\n  color: #ffe9a0;', hero_tag_new, css, count=1)

stats_new = '''background: linear-gradient(110deg, #1a1a2e 0%, #16213e 100%);'''
css = re.sub(r'background: linear-gradient\(110deg, var\(--primary\) 0%, var\(--primary-light\) 100%\);', stats_new, css, count=1)

footer_bg = '''background: linear-gradient(135deg, #0a0a14 0%, #12121f 100%);'''
css = re.sub(r'background: linear-gradient\(135deg, #1a2d4a 0%, #1c3a5e 100%\);', footer_bg, css, count=1)

css = css.replace('rgba(28,95,163,', 'rgba(201,149,107,')
css = css.replace('rgba(28, 95, 163,', 'rgba(201, 149, 107,')
css = css.replace('rgba(184,122,10,', 'rgba(201,149,107,')

css = css.replace('background: rgba(255,255,255,0.4)', 'background: rgba(201,149,107,0.2)')
css = css.replace('background: rgba(255,255,255,0.25)', 'background: rgba(201,149,107,0.15)')
css = css.replace('background: rgba(255,255,255,0.14)', 'background: rgba(30,30,47,0.6)')

css = css.replace('#ffe9a0', '#d4a574')

css = css.replace('color: #fff;', 'color: var(--neutral-dark);')
css = css.replace('color: white;', 'color: var(--neutral-dark);')
css = css.replace('color: white !important;', 'color: var(--neutral-dark) !important;')
css = css.replace('color: #ffffff;', 'color: var(--neutral-dark);')

css = re.sub(r'\.nav-logo img \{[^}]+\}', '''.nav-logo img {
  height: 48px;
  width: auto;
  object-fit: contain;
}''', css, count=1)

css = re.sub(r'\.footer-brand img \{[^}]+\}', '''.footer-brand img {
  height: 42px;
  width: auto;
  object-fit: contain;
  margin-bottom: 12px;
}''', css, count=1)

css = css.replace('background: rgba(255,255,255,0.75);', 'background: rgba(30,30,47,0.60);')
css = css.replace('background: #fff;', 'background: rgba(15,15,26,0.9);')
css = css.replace('background: rgba(255,255,255,0.97);', 'background: rgba(15,15,26,0.97);')
css = css.replace('background: rgba(255,255,255,0.92);', 'background: rgba(30,30,47,0.8);')
css = css.replace('background: rgba(255,255,255,0.80);', 'background: rgba(30,30,47,0.78);')

css = css.replace('background: var(--neutral-dark);', 'background: var(--primary-light);') # for hamburger spans

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
