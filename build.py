#!/usr/bin/env python3
"""Generates the site's HTML pages, sitemap and llms.txt from the data below.

Run: python3 build.py
"""
import html
import json
from datetime import date
from pathlib import Path

from tools import HIDDEN_TOOLS, POWERTOYS, TOOLS

SITE = 'https://berchj.github.io'
ROOT = Path(__file__).parent
TODAY = date.today().isoformat()
SUPPORT = 'https://cafecito.app/berchj'
USDT = '0xc39dfD297BAf6ab305e267D153bf11d37de7faF6'
VERSION = '0.1.4'
N = len(TOOLS)
# IndexNow (Bing, Yandex, Seznam...): the key file at the site root proves the site is ours.
INDEXNOW_KEY = '7c1f4a2e9b8d4e60a3f5c2b1d0e9f8a7'

# toolswitch: every tool in one app. Its code is private; the installers are published in this
# public repository, the downloads for every page.
REPO = 'berchj/toolswitch-releases'
REPO_URL = f'https://github.com/{REPO}'
# Says "open source" and links the code only when the repository is public.
OPEN_SOURCE = True
# The code (public since 2026-10-23); the installers stay in the releases repository.
CODE = 'berchj/toolswitch'
CODE_URL = f'https://github.com/{CODE}'
LICENSE_TEXT = 'Free · open source · MIT license' if OPEN_SOURCE else 'Free · no account · no ads'

TOOLSWITCH = {
    'name': 'toolswitch',
    'kind': 'Everyday tools in one app',
    'title': f'toolswitch — {N} free tools in one tiny app, with offline AI, for Windows, Mac and Linux',
    'description': f'Free desktop app with {N} everyday tools: clipboard history, text from screen (OCR), AI background remover, audio and WhatsApp voice notes to text, image and PDF compressor, PDF signing, wallpapers, reminders and breaks. The AI runs on your computer: nothing is uploaded, no account. Windows, macOS and Linux.',
    'tagline': f'{N} everyday tools in <strong>one tiny app</strong> that waits in your tray. The AI ones — remove backgrounds, audio to text, text from screen — <strong>run on your computer</strong>: nothing is uploaded, no account, no subscription.',
    'category': 'UtilitiesApplication',
    'keywords': 'powertoys alternative, powertoys for linux, powertoys for mac, offline ai tools, remove background offline, audio to text offline, whatsapp voice note to text, screen ocr, clipboard history, compress pdf offline, sign pdf, desktop utilities, linux utilities',
    'features': [(t['emoji'], t['name'], t['summary']) for t in TOOLS],
    'steps': [
        'Download and install toolswitch. It starts in your tray / top bar.',
        'On the welcome screen, turn on the tools you want.',
        'Use them from anywhere with their shortcut, for example <code>Super</code>+<code>Shift</code>+<code>V</code> for the clipboard (<code>Ctrl</code>+<code>Alt</code> on Windows, <code>Cmd</code>+<code>Option</code> on Mac).',
        'Change any shortcut by clicking it and pressing the keys you like.',
    ],
    'faq': [
        ('What is toolswitch?', f'A small desktop app with {N} everyday tools — clipboard history, text from screen (OCR), wallpapers, reminders, breaks, file compressor, AI background remover, PDF signing and audio to text — that waits in your tray.'),
        ('Do the AI tools upload my files?', 'No. Background removal (BiRefNet), audio to text (OpenAI Whisper) and text from screen (PaddleOCR) run on your computer. Their models are downloaded once and then work offline. Your photos, recordings and screenshots never leave your computer.'),
        ('Is it like Microsoft PowerToys?', 'It’s in the same spirit, but it works the same on Windows, macOS and Linux, and it focuses on everyday tasks instead of developer tools.'),
        ('Can it transcribe WhatsApp voice notes and videos?', 'Yes. Save them to your computer and drag them into Audio to text; it reads Spanish, English and about 100 other languages.'),
        ('How heavy is it?', 'The program is about 15 MB and uses about 90 MB of memory and almost no processor while it waits in the tray. A tool that’s off does nothing at all.'),
        ('Is toolswitch free and open source?', 'Yes. It’s free, with no account and no ads, and its code is open source under the MIT license on GitHub. If it helps you, you can support it with a coffee.'),
    ],
}

