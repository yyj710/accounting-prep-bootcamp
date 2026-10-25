# -*- coding: utf-8 -*-
import json, collections

ASSIGN = r"<workspace>/assign/08_预算法_解析.json"
PARSED = r"<workspace>/parsed/08_预算法_解析.json"

data = json.load(open(ASSIGN, encoding="utf-8"))
parsed = json.load(open(PARSED, encoding="utf-8"))

# 源文件真实题目: (etype, no)
real = collections.Counter()
for q in parsed["questions"]:
    real[(q["etype"], q["no"])] += 1

assign = collections.Counter()
type_count = collections.Counter()
for m in data["modules"]:
    for etype, nos in m["questions"].items():
        for no in nos:
            assign[(etype, no)] += 1
            type_count[etype] += 1

errors = []

# 1) 每题出现且仅一次
all_keys = set(real) | set(assign)
for k in sorted(all_keys):
    r, a = real.get(k, 0), assign.get(k, 0)
    if r != 1:
        errors.append(f"源数据异常 {k}: 出现{r}次")
    if a != 1:
        errors.append(f"归类异常 {k}: 出现{a}次(应为1)")

# 2) 各题型总数
expect = {"单选": 2, "多选": 10, "判断": 28}
for et, exp in expect.items():
    if type_count[et] != exp:
        errors.append(f"题型 {et} 总数={type_count[et]}，应为{exp}")

total = sum(type_count.values())
if total != 40:
    errors.append(f"总题数={total}，应为40")

print("分组数:", len(data["modules"]))
for m in data["modules"]:
    c = collections.Counter()
    for et, nos in m["questions"].items():
        c[et] = len(nos)
    print(f"  {m['name']}(单选{c['单选']}/多选{c['多选']}/判断{c['判断']})")

print("题型统计:", dict(type_count), "总计:", total)
if errors:
    print("校验失败:")
    for e in errors:
        print("  -", e)
else:
    print("校验通过: 每题唯一归属, 单选2/多选10/判断28, 合计40")
