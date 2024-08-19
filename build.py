import os
import shutil
import sys
import zipfile

SOURCE = "."
FILENAME = "raylib.c3l"
W32_PREFIX = ".\\"

def is_excluded(name):
    excludes = [
        FILENAME, 
        "build.py", 
        ".gitignore", 
        ".git", 
        ".DS_Store"
    ]

    for exclude in excludes:
        if name.endswith(exclude) or name.startswith(W32_PREFIX + exclude):
            print("[exclude `", exclude, "`] ", name, sep="")
            return True
    return False


relroot = os.path.abspath(os.path.join(SOURCE, os.pardir))
with zipfile.ZipFile(FILENAME, "w", zipfile.ZIP_DEFLATED) as zip:
    for root, dirs, files in os.walk(SOURCE):
        if is_excluded(root):
            continue

        for file in files:
            if is_excluded(file):
                continue
            filename = file if root == SOURCE else os.path.join(root, file)
            if os.path.isfile(filename): # regular files only
                print("[touch]", filename)
                zip.write(filename)

print("Zipped ", FILENAME, sep="`", end="`\n")

if len(sys.argv) > 1:
    dest = sys.argv[1]
    print("Moving", FILENAME, "to", dest)
    shutil.copyfile(W32_PREFIX + FILENAME, W32_PREFIX + dest + FILENAME)