# The first apps, now tools inside toolswitch. Their pages stay (people find them by search)
# and describe what the tool does in toolswitch today.
LEGACY = [
    {
        'name': 'wallswitch',
        'tool': 'Wallpapers',
        'kind': 'Wallpaper changer',
        'title': 'wallswitch is now part of toolswitch — free wallpaper changer for Windows, Mac and Linux',
        'description': 'wallswitch, the free automatic wallpaper changer, is now the Wallpapers tool inside toolswitch: rotate your wallpapers automatically and switch them with keyboard shortcuts. Windows, macOS and Linux.',
        'keywords': 'wallpaper changer, automatic wallpaper rotation, wallpaper slideshow, change wallpaper shortcut, ubuntu wallpaper changer, windows 11 wallpaper changer',
        'features': [
            ('🖼️', 'Your wallpapers in a grid', 'Add folders or single images; click to add them to the rotation, double-click to set one now.'),
            ('⏱️', 'Automatic change', 'They rotate by themselves every few minutes or hours — you pick the interval.'),
            ('⌨️', 'Keyboard shortcuts', 'Random, next and previous wallpaper from anywhere. Record your own keys.'),
        ],
    },
    {
        'name': 'clipswitch',
        'tool': 'Clipboard history',
        'kind': 'Clipboard manager',
        'title': 'clipswitch is now part of toolswitch — free clipboard history for Windows, Mac and Linux',
        'description': 'clipswitch, the free clipboard manager, is now the Clipboard history tool inside toolswitch: everything you copy, text and images, one keyboard shortcut away. Private and offline.',
        'keywords': 'clipboard manager, clipboard history, copy paste history, clipboard history linux, clipboard manager mac free, ditto alternative, windows clipboard history alternative',
        'features': [
            ('📋', 'Clipboard history', 'What you copied, newest first. Search it, use the arrows and Enter.'),
            ('🖼️', 'Images too', 'Screenshots and copied pictures, with a preview.'),
            ('⭐', 'Pin favorites', 'Pinned entries stay at the top and are never deleted.'),
        ],
    },
    {
        'name': 'tinyswitch',
        'tool': 'Compress files',
        'kind': 'Image & document compressor',
        'title': 'tinyswitch is now part of toolswitch — compress images, PDF, Word and PowerPoint offline',
        'description': 'tinyswitch, the free offline compressor, is now the Compress tool inside toolswitch: make JPG, PNG, PDF, Word, PowerPoint and Excel files smaller by dragging them in. Nothing is uploaded.',
        'keywords': 'compress images offline, compress pdf without uploading, reduce pdf size, compress powerpoint, reduce word file size, tinypng alternative, image compressor windows mac linux',
        'features': [
            ('🖼️', 'Images', 'JPG and PNG (smart palette, like TinyPNG).'),
            ('📄', 'PDF, Word, PowerPoint, Excel', 'Shrinks the photos inside; text and layout stay the same.'),
            ('🔒', 'Offline', 'Your files never leave your computer. A smaller copy is saved next to each one as name-min.'),
        ],
    },
]

# Visit counter (goatcounter.com): no cookies, nothing personal. The account's code, as in
# https://CODE.goatcounter.com; empty = no counter. Downloads count as events (download.js).
GOATCOUNTER = 'berchj'
ANALYTICS = (f'<script data-goatcounter="https://{GOATCOUNTER}.goatcounter.com/count" async '
             'src="https://gc.zgo.at/count.v4.js" crossorigin="anonymous" '
             'integrity="sha384-nRw6qfbWyJha9LhsOtSb2YJDyZdKvvCFh0fJYlkquSFjUxp9FVNugbfy8q1jdxI+"></script>\n'
             if GOATCOUNTER else '')

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
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<link rel="canonical" href="{url}">
<meta name="google-site-verification" content="UphS3aDveMRVv07rEHt7og08iggwHPVThZJLNYE1Gpw">
<meta property="og:type" content="website">
<meta property="og:site_name" content="toolswitch">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/img/{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(description)}">
<meta name="twitter:image" content="{SITE}/img/{image}">
<link rel="alternate" type="text/plain" title="llms.txt" href="/llms.txt">
<link rel="icon" href="/img/toolswitch-64.png">
<link rel="stylesheet" href="/style.css">
{THEME}
{ANALYTICS}{extra}</head>'''


def nav(current=None):
    current_attr = ' aria-current=page' if current == 'toolswitch' else ''
    return f'<nav><div class="wrap"><a class="home" href="/"><img src="/img/toolswitch-64.png" alt="">toolswitch</a><a class="wide" href="/toolswitch/"{current_attr}>The {N} tools</a><a class="wide" href="/powertoys-alternative/"{" aria-current=page" if current == "powertoys" else ""}>vs PowerToys</a><a href="{REPO_URL}/releases/latest">Download</a><a href="/es/" hreflang="es" lang="es">Español</a></div></nav>'


COUNTED = ('<span>Visits are counted with <a href="https://www.goatcounter.com">GoatCounter</a>: no cookies, nothing personal.</span>\n'
           if GOATCOUNTER else '')


def footer():
    made = f'made by <a href="https://github.com/berchj">berchj</a>'
    code = f' · <a href="{CODE_URL}">source code</a> · MIT license' if OPEN_SOURCE else ''
    tools = ' · '.join(f'<a href="/toolswitch/{t["slug"]}/">{t["name"]}</a>' for t in TOOLS)
    return f'''<footer><div class="wrap">
