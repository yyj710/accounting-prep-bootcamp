# -*- coding: utf-8 -*-
import json, sys

ASSIGN = r"<workspace>/assign/04_内部控制规范_解析.json"
PARSED = r"<workspace>/parsed/04_内部控制规范_解析.json"

assign = json.load(open(ASSIGN, encoding="utf-8"))
parsed = json.load(open(PARSED, encoding="utf-8"))

# 真实题库：按 etype 分组
truth = {"单选": [], "多选": [], "判断": []}
for q in parsed["questions"]:
    truth[q["etype"]].append(q["no"])

errors = []
seen = set()
for m in assign["modules"]:
    for et, nos in m["questions"].items():
        for no in nos:
            key = (et, no)
            if key in seen:
                errors.append(f"重复归属: {key}")
            seen.add(key)

# 每题型总数校验
for et, expect in [("单选", 82), ("多选", 48), ("判断", 52)]:
    got = sorted(no for (e, no) in seen if e == et)
    tset = sorted(truth[et])
    if len(got) != expect:
        errors.append(f"{et} 数量不符: 得到 {len(got)} 应为 {expect}")
    missing = set(tset) - set(got)
    extra = set(got) - set(tset)
    if missing:
        errors.append(f"{et} 缺失题号: {sorted(missing)}")
    if extra:
        errors.append(f"{et} 多余题号: {sorted(extra)}")

# 分组规模检查
print("分组数量:", len(assign["modules"]))
for m in assign["modules"]:
    a = len(m["questions"].get("单选", []))
    b = len(m["questions"].get("多选", []))
    c = len(m["questions"].get("判断", []))
    print(f"  {m['name']}: 单选{a}/多选{b}/判断{c} = 合计{a+b+c}")

print("总题数:", len(seen), "应=182")
if errors:
    print("校验失败:")
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("校验通过：每题仅归属一次，单选82 / 多选48 / 判断52，合计182")
