def format_to_markdown(parsed_data):
    md = []

    # Format classes
    for cls in parsed_data.get("classes", []):
        md.append(f"## Class `{cls['name']}`\n")
        if cls["description"]:
            md.append(f"{cls['description']}\n")

        if cls.get("events"):
            md.append("#### Events")
            for event in cls["events"]:
                md.append(f"- `{event}`")
            md.append("")

        if cls.get("variables"):
            md.append("#### Variables")
            for variable in cls["variables"]:
                line = f"- `{variable['name']}`"
                if variable.get("type"):
                    line += f" (*{variable['type']}*)"
                if variable.get("description"):
                    line += f": {variable['description']}"
                md.append(line)
            md.append("")

        if cls.get("functions"):
            md.append("#### Functions")
            for func in cls["functions"]:
                md.append(f"##### `{func['name']}({func['args']})`")
                if func["description"]:
                    md.append(func["description"])

                if func.get("params"):
                    md.append("**Parameters:**")
                    for p in func["params"]:
                        param_line = f"- `{p['name']}`"
                        if p["type"]:
                            param_line += f" ({p['type']})"
                        if p["description"]:
                            param_line += f": {p['description']}"
                        md.append(param_line)

                if func.get("returns"):
                    md.append("**Returns:**")
                    for r in func["returns"]:
                        ret_line = "- "
                        if r["type"]:
                            ret_line += f"({r['type']}) "
                        if r["name"]:
                            ret_line += f"{r['name']}"
                        if r["description"]:
                            ret_line += f": {r['description']}"
                        md.append(ret_line)
                md.append("")

        md.append("---\n")

    # Global functions
    if parsed_data.get("functions"):
        md.append("## Global Functions")
        for func in parsed_data["functions"]:
            md.append(f"### `{func['name']}({func['args']})`")
            if func["description"]:
                md.append(func["description"])

            if func.get("params"):
                md.append("**Parameters:**")
                for p in func["params"]:
                    param_line = f"- `{p['name']}`"
                    if p["type"]:
                        param_line += f" ({p['type']})"
                    if p["description"]:
                        param_line += f": {p['description']}"
                    md.append(param_line)

            if func.get("returns"):
                md.append("**Returns:**")
                for r in func["returns"]:
                    ret_line = "- "
                    if r["type"]:
                        ret_line += f"({r['type']}) "
                    if r["name"]:
                        ret_line += f"{r['name']}"
                    if r["description"]:
                        ret_line += f": {r['description']}"
                    md.append(ret_line)
            md.append("")

        md.append("---\n")

    # Global events
    if parsed_data.get("events"):
        md.append("## Global Events")
        for event in parsed_data["events"]:
            md.append(f"- `{event}`")
        md.append("")

    # Global variables
    if parsed_data.get("variables"):
        md.append("## Global Variables")
        for variable in parsed_data["variables"]:
            line = f"- `{variable['name']}`"
            if variable.get("type"):
                line += f" (*{variable['type']}*)"
            if variable.get("description"):
                line += f": {variable['description']}"
            md.append(line)
        md.append("")

    return "\n".join(md)

def format_to_json(parsed_data):
    """WIP"""
    return

def format_to_html(parsed_data):
    """WIP"""
    return