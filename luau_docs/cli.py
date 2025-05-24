import argparse
import os

from luau_docs.parser import parse_luau_file
from luau_docs.formatter import format_to_markdown

def generate_docs(input_path, output):
    os.makedirs(output, exist_ok=True)
    
    if os.path.isfile(input_path):
        # Single file case
        if input_path.endswith(".lua") or input_path.endswith(".luau"):
            lua_data = parse_luau_file(input_path)
            markdown_data = format_to_markdown(lua_data)

            filename = os.path.splitext(os.path.basename(input_path))[0] + ".md"
            output_file = os.path.join(output, filename)
            with open(output_file, "w", encoding="utf-8") as m:
                m.write(markdown_data)

    elif os.path.isdir(input_path):
        # Directory case
        for root, _, files in os.walk(input_path):
            for file in files:
                if file.endswith(".lua") or file.endswith(".luau"):
                    file_path = os.path.join(root, file)
                    lua_data = parse_luau_file(file_path)
                    markdown_data = format_to_markdown(lua_data)

                    output_file = os.path.join(output, f"{os.path.splitext(file)[0]}.md")
                    with open(output_file, "w", encoding="utf-8") as m:
                        m.write(markdown_data)

def main():
    parser = argparse.ArgumentParser(description="Generate Luau Docs from source files")
    parser.add_argument("path", help="Path to the Luau Project to convert")
    parser.add_argument("--out", default="docs", help="Directory to output docs to")

    args = parser.parse_args()
    generate_docs(args.path, args.out)


if __name__ == "__main__":
    main()
    
                    