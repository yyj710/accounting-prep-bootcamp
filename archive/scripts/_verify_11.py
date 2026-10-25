# -*- coding: utf-8 -*-
import json, sys

BASE = "<workspace>"
assign = json.load(open(BASE + "/assign/11_会计职业道德_解析.json", encoding="utf-8"))
parsed = json.load(open(BASE + "/parsed/11_会计职业道德_解析.json", encoding="utf-8"))

# 期望各题型题号
expected = {"单选": [], "多选": [], "判断": []}
for q in parsed["questions"]:
    expected[q["etype"]].append(q["no"])
expected = {k: sorted(v) for k, v in expected.items()}
print("原始题库:", {k: len(v) for k, v in expected.items()}, "合计", sum(len(v) for v in expected.values()))

# 收集归入结果
seen = {"单选": [], "多选": [], "判断": []}
errs = []
for m in assign["modules"]:
    for t, nos in m["questions"].items():
        for n in nos:
            seen[t].append(n)

seen = {k: sorted(v) for k, v in seen.items()}

ok = True
# 1) 每题型题号与原始完全一致（出现且仅出现一次）
for t in ["单选", "多选", "判断"]:
    if seen[t] != expected[t]:
        ok = False
        dup = [x for x in seen[t] if seen[t].count(x) > 1]
        miss = [x for x in expected[t] if x not in seen[t]]
        extra = [x for x in seen[t] if x not in expected[t]]
        errs.append(f"[{t}] 不一致 重复={sorted(set(dup))} 缺失={miss} 多余={extra}")

# 2) 各题型总数
counts = {t: len(seen[t]) for t in ["单选", "多选", "判断"]}
target = {"单选": 15, "多选": 7, "判断": 11}
for t in target:
    if counts[t] != target[t]:
        ok = False
        errs.append(f"[{t}] 总数 {counts[t]} != 期望 {target[t]}")

# 3) 分组规模检查（4-10）
for m in assign["modules"]:
    n = sum(len(v) for v in m["questions"].values())
    if not (4 <= n <= 10):
        errs.append(f"[分组规模] {m['name']} = {n} 题(超出4-10)")

print("归入统计:", counts, "合计", sum(counts.values()))
print("分组数:", len(assign["modules"]))
if ok and not errs:
    print("校验结果: 通过 ✔  每个题型+题号组合出现且仅出现一次；总数 单选15/多选7/判断11=33")
else:
    print("校验结果: 失败 ✘")
    for e in errs:
        print("  -", e)
    sys.exit(1)