<p class="tools">{tools}</p>
<span>toolswitch is free · {made}{code}</span>
<span>Like it? <a href="{SUPPORT}">☕ Buy me a coffee</a> · USDT (BEP20): <code>{USDT}</code></span>
{COUNTED}</div></footer>'''


def download_box(label='Download toolswitch', systems='Windows, macOS and Linux', note=LICENSE_TEXT):
    return f'''<div class="download" data-repo="{REPO}">
<a class="btn" href="{REPO_URL}/releases/latest">⬇ <span>{label}</span></a>
<div class="others"><a href="{REPO_URL}/releases/latest">{systems}</a></div>
<div class="npm version">{note}</div>
</div>'''


def software_ld(name, description, url, image, keywords):
    ld = {
        '@context': 'https://schema.org',
        '@type': 'SoftwareApplication',
        'name': name,
        'description': description,
        'applicationCategory': 'UtilitiesApplication',
        'operatingSystem': 'Windows 10, Windows 11, macOS, Linux, Ubuntu',
        'offers': {'@type': 'Offer', 'price': '0', 'priceCurrency': 'USD'},
        'downloadUrl': f'{REPO_URL}/releases/latest',
        'installUrl': f'{REPO_URL}/releases/latest',
        'url': url,
        'image': f'{SITE}/img/{image}',
        'screenshot': f'{SITE}/img/toolswitch-screenshot.png',
        'isAccessibleForFree': True,
        'author': {'@type': 'Person', 'name': 'berchj', 'url': 'https://github.com/berchj'},
        'keywords': keywords,
        'softwareVersion': VERSION,
        'featureList': [t['name'] for t in TOOLS],
        'fileSize': '15 MB',
        'memoryRequirements': '90 MB',
        'publisher': {'@type': 'Person', 'name': 'berchj', 'url': 'https://github.com/berchj'},
    }
    if OPEN_SOURCE:
        ld['license'] = 'https://opensource.org/licenses/MIT'
        ld['sameAs'] = [CODE_URL]
        ld['codeRepository'] = CODE_URL
    return ld


def ld_scripts(*items):
    return ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in items)


TOOL_URL = {t['name']: f"/toolswitch/{t['slug']}/" for t in TOOLS}


def cards(features):
    def card(em, t, d):
        inner = f'<div class="emoji">{em}</div><h3>{t}</h3><p>{d}</p>'
        return f'<a class="card" href="{TOOL_URL[t]}">{inner}</a>' if t in TOOL_URL else f'<div class="card">{inner}</div>'
    return ''.join(card(*f) for f in features)


NOTE = '<p class="note">First launch: the installers aren’t signed with a paid certificate yet. On Windows click <b>More info → Run anyway</b>; on macOS open <b>System Settings → Privacy &amp; Security → Open Anyway</b>.</p>'


def toolswitch_page():
    app = TOOLSWITCH
    url = f'{SITE}/toolswitch/'
    ld = ld_scripts(
        software_ld('toolswitch', app['description'], url, 'toolswitch-icon.png', app['keywords']),
        {
            '@context': 'https://schema.org',
            '@type': 'FAQPage',
            'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in app['faq']],
        },
    )
    steps = ''.join(f'<li>{s}</li>' for s in app['steps'])
    faq = ''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in app['faq'])
    code = f'<section class="wrap"><p>Source code and issues: <a href="{CODE_URL}">github.com/{CODE}</a> · downloads: <a href="{REPO_URL}/releases">github.com/{REPO}</a></p></section>' if OPEN_SOURCE else ''
    return f'''{head(app['title'], app['description'], url, 'toolswitch-social.png', ld + '<meta name="keywords" content="' + html.escape(app['keywords']) + '">' + chr(10))}
