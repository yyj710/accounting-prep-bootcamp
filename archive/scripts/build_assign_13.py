# -*- coding: utf-8 -*-
import json, os, collections

BASE = r"<workspace>"
SRC = os.path.join(BASE, "parsed/13_综合法规_解析.json")
OUT = os.path.join(BASE, "assign/13_综合法规_解析.json")

modules = [
    ("会计法与会计监督", "会计法、会计监督及内部控制",
        {"单选": [15, 91, 116], "多选": [31, 32, 34, 35, 36], "判断": [92, 93, 94, 99]}),
    ("会计基础理论与会计信息质量", "会计要素、权责发生制与信息质量特征",
        {"单选": [5, 95, 96], "多选": [22, 23], "判断": [47, 89, 97, 125]}),
    ("会计科目账务处理与代理记账", "会计科目核算、成本核算与代理记账",
        {"单选": [], "多选": [25, 37], "判断": [34, 41, 43, 44, 45, 46, 49, 51, 57, 58, 59, 126, 127]}),
    ("会计人员继续教育", "继续教育内容、学分与组织管理",
        {"单选": [100, 101, 103, 104, 105, 106, 107, 108, 109, 121], "多选": [33, 38],
         "判断": [60, 111, 112, 113, 114, 115, 128]}),
    ("企业会计准则——收入", "收入确认计量、合同变更与售后回购",
        {"单选": [], "多选": [1, 3], "判断": [24, 48, 52, 76, 87, 90]}),
    ("企业会计准则——租赁", "租赁识别、租赁期与出租人处理",
        {"单选": [14, 16], "多选": [4, 5, 29, 30], "判断": [30, 53, 77, 78]}),
    ("企业会计准则——合并报表、金融工具与外币折算", "合并范围、套期会计与外币折算",
        {"单选": [1, 3, 6, 7, 17, 117], "多选": [2, 24], "判断": [29]}),
    ("企业会计准则——会计政策变更、差错更正与报表列报", "政策变更、差错更正与报表列报",
        {"单选": [2, 4, 8, 11, 12, 13, 18, 19, 118], "多选": [26, 27, 28], "判断": [25, 75, 86]}),
    ("公司法与国有资产管理", "公司法及国有资产管理法律制度",
        {"单选": [119], "多选": [], "判断": [36, 62, 63, 70, 79, 80, 82]}),
    ("政府采购法律制度", "政府采购方式、程序与质疑投诉",
        {"单选": [], "多选": [17, 19, 21], "判断": [32, 55, 67, 71, 72, 81, 83, 85]}),
    ("行政事业单位财务与资产管理、绩效评价", "行政事业单位财务、资产与绩效评价",
        {"单选": [21, 22, 23, 98], "多选": [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 20],
         "判断": [33, 38, 39]}),
    ("财务管理与预算管理、税收法规", "财务管理、预算管理与税收法规",
        {"单选": [9, 10, 20, 122, 123, 124], "多选": [16], "判断": [26, 27, 28, 31, 35, 37, 61, 84]}),
]

src = json.load(open(SRC, encoding="utf-8"))
all_q = {(q["etype"], q["no"]) for q in src["questions"]}

seen = collections.Counter()
type_total = collections.Counter()
for name, desc, qs in modules:
    for et, nos in qs.items():
        for n in nos:
            seen[(et, n)] += 1
            type_total[et] += 1

# 校验1：每题型+题号出现且仅一次
dup = [k for k, v in seen.items() if v != 1]
miss = all_q - set(seen)
extra = set(seen) - all_q
assert not dup, ("重复", dup)
assert not miss, ("缺失", sorted(miss))
assert not extra, ("多余", sorted(extra))

# 校验2：各题型总数
assert type_total["单选"] == 44, type_total
assert type_total["多选"] == 38, type_total
assert type_total["判断"] == 68, type_total
assert sum(type_total.values()) == 150, type_total

os.makedirs(os.path.dirname(OUT), exist_ok=True)
out = {"file": "13_综合法规_解析.md",
       "modules": [{"name": n, "desc": d, "questions": q} for n, d, q in modules]}
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

print("校验通过：共 %d 个分组，150 题各归入且仅归入一个分组" % len(modules))
print("题型总数：单选=%d 多选=%d 判断=%d 合计=%d" %
      (type_total["单选"], type_total["多选"], type_total["判断"], sum(type_total.values())))
for n, d, q in modules:
    print("  %s (%d单选/%d多选/%d判断)" % (n, len(q["单选"]), len(q["多选"]), len(q["判断"])))
