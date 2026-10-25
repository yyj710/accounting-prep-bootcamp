# -*- coding: utf-8 -*-
"""统一各复习卡「考点速览」里模块小标题的写法为 `#### N. 模块名`。"""
import os
import re
import glob

REVIEW = r"<workspace>\review"

STRIP_PREFIX = re.compile(r"^\s*(?:模块\s*\d+|第[一二三四五六七八九十\d]+(?:个)?模块|"
                          r"[（(]\s*\d+\s*[)）]|\d+\s*[\.、\)])\s*")


def clean_name(s):
    s = s.strip()
    # 去掉 Markdown 粗体星号与首尾空白
    s = s.strip("*").strip()
    # 去掉常见编号前缀，可能叠加（如「模块1 1. xxx」）
    for _ in range(3):
        new = STRIP_PREFIX.sub("", s)
        if new == s:
            break
        s = new
    return s.strip()


def fix(text):
    lines = text.split("\n")
    # 定位考点速览区间
    try:
        i0 = next(i for i, l in enumerate(lines) if l.strip() == "### 一、考点速览")
    except StopIteration:
        return text, 0
    i1 = len(lines)
    for i in range(i0 + 1, len(lines)):
        if lines[i].startswith("### "):
            i1 = i
            break

    names = []
    positions = []
    for i in range(i0 + 1, i1):
        l = lines[i]
        if re.match(r"^#### .+$", l):
            names.append(clean_name(l[5:]))
            positions.append(i)
        elif re.match(r"^\*\*.+\*\*\s*$", l):
            names.append(clean_name(l))
            positions.append(i)

    for n, (pos, name) in enumerate(zip(positions, names), 1):
        lines[pos] = "#### %d. %s" % (n, name)
    return "\n".join(lines), len(names)


total = 0
for p in sorted(glob.glob(os.path.join(REVIEW, "*.md"))):
    raw = open(p, encoding="utf-8").read()
    new, n = fix(raw)
    if new != raw:
        open(p, "w", encoding="utf-8").write(new)
    total += n
    print("%-30s 规范化模块标题 %d 个" % (os.path.basename(p), n))
print("\n合计 %d 个模块标题" % total)
