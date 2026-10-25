# -*- coding: utf-8 -*-
import json, collections, os

SRC = r"<workspace>/parsed/07_税法相关_解析.json"
OUT = r"<workspace>/assign/07_税法相关_解析.json"

src = json.load(open(SRC, encoding="utf-8"))
out = json.load(open(OUT, encoding="utf-8"))

# 源数据中每个题型的题号
expect = collections.defaultdict(set)
for q in src["questions"]:
    expect[q["etype"]].add(q["no"])

# 归入分组
got = collections.defaultdict(list)
for m in out["modules"]:
    for et, nos in m["questions"].items():
        for n in nos:
            got[et].append(n)

ok = True

# 1. 各题型总数
for et in ["单选", "多选", "判断"]:
    total = len(got.get(et, []))
    print(f"{et}: 归入 {total} 题, 源 {len(expect[et])} 题")

# 2. 每个 题型+题号 出现且仅出现一次
for et in ["单选", "多选", "判断"]:
    dup = [n for n, c in collections.Counter(got.get(et, [])).items() if c > 1]
    missing = expect[et] - set(got.get(et, []))
    extra = set(got.get(et, [])) - expect[et]
    if dup:
        ok = False; print(f"[重复] {et}: {dup}")
    if missing:
        ok = False; print(f"[遗漏] {et}: {sorted(missing)}")
    if extra:
        ok = False; print(f"[多余] {et}: {sorted(extra)}")

# 3. 总数校验
assert len(got["单选"]) == 35, f"单选应为35, 实为{len(got['单选'])}"
assert len(got["多选"]) == 13, f"多选应为13, 实为{len(got['多选'])}"
assert len(got["判断"]) == 7, f"判断应为7, 实为{len(got['判断'])}"
alln = len(got["单选"]) + len(got["多选"]) + len(got["判断"])
assert alln == 55, f"合计应为55, 实为{alln}"

# 4. 分组数量与规模
mods = out["modules"]
print(f"\n分组数量: {len(mods)}")
for m in mods:
    c = sum(len(v) for v in m["questions"].values())
    print(f"  {m['name']}: {c} 题")
    if not (4 <= c <= 12):
        ok = False; print(f"    [规模越界] {m['name']} = {c}")

print("\n校验通过 ✓" if ok else "\n校验失败 ✗")
