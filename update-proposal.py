#!/usr/bin/env python3
"""Regenerate the HTML proposal article while preserving its page layout."""
from pathlib import Path
import subprocess
import re

root = Path(__file__).resolve().parent
page = root / 'docs' / 'proposal.html'
article = subprocess.check_output([
    'pandoc', str(root / 'proposal.md'), '-f', 'markdown', '-t', 'html5',
    '--mathml', '--shift-heading-level-by=1'
], text=True)
parts = re.split(r'(?=<h2\b)', article)
article = parts[0] + ''.join('<section class="content-section">' + part + '</section>\n' for part in parts[1:])
html = page.read_text(encoding='utf-8')
before, remainder = html.split('<article>', 1)
_, after = remainder.split('</article>', 1)
page.write_text(before + '<article>' + article + '</article>' + after,
                encoding='utf-8')
print('Updated docs/proposal.html')
