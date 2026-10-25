import json, collections, sys

path = r"<workspace>/assign/12_数据资产管理_解析.json"
d = json.load(open(path, encoding="utf-8"))

mods = d["modules"]
seen = collections.Counter()
per_type = collections.Counter()
ok = True

for m in mods:
    for t in ("单选", "多选", "判断"):
        for no in m["questions"].get(t, []):
            key = (t, no)
            seen[key] += 1
            per_type[t] += 1

# 重复检查
dups = [k for k, c in seen.items() if c > 1]
if dups:
    ok = False
    print("重复题:", dups)

# 总数校验
expect = {"单选": 11, "多选": 10, "判断": 6}
for t, e in expect.items():
    got = per_type[t]
    flag = "OK" if got == e else "FAIL"
    if got != e:
        ok = False
    print(f"{t}: {got}/{e} {flag}")

total = sum(per_type.values())
print(f"合计: {total}/27 {'OK' if total == 27 else 'FAIL'}")
if total != 27:
    ok = False

# 分组规模
print("--- 分组规模 ---")
for m in mods:
    n = sum(len(m["questions"].get(t, [])) for t in ("单选", "多选", "判断"))
    print(f"{m['name']}: {n} 题")

print("=== 校验结果:", "全部通过" if ok else "存在问题", "===")
sys.exit(0 if ok else 1)
