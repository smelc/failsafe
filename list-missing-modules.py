#!/usr/bin/env python3
import os
import pathlib

# File extensions we care about
SOURCE_EXTS = {".java", ".kt", ".scala"}

def find_dirs(base="."):
    base = pathlib.Path(base).resolve()
    results = []

    for root, dirs, files in os.walk(base):
        root_path = pathlib.Path(root)

        # check if "src" exists inside this directory
        if "src" in dirs:
            src_dir = root_path / "src"

            # look for Java/Kotlin/Scala files inside "src"
            has_source = any(
                f.suffix in SOURCE_EXTS
                for f in src_dir.rglob("*")
                if f.is_file()
            )

            if has_source:
                # check for BUILD file in the directory (case sensitive)
                build_file = root_path / "BUILD"
                if not build_file.exists():
                    results.append(os.path.relpath(root_path, pathlib.Path.cwd()))

    return sorted(results)

if __name__ == "__main__":
    for d in find_dirs():
        print(d)
