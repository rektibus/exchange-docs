import json
import sys

def convert_swagger(in_file, out_file, title_prefix):
    with open(in_file) as f:
        data = json.load(f)
    with open(out_file, 'w') as out:
        out.write(f'# {title_prefix} API Documentation\n\n')
        out.write(f'Source: Official OpenAPI Spec ({in_file})\n\n')
        if 'info' in data:
            info = data['info']
            out.write(f'## {info.get("title", "API")}\n\n')
            if 'description' in info: out.write(f'{info["description"]}\n\n')
            out.write(f'Version: {info.get("version", "?")}\n\n')
        if 'servers' in data:
            out.write('## Servers\n\n')
            for s in data['servers']:
                out.write(f'- {s.get("url","")} — {s.get("description","")}\n')
            out.write('\n')
        if 'paths' in data:
            out.write('## Endpoints\n\n')
            for path, methods in sorted(data['paths'].items()):
                for method, spec in methods.items():
                    if method in ('get','post','put','delete','patch'):
                        summary = spec.get('summary', '')
                        desc = spec.get('description', '')
                        out.write(f'### {method.upper()} `{path}`\n\n')
                        if summary: out.write(f'**{summary}**\n\n')
                        if desc: out.write(f'{desc}\n\n')
                        if 'parameters' in spec:
                            out.write('**Parameters:**\n\n')
                            out.write('| Name | In | Type | Required | Description |\n')
                            out.write('|------|-----|------|----------|-------------|\n')
                            for p in spec['parameters']:
                                if not isinstance(p, dict): continue
                                name = p.get('name','')
                                loc = p.get('in','')
                                req = p.get('required', False)
                                pdesc = str(p.get('description','')).replace('\n',' ')[:100]
                                ptype = p.get('type','')
                                if 'schema' in p and isinstance(p['schema'], dict):
                                    ptype = p['schema'].get('type', ptype)
                                out.write(f'| {name} | {loc} | {ptype} | {req} | {pdesc} |\n')
                            out.write('\n')
                        if 'responses' in spec:
                            out.write('**Responses:**\n\n')
                            for code, resp in spec['responses'].items():
                                rdesc = resp.get('description','')[:200] if isinstance(resp, dict) else ''
                                out.write(f'- `{code}`: {rdesc}\n')
                            out.write('\n')
        if 'components' in data and 'schemas' in data['components']:
            out.write('## Schemas\n\n')
            for name, schema in sorted(data['components']['schemas'].items()):
                out.write(f'### {name}\n\n')
                if 'description' in schema:
                    out.write(f'{schema["description"]}\n\n')
                if 'properties' in schema:
                    out.write('| Property | Type | Description |\n')
                    out.write('|----------|------|-------------|\n')
                    for pname, pspec in schema['properties'].items():
                        ptype = pspec.get('type', pspec.get('$ref', ''))
                        pdesc = str(pspec.get('description', '')).replace('\n', ' ')
                        out.write(f'| {pname} | {ptype} | {pdesc} |\n')
                    out.write('\n')
        if 'components' in data and 'securitySchemes' in data['components']:
            out.write('## Authentication\n\n')
            for name, scheme in data['components']['securitySchemes'].items():
                out.write(f'### {name}\n\n')
                out.write(f'Type: {scheme.get("type","")}\n')
                out.write(f'In: {scheme.get("in","")}\n')
                out.write(f'Name: {scheme.get("name","")}\n\n')
        if 'definitions' in data: # Swagger 2.0 fallback
            out.write('## Schemas\n\n')
            for name, schema in sorted(data['definitions'].items()):
                out.write(f'### {name}\n\n')
                if 'description' in schema:
                    out.write(f'{schema["description"]}\n\n')
                if 'properties' in schema:
                    out.write('| Property | Type | Description |\n')
                    out.write('|----------|------|-------------|\n')
                    for pname, pspec in schema['properties'].items():
                        ptype = pspec.get('type', pspec.get('$ref', ''))
                        pdesc = str(pspec.get('description', '')).replace('\n', ' ')
                        out.write(f'| {pname} | {ptype} | {pdesc} |\n')
                    out.write('\n')

if __name__ == '__main__':
    convert_swagger(sys.argv[1], sys.argv[2], sys.argv[3])
