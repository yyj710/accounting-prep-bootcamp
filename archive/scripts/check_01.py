# -*- coding: utf-8 -*-
import json
from collections import Counter

SRC = "parsed/01_会计法_解析.json"
ASSIGN = "assign/01_会计法_解析.json"

src = json.load(open(SRC, encoding="utf-8"))
asg = json.load(open(ASSIGN, encoding="utf-8"))

# 源数据真实分布
src_types = Counter(q["etype"] for q in src["questions"])
expected = {"单选": 58, "多选": 50, "判断": 66}
print("源文件各题型数量:", dict(src_types))
assert dict(src_types) == expected, "源数据题型数量与预期不符！"

# 收集分配
seen = Counter()
mod_types = []
errs = []
for m in asg["modules"]:
    if not m["questions"]:
        errs.append(f"空分组: {m['name']}")
        continue
    mt = Counter()
    for t, nos in m["questions"].items():
        for n in nos:
            seen[(t, n)] += 1
            mt[t] += 1
    mod_types.append((m["name"], mt))

# 1) 每个 题型+题号 出现且仅出现一次
dups = [k for k, v in seen.items() if v != 1]
print("重复/缺失(重复计数>1):", dups)

# 2) 与源题号集合对比
src_set = {(q["etype"], q["no"]) for q in src["questions"]}
asg_set = set(seen.keys())
missing = src_set - asg_set
extra = asg_set - src_set
print("遗漏题:", sorted(missing))
print("多余题:", sorted(extra))

# 3) 各题型总数
got = Counter()
for (t, n), c in seen.items():
    got[t] += c
print("分配后各题型数量:", dict(got))

# 分组统计
print("\n分组明细:")
for name, mt in mod_types:
    print(f"  {name}: 单选{mt.get('单选',0)}/多选{mt.get('多选',0)}/判断{mt.get('判断',0)} 合计{sum(mt.values())}")

total = sum(seen.values())
other = sum(sum(mt.values()) for name, mt in mod_types if name == "其他")
print(f"\n分组数: {len(mod_types)}")
print(f"总题数: {total}")
print(f"其他占比: {other}/{total} = {other/total:.2%}")

ok = (not dups) and (not missing) and (not extra) and got == Counter(expected) and total == 174
print("\n校验结果:", "通过 ✅" if ok else "失败 ❌")
assert ok
