# -*- coding: utf-8 -*-
"""按「知识点模块 → 题型」重建 md 文件。"""
import json
import os
import re

SRC = r"<source>"
BASE = r"<workspace>"
OUT = os.path.join(SRC, "按知识点版")
os.makedirs(OUT, exist_ok=True)

TYPE_ORDER = ["单选", "多选", "判断"]
TYPE_NAME = {"单选": "单选题", "多选": "多选题", "判断": "判断题"}
STRIP_PREFIX = ["基础概念·", "判断题·", "判断·", "概念·", "应用·", "计算·",
                "易混·", "易错·", "案例·", "条文·"]
GENERIC = {"概念", "应用", "计算", "判断", "判断题", "基础概念", "易混", "易错"}


def clean_label(label: str) -> str:
    lab = (label or "").strip()
    for p in STRIP_PREFIX:
        if lab.startswith(p):
            lab = lab[len(p):]
            break
    lab = lab.strip("· ").strip()
    if lab in GENERIC:
        return ""
    return lab


def build(key):
    data = json.load(open(os.path.join(BASE, "parsed", key + ".json"), encoding="utf-8"))
    raw = open(os.path.join(BASE, "assign", key + ".json"), encoding="utf-8").read()
    raw = re.sub(r"^```(?:json)?|```$", "", raw.strip(), flags=re.M).strip()
    assign = json.loads(raw)
    qs = {}
    for q in data["questions"]:
        qs[(q["etype"], q["no"])] = q

    lines = []
    total_by_type = {}
    for q in data["questions"]:
        total_by_type[q["etype"]] = total_by_type.get(q["etype"], 0) + 1
    total = sum(total_by_type.values())
    parts = " / ".join("%s %d" % (TYPE_NAME[t], total_by_type.get(t, 0)) for t in TYPE_ORDER if total_by_type.get(t))
    title = re.sub(r"^#\s*", "", data["head"].split("\n")[0]).strip()

    lines.append("# %s（按知识点归类）" % title.replace(" · 逐题解析", "").replace(" · 题目解析（全）", ""))
    lines.append("")
    lines.append("> 共 %d 题（%s）。本版已按 **知识点模块 → 题型** 重新归并，方便同一考点集中刷题。" % (total, parts))
    lines.append(">")
    lines.append("> 题目内容与原文件完全一致，仅调整顺序；题号为**原文件题号**（单选 / 多选 / 判断各自独立编号）。")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 知识点总览")
    lines.append("")
    lines.append("| # | 知识点模块 | 单选 | 多选 | 判断 | 合计 |")
    lines.append("|---|---|---|---|---|---|")
    for i, m in enumerate(assign["modules"], 1):
        c = {t: len(m.get("questions", {}).get(t, [])) for t in TYPE_ORDER}
        lines.append("| %d | %s | %d | %d | %d | %d |" %
                     (i, m["name"], c["单选"], c["多选"], c["判断"], sum(c.values())))
    lines.append("")
    lines.append("---")
    lines.append("")

    for i, m in enumerate(assign["modules"], 1):
        c = {t: len(m.get("questions", {}).get(t, [])) for t in TYPE_ORDER}
        lines.append("## %d. %s" % (i, m["name"]))
        lines.append("")
        desc = (m.get("desc") or "").strip()
        seg = "、".join("%s %d 题" % (TYPE_NAME[t], c[t]) for t in TYPE_ORDER if c[t])
        lines.append("> 共 %d 题（%s）%s" % (sum(c.values()), seg,
                                            ("　—— %s" % desc) if desc else ""))
        lines.append("")
        for t in TYPE_ORDER:
            nos = sorted(m.get("questions", {}).get(t, []))
            if not nos:
                continue
            lines.append("### %s（%d题）" % (TYPE_NAME[t], len(nos)))
            lines.append("")
            for n in nos:
                q = qs.get((t, n))
                if q is None:
                    lines.append("#### 第%d题" % n)
                    lines.append("")
                    lines.append("> 数据缺失")
                    lines.append("")
                    continue
                lab = clean_label(q["label"])
                lines.append("#### 第%d题%s" % (n, ("（%s）" % lab) if lab else ""))
                lines.append("")
                lines.append(q["body"])
                lines.append("")
                lines.append("---")
                lines.append("")
        lines.append("")

    text = "\n".join(lines).rstrip() + "\n"
    path = os.path.join(OUT, key + "_按知识点.md")
    open(path, "w", encoding="utf-8").write(text)
    return key, len(assign["modules"]), total, len(text)


FILES = ["01_会计法_解析", "02_企业会计准则_解析", "03_政府会计准则_解析",
         "04_内部控制规范_解析", "05_会计信息化_解析", "06_管理会计_解析",
         "07_税法相关_解析", "08_预算法_解析", "09_会计档案管理办法_解析",
         "10_会计基础工作规范_解析", "11_会计职业道德_解析",
         "12_数据资产管理_解析", "13_综合法规_解析"]

for k in FILES:
    print("生成 %-28s %2d组 %4d题 %7d字符" % build(k))

# 未改动的两个文件直接复制，保证 Word 集完整
import shutil
for n in ["00_总复习_知识点与易错点.md", "README.md"]:
    shutil.copyfile(os.path.join(SRC, n), os.path.join(OUT, n))
    print("复制", n)
