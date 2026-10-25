# -*- coding: utf-8 -*-
import glob
import os
import re

D = r"<workspace>\review"
for f in sorted(glob.glob(os.path.join(D, "*.md"))):
    t = open(f, encoding="utf-8").read()
    m = re.search(r"^### 三、.*?\n(.*?)(?=^### |\Z)", t, re.M | re.S)
    if not m:
        continue
    lines = [l.strip() for l in m.group(1).split("\n") if l.strip().startswith("- ")]
    print("##### " + os.path.basename(f)[:-3])
    for l in lines:
        print(l)
    print()
