import json
from collections import Counter

BASE = "<workspace>"
data = json.load(open(f"{BASE}/assign/05_会计信息化_解析.json", encoding="utf-8"))

# 从原始解析JSON读取真实的题型+题号全集
src = json.load(open(f"{BASE}/parsed/05_会计信息化_解析.json", encoding="utf-8"))
truth = Counter()
for q in src["questions"]:
    truth[(q["etype"], q["no"])] += 1

assigned = Counter()
for m in data["modules"]:
    for etype, nos in m["questions"].items():
        for no in nos:
            assigned[(etype, no)] += 1

# 1) 每个组合出现且仅出现一次
dup = [k for k, v in assigned.items() if v > 1]
missing = [k for k in truth if k not in assigned]
extra = [k for k in assigned if k not in truth]

# 2) 各题型总数
by_type = Counter()
for (etype, no) in assigned:
    by_type[etype] += 1

print("真实题数:", dict(Counter(t for t, n in truth)))
print("归类题数:", dict(by_type))
print("重复:", dup)
print("遗漏:", missing)
print("多余:", extra)
print("分组数:", len(data["modules"]))
for m in data["modules"]:
    q = m["questions"]
    print(f"  {m['name']}: 单选{len(q['单选'])}/多选{len(q['多选'])}/判断{len(q['判断'])}")

ok = (not dup) and (not missing) and (not extra) \
     and by_type["单选"] == 26 and by_type["多选"] == 17 and by_type["判断"] == 32
print("校验结果:", "PASS" if ok else "FAIL")
