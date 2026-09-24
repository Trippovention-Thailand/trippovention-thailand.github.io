import os
import re
import sys
import json
from urllib.parse import urlparse, unquote

DOCS_DIR = os.path.abspath('docs')

# 1. Check all HTML tags with href, src, poster, data-src, srcset
HTML_ATTR_PATTERN = re.compile(r'(?:href|src|poster|data-src)\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
SRCSET_PATTERN = re.compile(r'srcset\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)
CSS_URL_PATTERN = re.compile(r'url\s*\(\s*["\']?([^"\'\)\s]+)["\']?\s*\)', re.IGNORECASE)
ONCLICK_PATTERN = re.compile(r'(?:window\.location|location\.href)\s*=\s*["\']([^"\']+)["\']', re.IGNORECASE)

html_files = []
css_files = []
for root, dirs, files in os.walk(DOCS_DIR):
    for f in files:
        full = os.path.join(root, f)
        if f.endswith('.html'):
            html_files.append(full)
        elif f.endswith('.css'):
            css_files.append(full)

print(f"Loaded {len(html_files)} HTML files and {len(css_files)} CSS files.")

# Collect all element IDs and names in each HTML file for anchor resolution
file_anchors = {}
for hfile in html_files:
    rel = os.path.relpath(hfile, DOCS_DIR)
    with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
        c = f.read()
    ids = set(re.findall(r'\bid=["\']([^"\']+)["\']', c, re.IGNORECASE))
    names = set(re.findall(r'\bname=["\']([^"\']+)["\']', c, re.IGNORECASE))
    file_anchors[rel] = ids.union(names)

issues = []

def resolve_target(source_file, url):
    file_dir = os.path.dirname(source_file)
    parsed = urlparse(url)
    path = unquote(parsed.path)
    fragment = parsed.fragment

    if url.startswith(('https://trippovention.co.th', 'http://trippovention.co.th')):
        clean_path = path.lstrip('/')
        if not clean_path:
            clean_path = 'index.html'
        target = os.path.normpath(os.path.join(DOCS_DIR, clean_path))
    elif path.startswith('/'):
        clean_path = path.lstrip('/')
        if not clean_path:
            clean_path = 'index.html'
        target = os.path.normpath(os.path.join(DOCS_DIR, clean_path))
    else:
        target = os.path.normpath(os.path.join(file_dir, path))

    # If target is directory, resolve to index.html
    if os.path.isdir(target):
        target = os.path.join(target, 'index.html')

    return target, fragment

# Check all HTML files
for hfile in html_files:
    rel_src = os.path.relpath(hfile, DOCS_DIR)
    with open(hfile, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Check href, src, etc.
    for match in HTML_ATTR_PATTERN.finditer(content):
        url = match.group(1).strip()
        if not url or url.startswith(('javascript:', 'data:', 'mailto:', 'tel:')):
            continue

        if url.startswith('#'):
            frag = url.lstrip('#')
            if frag and frag not in file_anchors[rel_src]:
                issues.append({
                    'source': rel_src,
                    'type': 'broken_same_page_anchor',
                    'url': url,
                    'detail': f'Anchor #{frag} does not exist in {rel_src}'
                })
            continue

        if url.startswith(('http://', 'https://', '//')):
            if not url.startswith(('https://trippovention.co.th', 'http://trippovention.co.th')):
                # External link
                continue

        target_file, fragment = resolve_target(hfile, url)
        if not os.path.exists(target_file):
            issues.append({
                'source': rel_src,
                'type': 'missing_file',
                'url': url,
                'target': os.path.relpath(target_file, DOCS_DIR) if target_file.startswith(DOCS_DIR) else target_file
            })
        elif fragment and target_file.endswith('.html'):
            target_rel = os.path.relpath(target_file, DOCS_DIR)
            if target_rel in file_anchors and fragment not in file_anchors[target_rel]:
                issues.append({
                    'source': rel_src,
                    'type': 'broken_cross_page_anchor',
                    'url': url,
                    'detail': f'Anchor #{fragment} does not exist in {target_rel}'
                })

    # Check srcset
    for match in SRCSET_PATTERN.finditer(content):
        val = match.group(1).strip()
        candidates = [c.strip().split()[0] for c in val.split(',') if c.strip()]
        for cand in candidates:
            if cand.startswith(('http://', 'https://', 'data:')):
                continue
            target_file, _ = resolve_target(hfile, cand)
            if not os.path.exists(target_file):
                issues.append({
                    'source': rel_src,
                    'type': 'missing_srcset_image',
                    'url': cand,
                    'target': os.path.relpath(target_file, DOCS_DIR) if target_file.startswith(DOCS_DIR) else target_file
                })

    # Check CSS url() in style tags or style attributes
    for match in CSS_URL_PATTERN.finditer(content):
        cand = match.group(1).strip()
        if cand.startswith(('http://', 'https://', 'data:')):
            continue
        clean_cand = cand.split('?')[0].split('#')[0]
        target_file, _ = resolve_target(hfile, clean_cand)
        if not os.path.exists(target_file):
            issues.append({
                'source': rel_src,
                'type': 'missing_inline_css_asset',
                'url': cand,
                'target': os.path.relpath(target_file, DOCS_DIR) if target_file.startswith(DOCS_DIR) else target_file
            })

    # Check onclick navigation
    for match in ONCLICK_PATTERN.finditer(content):
        cand = match.group(1).strip()
        if cand.startswith(('http://', 'https://', 'data:')):
            continue
        clean_cand = cand.split('?')[0].split('#')[0]
        target_file, _ = resolve_target(hfile, clean_cand)
        if not os.path.exists(target_file):
            issues.append({
                'source': rel_src,
                'type': 'missing_onclick_target',
                'url': cand,
                'target': os.path.relpath(target_file, DOCS_DIR) if target_file.startswith(DOCS_DIR) else target_file
            })

# Check all CSS files
for cfile in css_files:
    rel_src = os.path.relpath(cfile, DOCS_DIR)
    with open(cfile, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    for match in CSS_URL_PATTERN.finditer(content):
        cand = match.group(1).strip()
        if cand.startswith(('http://', 'https://', 'data:')):
            continue
        clean_cand = cand.split('?')[0].split('#')[0]
        target_file, _ = resolve_target(cfile, clean_cand)
        if not os.path.exists(target_file):
            issues.append({
                'source': rel_src,
                'type': 'missing_css_url',
                'url': cand,
                'target': os.path.relpath(target_file, DOCS_DIR) if target_file.startswith(DOCS_DIR) else target_file
            })

# Check site.webmanifest
manifest_path = os.path.join(DOCS_DIR, 'site.webmanifest')
if os.path.exists(manifest_path):
    with open(manifest_path, 'r', encoding='utf-8') as f:
        try:
            mdata = json.load(f)
            icons = mdata.get('icons', [])
            for icon in icons:
                src = icon.get('src')
                if src:
                    target_file, _ = resolve_target(manifest_path, src)
                    if not os.path.exists(target_file):
                        issues.append({
                            'source': 'site.webmanifest',
                            'type': 'missing_manifest_icon',
                            'url': src,
                            'target': os.path.relpath(target_file, DOCS_DIR) if target_file.startswith(DOCS_DIR) else target_file
                        })
        except Exception as e:
            issues.append({
                'source': 'site.webmanifest',
                'type': 'manifest_json_error',
                'url': 'site.webmanifest',
                'detail': str(e)
            })

# Check llms.txt and llms-full.txt
for llm_file in ['llms.txt', 'llms-full.txt']:
    fpath = os.path.join(DOCS_DIR, llm_file)
    if os.path.exists(fpath):
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        for m in re.finditer(r'https://trippovention\.co\.th(/[^\s\)\],]*)', c):
            raw_url = m.group(0)
            target_file, fragment = resolve_target(fpath, raw_url)
            if not os.path.exists(target_file):
                issues.append({
                    'source': llm_file,
                    'type': 'missing_llm_file_link',
                    'url': raw_url,
                    'target': os.path.relpath(target_file, DOCS_DIR) if target_file.startswith(DOCS_DIR) else target_file
                })

# Print summary
print(f"\n==========================================")
print(f"Total issues found: {len(issues)}")
print(f"==========================================")
for i in issues:
    print(f"[{i['type']}] in {i['source']}")
    print(f"  URL: {i['url']}")
    if 'detail' in i:
        print(f"  Detail: {i['detail']}")
    if 'target' in i:
        print(f"  Resolved Target: {i['target']}")
    print()
