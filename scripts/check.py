"""Check profile integrity and navigation without a browser or server."""
import json
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / 'dist'
profile = json.loads((ROOT / 'content/profile.json').read_text())


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.references, self.labelledby, self.scripts = [], [], [], []
        self.h1_count = 0

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        for key in ('href', 'src'):
            if key in attrs:
                self.references.append(attrs[key])
        self.labelledby.extend(attrs.get('aria-labelledby', '').split())
        self.h1_count += tag == 'h1'
        if tag == 'script':
            self.scripts.append(attrs.get('src'))


for path in DIST.rglob('*.html'):
    text = path.read_text()
    parsed = Page()
    parsed.feed(text)
    assert len(set(parsed.ids)) == len(parsed.ids), f'Duplicate IDs: {path}'
    for target in parsed.labelledby:
        assert target in parsed.ids, f'Missing accessible heading: {target}'
    for url in parsed.references:
        if url.startswith('#'):
            assert url[1:] in parsed.ids, f'Broken anchor {url}'
        if url.startswith('/'):
            target = DIST / url.split('?')[0].split('#')[0].lstrip('/')
            assert target.exists(), f'Missing file {url}'
    assert not re.search(r'ismile|iamismile|thisisismile|Tuco', text, re.I), f'Stale identity: {path}'
    if path == DIST / 'index.html':
        assert parsed.h1_count == 1
        assert parsed.scripts == ['/assets/app.js']
        for value in [profile['name'], profile['email'], profile['github'], 'Razorpay', 'Kinara Capital', 'Netsurion', 'RoleOS']:
            assert value in text, f'Missing profile content: {value}'
    print('PASS', path.relative_to(ROOT), 'identity, assets, anchors, accessible headings')

for url in re.findall(r"url\(['\"]?([^)'\"]+)", (DIST / 'assets/site.css').read_text()):
    assert (DIST / url.lstrip('/')).is_file(), f'Missing CSS resource: {url}'
assert not (DIST / 'assets/avatar.png').exists(), 'Reference portrait is still served'
assert not (DIST / 'assets/contributions.json').exists(), 'Reference contributions are still served'
print('PASS local fonts and removal of reference owner assets')
