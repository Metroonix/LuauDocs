<p align="center">
  <img src="assets/banner.png" alt="LuauDocs by Metroonix" width="600"/>
</p>

<p align="center">
  <a href="https://pypi.org/project/luau-docs/"><img src="https://img.shields.io/pypi/v/luau-docs?color=blue" alt="PyPI version"></a>
  <img src="https://img.shields.io/github/license/Metroonix/Luau-Docs" alt="License">
</p>

# LuauDocs 

A CLI & library to generate beautifully structured Markdown documentation from annotated Luau (`.lua`/`.luau`) source files.

Great for:
- Internal dev tools
- Open source Luau modules
- Keeping documentation in sync with code

---

## 🔧 Features


✅ Parse Luau annotations and emit Markdown  
📁 Works with files or entire folders  
🧱 Supports classes, parameters, events, types, returns  
🛠 Extensible design for adding new tags  
📄 Output as Markdown (HTML coming soon)


- **Class** parsing via `--- @class MyClass`
- **Function** docs: `@param`, `@return`
- **Event** docs: `@event`
- **Variable** docs: `@type`
- **Global** & **class-scoped** sections
- Output formats: **Markdown** (future: HTML/JSON)
- Extensible: you can add your own tags

---

## 🚀 Installation

```bash
# Once published to PyPI (soon):
pip install luau_docs   
# Or for local development/editable install:
git clone https://github.com/Metroonix/LuauDocs.git
cd LuauDocs
pip install -e .
```

## License

LuauDocs uses a [MIT License](/LICENSE)

## Contributions

Interested in contributing to LuauDocs, find out how [here](/CONTRIBUTING.md)

## Roadmap

Want to see where we are going with RoBall? View the [Roadmap](/ROADMAP.md)