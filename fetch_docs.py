#!/usr/bin/env python3
"""
Fetch exchange API documentation from web pages and save as markdown.
Usage: python3 fetch_docs.py <exchange_name> <url1> [url2] [url3] ...

Fetches each URL, converts HTML to markdown, and concatenates into a single
<exchange_name>.md file in the current directory.
"""

import sys
import time
import requests
import html2text

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def fetch_page(url: str) -> str:
    """Fetch a URL and convert to markdown."""
    resp = requests.get(url, headers=HEADERS, timeout=30)
    resp.raise_for_status()
    
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.body_width = 0  # No line wrapping
    h.unicode_snob = True
    h.skip_internal_links = False
    h.ignore_tables = False
    h.single_line_break = False
    
    md = h.handle(resp.text)
    return md


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 fetch_docs.py <exchange_name> <url1> [url2] ...")
        sys.exit(1)
    
    exchange = sys.argv[1]
    urls = sys.argv[2:]
    
    print(f"Fetching docs for: {exchange}")
    print(f"URLs: {len(urls)}")
    
    all_content = []
    for i, url in enumerate(urls):
        print(f"  [{i+1}/{len(urls)}] {url}")
        try:
            md = fetch_page(url)
            all_content.append(f"\n\n---\n\n# Source: {url}\n\n{md}")
            time.sleep(0.5)  # Rate limit
        except Exception as e:
            print(f"    ERROR: {e}")
            all_content.append(f"\n\n---\n\n# Source: {url}\n\nERROR: Failed to fetch: {e}\n")
    
    output_file = f"{exchange}.md"
    with open(output_file, "w") as f:
        f.write(f"# {exchange.replace('_', ' ').title()} API Documentation\n\n")
        f.write(f"Auto-fetched from {len(urls)} page(s)\n")
        f.write("".join(all_content))
    
    lines = sum(1 for _ in open(output_file))
    print(f"\nSaved: {output_file} ({lines} lines)")


if __name__ == "__main__":
    main()
