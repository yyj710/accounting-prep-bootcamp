import json
from collections import Counter

base = "<workspace>"
assign = json.load(open(f"{base}/assign/06_管理会计_解析.json", encoding="utf-8"))
data = json.load(open(f"{base}/parsed/06_管理会计_解析.json", encoding="utf-8"))

# 源数据真实题型+题号
truth = Counter((q["etype"], q["no"]) for q in data["questions"])
need = Counter()
need["单选"] = 12
need["多选"] = 12
need["判断"] = 14

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

print("分组数:", len(assign["modules"]))
for m in assign["modules"]:
    c = {k: len(v) for k, v in m["questions"].items()}
    print(f"  {m['name']}: 单选{c['单选']}/多选{c['多选']}/判断{c['判断']}")

print("题型总数:", dict(per), "| 期望: 单选12 多选12 判断14")
print("重复/计数异常:", dup or "无")
print("源数据中漏归:", missing or "无")
print("归入了源数据不存在的题:", extra or "无")
print("源数据总题数:", len(truth), "| 已归类题数:", sum(per.values()))

ok = (not dup) and (not missing) and (not extra) and \
     per["单选"] == 12 and per["多选"] == 12 and per["判断"] == 14 and \
     sum(per.values()) == 38 and len(truth) == 38 and \
     all(4 <= sum(len(v) for v in m["questions"].values()) <= 12 for m in assign["modules"])
print("校验结果:", "PASS" if ok else "FAIL")
