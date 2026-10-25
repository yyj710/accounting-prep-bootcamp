# -*- coding: utf-8 -*-
"""为企业会计准则文件生成模块级归类，并做完整性校验。"""
import json, os, collections

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "parsed", "02_企业会计准则_解析.json")
OUT = os.path.join(BASE, "assign", "02_企业会计准则_解析.json")

# 模块定义（按知识体系逻辑顺序）
MODULES = [
    {
        "name": "会计基本准则与会计信息质量",
        "desc": "基本准则、会计信息质量要求与会计要素",
        "单选": [19, 32, 35, 50, 60, 79, 83, 202, 203, 204, 205, 206, 208,
                 209, 210, 211, 212, 213, 214, 215, 216, 217, 218],
        "多选": [9, 24, 27, 29, 30, 31, 32, 33, 34, 35, 36],
        "判断": [136, 139, 159, 165, 176, 197],
    },
    {
        "name": "存货、固定资产与无形资产",
        "desc": "三类资产的确认、计量与后续核算",
        "单选": [4, 15, 16, 18, 27, 37, 38, 39, 47, 56, 57, 68, 69, 76, 77,
                 86, 94, 95, 96, 222],
        "多选": [5, 14, 19, 28, 40, 41, 42, 43, 44, 47],
        "判断": [104, 114, 122, 126, 130, 138, 161, 180, 184, 186, 190],
    },
    {
        "name": "投资性房地产",
        "desc": "投资性房地产范围、模式转换与后续计量",
        "单选": [12, 21, 36, 53, 54, 80, 81, 92],
        "多选": [13],
        "判断": [103, 144, 146],
    },
    {
        "name": "金融工具",
        "desc": "金融资产分类、转移与套期会计",
        "单选": [7, 48, 49, 70, 87, 88],
        "多选": [4, 8, 10, 12, 48],
        "判断": [110, 119, 133, 188, 191],
    },
    {
        "name": "长期股权投资与企业合并",
        "desc": "长投核算、企业合并与合并报表",
        "单选": [10, 13, 28, 31, 51, 73, 74, 75, 91],
        "多选": [3, 37, 38, 39],
        "判断": [101, 121, 128, 137, 140, 150, 154, 172, 175, 181, 187],
    },
    {
        "name": "收入",
        "desc": "收入确认五步法与合同成本",
        "单选": [3, 24, 25, 43, 44, 64, 65, 66, 84, 98],
        "多选": [11, 22, 45, 46, 57],
        "判断": [99, 105, 107, 108, 117, 124, 129, 132, 157, 198, 199],
    },
    {
        "name": "租赁",
        "desc": "使用权资产与租赁负债的确认计量",
        "单选": [5, 6, 29, 30, 220, 223],
        "多选": [23],
        "判断": [100, 127],
    },
    {
        "name": "职工薪酬与股份支付",
        "desc": "职工薪酬构成与股份支付确认计量",
        "单选": [2, 22, 41, 42, 59, 61],
        "多选": [2, 6, 51, 56],
        "判断": [116, 131, 156, 189],
    },
    {
        "name": "借款费用、政府补助与所得税",
        "desc": "费用资本化、补助与递延所得税",
        "单选": [26, 45, 46, 67, 85],
        "多选": [17, 18, 52],
        "判断": [113, 115, 118, 125, 147, 151, 171, 182],
    },
    {
        "name": "或有事项、债务重组与非货币性资产交换",
        "desc": "或有利得负债、债务重组与资产置换",
        "单选": [17, 23, 62, 63, 82, 219],
        "多选": [7, 16, 20, 21, 26],
        "判断": [123, 170, 192],
    },
    {
        "name": "资产减值与持有待售",
        "desc": "减值测试、转回规则与持有待售",
        "单选": [14, 40, 55, 58, 78, 93, 97],
        "多选": [15, 49, 50],
        "判断": [134, 135, 166, 167, 169],
    },
    {
        "name": "财务报告与特殊列报事项",
        "desc": "每股收益、日后事项、现金流量与披露",
        "单选": [1, 8, 9, 11, 20, 33, 34, 52, 71, 72, 89, 90],
        "多选": [1, 25],
        "判断": [102, 106, 109, 111, 112, 120, 145, 148, 158, 193, 194],
    },
]

def main():
    out_modules = []
    actual = collections.Counter()  # (etype,no)
    for m in MODULES:
        qs = {}
        for t in ("单选", "多选", "判断"):
            nums = sorted(m[t])
            qs[t] = nums
            for n in nums:
                actual[(t, n)] += 1
        out_modules.append({"name": m["name"], "desc": m["desc"], "questions": qs})

    result = {"file": "02_企业会计准则_解析.md", "modules": out_modules}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=1)

    # ---- 校验 ----
    src = json.load(open(SRC, encoding="utf-8"))
    expected = collections.Counter((q["etype"], q["no"]) for q in src["questions"])

    errors = []
    # 1. 重复
    dups = [k for k, v in actual.items() if v > 1]
    if dups:
        errors.append(f"重复题目: {dups}")
    # 2. 覆盖一致性
    missing = set(expected) - set(actual)
    extra = set(actual) - set(expected)
    if missing:
        errors.append(f"漏掉题目: {sorted(missing)}")
    if extra:
        errors.append(f"多出题目: {sorted(extra)}")
    # 3. 各题型总数
    for t in ("单选", "多选", "判断"):
        cnt = sum(1 for (et, _) in actual if et == t)
        if cnt != expected_total(t, expected):
            errors.append(f"{t}总数={cnt}，应为{expected_total(t, expected)}")

    print("模块数:", len(MODULES))
    for m in out_modules:
        q = m["questions"]
        print(f"  {m['name']}（单选{len(q['单选'])}/多选{len(q['多选'])}/判断{len(q['判断'])}）"
              f" 合计{len(q['单选'])+len(q['多选'])+len(q['判断'])}")
    print("各题型校验:", {t: sum(1 for (et, _) in actual if et == t) for t in ("单选", "多选", "判断")})
    print("题目总数:", sum(actual.values()))
    if errors:
        print("校验失败:")
        for e in errors:
            print("  -", e)
        raise SystemExit(1)
    print("校验通过：每题归入且仅归入一个分组，各题型总数正确。")

def expected_total(t, expected):
    return sum(v for (et, _), v in expected.items() if et == t)

if __name__ == "__main__":
    main()
