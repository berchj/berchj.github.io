#!/usr/bin/env python3
"""Generates the site's HTML pages, sitemap and llms.txt from the data below.

Run: python3 build.py
"""
import html
import json
from datetime import date
from pathlib import Path

SITE = 'https://berchj.github.io'
ROOT = Path(__file__).parent
TODAY = date.today().isoformat()
SUPPORT = 'https://cafecito.app/berchj'
USDT = '0xc39dfD297BAf6ab305e267D153bf11d37de7faF6'

APPS = [
    {
        'name': 'wallswitch',
        'kind': 'Wallpaper changer',
        'title': 'wallswitch — Free automatic wallpaper changer for Windows, Mac and Linux',
        'description': 'Free, open-source wallpaper changer: rotate your desktop backgrounds automatically, get a new 4K photo every day and switch wallpapers with keyboard shortcuts. Windows, macOS and Linux.',
        'tagline': 'Your desktop, <strong>always fresh</strong>. Rotate your wallpapers automatically, get a new photo every day, and switch with a keystroke.',
        'category': 'UtilitiesApplication',
        'keywords': 'wallpaper changer, automatic wallpaper rotation, wallpaper slideshow, photo of the day wallpaper, bing wallpaper, change wallpaper shortcut, ubuntu wallpaper changer, windows 11 wallpaper changer',
        'features': [
            ('🖼️', 'Wallpaper carousel', 'Click the images you like and they rotate every 1 minute to 1 day.'),
            ('🌅', 'Photo of the day', 'A new 4K photo from Bing every day, set as your wallpaper automatically.'),
            ('⌨️', 'Keyboard shortcuts', 'Next, previous and random wallpaper from anywhere. Record your own keys.'),
            ('🔔', 'Tray icon', 'Lives quietly in your system tray / top bar with a quick menu.'),
            ('📁', 'Folders or single images', 'Uses your Pictures/Wallpapers folder and the system wallpapers by default.'),
            ('💻', 'Command line', '<code>wallswitch next</code>, <code>wallswitch daily</code>, <code>wallswitch set photo.jpg</code>… great for scripts.'),
        ],
        'steps': [
            'Download and install wallswitch.',
            'Click the images you want in your carousel (blue outline).',
            'Turn on <b>Auto change</b>, or <b>Photo of the day</b> for a new wallpaper every morning.',
            'Use <code>Super</code>+<code>.</code> / <code>Super</code>+<code>,</code> (<code>Ctrl</code>+<code>Alt</code>+<code>.</code> on Windows/Mac) for next and previous.',
        ],
        'faq': [
            ('How do I change my wallpaper automatically on Windows 11, Mac or Ubuntu?', 'Install wallswitch, click the images you want and turn on Auto change. It rotates them every few minutes or hours — you choose the interval.'),
            ('Can I get a new wallpaper every day?', 'Yes. Turn on Photo of the day and wallswitch downloads Bing’s photo of the day in 4K and sets it as your wallpaper each morning.'),
            ('Can I change the wallpaper with a keyboard shortcut?', 'Yes: next, previous and random wallpaper have global shortcuts, and you can record your own keys from the Shortcuts panel.'),
            ('Can I change the wallpaper from the terminal?', 'Yes: wallswitch next, wallswitch prev, wallswitch random, wallswitch daily or wallswitch set path/to/image.jpg.'),
            ('Does wallswitch delete or move my images?', 'No. Your files are never touched; Remove only hides an image from the list.'),
            ('Is wallswitch free?', 'Yes, it’s free and open source under the MIT license. No account, no ads.'),
        ],
    },
    {
        'name': 'clipswitch',
        'kind': 'Clipboard manager',
        'title': 'clipswitch — Free clipboard history manager for Windows, Mac and Linux',
        'description': 'Free, open-source clipboard manager: keeps everything you copy (text and images), pin favorites and paste them again with one keyboard shortcut. Windows, macOS and Linux. Private and offline.',
        'tagline': 'Everything you copy, <strong>one shortcut away</strong>. Text and images, searchable, with favorites you can pin forever.',
        'category': 'UtilitiesApplication',
        'keywords': 'clipboard manager, clipboard history, copy paste history, clipboard history linux, clipboard manager mac free, ditto alternative, windows clipboard history alternative',
        'features': [
            ('📋', 'Clipboard history', 'The last 50 things you copied, newest first, no duplicates.'),
            ('🖼️', 'Images too', 'Screenshots and copied pictures, with a preview.'),
            ('⭐', 'Pin favorites', 'Your address, a bank account, a signature: pinned items stay at the top forever.'),
            ('🔎', 'Instant search', 'Type to filter, arrows to move, Enter to copy.'),
            ('⌨️', 'Your own shortcut', '<code>Super</code>+<code>Shift</code>+<code>V</code> by default — record any keys you like.'),
            ('🔒', 'Private', 'Nothing you copy leaves your computer. Pause recording any time.'),
        ],
        'steps': [
            'Download and install clipswitch — it starts in your tray.',
            'Copy things as usual.',
            'Press <code>Super</code>+<code>Shift</code>+<code>V</code> (<code>Ctrl</code>+<code>Alt</code>+<code>V</code> on Windows/Mac).',
            'Pick an entry and paste it anywhere with <code>Ctrl</code>+<code>V</code>.',
        ],
        'faq': [
            ('How do I see my clipboard history?', 'Install clipswitch and press Super+Shift+V (Ctrl+Alt+V on Windows and Mac). You’ll see everything you copied, newest first, and can search it.'),
            ('Does it save copied images and screenshots?', 'Yes. Images show up with a preview; pick one and it’s back on your clipboard, ready to paste.'),
            ('How do I keep a text forever?', 'Pin it with the star or Ctrl+P. Pinned entries stay at the top and are never deleted, not even by Clear history.'),
            ('Is my clipboard sent anywhere?', 'No. Everything is stored in a local file on your computer. There’s no account and no cloud.'),
            ('Is there a clipboard manager for Linux and Mac like Windows’ Win+V?', 'Yes, clipswitch works the same on Linux, macOS and Windows, with text and images.'),
            ('Is clipswitch free?', 'Yes, it’s free and open source under the MIT license.'),
        ],
    },
    {
        'name': 'tinyswitch',
        'kind': 'Image & document compressor',
        'title': 'tinyswitch — Compress images, PDF, Word and PowerPoint offline (free)',
        'description': 'Free, open-source compressor for Windows, Mac and Linux: make JPG, PNG, HEIC photos, PDF, Word, PowerPoint and Excel files smaller by dragging them in. Works offline — nothing is uploaded.',
        'tagline': 'Make photos and documents <strong>up to 80% smaller</strong>. Drag them in — nothing is uploaded, your originals stay untouched.',
        'category': 'MultimediaApplication',
        'keywords': 'compress images offline, compress pdf without uploading, reduce pdf size, compress powerpoint, reduce word file size, heic to jpg, tinypng alternative, image compressor windows mac linux',
        'features': [
            ('🖼️', 'Images', 'JPG (mozjpeg), PNG (smart palette, like TinyPNG), WebP, AVIF and TIFF.'),
            ('📱', 'iPhone photos', 'HEIC photos are converted to JPG while compressing.'),
            ('📄', 'PDF', 'Shrinks the photos inside scanned and photo-heavy PDFs.'),
            ('📊', 'Word, PowerPoint, Excel', 'Shrinks the images inside; text and layout stay exactly the same.'),
            ('🖱️', 'Right-click menu', '<i>Compress with tinyswitch</i> from your file manager (Windows and Linux).'),
            ('🔒', 'Offline', 'Unlike online compressors, your files never leave your computer.'),
        ],
        'steps': [
            'Download and install tinyswitch.',
            'Drag photos, PDFs, Word or PowerPoint files (or whole folders) onto the window.',
            'A smaller copy is saved next to each one as <code>name-min.ext</code>.',
            'Optional: lower the quality, set a max width or convert photos to WebP.',
        ],
        'faq': [
            ('How do I reduce the size of a PDF without uploading it?', 'Drop it on tinyswitch. It recompresses the photos inside — what makes scanned PDFs heavy — and saves name-min.pdf next to it. Nothing leaves your computer.'),
            ('How do I make a PowerPoint or Word file smaller to send it by email?', 'Drop it on tinyswitch. Files full of photos often shrink by half or more; text, slides and layout are unchanged.'),
            ('How do I convert iPhone HEIC photos to JPG?', 'Drop them on tinyswitch: they come out as compressed JPG files that open everywhere.'),
            ('Is it like TinyPNG?', 'Similar results for PNG and JPG, but it runs on your computer: no upload limits, no file size limits, and private files stay private.'),
            ('Does it change my original files?', 'Never. It always writes a new file next to the original.'),
            ('Is tinyswitch free?', 'Yes, it’s free and open source under the MIT license.'),
        ],
    },
]

