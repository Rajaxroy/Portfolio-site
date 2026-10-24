# Raja Roy — Backend Software Engineer

A local portfolio personalized from Raja Roy's résumé. Preserves the reference's cream paper, sketch borders, pastel accents, local Nunito font, and compact layout.

## Run

```sh
cd /home/eos/Development/portfolio-clone
npm run dev
```

Open http://localhost:4173 or http://localhost:4173/#skills. No package installation is required. Python 3 serves the static files.

## Edit

Update `content/profile.json`, then run `npm run build` and `npm run check`. Structural edits belong in `scripts/build.py`. Visual styles are in `dist/assets/site.css`; email copying, active navigation, and back-to-top behavior are in `dist/assets/app.js`. Experience disclosures use native HTML `details` and work without JavaScript.

## Sources and limits

- `/home/eos/Development/resume-updates/Raja_Roy_Backend_Resume_RoleOS.pdf`: identity, contact links, location, experience, metrics, skills, and education. A copy is linked by the résumé buttons.
- `/home/eos/Development/job-search-agent/README.md`: current RoleOS functionality. The résumé mentions LangGraph, while this README explicitly excludes it; the portfolio does not claim LangGraph.
- The local RoleOS Git remote supplies its source link.

ChatGPT history was not accessible. Dates and metrics reflect the local résumé and have not been independently verified. No headshot, availability status, response-time promise, contribution counts, or personal articles were invented. An initials avatar replaces the reference portrait; `/notes/` redirects home.

The résumé's phone number is not repeated on the page; it remains in the downloadable PDF. Production: https://raja-roy-portfolio.vercel.app. Source branch: https://github.com/Rajaxroy/Portfolio-site/tree/raja-roy-portfolio. Vercel deployments currently use direct source uploads; automatic Git deployments are not configured. External project and profile links use destinations supplied by the résumé or local project metadata.

Checks cover JavaScript syntax, identity, assets, anchors, accessible heading references, and removal of the previous owner's content. The production page was checked at desktop and mobile viewport sizes with REA, including navigation, experience disclosures, email copying, and page errors. Local server sockets remain blocked in this session.

REA observations and screenshots remain in `evidence/` for design provenance, outside the served `dist/` directory. They describe the reference author, not Raja Roy.
