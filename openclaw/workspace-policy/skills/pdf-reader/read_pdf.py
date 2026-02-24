#!/usr/bin/env python3
import sys
import argparse
from pathlib import Path
import fitz  # PyMuPDF

APPROVED_DIR = Path.home() / '.openclaw' / 'workspaces' / 'default' / 'docs' / 'govt-policies'

def is_inside(p: Path) -> bool:
    try:
        p = p.resolve()
        return APPROVED_DIR.resolve() in p.parents or p == APPROVED_DIR
    except Exception:
        return False


def list_pdfs():
    if not APPROVED_DIR.exists():
        return []
    return sorted([str(p.name) for p in APPROVED_DIR.glob('*.pdf')])


def read_pdf(file_path: Path, query: str):
    doc = fitz.open(str(file_path))
    if not query:
        text = ''
        for page in doc:
            text += page.get_text()
        return text
    q = query.lower()
    best = None
    best_score = -1
    for i in range(doc.page_count):
        page = doc.load_page(i)
        text = page.get_text().lower()
        if q in text:
            if best is None or text.find(q) < best_score:
                best = text
                best_score = text.find(q)
    if best is None:
        # fallback to first page
        best = doc.load_page(0).get_text()
    return best


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=False)
    parser.add_argument('--query', required=False)
    parser.add_argument('--list', action='store_true')
    args = parser.parse_args()

    if args.list:
        for name in list_pdfs():
            print(name)
        return

    if not args.file:
        print("[BLOCKED] File outside approved documents directory")
        sys.exit(1)

    p = Path(args.file)
    if not is_inside(p):
        print("[BLOCKED] File outside approved documents directory")
        sys.exit(1)

    print(f"[ALLOWED] Reading approved policy document: {p.name}")
    content = read_pdf(p, args.query or '')
    if content:
        snippet = content[:4000]
        print(snippet)
    print(f"[SOURCE] Official document: {p.name}")

if __name__ == '__main__':
    main()
