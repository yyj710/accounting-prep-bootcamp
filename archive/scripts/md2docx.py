# -*- coding: utf-8 -*-
"""批量把 Markdown 转成 Word(.docx)：pandoc + 中文友好字体样式。"""
import os
import re
import subprocess
import tempfile
import zipfile

import sys

import pypandoc

SRC = sys.argv[1] if len(sys.argv) > 1 else \
    r"<source>"
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(SRC, "Word版")

PANDOC = pypandoc.get_pandoc_path()
LATIN = "Times New Roman"
EA_BODY = "宋体"
EA_HEAD = "微软雅黑"

tmp = tempfile.mkdtemp()
ref_default = os.path.join(tmp, "ref_default.docx")
with open(ref_default, "wb") as f:
    subprocess.run([PANDOC, "--print-default-data-file", "reference.docx"],
                   stdout=f, check=True)

with zipfile.ZipFile(ref_default) as z:
    names = z.namelist()
    blobs = {n: z.read(n) for n in names}

xml = blobs["word/styles.xml"].decode("utf-8")


def patch_tag(tag: str, ea: str, force_latin: bool) -> str:
    """给 rFonts 补/改 eastAsia；非主题字体再统一西文字体。"""
    if force_latin:
        if 'w:ascii="' in tag:
            tag = re.sub(r'w:ascii="[^"]*"', 'w:ascii="%s"' % LATIN, tag)
        if 'w:hAnsi="' in tag:
            tag = re.sub(r'w:hAnsi="[^"]*"', 'w:hAnsi="%s"' % LATIN, tag)
    if 'w:eastAsia="' in tag:
        tag = re.sub(r'w:eastAsia="[^"]*"', 'w:eastAsia="%s"' % ea, tag)
    else:
        tag = tag[:-2] + ' w:eastAsia="%s"/>' % ea
    return tag


def patch_style_block(m: re.Match) -> str:
    open_tag, sid, body, close_tag = m.group(1), m.group(2), m.group(3), m.group(4)
    ea = EA_HEAD if (sid.startswith("Heading") or sid in ("Title", "Subtitle")) else EA_BODY
    body = re.sub(r"<w:rFonts\b[^>]*/>",
                  lambda mm: patch_tag(mm.group(0), ea, force_latin=("Theme" not in mm.group(0))),
                  body)
    return open_tag + body + close_tag


xml = re.sub(r'(<w:style\b[^>]*w:styleId="([^"]+)"[^>]*>)(.*?)(</w:style>)',
             patch_style_block, xml, flags=re.S)

# docDefaults 里也补一份东亚字体
xml = re.sub(r'(<w:docDefaults>.*?</w:docDefaults>)',
             lambda m: re.sub(r"<w:rFonts\b[^>]*/>",
                              lambda mm: patch_tag(mm.group(0), EA_BODY, force_latin=True),
                              m.group(1), flags=re.S),
             xml, count=1, flags=re.S)

blobs["word/styles.xml"] = xml.encode("utf-8")
ref_custom = os.path.join(tmp, "ref_custom.docx")
with zipfile.ZipFile(ref_custom, "w", zipfile.ZIP_DEFLATED) as z:
    for n in names:
        z.writestr(n, blobs[n])

os.makedirs(OUT, exist_ok=True)
srcs = sorted(f for f in os.listdir(SRC) if f.lower().endswith(".md"))
print("found %d md files" % len(srcs))

ok, fail = 0, []
for name in srcs:
    src = os.path.join(SRC, name)
    dst = os.path.join(OUT, os.path.splitext(name)[0] + ".docx")
    try:
        subprocess.run(
            [PANDOC, "-f", "gfm", "-t", "docx",
             "--reference-doc", ref_custom,
             "-o", dst, src],
            check=True, capture_output=True)
        size = os.path.getsize(dst)
        print("OK  %-40s %8.1f KB" % (name, size / 1024))
        ok += 1
    except subprocess.CalledProcessError as e:
        fail.append(name)
        print("FAIL", name, e.stderr.decode("utf-8", "ignore")[:300])

print("\n完成 %d/%d，输出目录：%s" % (ok, len(srcs), OUT))
if fail:
    print("失败：", fail)