<body class="toolswitch">
{nav('toolswitch')}
<main>
<div class="hero wrap">
<img class="icon" src="/img/toolswitch-icon.png" alt="toolswitch icon" width="96" height="96">
<h1>toolswitch</h1>
<p class="tagline">{app['tagline']}</p>
{download_box()}
<div class="shot"><img src="/img/toolswitch-screenshot.png" alt="Screenshot of toolswitch: the list of tools with their switches and shortcuts"></div>
</div>

<section class="wrap">
<h2>{N} tools, one app</h2>
<div class="grid">{cards(app['features'])}</div>
</section>

<section class="wrap">
<h2>How to use it</h2>
<ol class="steps">{steps}</ol>
{NOTE}
</section>

<section class="wrap">
<h2>Questions</h2>
{faq}
</section>
{code}
</main>
{footer()}
<script src="/download.js" defer></script>
</body>
</html>
'''


def legacy_page(app):
    n = app['name']
    url = f'{SITE}/{n}/'
    ld = ld_scripts(software_ld('toolswitch', app['description'], url, 'toolswitch-icon.png', app['keywords']))
    return f'''{head(app['title'], app['description'], url, 'toolswitch-social.png', ld + '<meta name="keywords" content="' + html.escape(app['keywords']) + '">' + chr(10))}
<body class="toolswitch">
{nav()}
<main>
<div class="hero wrap">
<img class="icon" src="/img/toolswitch-icon.png" alt="toolswitch icon" width="96" height="96">
<h1>{n} is now part of toolswitch</h1>
<p class="tagline">The {app['kind'].lower()} you know is now the <strong>{app['tool']}</strong> tool inside <a href="/toolswitch/">toolswitch</a>: one tiny app with {N} everyday tools for Windows, macOS and Linux.</p>
{download_box()}
</div>

<section class="wrap">
<h2>{app['tool']} in toolswitch</h2>
<div class="grid">{cards(app['features'])}</div>
<p><a href="{TOOL_URL[app['tool']]}">More about {app['tool']} →</a></p>
<p>Plus {N - 1} more tools — clipboard, text from screen, audio to text, background remover, PDF signing and more. <a href="/toolswitch/">See them all</a>.</p>
{NOTE}
</section>
</main>
{footer()}
<script src="/download.js" defer></script>
</body>
</html>
'''


def home_page():
    title = TOOLSWITCH['title']
    description = TOOLSWITCH['description']
    site = {'@context': 'https://schema.org', '@type': 'WebSite', 'name': 'toolswitch', 'url': SITE + '/', 'description': description}
    tools = {
        '@context': 'https://schema.org',
        '@type': 'ItemList',
        'name': f'The {N} tools in toolswitch',
        'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'url': f'{SITE}/toolswitch/{t["slug"]}/', 'name': t['name']} for i, t in enumerate(TOOLS)],
    }
    ld = ld_scripts(site, software_ld('toolswitch', description, SITE + '/', 'toolswitch-icon.png', TOOLSWITCH['keywords']), tools)
    alt = f'<link rel="alternate" hreflang="en" href="{SITE}/">\n<link rel="alternate" hreflang="es" href="{SITE}/es/">\n<link rel="alternate" hreflang="x-default" href="{SITE}/">\n'
    return f'''{head(title, description, SITE + '/', 'toolswitch-social.png', ld + alt)}
