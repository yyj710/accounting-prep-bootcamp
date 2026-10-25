# -*- coding: utf-8 -*-
"""把 13 份模块复习卡 + 跨模块附录，合并成一份总复习文档。"""
import os
import re

BASE = r"<workspace>"
REVIEW = os.path.join(BASE, "review")
ORIG = r"<source>\00_总复习_知识点与易错点.md"
OUTDIR = os.path.join(BASE, "master_md")
os.makedirs(OUTDIR, exist_ok=True)

MODULES = [
    ("01_会计法_解析", "01 会计法", 174),
    ("02_企业会计准则_解析", "02 企业会计准则", 252),
    ("03_政府会计准则_解析", "03 政府会计准则", 258),
    ("04_内部控制规范_解析", "04 内部控制规范", 182),
    ("05_会计信息化_解析", "05 会计信息化", 75),
    ("06_管理会计_解析", "06 管理会计", 38),
    ("07_税法相关_解析", "07 税法相关", 55),
    ("08_预算法_解析", "08 预算法", 40),
    ("09_会计档案管理办法_解析", "09 会计档案管理办法", 53),
    ("10_会计基础工作规范_解析", "10 会计基础工作规范", 48),
    ("11_会计职业道德_解析", "11 会计职业道德", 33),
    ("12_数据资产管理_解析", "12 数据资产管理", 27),
    ("13_综合法规_解析", "13 综合法规", 150),
]

# ---------- 拼接模块复习卡 ----------
parts = []
for key, title, n in MODULES:
    p = os.path.join(REVIEW, key + ".md")
    body = open(p, encoding="utf-8").read().strip()
    parts.append("## %s（%d 题）\n\n%s" % (title, n, body))

# ---------- 读取原文的跨模块章节 ----------
orig = open(ORIG, encoding="utf-8").read()


def slice_section(text, heading_prefix):
    """取出以 `## {heading_prefix}` 开头、到下一个 `## ` 前的整段（不含该 ## 行）。"""
    m = re.search(r"^## " + re.escape(heading_prefix) + r".*?$", text, re.M)
    if not m:
        raise SystemExit("未找到章节：" + heading_prefix)
    start = m.end()
    nxt = re.search(r"^## ", text[start:], re.M)
    end = start + (nxt.start() if nxt else len(text) - start)
    return text[start:end].strip()


mis = slice_section(orig, "二、易错点")
mnemo = slice_section(orig, "三、记忆口诀")
nums = slice_section(orig, "四、高频数字")
strat = slice_section(orig, "六、备考策略")

# 把附录里的 ### 小标题保留；修正内部交叉引用
strat = strat.replace("（见第三节）", "（见附录 B）").replace("（见第二节）", "（见附录 A）")
# 附录 B 口诀里的整行粗体分组标签提升为 ###，便于导航
mnemo = re.sub(r"^\*\*(.+?)\*\*\s*$", r"### \1", mnemo, flags=re.M)

appendix = []
appendix.append("## 附录 A · 跨模块易错对比表\n\n" + mis)
appendix.append("## 附录 B · 记忆口诀总汇\n\n" + mnemo)
appendix.append("## 附录 C · 高频数字 · 期限 · 比例速查\n\n" + nums)
appendix.append("## 附录 D · 备考策略与冲刺提醒\n\n" + strat)

# ---------- 头部（标题 + 目录） ----------
toc_lines = []
for _, title, n in MODULES:
    toc_lines.append("- %s（%d 题）" % (title, n))
toc_lines += [
    "- 附录 A · 跨模块易错对比表",
    "- 附录 B · 记忆口诀总汇",
    "- 附录 C · 高频数字 · 期限 · 比例速查",
    "- 附录 D · 备考策略与冲刺提醒",
]

header = """# 会计知识竞赛 · 总复习

> 覆盖 **13 个文件、1385 道题**。每个模块一段「复习卡」，含四部分：
> **一、考点速览**（按知识模块归纳的核心结论）· **二、易错点 · 陷阱**（易混对比）·
> **三、记忆点 · 口诀**（速记法）· **四、高频数字 · 期限 · 比例**（可直接背的硬信息）。
> 文末另附跨模块对比表、口诀总汇、数字速查与备考策略。
>
> 全部内容均从各文件题目的题干 / 答案 / 解析中提取，未引入文件以外的知识。

## 目录

%s

---

""" % "\n".join(toc_lines)

master = header + "\n\n---\n\n".join(parts) + "\n\n---\n\n" + "\n\n---\n\n".join(appendix) + "\n"

dst = os.path.join(OUTDIR, "00_总复习_全模块汇总.md")
with open(dst, "w", encoding="utf-8") as f:
    f.write(master)

# ---------- 统计 ----------
print("写出：", dst)
print("总字节：%.1f KB" % (len(master.encode("utf-8")) / 1024))
print("H1:%d  H2:%d  H3:%d  H4:%d" % (
    len(re.findall(r"^# ", master, re.M)),
    len(re.findall(r"^## ", master, re.M)),
    len(re.findall(r"^### ", master, re.M)),
    len(re.findall(r"^#### ", master, re.M))))
