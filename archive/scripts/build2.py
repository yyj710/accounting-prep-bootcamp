# -*- coding: utf-8 -*-
"""v2：知识点整理前置 + 模块内连续编号。输出到 regroup/final_md/"""
import json
import os
import re
import shutil

BASE = r"<workspace>"
MD = os.path.join(BASE, "final_md")
os.makedirs(MD, exist_ok=True)

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
    return "" if lab in GENERIC else lab


def load(key):
    data = json.load(open(os.path.join(BASE, "parsed", key + ".json"), encoding="utf-8"))
    raw = open(os.path.join(BASE, "assign", key + ".json"), encoding="utf-8").read()
    raw = re.sub(r"^```(?:json)?|```$", "", raw.strip(), flags=re.M).strip()
    assign = json.loads(raw)
    notes_path = os.path.join(BASE, "notes", key + ".md")
    notes = open(notes_path, encoding="utf-8").read().strip() if os.path.exists(notes_path) else ""
    return data, assign, notes


def build(key):
    data, assign, notes = load(key)
    qs = {(q["etype"], q["no"]): q for q in data["questions"]}
    cnt = {}
    for q in data["questions"]:
        cnt[q["etype"]] = cnt.get(q["etype"], 0) + 1
    total = sum(cnt.values())
    parts = " / ".join("%s %d" % (TYPE_NAME[t], cnt[t]) for t in TYPE_ORDER if cnt.get(t))
    title = re.sub(r"^#\s*", "", data["head"].split("\n")[0]).strip()
    title = title.replace(" · 逐题解析", "").replace(" · 题目解析（全）", "").strip()

    L = []
    L.append("# %s（按知识点归类）" % title)
    L.append("")
    L.append("> 共 **%d** 题（%s）。已按 **知识点模块 → 题型** 重新归并。" % (total, parts))
    L.append(">")
    L.append("> 阅读顺序：① 知识点整理（考点速览） → ② 分模块刷题。题目在各模块内**从 1 开始连续编号**，")
    L.append("> 不再对应原文件题号；题目内容（题干 / 答案 / 解析）与原文件完全一致。")
    L.append("")
    L.append("---")
    L.append("")
    L.append("## 知识点整理")
    L.append("")
    L.append("### 模块总览")
    L.append("")
    L.append("| # | 知识点模块 | 单选 | 多选 | 判断 | 合计 |")
    L.append("|---|---|---|---|---|---|")
    for i, m in enumerate(assign["modules"], 1):
        c = {t: len(m.get("questions", {}).get(t, [])) for t in TYPE_ORDER}
        L.append("| %d | %s | %d | %d | %d | %d |" %
                 (i, m["name"], c["单选"], c["多选"], c["判断"], sum(c.values())))
    L.append("")
    if notes:
        L.append(notes)
    else:
        L.append("> （本文件暂无知识点整理内容）")
    L.append("")
    L.append("---")
    L.append("")

    for i, m in enumerate(assign["modules"], 1):
        c = {t: len(m.get("questions", {}).get(t, [])) for t in TYPE_ORDER}
        L.append("## %d. %s" % (i, m["name"]))
        L.append("")
        seg = "、".join("%s %d 题" % (TYPE_NAME[t], c[t]) for t in TYPE_ORDER if c[t])
        L.append("> 共 %d 题（%s）" % (sum(c.values()), seg))
        L.append("")
        seq = 0
        for t in TYPE_ORDER:
            nos = sorted(m.get("questions", {}).get(t, []))
            if not nos:
                continue
            L.append("### %s（%d题）" % (TYPE_NAME[t], len(nos)))
            L.append("")
            for n in nos:
                seq += 1
                q = qs.get((t, n))
                lab = clean_label(q["label"]) if q else ""
                L.append("#### 第%d题%s" % (seq, ("　%s" % lab) if lab else ""))
                L.append("")
                if q:
                    L.append(q["body"])
                else:
                    L.append("> 数据缺失")
                L.append("")
                L.append("---")
                L.append("")
        L.append("")

    text = "\n".join(L).rstrip() + "\n"
    open(os.path.join(MD, key + ".md"), "w", encoding="utf-8").write(text)
    return key, total, len(text)


FILES = ["01_会计法_解析", "02_企业会计准则_解析", "03_政府会计准则_解析",
         "04_内部控制规范_解析", "05_会计信息化_解析", "06_管理会计_解析",
         "07_税法相关_解析", "08_预算法_解析", "09_会计档案管理办法_解析",
         "10_会计基础工作规范_解析", "11_会计职业道德_解析",
         "12_数据资产管理_解析", "13_综合法规_解析"]

for k in FILES:
    print("v2 %-28s %4d题 %7d字符" % build(k))

SRC = r"<source>"
for n in ["00_总复习_知识点与易错点.md", "README.md"]:
    shutil.copyfile(os.path.join(SRC, n), os.path.join(MD, n))
print("复制 00_总复习 + README")