<body class="toolswitch">
{nav()}
<main>
<div class="hero wrap">
<img class="icon" src="/img/toolswitch-icon.png" alt="toolswitch icon" width="96" height="96">
<h1>toolswitch</h1>
<p class="tagline">{TOOLSWITCH['tagline']}</p>
{download_box()}
<p><a href="/toolswitch/">See the {N} tools →</a></p>
</div>
<section class="wrap">
<div class="grid">{cards(TOOLSWITCH['features'])}</div>
<p class="note">wallswitch, clipswitch and tinyswitch are now tools inside toolswitch.</p>
</section>
</main>
{footer()}
<script src="/download.js" defer></script>
</body>
</html>
'''


def shortcut(key, plain=False):
    """The tool's shortcut on each system."""
    combos = [('Linux', 'Super+Shift'), ('Windows', 'Ctrl+Alt'), ('Mac', 'Cmd+Option')]
    if plain:
        return ', '.join(f'{c}+{key} on {os}' for os, c in combos)
    kbd = lambda c: '+'.join(f'<code>{k}</code>' for k in (c + '+' + key).split('+'))
    return ' · '.join(f'{kbd(c)} on {os}' for os, c in combos)


def breadcrumb_ld(*items):
    return {
        '@context': 'https://schema.org',
        '@type': 'BreadcrumbList',
        'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': u} for i, (n, u) in enumerate(items)],
    }


def faq_ld(faq):
    return {
        '@context': 'https://schema.org',
        '@type': 'FAQPage',
        'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq],
    }


def faq_html(faq):
    return ''.join(f'<details><summary>{html.escape(q)}</summary><p>{html.escape(a)}</p></details>' for q, a in faq)


def strip_tags(text):
    import re
    return re.sub(r'<[^>]+>', '', text)


def tool_page(t):
    url = f'{SITE}/toolswitch/{t["slug"]}/'
    title = f'{t["title"]} | toolswitch'
    app = software_ld(f'toolswitch — {t["name"]}', t['description'], url, 'toolswitch-icon.png', t['keywords'])
    howto = {
        '@context': 'https://schema.org',
        '@type': 'HowTo',
        'name': f'How to use {t["name"]} in toolswitch',
        'step': [{'@type': 'HowToStep', 'position': i + 1, 'text': strip_tags(s)} for i, s in enumerate(t['steps'])],
    }
    crumbs = breadcrumb_ld(('toolswitch', f'{SITE}/toolswitch/'), (t['name'], url))
    ld = ld_scripts(app, faq_ld(t['faq']), howto, crumbs)
    points = ''.join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a, b in t['points'])
    steps = ''.join(f'<li>{s}</li>' for s in t['steps'])
    replaces = ', '.join(t['replaces'])
    others = ''.join(f'<a class="card" href="/toolswitch/{o["slug"]}/"><div class="emoji">{o["emoji"]}</div><h3>{o["name"]}</h3></a>' for o in TOOLS if o is not t)
    return f'''{head(title, t['description'], url, 'toolswitch-social.png', ld + '<meta name="keywords" content="' + html.escape(t['keywords']) + '">' + chr(10))}
<body class="toolswitch">
{nav()}
<main>
<p class="crumbs wrap"><a href="/toolswitch/">toolswitch</a> › {t['name']}</p>
<div class="hero wrap">
<div class="big-emoji" aria-hidden="true">{t['emoji']}</div>
<h1>{t['title']}</h1>
<p class="tagline">{t['intro']}</p>
{download_box()}
<p class="keys">Shortcut: {shortcut(t['key'])}</p>
</div>

<section class="wrap">
<h2>What it does</h2>
<div class="grid">{points}</div>
</section>

<section class="wrap">
<h2>How to use it</h2>
<ol class="steps"><li>Download and install <a href="/toolswitch/">toolswitch</a>. It waits in your tray / top bar.</li>{steps}</ol>
<p>Use it instead of: {replaces}.</p>
{NOTE}
</section>

<section class="wrap">
<h2>Questions</h2>
{faq_html(t['faq'])}
</section>

<section class="wrap">
<h2>{N - 1} more tools in the same app</h2>
<div class="grid mini">{others}</div>
</section>
</main>
{footer()}
<script src="/download.js" defer></script>
</body>
</html>
'''


def powertoys_page():
    p = POWERTOYS
    url = f'{SITE}/{p["slug"]}/'
    ld = ld_scripts(
        software_ld('toolswitch', p['description'], url, 'toolswitch-icon.png', 'powertoys alternative, powertoys for mac, powertoys for linux, powertoys mac alternative, powertoys linux alternative'),
        faq_ld(p['faq']),
        breadcrumb_ld(('toolswitch', f'{SITE}/toolswitch/'), ('PowerToys alternative', url)),
    )
    rows = ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in p['rows'])
    return f'''{head(p['title'], p['description'], url, 'toolswitch-social.png', ld)}
