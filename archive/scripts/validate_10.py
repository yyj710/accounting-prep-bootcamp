import json
from collections import Counter

base = "<workspace>"
assign = json.load(open(f"{base}/assign/10_会计基础工作规范_解析.json", encoding="utf-8"))
data = json.load(open(f"{base}/parsed/10_会计基础工作规范_解析.json", encoding="utf-8"))

# 源数据真实题型+题号
truth = Counter((q["etype"], q["no"]) for q in data["questions"])
need = Counter({"单选": 19, "多选": 12, "判断": 17})

# 从分组收集
seen = Counter()
for m in assign["modules"]:
    for et, nos in m["questions"].items():
        for n in nos:
            seen[(et, n)] += 1

# 1) 每组合出现且仅一次
dup = [k for k, v in seen.items() if v != 1]
missing = [k for k in truth if seen[k] == 0]
extra = [k for k in seen if k not in truth]

# 2) 各题型总数
per = Counter()
for (et, n), v in seen.items():
    per[et] += v

sizes = [sum(len(v) for v in m["questions"].values()) for m in assign["modules"]]

print("分组数:", len(assign["modules"]))
for m in assign["modules"]:
    c = {k: len(v) for k, v in m["questions"].items()}
    print(f"  {m['name']}: 单选{c['单选']}/多选{c['多选']}/判断{c['判断']}  共{c['单选']+c['多选']+c['判断']}")

print("题型总数:", dict(per), "| 期望: 单选19 多选12 判断17")
print("分组题数区间:", (min(sizes), max(sizes)), "| 要求 5~15")
print("重复/计数异常:", dup or "无")
print("源数据中漏归:", missing or "无")
print("归入了源数据不存在的题:", extra or "无")
print("源数据总题数:", len(truth), "| 已归类题数:", sum(per.values()))

ok = (not dup) and (not missing) and (not extra) and \
     per["单选"] == need["单选"] and per["多选"] == need["多选"] and per["判断"] == need["判断"] and \
     sum(per.values()) == 48 and len(truth) == 48 and \
     len(assign["modules"]) >= 5 and len(assign["modules"]) <= 8 and \
     all(5 <= s <= 15 for s in sizes)
print("校验结果:", "PASS" if ok else "FAIL")
