#!/usr/bin/env python3

import os
import pathlib

def list_jars(bazel_bin="bazel-bin"):
    jars = []

    # Walk bazel-bin, follow symlinked directories
    for root, dirpath, files in os.walk(bazel_bin, followlinks=True):
        for f in files:
            if f.endswith(".jar"):
                if root.startswith(bazel_bin+"/external"):
                    # Skip jars pulled by bazel from external repos
                    continue
                full_path = pathlib.Path(root) / f
                # Make relative to current working directory
                jars.append(os.path.relpath(full_path, pathlib.Path.cwd()))

    jars.sort()
    return jars

if __name__ == "__main__":
    for jar in list_jars():
        print(jar)
