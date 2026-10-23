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

# toolswitch: every tool in one app. Its code is private; the installers are published in this
# public repository, the downloads for every page.
REPO = 'berchj/toolswitch-releases'
REPO_URL = f'https://github.com/{REPO}'
# Says "open source" and links the code only when the repository is public.
OPEN_SOURCE = False
LICENSE_TEXT = 'Free · open source · MIT license' if OPEN_SOURCE else 'Free · no account · no ads'

TOOLSWITCH = {
    'name': 'toolswitch',
    'kind': 'Everyday tools in one app',
    'title': 'toolswitch — 18 free everyday tools in one tiny app for Windows, Mac and Linux',
    'description': 'Free desktop app with 18 everyday tools: clipboard history, text from screen (OCR), wallpaper changer, reminders, Google Calendar, breaks, image and PDF compressor, background remover, PDF signing, audio to text, tidy downloads, backup, clean up, PC monitor, shut down timer, updates, security check and Jira. Offline, no account. Windows, macOS and Linux.',
    'tagline': '18 everyday tools in <strong>one tiny app</strong> that waits in your tray. Turn on the ones you want and use them from anywhere with a shortcut.',
    'category': 'UtilitiesApplication',
    'keywords': 'powertoys alternative, desktop utilities, clipboard history, screen ocr, wallpaper changer, compress pdf offline, remove background offline, sign pdf, pomodoro timer, shutdown timer, linux utilities, windows utilities, mac utilities',
    'features': [
        ('📋', 'Clipboard history', 'Everything you copy, text and images, one shortcut away. Search it and pin favorites.'),
        ('🔍', 'Text from screen', 'Select part of the screen and copy the text in it (OCR). Reads accents and ñ, in 30+ languages.'),
        ('🖼️', 'Wallpapers', 'Pick your wallpapers and switch them with a shortcut or every few minutes.'),
        ('⏰', 'Reminders', 'Write “in 20 min call Juan” and get a notification then. No calendar, no account.'),
        ('📅', 'Calendar', 'Your Google Calendar: today’s events, new ones with guests, and a heads-up 10 minutes before each.'),
        ('☕', 'Breaks', 'Rest your eyes every 20 minutes (20-20-20), or work with a Pomodoro timer.'),
        ('📦', 'Compress files', 'Smaller JPG, PNG, PDF, Word, PowerPoint and Excel files. Your originals stay untouched.'),
        ('✂️', 'Remove background', 'Transparent PNG of any photo, with an AI model that runs on your computer.'),
        ('✒️', 'Sign PDF', 'Draw your signature once, drag it to its place on the page and sign PDFs without printing them.'),
        ('🎤', 'Audio to text', 'Voice notes, recordings and videos into text, offline, in ~100 languages (Whisper).'),
        ('📂', 'Tidy downloads', 'Moves what you download to its folder by type, by itself. Every move can be undone.'),
        ('💾', 'Backup', 'Copies the folders you pick to another disk every day. Only what changed.'),
        ('♻️', 'Clean up', 'Shows what takes space — trash, caches, old downloads, big files — and frees it.'),
        ('📈', 'Watch the PC', 'Warns when a disk is almost full or a program gets stuck eating the processor or memory.'),
        ('🔌', 'Shut down timer', 'Shut down, restart or sleep later, at a time, or when the downloads finish.'),
        ('🛡️', 'Security check', 'Finds what’s risky in how your computer is set up — firewall, open ports, updates, encryption — and how to fix it. Claude can write the plan.'),
        ('☑️', 'Jira', 'The Jira issues assigned to you, and a heads-up when you get a new one.'),
        ('⟳', 'Updates', 'Updates the system and your apps with one click, and tells you when there’s something new.'),
    ],
    'steps': [
        'Download and install toolswitch. It starts in your tray / top bar.',
        'On the welcome screen, turn on the tools you want.',
        'Use them from anywhere with their shortcut, for example <code>Super</code>+<code>Shift</code>+<code>V</code> for the clipboard (<code>Ctrl</code>+<code>Alt</code> on Windows, <code>Cmd</code>+<code>Option</code> on Mac).',
        'Change any shortcut by clicking it and pressing the keys you like.',
    ],
    'faq': [
        ('What is toolswitch?', 'A small desktop app with 18 everyday tools — clipboard history, screen OCR, wallpapers, reminders, Google Calendar, breaks, file compressor, background remover, PDF signing, audio to text, tidy downloads, backup, clean up, PC monitor, shut down timer, updates, security check and Jira — that waits in your tray.'),
        ('Is it like Microsoft PowerToys?', 'It’s in the same spirit, but it works the same on Windows, macOS and Linux, and it focuses on everyday tasks instead of developer tools.'),
        ('Does it upload my files or what I copy?', 'No. Everything runs on your computer. The AI models for text from screen, background removal and audio to text are downloaded once and then work offline. Only Calendar and Jira talk to Google and Atlassian, and Security check to Anthropic’s Claude if you add a key — and only when you connect them.'),
        ('How heavy is it?', 'The program is about 15 MB and uses about 90 MB of memory and almost no processor while it waits in the tray. A tool that’s off does nothing at all.'),
        ('Can I use only some of the tools?', 'Yes. Each tool has its own switch; the ones you turn off don’t run.'),
        ('Is toolswitch free?', 'Yes, it’s free to download and use. No account, no ads.'),
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
            ('🖼️', 'Images too', 'Screenshots and copied pictures, with a preview (on Wayland, text only for now).'),
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
<meta name="google-site-verification" content="UphS3aDveMRVv07rEHt7og08iggwHPVThZJLNYE1Gpw">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(description)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/img/{image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/img/toolswitch-64.png">
<link rel="stylesheet" href="/style.css">
{THEME}
{extra}</head>'''


def nav(current=None):
    current_attr = ' aria-current=page' if current == 'toolswitch' else ''
    return f'<nav><div class="wrap"><a class="home" href="/"><img src="/img/toolswitch-64.png" alt="">toolswitch</a><a href="/toolswitch/"{current_attr}>The 18 tools</a><a href="{REPO_URL}/releases/latest">Download</a></div></nav>'


def footer():
    made = f'made by <a href="https://github.com/berchj">berchj</a>'
    code = f' · <a href="{REPO_URL}">source code</a> · MIT license' if OPEN_SOURCE else ''
    return f'''<footer><div class="wrap">
<span>toolswitch is free · {made}{code}</span>
<span>Like it? <a href="{SUPPORT}">☕ Buy me a coffee</a> · USDT (BEP20): <code>{USDT}</code></span>
</div></footer>'''


def download_box(label='Download toolswitch'):
    return f'''<div class="download" data-repo="{REPO}">
<a class="btn" href="{REPO_URL}/releases/latest">⬇ <span>{label}</span></a>
<div class="others"><a href="{REPO_URL}/releases/latest">Windows, macOS and Linux</a></div>
<div class="npm version">{LICENSE_TEXT}</div>
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
    }
    if OPEN_SOURCE:
        ld['license'] = 'https://opensource.org/licenses/MIT'
        ld['sameAs'] = [REPO_URL]
    return ld


def ld_scripts(*items):
    return ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>\n' for x in items)


def cards(features):
    return ''.join(f'<div class="card"><div class="emoji">{em}</div><h3>{t}</h3><p>{d}</p></div>' for em, t, d in features)


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
    code = f'<section class="wrap"><p>Source code, issues and release notes: <a href="{REPO_URL}">github.com/{REPO}</a></p></section>' if OPEN_SOURCE else ''
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
<h2>18 tools, one app</h2>
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
<p class="tagline">The {app['kind'].lower()} you know is now the <strong>{app['tool']}</strong> tool inside <a href="/toolswitch/">toolswitch</a>: one tiny app with 18 everyday tools for Windows, macOS and Linux.</p>
{download_box()}
</div>

<section class="wrap">
<h2>{app['tool']} in toolswitch</h2>
<div class="grid">{cards(app['features'])}</div>
<p>Plus 17 more tools — clipboard, text from screen, reminders, breaks, background remover, PDF signing and more. <a href="/toolswitch/">See them all</a>.</p>
{NOTE}
</section>
</main>
{footer()}
<script src="/download.js" defer></script>
</body>
</html>
'''


def home_page():
    title = 'toolswitch — 18 free everyday tools in one app for Windows, Mac and Linux'
    description = TOOLSWITCH['description']
    ld = {
        '@context': 'https://schema.org',
        '@type': 'ItemList',
        'name': 'toolswitch',
        'itemListElement': [{'@type': 'ListItem', 'position': 1, 'url': f'{SITE}/toolswitch/', 'name': 'toolswitch'}],
    }
    return f'''{head(title, description, SITE + '/', 'toolswitch-social.png', '<script type="application/ld+json">' + json.dumps(ld) + '</script>' + chr(10))}
<body class="toolswitch">
{nav()}
<main>
<div class="hero wrap">
<img class="icon" src="/img/toolswitch-icon.png" alt="toolswitch icon" width="96" height="96">
<h1>toolswitch</h1>
<p class="tagline">{TOOLSWITCH['tagline']}</p>
{download_box()}
<p><a href="/toolswitch/">See the 18 tools →</a></p>
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
        lines.append(f'- Source: {REPO_URL}')
    lines += ['', '## Tools', '']
    lines += [f'- {t}: {d}' for _, t, d in a['features']]
    lines += ['', '## Questions', '']
    lines += [f'- {q} {ans}' for q, ans in a['faq']]
    lines += ['', '## Earlier apps', '']
    lines += [f'- {x["name"]} ({x["kind"].lower()}) is now the {x["tool"]} tool in toolswitch: {SITE}/{x["name"]}/' for x in LEGACY]
    return '\n'.join(lines) + '\n'


def main():
    (ROOT / 'index.html').write_text(home_page())
    pages = {'toolswitch': toolswitch_page()} | {x['name']: legacy_page(x) for x in LEGACY}
    for name, page in pages.items():
        d = ROOT / name
        d.mkdir(exist_ok=True)
        (d / 'index.html').write_text(page)
    urls = [SITE + '/'] + [f'{SITE}/{name}/' for name in pages]
    (ROOT / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{u}</loc><lastmod>{TODAY}</lastmod></url>\n' for u in urls) + '</urlset>\n')
    (ROOT / 'robots.txt').write_text(f'User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n')
    (ROOT / 'llms.txt').write_text(llms_txt())
    (ROOT / '.nojekyll').write_text('')
    print('built', len(urls), 'pages')


if __name__ == '__main__':
    main()
