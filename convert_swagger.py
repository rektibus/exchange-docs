import sys, json, yaml, os

def parse_spec(filepath):
    try:
        with open(filepath, "r") as f:
            if filepath.endswith(".yaml") or filepath.endswith(".yml"):
                return yaml.safe_load(f)
            else:
                return json.load(f)
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None

def convert_to_md(data, outpath):
    with open(outpath, "w") as out:
        if "info" in data:
            title = data["info"].get("title", "API Docs")
            desc = data["info"].get("description", "")
            out.write(f"# {title}\n{desc}\n\n")
            
        if "paths" in data:
            for path, methods in data["paths"].items():
                for m, v in methods.items():
                    out.write(f"## {m.upper()} {path}\n")
                    if "summary" in v: 
                        out.write(f"{v['summary']}\n\n")
                    if "parameters" in v:
                        out.write("### Parameters\n| Name | In | Required | Type |\n|---|---|---|---|\n")
                        for p in v["parameters"]:
                            name = p.get("name", "")
                            loc = p.get("in", "")
                            req = str(p.get("required", False))
                            typ = p.get("schema", {}).get("type", p.get("type", "string"))
                            out.write(f"| {name} | {loc} | {req} | {typ} |\n")
                        out.write("\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 convert_swagger.py <input> <output>")
        sys.exit(1)
    
    data = parse_spec(sys.argv[1])
    if data:
        convert_to_md(data, sys.argv[2])
        print(f"Converted {sys.argv[1]} to {sys.argv[2]}")
