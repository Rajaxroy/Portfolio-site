"""Render the local portfolio from a small, editable profile. Standard library only."""
import json
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROFILE = json.loads((ROOT / "content/profile.json").read_text())


def e(value):
    return escape(str(value), quote=True)


def icon(name):
    paths = {
        "code": '<path d="m8 7-5 5 5 5m8-10 5 5-5 5m-3-13-2 16"/>',
        "server": '<rect x="3" y="3" width="18" height="7" rx="2"/><rect x="3" y="14" width="18" height="7" rx="2"/><path d="M7 6.5h.01M7 17.5h.01M11 6.5h6M11 17.5h6"/>',
        "database": '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 4 16 4 16 0V5M4 12c0 4 16 4 16 0"/>',
        "workflow": '<rect x="3" y="3" width="6" height="6" rx="1"/><rect x="15" y="15" width="6" height="6" rx="1"/><path d="M9 6h9v9M6 9v9h9"/>',
        "cloud": '<path d="M6 18a5 5 0 0 1-1-10 7 7 0 0 1 13-1 5.5 5.5 0 0 1 0 11H6Z"/>',
        "tools": '<path d="m4 20 9-9m-6-8 3 3-3 3-3-3a6 6 0 0 0 7 7l7 7 3-3-7-7a6 6 0 0 0-7-7Z"/>',
        "arrow": '<path d="M4 12h16m-6-6 6 6-6 6"/>',
        "github": '<path d="M9 19c-4 1-4-2-6-2m12 5v-4a4 4 0 0 0-1-3c4-.5 7-2 7-6a5 5 0 0 0-1-4 5 5 0 0 0 0-4s-2 0-4 2a15 15 0 0 0-8 0C6 1 4 1 4 1a5 5 0 0 0 0 4 5 5 0 0 0-1 4c0 4 3 5.5 7 6a4 4 0 0 0-1 3v4"/>',
        "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 6 9 7 9-7"/>',
        "linkedin": '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M7 10v7m0-10h.01M11 17v-7m0 3c0-4 6-4 6 0v4"/>',
        "book": '<path d="M4 4h6a3 3 0 0 1 2 1 3 3 0 0 1 2-1h6v15h-6a3 3 0 0 0-2 1 3 3 0 0 0-2-1H4V4Zm8 1v15"/>',
    }
    return f'<svg class="icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{paths[name]}</svg>'


def pills(items):
    return ''.join(f'<span class="tag">{e(item)}</span>' for item in items)


def divider():
    return '<div class="divider" aria-hidden="true"><span>✸</span></div>'


def section_heading(label, title, description):
    return f'<div class="section-heading"><p class="eyebrow"><span aria-hidden="true">✦</span> {e(label)}</p><h2>{e(title)}<span class="green-text">.</span></h2><p class="section-intro">{e(description)}</p></div>'


p = PROFILE
nav = ''.join(f'<a href="#{key}">{label}</a>' for key, label in [
    ('skills', 'Skills'), ('experience', 'Experience'), ('projects', 'Projects'), ('education', 'Education'), ('contact', 'Contact')])
skills = ''.join(f'''<article class="sketch-card skill-card">
  <div class="card-heading"><span class="icon-badge {e(group['color'])}">{icon(group['icon'])}</span><h3>{e(group['name'])}</h3><span class="count" aria-label="{len(group['items'])} skills">{len(group['items'])}</span></div>
  <ul class="skill-list" aria-label="{e(group['name'])} skills">{''.join(f'<li><span aria-hidden="true">⌁</span>{e(item)}</li>' for item in group['items'])}</ul>
</article>''' for group in p['skills'])

