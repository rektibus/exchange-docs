#!/usr/bin/env python3
"""
Convert Postman collection JSON files to readable Markdown documentation.
Handles nested folder structures and extracts endpoints with parameters.
Usage: python3 convert_postman.py <collection.json> <output.md>
"""
import sys, json

def extract_items(items, depth=0):
    """Recursively extract endpoints from Postman collection items."""
    lines = []
    for item in items:
        if "item" in item:
            # Folder
            name = item.get("name", "Unnamed Folder")
            prefix = "#" * min(depth + 2, 4)
            lines.append(f"\n{prefix} {name}\n")
            if "description" in item:
                lines.append(f"{item['description']}\n")
            lines.extend(extract_items(item["item"], depth + 1))
        elif "request" in item:
            # Endpoint
            req = item["request"]
            name = item.get("name", "Unnamed")
            method = req.get("method", "GET")
            
            # Build URL
            url_obj = req.get("url", {})
            if isinstance(url_obj, str):
                url = url_obj
            else:
                raw = url_obj.get("raw", "")
                url = raw
            
            lines.append(f"\n**{method}** `{url}`\n")
            
            # Description
            desc = req.get("description", "")
            if desc:
                lines.append(f"{desc}\n")
            
            # Headers
            headers = req.get("header", [])
            if headers:
                lines.append("| Header | Value |")
                lines.append("|--------|-------|")
                for h in headers:
                    if isinstance(h, dict):
                        lines.append(f"| {h.get('key', '')} | {h.get('value', '')} |")
                lines.append("")
            
            # Query params
            if isinstance(url_obj, dict):
                query = url_obj.get("query", [])
                if query:
                    lines.append("| Parameter | Value | Description |")
                    lines.append("|-----------|-------|-------------|")
                    for q in query:
                        if isinstance(q, dict):
                            lines.append(f"| {q.get('key', '')} | {q.get('value', '')} | {q.get('description', '')} |")
                    lines.append("")
            
            # Body
            body = req.get("body", {})
            if body and body.get("raw"):
                lines.append("```json")
                lines.append(body["raw"])
                lines.append("```\n")
    
    return lines

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 convert_postman.py <collection.json> <output.md>")
        sys.exit(1)
    
    with open(sys.argv[1], "r") as f:
        data = json.load(f)
    
    info = data.get("info", {})
    title = info.get("name", "API Collection")
    desc = info.get("description", "")
    
    lines = [f"# {title}\n", f"{desc}\n"]
    
    items = data.get("item", [])
    lines.extend(extract_items(items))
    
    with open(sys.argv[2], "w") as f:
        f.write("\n".join(lines))
    
    count = len(lines)
    print(f"Converted {sys.argv[1]} -> {sys.argv[2]} ({count} lines)")

if __name__ == "__main__":
    main()
