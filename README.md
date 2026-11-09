# Parallelizing a quantum computation simulator

**Ayush Garg · Carnegie Mellon University · 15-418 · Fall 2026**

A static project website based on the final November 9 proposal. The original uploaded PDF is included unchanged. The HTML version has minor spelling and grammar corrections, a clarified gate-universality sentence, and a working citation in place of the PDF's unresolved `[3]` reference.

## Publish with GitHub Pages

1. Create a repository on GitHub and upload the contents of this folder. Preserve the `docs/` folder structure.
2. Open **Settings → Pages**.
3. Under **Build and deployment**, select **Deploy from a branch**.
4. Select your branch (usually `main`) and the **/docs** folder, then save.
5. Use the website URL GitHub reports once deployment completes.

There is no build step and no framework to install. All internal links are relative, so the site works on a repository-specific Pages URL. `docs/.nojekyll` disables Jekyll processing.

## Repository contents

- `docs/index.html` — homepage with project overview, schedule, and report links.
- `docs/proposal.html` — full web proposal with rendered math.
- `docs/proposal.pdf` — your original final proposal PDF, unchanged.
- `docs/style.css` — responsive styling shared by both pages.
- `proposal.md` — editable proposal text and equations.
- `update-proposal.py` — optional helper to regenerate the HTML article from Markdown.

## Preview locally

Open `docs/index.html` directly in a modern browser, or run:

```bash
python3 -m http.server 8000 --directory docs
```

Then visit `http://localhost:8000`. Equations use browser-native MathML; no CDN, fonts, analytics, or JavaScript dependencies are required.

## Update the proposal

Edit `proposal.md`. If Pandoc is installed, regenerate the article with:

```bash
python3 update-proposal.py
```

Alternatively, edit `docs/proposal.html` directly. Replace `docs/proposal.pdf` separately when you have a new PDF. Update the homepage summary and schedule if the plan changes.

The PDF still contains its original project-URL placeholder. After deployment, add the published URL to your document and replace the PDF before submitting.

## Add milestone and final reports

Place each new document in `docs/`. In `docs/index.html`, replace the relevant "Not yet available" label with a link to the actual document. No future report links are active until those files exist. Nothing on this website claims completed experiments or measured speedups.