experience = ''
for i, job in enumerate(p['experience']):
    experience += f'''<article class="sketch-card experience-card">
  <span class="company-marker {e(job['color'])}" aria-hidden="true">{e(job['company'][0])}</span>
  <div class="experience-content"><div class="job-topline"><h3>{e(job['company'])}</h3>{'<span class="status">current</span>' if job['current'] else '<span class="past">past</span>'}</div>
    <p class="job-role">{e(job['role'])} <span>· {e(job['area'])}</span></p><p class="job-dates">{e(job['dates'])}</p>
    <p class="job-intro">{e(job['intro'])}</p>
    <details {'open' if i == 0 else ''}><summary>Selected contributions <span class="chevron" aria-hidden="true">⌄</span></summary><ul class="highlights">{''.join(f'<li>{e(point)}</li>' for point in job['highlights'])}</ul></details>
    <div class="tags">{pills(job['tags'])}</div>
  </div>
</article>'''

project = p['project']
education = p['education']
html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#f3f1e7"><meta name="color-scheme" content="light">
  <title>{e(p['name'])} — {e(p['title'])}</title>
  <meta name="description" content="Raja Roy is a backend software engineer in Bengaluru, building APIs, asynchronous workflows, and reliable fintech systems with Python, Go, and TypeScript.">
  <link rel="icon" href="/assets/monogram.svg" type="image/svg+xml">
  <link rel="preload" href="/assets/fonts/nunito.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/site.css"><script src="/assets/app.js" defer></script>