<body class="toolswitch">
{nav('powertoys')}
<main>
<div class="hero wrap">
<img class="icon" src="/img/toolswitch-icon.png" alt="toolswitch icon" width="96" height="96">
<h1>{p['h1']}</h1>
<p class="tagline">{p['intro']}</p>
{download_box()}
</div>

<section class="wrap">
<h2>PowerToys vs toolswitch</h2>
<div class="table"><table>
<thead><tr><th></th><th>PowerToys</th><th>toolswitch</th></tr></thead>
<tbody>{rows}</tbody>
</table></div>
</section>

<section class="wrap">
<h2>Questions</h2>
{faq_html(p['faq'])}
</section>

<section class="wrap">
<h2>The {N} tools</h2>
<div class="grid">{cards(TOOLSWITCH['features'])}</div>
</section>
</main>
{footer()}
<script src="/download.js" defer></script>
</body>
</html>
'''


def moved_page(t):
    """A tool taken out of the app: its old address sends people to the list of tools."""
    to = f'{SITE}/toolswitch/'
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{html.escape(t['name'])} — toolswitch</title>
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="{to}">
<meta http-equiv="refresh" content="0; url={to}">
</head>
<body><p>{html.escape(t['name'])} isn’t in toolswitch anymore. <a href="{to}">See the tools</a>.</p></body>
</html>
'''


ES = {
    'title': f'toolswitch — {N} herramientas gratis con IA sin internet para Windows, Mac y Linux',
    'description': f'App gratis con {N} herramientas: quitar el fondo de fotos, pasar audios y videos de WhatsApp a texto, copiar texto de la pantalla (OCR), comprimir PDF e imágenes, firmar PDF, historial del portapapeles y más. La IA corre en tu computadora: no subís nada, sin cuenta.',
    'tagline': f'{N} herramientas en <strong>una app chiquita</strong> que espera en la bandeja. Las de inteligencia artificial — quitar fondos, audio a texto, texto de la pantalla — <strong>corren en tu computadora</strong>: no subís nada, sin cuenta, sin suscripción.',
    'keywords': 'quitar fondo sin internet, quitar fondo de imagen gratis, pasar audio de whatsapp a texto, transcribir audio gratis sin internet, convertir audio a texto, copiar texto de una imagen, ocr gratis, comprimir pdf sin subir, firmar pdf gratis, historial portapapeles, alternativa powertoys linux',
    'features': [
        ('🎤', 'Audio a texto', 'Audios y videos de WhatsApp, grabaciones y reuniones a texto, sin internet, en español y ~100 idiomas (Whisper).', 'audio-to-text'),
        ('✂️', 'Quitar fondo', 'PNG transparente de cualquier foto con IA que corre en tu PC. Sin marca de agua ni límites.', 'remove-background'),
        ('🔍', 'Texto de la pantalla', 'Marcás una parte de la pantalla y copiás el texto (OCR). Lee tildes, ñ y tablas.', 'text-from-screen'),
        ('📦', 'Comprimir archivos', 'JPG, PNG, PDF, Word, PowerPoint y Excel más livianos. El original no se toca.', 'compress-files'),
        ('✒️', 'Firmar PDF', 'Dibujás tu firma una vez, la arrastrás a su lugar y firmás sin imprimir ni escanear.', 'sign-pdf'),
        ('📋', 'Historial del portapapeles', 'Todo lo que copiás, textos e imágenes, a un atajo de distancia.', 'clipboard-history'),
        ('🖼️', 'Fondos de pantalla', 'Elegís tus fondos y cambian con un atajo o cada tantos minutos.', 'wallpaper-changer'),
        ('⏰', 'Recordatorios', 'Escribís “en 20 min llamar a Juan” y te avisa. Sin calendario ni cuenta.', 'reminders'),
        ('☕', 'Pausas', 'Descanso de vista cada 20 minutos (20-20-20) o Pomodoro.', 'break-reminder'),
    ],
    'faq': [
        ('¿Cómo paso un audio de WhatsApp a texto en la computadora?', 'Guardá el audio o el video (o descargalo desde WhatsApp Web), abrí Audio a texto en toolswitch y arrastralo. En unos segundos tenés el texto, sin subirlo a ninguna página.'),
        ('¿Puedo quitar el fondo de una foto sin internet?', 'Sí. toolswitch usa un modelo de IA (BiRefNet) que se descarga una vez y después funciona sin conexión, sin marca de agua ni límites.'),
        ('¿Sube mis archivos a algún lado?', 'No. Todo corre en tu computadora: fotos, audios y capturas nunca salen de tu PC.'),
        ('¿Es gratis?', 'Sí, es gratis, sin cuenta y sin publicidad, y el código es abierto (licencia MIT, en GitHub). Si te sirve, podés invitarme un cafecito.'),
        ('¿Funciona en Linux?', 'Sí, en Ubuntu y otras distribuciones, igual que en Windows y Mac. Es una alternativa a PowerToys, que solo existe para Windows.'),
        ('¿Cuánto pesa?', 'Unos 15 MB, y usa unos 90 MB de memoria y casi nada de procesador mientras espera en la bandeja.'),
    ],
}


