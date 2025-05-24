def format_to_markdown(parsed_data):
    """
    Formats the parsed Luau doc data into Markdown string.
    Expects a dict with 'classes', 'functions','events' and 'variables' keys.
    """
    md = []

    
    # Format classes
    if parsed_data.get("classes"):
        for cls in parsed_data.get("classes", []):
            md.append(f"## Class `{cls['name']}`\n")
            if cls["description"]:
                md.append(f"{cls['description']}\n")

            # Events in the class
            if cls.get("events"):
                md.append("#### Events\n")
                for event in cls["events"]:
                    md.append(f"- `{event}`\n")
                md.append("")

            # Functions in the class
            if cls.get("functions"):
                md.append("### Functions\n")
                for func in cls["functions"]:
                    md.append(f"### `{func['name']}({func['args']})`\n")
                    if func["description"]:
                        md.append(f"{func['description']}\n")

                    # Parameters
                    if func.get("params"):
                        md.append("**Parameters:**\n")
                        for p in func["params"]:
                            # Format: - `name` (type): description
                            param_line = f"- `{p['name']}`"
                            if p['type']:
                                param_line += f" ({p['type']})"
                            if p['description']:
                                param_line += f": {p['description']}"
                            md.append(param_line)
                        md.append("")

                    # Return values
                    if func.get("returns"):
                        md.append("**Returns:**\n")
                        for r in func["returns"]:
                            # Format: - (type) name: description
                            ret_line = "- "
                            if r['type']:
                                ret_line += f"({r['type']}) "
                            if r['name']:
                                ret_line += f"{r['name']}"
                            if r['description']:
                                ret_line += f": {r['description']}"
                            md.append(ret_line)
                        md.append("")

            md.append("---\n")

    # Format global functions (not in a class)
    if parsed_data.get("functions"):
        md.append("## Global Functions\n")
        for func in parsed_data["functions"]:
            md.append(f"### `{func['name']}({func['args']})`\n")
            if func["description"]:
                md.append(f"{func['description']}\n")

            if func.get("params"):
                md.append("**Parameters:**\n")
                for p in func["params"]:
                    param_line = f"- `{p['name']}`"
                    if p['type']:
                        param_line += f" ({p['type']})"
                    if p['description']:
                        param_line += f": {p['description']}"
                    md.append(param_line)
                md.append("")

            if func.get("returns"):
                md.append("**Returns:**\n")
                for r in func["returns"]:
                    ret_line = "- "
                    if r['type']:
                        ret_line += f"({r['type']}) "
                    if r['name']:
                        ret_line += f"{r['name']}"
                    if r['description']:
                        ret_line += f": {r['description']}"
                    md.append(ret_line)
                md.append("")

        md.append("---\n")

    # Format global events if any
    if parsed_data.get("events"):
        md.append("## Global Events\n")
        for event in parsed_data["events"]:
            md.append(f"- `{event}`\n")
        md.append("")

    if parsed_data.get("variables"):
        md.append("## Global Variables\n")
        for variable in parsed_data["variables"]:
            line = f"- `{variable['name']}`"
            if variable.get("type"):
                line += f" (*{variable['type']}*)"
            if variable.get("description"):
                line += f": {variable['description']}"
            md.append(line)
        md.append("")

    return "\n".join(md)