</head>
<body id="top">
<a class="skip-link" href="#main-content">Skip to content</a>
<header class="site-header"><div class="header-inner"><a class="brand" href="#top"><span class="brand-mark">{e(p['initials'])}</span><span>{e(p['name'])}</span></a><nav aria-label="Primary">{nav}</nav></div></header>
<main id="main-content" class="container">
  <section id="home" aria-label="Introduction" class="hero-section">
    <div class="sketch-card hero"><span class="paper-label">hello, human!</span><span class="sparkle sparkle-one" aria-hidden="true">✦</span><span class="sparkle sparkle-two" aria-hidden="true">✧</span>
      <div class="avatar" aria-label="Raja Roy initials">{e(p['initials'])}<span aria-hidden="true">✦</span></div>
      <h1>{e(p['name'])}</h1><p class="hero-role">{e(p['title'])}</p>
      <div class="hero-meta"><span>{e(p['location'])}</span><span class="meta-separator" aria-hidden="true">·</span><span>Python · Go · TypeScript</span></div>
      <p class="hero-summary">{e(p['summary'])}</p>
      <div class="hero-actions"><a class="button primary" href="#projects">view my work {icon('arrow')}</a><a class="button" href="#contact"><span class="small-dot" aria-hidden="true"></span>get in touch</a><a class="button" href="{e(p['resume'])}" target="_blank" rel="noopener">résumé {icon('arrow')}</a></div>
      <div class="social-links"><a href="{e(p['github'])}" target="_blank" rel="noopener noreferrer">{icon('github')}GitHub</a><a href="{e(p['linkedin'])}" target="_blank" rel="noopener noreferrer">{icon('linkedin')}LinkedIn</a><a href="mailto:{e(p['email'])}">{icon('mail')}Email</a></div>
    </div>
    <aside class="focus-note"><span class="paper-label">how I build</span><p>{e(p['focus'])}</p><span>{e(p['focus_description'])}</span></aside>
  </section>
  {divider()}
  <section id="skills" aria-labelledby="skills-title">
    {section_heading('Tools of the trade', 'A practical toolkit', 'A backend-focused stack shaped by payment workflows, lending platforms, service integrations, and production incidents.')}
    <div class="skills-grid">{skills}</div>
    <div class="toolbox"><p>Working knowledge</p><div>{pills(p['familiarity'])}</div></div>
  </section>
  {divider()}
  <section id="experience" aria-label="Experience">
    {section_heading('The journey so far', 'Experience', 'From security event streams to lending decisions and payroll compliance — building the services behind everyday operations.')}
    <div class="experience-list">{experience}</div>
  </section>
  {divider()}
  <section id="projects" aria-label="Projects">
    {section_heading('Built outside the day job', 'Something I’m building', 'Applying backend engineering and AI assistance to a practical problem: making the job search easier to navigate.')}
    <article class="sketch-card project-card"><span class="paper-label yellow">personal project</span><div class="project-heading"><div><p class="eyebrow">{e(project['label'])}</p><h3>{e(project['name'])}</h3></div><span class="project-symbol" aria-hidden="true">↗</span></div>
      <p>{e(project['description'])}</p><ul class="highlights">{''.join(f'<li>{e(point)}</li>' for point in project['highlights'])}</ul><div class="tags">{pills(project['tags'])}</div>
      <div class="project-actions"><a class="button primary" href="{e(project['url'])}" target="_blank" rel="noopener noreferrer">view project {icon('arrow')}</a><a class="text-link" href="{e(project['github'])}" target="_blank" rel="noopener noreferrer">{icon('github')}Source on GitHub</a></div>
    </article>
    <a class="more-link" href="{e(p['github'])}" target="_blank" rel="noopener noreferrer">more on GitHub {icon('arrow')}</a>
  </section>
  {divider()}
  <section id="education" aria-label="Education">
    {section_heading('The foundation', 'Education', 'An engineering foundation, followed by hands-on work across backend systems and product delivery.')}
    <article class="sketch-card education-card"><span class="icon-badge yellow">{icon('book')}</span><div><h3>{e(education['degree'])}</h3><p>{e(education['institution'])}</p><p class="job-dates">{e(education['dates'])}<span aria-hidden="true"> · </span>{e(education['grade'])}</p></div></article>
  </section>
  {divider()}
  <section id="contact" aria-label="Contact">
    {section_heading('Say hello', 'Let’s build something reliable', 'Have a backend challenge, an engineering role, or a project worth talking about? Let’s connect.')}
    <div class="sketch-card contact-card"><span class="paper-label pink">start a conversation</span><h3>Good systems start with a conversation.</h3><p>APIs, distributed workflows, fintech, or the next useful thing — I’d be happy to hear about it.</p>
      <div class="email-row"><a class="email-link" href="mailto:{e(p['email'])}">{e(p['email'])}</a><button class="copy-button" type="button" aria-label="Copy email address" data-email="{e(p['email'])}">copy</button></div>
      <a class="button primary" href="mailto:{e(p['email'])}?subject=Hello%20Raja">say hello {icon('arrow')}</a><p class="contact-location">{e(p['location'])}<span aria-hidden="true"> · </span>UTC+5:30</p>
      <div class="contact-socials"><span>find me on</span><a href="{e(p['github'])}" target="_blank" rel="noopener noreferrer">GitHub ↗</a><a href="{e(p['linkedin'])}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a><a href="{e(p['resume'])}" target="_blank" rel="noopener">Résumé ↗</a></div>
    </div>
  </section>
</main>
<footer class="container site-footer"><p>{e(p['name'])}<span aria-hidden="true"> · </span>{e(p['title'])}</p><div><span>© 2026</span><button type="button" aria-label="Back to top">↑ Top</button></div></footer>
<div class="toast" role="status" aria-live="polite" aria-atomic="true"></div>
</body></html>
'''
# Set the referenced section title ID without duplicating heading rendering logic.
html = html.replace('<h2>A practical toolkit', '<h2 id="skills-title">A practical toolkit')
(ROOT / 'dist/index.html').write_text(html)
# Do not leave the reference author's writing at a discoverable local route.
(ROOT / 'dist/notes/index.html').write_text('''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Raja Roy — Portfolio</title><meta http-equiv="refresh" content="0;url=/"><link rel="canonical" href="/"></head><body><p>The portfolio has moved to <a href="/">Raja Roy’s home page</a>.</p></body></html>''')
print('Built Raja Roy portfolio from content/profile.json')
