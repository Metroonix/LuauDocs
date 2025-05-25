import argparse, os, fnmatch
from luau_docs.parser import parse_luau_file
from luau_docs.formatter import format_to_markdown

def gather_files(input_path, excludes):
    matches = []
    if os.path.isfile(input_path):
        return [input_path]
    for root, dirs, files in os.walk(input_path):
        # remove excluded dirs
        dirs[:] = [d for d in dirs if not any(fnmatch.fnmatch(d, pat) for pat in excludes)]
        for file in files:
            if file.endswith((".lua", ".luau")) and not any(fnmatch.fnmatch(file, pat) for pat in excludes):
                matches.append(os.path.join(root, file))
    return matches

def main():
    p = argparse.ArgumentParser(
        prog="luau_docs",
        description="Generate documentation from Luau source files",
        epilog="Visit https://github.com/Metroonix/LuauDocs for examples and more info."
    )

    p.add_argument("input", nargs="?", help="File or directory to process")
    p.add_argument("-o", "--out", default="docs", help="Output directory")
    p.add_argument("-e", "--exclude", default="", help="Comma-separated exclude patterns")
    p.add_argument("-f", "--format", choices=["md"], default="md", help="Output format (HTML Coming Soon)")
    p.add_argument("--tags", action="store_true", help="List supported tags and exit")
    p.add_argument("--html", action="store_true", help="(Coming soon) Generate HTML output")
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
            text = format_to_markdown(data)
            ext = ".md"
        name = os.path.splitext(os.path.basename(path))[0] + ext
        dest = os.path.join(out, name)
        with open(dest, "w", encoding="utf-8") as f:
            f.write(text)
        if args.verbose:
            print(f"→ Written {dest}")


if __name__ == "__main__":
    main()