THEME = '<script>try{const t=localStorage.getItem("theme");if(t)document.documentElement.dataset.theme=t}catch{}</script>'


def head(title, description, url, image, extra=''):
    e = html.escape
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(description)}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/img/{image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="stylesheet" href="/style.css">
{THEME}
{extra}</head>'''


def nav(current=None):
    links = ''.join(
        f'<a href="/{a["name"]}/"{" aria-current=page" if a["name"] == current else ""}><img src="/img/{a["name"]}-64.png" alt="">{a["name"]}</a>'
        for a in APPS
    )
    return f'<nav><div class="wrap"><a class="home" href="/">berchj tools</a>{links}</div></nav>'


def footer():
    return f'''<footer><div class="wrap">
<span>Free and open source · MIT license · made by <a href="https://github.com/berchj">berchj</a></span>
<span>Like these apps? <a href="{SUPPORT}">☕ Buy me a coffee</a> · USDT (BEP20): <code>{USDT}</code></span>
</div></footer>'''


def app_page(app):
    n = app['name']
    url = f'{SITE}/{n}/'
    repo = f'https://github.com/berchj/{n}'
    ld = [
        {
            '@context': 'https://schema.org',
            '@type': 'SoftwareApplication',
            'name': n,
            'description': app['description'],
            'applicationCategory': app['category'],
            'operatingSystem': 'Windows 10, Windows 11, macOS, Linux, Ubuntu',
            'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'},
            'downloadUrl': f'{repo}/releases/latest',
            'installUrl': f'{repo}/releases/latest',
            'url': url,
            'image': f'{SITE}/img/{n}-icon.png',
            'screenshot': f'{SITE}/img/{n}-screenshot.png',
            'license': 'https://opensource.org/licenses/MIT',
            'isAccessibleForFree': True,
            'author': {'@type': 'Person', 'name': 'berchj', 'url': 'https://github.com/berchj'},
            'sameAs': [repo, f'https://www.npmjs.com/package/{n}'],
            'keywords': app['keywords'],
        },
        {
            '@context': 'https://schema.org',
            '@type': 'FAQPage',
            'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in app['faq']],
        },
    ]
    ld_html = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in ld)
    features = ''.join(f'<div class="card"><div class="emoji">{em}</div><h3>{t}</h3><p>{d}</p></div>' for em, t, d in app['features'])
    steps = ''.join(f'<li>{s}</li>' for s in app['steps'])
    faq = ''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in app['faq'])
    return f'''{head(app['title'], app['description'], url, f'{n}-social.png', ld_html + '<meta name="keywords" content="' + html.escape(app['keywords']) + '">' + chr(10))}
<body class="{n}">
{nav(n)}
<main>
<div class="hero wrap">
<img class="icon" src="/img/{n}-icon.png" alt="{n} icon" width="96" height="96">
<h1>{n}</h1>
<p class="tagline">{app['tagline']}</p>
<div class="download" data-repo="berchj/{n}">
<a class="btn" href="{repo}/releases/latest">⬇ <span>Download {n}</span></a>
<div class="others"><a href="{repo}/releases/latest">Windows, macOS and Linux</a></div>
<div class="npm version">Free · open source · MIT license</div>
<div class="npm">Developer? <code>npm install -g {n}</code></div>
</div>
<div class="shot"><img src="/img/{n}-screenshot.png" alt="Screenshot of {n}, the {app['kind'].lower()}"></div>
</div>

<section class="wrap">
<h2>What {n} does</h2>
<div class="grid">{features}</div>
</section>

<section class="wrap">
<h2>How to use it</h2>
<ol class="steps">{steps}</ol>
<p class="note">First launch: the installers aren’t signed with a paid certificate yet. On Windows click <b>More info → Run anyway</b>; on macOS open <b>System Settings → Privacy &amp; Security → Open Anyway</b>.</p>
</section>

<section class="wrap">
<h2>Questions</h2>
{faq}
</section>

<section class="wrap">
<p>Source code, issues and release notes: <a href="{repo}">github.com/berchj/{n}</a> · <a href="https://www.npmjs.com/package/{n}">npm</a></p>
</section>
</main>
{footer()}
<script src="/download.js" defer></script>
</body>
</html>
'''


def blurb(app):
    """The part of the description after "Free, open-source X:", capitalized."""
    text = app['description'].split(':', 1)[-1].strip()
    return text[:1].upper() + text[1:]


def home_page():
    title = 'berchj tools — Free, tiny desktop apps for Windows, Mac and Linux'
    description = 'Free, open-source desktop utilities: wallswitch (wallpaper changer), clipswitch (clipboard history) and tinyswitch (image, PDF and document compressor). Windows, macOS and Linux.'
    cards = ''.join(
        f'<a class="card {a["name"]}" href="/{a["name"]}/"><img src="/img/{a["name"]}-icon.png" alt="" width="64" height="64"><h3>{a["name"]}</h3><p><b>{a["kind"]}.</b> {html.escape(blurb(a))}</p></a>'
        for a in APPS
    )
    ld = {
        '@context': 'https://schema.org',
        '@type': 'ItemList',
        'name': 'berchj tools',
        'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': f'{SITE}/{a["name"]}/', 'name': a['name']} for i, a in enumerate(APPS)],
    }
    return f'''{head(title, description, SITE + '/', 'tinyswitch-social.png', '<script type="application/ld+json">' + json.dumps(ld) + '</script>' + chr(10))}
<body>
{nav()}
<main>
<div class="hero wrap">
<h1>Small apps that do one thing well</h1>
<p class="tagline">Free and open source, for <strong>Windows, macOS and Linux</strong>. No accounts, no ads, no tracking.</p>
</div>
<section class="wrap"><div class="grid">{cards}</div></section>
</main>
{footer()}
</body>
</html>
'''


def llms_txt():
    lines = ['# berchj tools', '', '> Free, open-source desktop utilities for Windows, macOS and Linux by berchj. MIT license, no accounts, no tracking. Each one installs with a regular installer (GitHub Releases) or with `npm install -g <name>`.', '']
    for a in APPS:
        n = a['name']
        lines += [f'## {n} — {a["kind"]}', '', a['description'], '', f'- Website: {SITE}/{n}/', f'- Download: https://github.com/berchj/{n}/releases/latest', f'- npm: `npm install -g {n}`', f'- Source: https://github.com/berchj/{n}', '']
        lines += [f'- {q} {ans}' for q, ans in a['faq']]
        lines.append('')
    return '\n'.join(lines)


def main():
    (ROOT / 'index.html').write_text(home_page())
    for a in APPS:
        d = ROOT / a['name']
        d.mkdir(exist_ok=True)
        (d / 'index.html').write_text(app_page(a))
    urls = [SITE + '/'] + [f'{SITE}/{a["name"]}/' for a in APPS]
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n' for u in urls) + '</urlset>\n')
    (ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
    (ROOT / 'llms.txt').write_text(llms_txt())
    (ROOT / '.nojekyll').write_text('')
    print('built', len(urls), 'pages')


if __name__ == '__main__':
    main()
