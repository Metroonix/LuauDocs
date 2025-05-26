import os
import fnmatch

def check_output_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

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