def es_page():
    url = f'{SITE}/es/'
    ld = ld_scripts(
        software_ld('toolswitch', ES['description'], url, 'toolswitch-icon.png', ES['keywords']) | {'inLanguage': 'es'},
        faq_ld(ES['faq']) | {'inLanguage': 'es'},
    )
    alt = f'<link rel="alternate" hreflang="en" href="{SITE}/">\n<link rel="alternate" hreflang="es" href="{url}">\n<link rel="alternate" hreflang="x-default" href="{SITE}/">\n'
    page = head(ES['title'], ES['description'], url, 'toolswitch-social.png', ld + alt + '<meta name="keywords" content="' + html.escape(ES['keywords']) + '">\n')
    page = page.replace('<html lang="en">', '<html lang="es">').replace('<meta property="og:type" content="website">', '<meta property="og:type" content="website">\n<meta property="og:locale" content="es_AR">')
    cards_es = ''.join(f'<a class="card" href="/toolswitch/{slug}/"><div class="emoji">{em}</div><h3>{t}</h3><p>{d}</p></a>' for em, t, d, slug in ES['features'])
    return f'''{page}
<body class="toolswitch">
{nav()}
<main>
<div class="hero wrap">
<img class="icon" src="/img/toolswitch-icon.png" alt="ícono de toolswitch" width="96" height="96">
<h1>toolswitch: herramientas con IA que corren en tu computadora</h1>
<p class="tagline">{ES['tagline']}</p>
{download_box('Descargar toolswitch', 'Windows, macOS y Linux', 'Gratis · código abierto · sin cuenta')}
<div class="shot"><img src="/img/toolswitch-screenshot.png" alt="Captura de toolswitch con la lista de herramientas"></div>
</div>

<section class="wrap">
<h2>Las {N} herramientas</h2>
<div class="grid">{cards_es}</div>
</section>

<section class="wrap">
<h2>Cómo se usa</h2>
<ol class="steps">
<li>Descargá e instalá toolswitch. Queda esperando en la bandeja / barra de arriba.</li>
<li>En la bienvenida, prendé las herramientas que quieras.</li>
<li>Usalas desde cualquier lado con su atajo, por ejemplo <code>Super</code>+<code>Shift</code>+<code>V</code> para el portapapeles (<code>Ctrl</code>+<code>Alt</code> en Windows, <code>Cmd</code>+<code>Option</code> en Mac).</li>
</ol>
<p class="note">Primera vez: los instaladores todavía no están firmados con un certificado pago. En Windows tocá <b>Más información → Ejecutar de todas formas</b>; en Mac, <b>Configuración del Sistema → Privacidad y seguridad → Abrir igualmente</b>.</p>
</section>

<section class="wrap">
<h2>Preguntas</h2>
{faq_html(ES['faq'])}
</section>

<section class="wrap">
<h2>Apoyá toolswitch</h2>
<p>toolswitch es gratis y lo hace una sola persona. Si te ahorra tiempo, <a href="{SUPPORT}">invitame un cafecito ☕</a> (desde Argentina, en pesos) o mandá USDT (solo red BNB Smart Chain, BEP20): <code>{USDT}</code></p>
</section>
</main>
{footer()}
<script src="/download.js" defer></script>
</body>
</html>
'''


