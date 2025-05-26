import argparse
import os
import json
from luau_docs.parser import parse_luau_file
from luau_docs.formatter import format_to_markdown
from luau_docs.utils import gather_files

default_markdown_path = "generated_markdown_docs"
default_json_path = "generated_json_docs"


def main():
    p = argparse.ArgumentParser(
        prog="luau_docs",
        description="Generate documentation from Luau source files",
        epilog="Visit https://github.com/Metroonix/LuauDocs for examples and more info."
    )

    p.add_argument("input", nargs="?", help="File or directory to process")
    p.add_argument("-o", "--out", default=default_markdown_path, help="Output directory")
    p.add_argument("-e", "--exclude", default="", help="Comma-separated exclude patterns")
    p.add_argument("-f", "--format", choices=["md"], default="md", help="Output format (HTML Coming Soon)")
    p.add_argument("--tags", action="store_true", help="List supported tags and exit")
    p.add_argument("--html", action="store_true", help="(Coming soon) Generate HTML output")
    p.add_argument("--json",action="store_true", help="Generate JSON file(s) for the Luau file(s)")
    p.add_argument("-v", "--verbose", action="store_true", help="Verbose logging")

    args = p.parse_args()

    if args.tags:
        print("Supported tags:")
        print("  @class    – Define a class or module")
        print("  @param    – Describe a function parameter")
        print("  @return   – Describe a return value")
        print("  @event    – Describe a custom event")
        print("  @type     – Type annotation for a variable or class property")
        return

    if args.html:
        print("HTML output is coming soon. Follow the project for updates.")
        return

    if not args.input:
        p.print_help()
        return

    out = args.out
    os.makedirs(out, exist_ok=True)
    excludes = [pat.strip() for pat in args.exclude.split(",") if pat.strip()]
    files = gather_files(args.input, excludes)

    if args.verbose:
        print(f"Found {len(files)} file(s) to process.")

    for path in files:
        data = parse_luau_file(path)
        if args.format == "md":
            md_text = format_to_markdown(data)
            md_name = os.path.splitext(os.path.basename(path))[0] + ".md"
            dest = os.path.join(out, md_name)
            with open(dest, "w", encoding="utf-8") as f:
                f.write(md_text)
            if args.verbose:
                print(f"→ Written {dest}")


        """ If the User decides to generate a JSON file as well, it will by default be created in the same folder as all markdown files as specified by the user otherwise,
            a new folder called 'generated_json_docs' will be created as well.' """
        if args.json:
            if out == default_markdown_path:
                os.makedirs(default_json_path,exist_ok=True)
            json_name = os.path.splitext(os.path.basename(path))[0] + ".json"
            dest = os.path.join(default_json_path if out == default_markdown_path else out, json_name)
            with open(dest, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
            if args.verbose:
                print(f"→ Written {dest}")


if __name__ == "__main__":
    main()