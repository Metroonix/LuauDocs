import re

# Regex to capture tagged lines
TAG_REGEX = re.compile(r"---\s*@(\w+)\s*(.*)?")
# Regex to capture description lines 
DESC_REGEX = re.compile(r"--\s?(.*)")
# Regex to capture function signatures 
FUNC_REGEX = re.compile(r"function\s+([\w\.]+)\((.*?)\)")
# Regex to capture variables
VAR_REGEX = re.compile(r"^(local\s+)?(\w+)\s*=\s*.*$")

def parse_luau_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    docs = {
        "classes": [],
        "functions": [],
        "events": [],
        "variables": [],  # Add variables list here
    }

    current_class = None
    current_func = None
    current_variable = None  # Track current variable
    current_desc = []
    current_tags = {}

    def store_function():
        nonlocal current_func, current_desc, current_tags
        if current_func:
            func_info = {
                "name": current_func["name"],
                "args": current_func["args"],
                "description": " ".join(current_desc).strip(),
                "params": [],
                "returns": [],
            }
            for tag, values in current_tags.items():
                if tag == "param":
                    for v in values:
                        parts = v.split(None, 2)
                        func_info["params"].append({
                            "name": parts[0] if len(parts) > 0 else "",
                            "type": parts[1] if len(parts) > 1 else "",
                            "description": parts[2] if len(parts) > 2 else "",
                        })
                elif tag == "return":
                    for v in values:
                        parts = v.split(None, 2)
                        func_info["returns"].append({
                            "type": parts[0] if len(parts) > 0 else "",
                            "name": parts[1] if len(parts) > 1 else "",
                            "description": parts[2] if len(parts) > 2 else "",
                        })
            if current_class is not None:
                current_class.setdefault("functions", []).append(func_info)
            else:
                docs["functions"].append(func_info)
        current_func = None
        current_desc = []
        current_tags = {}

    def store_class():
        nonlocal current_class, current_desc, current_tags
        if current_class:
            current_class["description"] = " ".join(current_desc).strip()
            docs["classes"].append(current_class)
        current_class = None
        current_desc = []
        current_tags = {}

    def store_variable():
        nonlocal current_variable, current_desc, current_tags
        if current_variable:
            current_variable["description"] = " ".join(current_desc).strip()
            # Try to get type from tags if exists
            current_variable["type"] = current_tags.get("type", [""])[0]
            if current_class is not None:
                current_class.setdefault("variables", []).append(current_variable)
            else:
                docs["variables"].append(current_variable)
        current_variable = None
        current_desc = []
        current_tags = {}

    for i, line in enumerate(lines):
        tag_match = TAG_REGEX.match(line)
        desc_match = DESC_REGEX.match(line)
        func_match = FUNC_REGEX.search(line)
        var_match = VAR_REGEX.match(line)

        if tag_match:
            tag, value = tag_match.groups()
            if tag == "class":
                store_function()
                store_variable()
                store_class()
                current_class = {"name": value.strip(), "description": "", "functions": [], "events": [], "variables": []}
                current_desc = []
                current_tags = {}
            elif tag == "event":
                event_name = value.strip()
                if current_class is not None:
                    current_class.setdefault("events", []).append(event_name)
                else:
                    docs["events"].append(event_name)
            else:
                current_tags.setdefault(tag, []).append(value.strip())

        elif func_match:
            store_function()
            store_variable()
            func_name, func_args = func_match.groups()
            current_func = {"name": func_name, "args": func_args}
            current_desc = []
            current_tags = {}

        elif var_match:
            store_function()
            store_variable()
            var_name = var_match.group(2)
            current_variable = {"name": var_name, "type": "", "description": ""}
            current_desc = []
            current_tags = {}

        elif desc_match:
            content = desc_match.group(1).strip()
            if content:
                current_desc.append(content)

        else:
            # ignore other lines
            pass

    store_function()
    store_variable()
    store_class()

    return docs