def llms_full_txt():
    """Everything on the site in one plain text file, for AI assistants."""
    lines = [llms_txt().rstrip(), '', '# Each tool in detail', '']
    for t in TOOLS:
        lines += [f'## {t["name"]} — {t["title"]}', '', f'URL: {SITE}/toolswitch/{t["slug"]}/', f'Shortcut: {shortcut(t["key"], plain=True)}.', '', strip_tags(t['intro']), '']
        lines += [f'- {a}: {strip_tags(b)}' for a, b in t['points']]
        lines += ['', 'How to use it:'] + [f'{i + 1}. {strip_tags(s)}' for i, s in enumerate(t['steps'])]
        lines += ['', f'Alternative to: {", ".join(t["replaces"])}.', '']
        lines += [f'Q: {q}\nA: {a}' for q, a in t['faq']]
        lines.append('')
    p = POWERTOYS
    lines += [f'# {p["h1"]}', '', f'URL: {SITE}/{p["slug"]}/', '', p['intro'], '', '| | PowerToys | toolswitch |', '|---|---|---|']
    lines += [f'| {a} | {b} | {c} |' for a, b, c in p['rows']]
    lines += [''] + [f'Q: {q}\nA: {a}' for q, a in p['faq']]
    return '\n'.join(lines) + '\n'


def llms_txt():
    a = TOOLSWITCH
    lines = [
        '# toolswitch',
        '',
        f'> toolswitch: {a["description"]}',
        '',
        f'- Website: {SITE}/toolswitch/',
        f'- Download: {REPO_URL}/releases/latest',
    ]
    if OPEN_SOURCE:
        lines.append(f'- Source code (MIT): {CODE_URL}')
    lines += [f'- Compared with Microsoft PowerToys: {SITE}/{POWERTOYS["slug"]}/', f'- Full text of the site: {SITE}/llms-full.txt', f'- En español: {SITE}/es/']
    lines += ['', '## Tools', '']
    lines += [f'- [{t}]({SITE}{TOOL_URL[t]}): {d}' for _, t, d in a['features']]
    lines += ['', '## Questions', '']
    lines += [f'- {q} {ans}' for q, ans in a['faq']]
    lines += ['', '## Earlier apps', '']
    lines += [f'- {x["name"]} ({x["kind"].lower()}) is now the {x["tool"]} tool in toolswitch: {SITE}/{x["name"]}/' for x in LEGACY]
    return '\n'.join(lines) + '\n'


def main():
    (ROOT / 'index.html').write_text(home_page())
    pages = {'toolswitch': toolswitch_page(), POWERTOYS['slug']: powertoys_page()}
    pages |= {f'toolswitch/{t["slug"]}': tool_page(t) for t in TOOLS}
    pages |= {x['name']: legacy_page(x) for x in LEGACY}
    pages['es'] = es_page()
    for name, page in pages.items():
        d = ROOT / name
        d.mkdir(parents=True, exist_ok=True)
        (d / 'index.html').write_text(page)
    for t in HIDDEN_TOOLS:
        d = ROOT / 'toolswitch' / t['slug']
        d.mkdir(parents=True, exist_ok=True)
        (d / 'index.html').write_text(moved_page(t))
    urls = [SITE + '/'] + [f'{SITE}/{name}/' for name in pages]
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n' for u in urls) + '</urlset>\n')
    # Search engines and AI assistants are all welcome: being quoted by them is the point.
    bots = ['Googlebot', 'Bingbot', 'GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-SearchBot', 'Claude-User', 'PerplexityBot', 'Perplexity-User', 'Google-Extended', 'Applebot', 'Applebot-Extended', 'DuckAssistBot', 'CCBot']
    (ROOT / 'robots.txt').write_text(''.join(f'User-agent: {b}\nAllow: /\n\n' for b in bots) + f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
    (ROOT / 'llms.txt').write_text(llms_txt())
    (ROOT / 'llms-full.txt').write_text(llms_full_txt())
    (ROOT / f'{INDEXNOW_KEY}.txt').write_text(INDEXNOW_KEY)
    (ROOT / '.nojekyll').write_text('')
    print('built', len(urls), 'pages')


if __name__ == '__main__':
    main()
