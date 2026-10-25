# -*- coding: utf-8 -*-
"""样板版：知识点讲解前置到每个模块的题目前（先学懂再刷题）。仅处理 02。"""
import json
import os
import re

BASE = r"<workspace>"
KEY = "02_企业会计准则_解析"
MD = os.path.join(BASE, "sample_md")
os.makedirs(MD, exist_ok=True)

TYPE_ORDER = ["单选", "多选", "判断"]
TYPE_NAME = {"单选": "单选题", "多选": "多选题", "判断": "判断题"}
STRIP_PREFIX = ["基础概念·", "判断题·", "判断·", "概念·", "应用·", "计算·",
                "易混·", "易错·", "案例·", "条文·"]
GENERIC = {"概念", "应用", "计算", "判断", "判断题", "基础概念", "易混", "易错"}


def clean_label(label):
    lab = (label or "").strip()
    for p in STRIP_PREFIX:
        if lab.startswith(p):
            lab = lab[len(p):]
            break
    lab = lab.strip("· ").strip()
    return "" if lab in GENERIC else lab


data = json.load(open(os.path.join(BASE, "parsed", KEY + ".json"), encoding="utf-8"))
raw = open(os.path.join(BASE, "assign", KEY + ".json"), encoding="utf-8").read()
raw = re.sub(r"^```(?:json)?|```$", "", raw.strip(), flags=re.M).strip()
assign = json.loads(raw)
qs = {(q["etype"], q["no"]): q for q in data["questions"]}

cnt = {}
for q in data["questions"]:
    cnt[q["etype"]] = cnt.get(q["etype"], 0) + 1
total = sum(cnt.values())
parts = " / ".join("%s %d" % (TYPE_NAME[t], cnt[t]) for t in TYPE_ORDER if cnt.get(t))
title = re.sub(r"^#\s*", "", data["head"].split("\n")[0]).strip()
title = title.replace(" · 逐题解析", "").replace(" · 题目解析（全）", "").strip()

L = []
L.append("# %s（讲解版 · 样板）" % title)
L.append("")
L.append("> 共 **%d** 题（%s），%d 个知识模块。" % (total, parts, len(assign["modules"])))
L.append(">")
L.append("> **怎么用**：每个模块先读「知识点讲解」（含核心考点 + 为什么 + 生活化例子 + 易混提醒），")
L.append("> 读懂了再刷该模块的题；做错了回到讲解找对应考点。题目在模块内从 1 连续编号，")
L.append("> 题目内容（题干 / 答案 / 解析）与原文件完全一致。")
L.append("")
L.append("---")
L.append("")
L.append("## 模块总览")
L.append("")
L.append("| # | 知识点模块 | 单选 | 多选 | 判断 | 合计 |")
L.append("|---|---|---|---|---|---|")
for i, m in enumerate(assign["modules"], 1):
    c = {t: len(m.get("questions", {}).get(t, [])) for t in TYPE_ORDER}
    L.append("| %d | %s | %d | %d | %d | %d |" %
             (i, m["name"], c["单选"], c["多选"], c["判断"], sum(c.values())))
L.append("")
L.append("---")
L.append("")

for i, m in enumerate(assign["modules"], 1):
    c = {t: len(m.get("questions", {}).get(t, [])) for t in TYPE_ORDER}
    seg = "、".join("%s %d 题" % (TYPE_NAME[t], c[t]) for t in TYPE_ORDER if c[t])
    L.append("## %d. %s（共%d题：%s）" % (i, m["name"], sum(c.values()), seg))
    L.append("")

    teach_path = os.path.join(BASE, "teach", "%s_m%02d.md" % (KEY.split("_")[0], i))
    teach = open(teach_path, encoding="utf-8").read().strip() if os.path.exists(teach_path) else ""
    L.append("### 知识点讲解")
    L.append("")
    if teach:
        L.append(teach)
    else:
        L.append("> （讲解缺失）")
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
            L.append(q["body"] if q else "> 数据缺失")
            L.append("")
            L.append("---")
            L.append("")
    L.append("")

text = "\n".join(L).rstrip() + "\n"
out = os.path.join(MD, KEY + "_样板.md")
open(out, "w", encoding="utf-8").write(text)
print("写出：", out)
print("%.1f KB，H1:%d H2:%d H3:%d H4:%d" % (
    len(text.encode("utf-8")) / 1024,
    len(re.findall(r"^# ", text, re.M)), len(re.findall(r"^## ", text, re.M)),
    len(re.findall(r"^### ", text, re.M)), len(re.findall(r"^#### ", text, re.M))))

# ---- 校验 1：题目正文零丢失 ----
norm = lambda s: re.sub(r"\s+", "", re.sub(r"^-{3,}$", "", s, flags=re.M)).strip()
orig = sorted(norm(q["body"]) for q in data["questions"])
PAT = re.compile(r"^#### 第\d+题[^\n]*\n(.*?)(?=^#### |^### |^## |\Z)", re.M | re.S)
new = sorted(norm(m.group(1)) for m in PAT.finditer(text))
print("题目零丢失：", "通过" if orig == new else "失败 原%d 新%d" % (len(orig), len(new)))
if orig != new:
    so, sn = set(orig), set(new)
    print("  丢失", len(so - sn), "新增", len(sn - sn))
    for x in list(so - sn)[:2]:
        print("   原:", x[:120])
    for x in list(sn - so)[:2]:
        print("   新:", x[:120])

# ---- 校验 2：每个模块内编号连续 1..n ----
ok = True
for segm in re.split(r"^## ", text, flags=re.M)[1:]:
    nums = [int(x) for x in re.findall(r"^#### 第(\d+)题", segm, re.M)]
    if nums and nums != list(range(1, len(nums) + 1)):
        ok = False
        print("编号异常：", segm.split("\n")[0], nums[:10])
print("模块内编号连续：", "通过" if ok else "失败")

# ---- 校验 3：12 个模块都有讲解 ----
teach_cnt = len(re.findall(r"^### 知识点讲解", text, flags=re.M))
print("知识点讲解节数：", teach_cnt)
