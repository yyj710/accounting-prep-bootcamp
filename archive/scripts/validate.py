# -*- coding: utf-8 -*-
"""独立校验归类结果：全部题目必须恰好出现一次。"""
import json
import os
import re
import sys

BASE = r"<workspace>"
PARSED = os.path.join(BASE, "parsed")
ASSIGN = os.path.join(BASE, "assign")

ok_all = True
for fn in sorted(os.listdir(PARSED)):
    key = fn[:-5]
    pq = json.load(open(os.path.join(PARSED, fn), encoding="utf-8"))["questions"]
    expected = {}
    for q in pq:
        expected.setdefault(q["etype"], []).append(q["no"])
    for k in expected:
        expected[k].sort()

    ap = os.path.join(ASSIGN, key + ".json")
    if not os.path.exists(ap):
        print("MISSING assign:", key); ok_all = False; continue
    raw = open(ap, encoding="utf-8").read()
    raw = re.sub(r"^```(?:json)?|```$", "", raw.strip(), flags=re.M).strip()
    a = json.loads(raw)

    got, dup = {}, []
    for m in a["modules"]:
        for t, nos in m.get("questions", {}).items():
            got.setdefault(t, [])
            for n in nos:
                if n in got[t]:
                    dup.append((t, n))
                got[t].append(n)
    for k in got:
        got[k].sort()

    probs = []
    if set(got) != set(expected):
        probs.append("题型集合不一致 %s vs %s" % (sorted(got), sorted(expected)))
    else:
        for k in expected:
            if got[k] != expected[k]:
                miss = sorted(set(expected[k]) - set(got[k]))
                extra = sorted(set(got[k]) - set(expected[k]))
                probs.append("%s 缺失%s 多余%s" % (k, miss, extra))
    if dup:
        probs.append("重复: %s" % dup)

    nmod = len(a["modules"])
    if probs:
        ok_all = False
        print("FAIL %-28s %s" % (key, "; ".join(probs)))
    else:
        print("OK   %-28s %2d组  %s  合计%d" %
              (key, nmod, {k: len(v) for k, v in sorted(got.items())}, sum(len(v) for v in got.values())))

print("\n总体：", "全部通过" if ok_all else "存在问题")
sys.exit(0 if ok_all else 1)
