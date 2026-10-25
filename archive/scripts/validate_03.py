import json, re, collections

assign_path = r"<workspace>/assign/03_政府会计准则_解析.json"
preview_path = r"<workspace>/preview/03_政府会计准则_解析.txt"

data = json.load(open(assign_path, encoding="utf-8"))
mods = data["modules"]

# 收集清单里真实存在的 (题型, 题号)
expected = collections.defaultdict(set)
for line in open(preview_path, encoding="utf-8"):
    line = line.strip()
    m = re.match(r"^(单选|多选|判断)\|(\d+)\|", line)
    if m:
        expected[m.group(1)].add(int(m.group(2)))

seen = collections.Counter()
dup = []
mod_count = []
for mod in mods:
    c = 0
    for etype in ("单选", "多选", "判断"):
        for no in mod["questions"].get(etype, []):
            seen[(etype, no)] += 1
            c += 1
    mod_count.append((mod["name"], c))

# 1) 唯一性
for (etype, no), cnt in seen.items():
    if cnt != 1:
        dup.append((etype, no, cnt))
for etype in ("单选", "多选", "判断"):
    for no in expected[etype]:
        if seen[(etype, no)] == 0:
            dup.append((etype, no, "MISSING"))

# 2) 题型总数
totals = {etype: sum(1 for (e, n), c in seen.items() if e == etype and c == 1)
          for etype in ("单选", "多选", "判断")}

print("模块数:", len(mods))
for name, c in mod_count:
    print(f"  {name}: {c}")
print("题型总数:", totals, "合计:", sum(totals.values()))
print("清单期望:", {k: len(v) for k, v in expected.items()},
      "合计:", sum(len(v) for v in expected.values()))
print("重复/缺失:", dup if dup else "无")
ok = (not dup and totals["单选"] == 133 and totals["多选"] == 66
      and totals["判断"] == 59 and sum(totals.values()) == 258
      and len(mods) == len({m["name"] for m in mods}))
print("校验结果:", "PASS" if ok else "FAIL")
