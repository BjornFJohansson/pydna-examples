#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

links = [f"[{p.stem}]({p.relative_to(Path.cwd())})" for p in Path.cwd().rglob("*.ipynb") if ".ipynb_checkpoints" not in p.parts] 

for link in sorted(links):
    print(link)
    print()

if __name__ == "__main__":
    pass
    input("press enter to close")
