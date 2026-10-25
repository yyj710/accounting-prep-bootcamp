# -*- coding: utf-8 -*-
"""把各解析 md 拆成结构化题目，输出 JSON + 紧凑预览清单（供归类用）。

题型判定：标签以「判断」开头 → 判断题；否则按所在章节（单选/多选）。
"""
import json
import os
import re

SRC = r"<source>"
BASE = r"<workspace>"
os.makedirs(os.path.join(BASE, "parsed"), exist_ok=True)
os.makedirs(os.path.join(BASE, "preview"), exist_ok=True)

FILES = ["01_会计法_解析.md", "02_企业会计准则_解析.md", "03_政府会计准则_解析.md",
         "04_内部控制规范_解析.md", "05_会计信息化_解析.md", "06_管理会计_解析.md",
         "07_税法相关_解析.md", "08_预算法_解析.md", "09_会计档案管理办法_解析.md",
         "10_会计基础工作规范_解析.md", "11_会计职业道德_解析.md",
         "12_数据资产管理_解析.md", "13_综合法规_解析.md"]

QTYPE_RE = re.compile(r"^##\s*(单选题|多选题|判断题)")
QNO_RE = re.compile(r"^###\s*第(\d+)题\s*(?:（(.+?)）)?\s*$")
STEM_RE = re.compile(r"\*\*题目\*\*[：:]\s*(.*)")


def true_type(label, section):
    if label.startswith("判断"):
        return "判断"
    return "多选" if "多选" in (section or "") else "单选"


def parse(path):
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    head_lines, section, qs, cur = [], None, [], None
    for ln in lines:
        mq = QTYPE_RE.match(ln)
        if mq:
            section = mq.group(1)
            if cur:
                qs.append(cur); cur = None
            continue
        mh = QNO_RE.match(ln)
        if mh:
            if cur:
                qs.append(cur)
            label = (mh.group(2) or "").strip()
            cur = {"no": int(mh.group(1)), "section": section or "", "label": label,
                   "etype": true_type(label, section), "body": []}
            continue
        if cur is not None:
            cur["body"].append(ln)
        else:
            head_lines.append(ln)
    if cur:
        qs.append(cur)
    for q in qs:
        body = "\n".join(q["body"]).strip("\n")
        body = re.sub(r"\n-{3,}\s*$", "", body).strip("\n")
        q["body"] = body
        m = STEM_RE.search(body)
        q["stem"] = m.group(1).strip() if m else body.split("\n", 1)[0]
        ma = re.search(r"\*\*答案\*\*[：:]\s*(.+)", body)
        q["answer"] = ma.group(1).strip() if ma else ""
    return "\n".join(head_lines).strip("\n"), qs


index = {}
for f in FILES:
    head, qs = parse(os.path.join(SRC, f))
    key = f.replace(".md", "")
    json.dump({"file": f, "head": head, "questions": qs},
              open(os.path.join(BASE, "parsed", key + ".json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    out = ["### %s  共%d题" % (f, len(qs))]
    for q in qs:
        out.append("%s|%d|%s|%s" % (q["etype"], q["no"], q["label"] or "-",
                                    q["stem"][:110].replace("\n", " ")))
    open(os.path.join(BASE, "preview", key + ".txt"), "w", encoding="utf-8").write("\n".join(out))
    cnt = {}
    for q in qs:
        cnt[q["etype"]] = cnt.get(q["etype"], 0) + 1
    index[key] = {"file": f, "total": len(qs), "by_type": cnt,
                  "keys": ["%s-%d" % (q["etype"], q["no"]) for q in qs]}
    print("%-30s 共%4d题  %s" % (f, len(qs), cnt))

json.dump(index, open(os.path.join(BASE, "index.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
