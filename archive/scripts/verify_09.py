import json
from collections import Counter

ASSIGN = r"<workspace>/assign/09_会计档案管理办法_解析.json"
PARSED = r"<workspace>/parsed/09_会计档案管理办法_解析.json"

data = json.load(open(ASSIGN, encoding="utf-8"))
parsed = json.load(open(PARSED, encoding="utf-8"))

# 期望集合（按题型+题号）
expect = Counter()
for q in parsed["questions"]:
    expect[q["etype"]] += 1

seen = []
for m in data["modules"]:
    for et, nos in m["questions"].items():
        for n in nos:
            seen.append((et, n))

cnt = Counter(seen)
dups = [k for k, v in cnt.items() if v > 1]
if dups:
    print("重复:", dups)

# 各题型总数
by_type = Counter()
for et, n in seen:
    by_type[et] += 1

print("题型总数:", dict(by_type), "合计:", sum(by_type.values()), "期望:", dict(expect))
print("分组数:", len(data["modules"]))
for m in data["modules"]:
    q = m["questions"]
    tot = sum(len(q.get(k, [])) for k in ("单选", "多选", "判断"))
    print(f'  {m["name"]}: 单选{len(q.get("单选",[]))}/多选{len(q.get("多选",[]))}/判断{len(q.get("判断",[]))} = {tot}')

ok = (by_type["单选"] == 21 and by_type["多选"] == 12 and by_type["判断"] == 20
      and sum(by_type.values()) == 53 and not dups)
print("校验:", "通过" if ok else "失败")
