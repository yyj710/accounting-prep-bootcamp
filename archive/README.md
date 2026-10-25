# 项目归档说明

> 本文件夹是「会计知识竞赛学习文档」项目的完整过程资产归档。
> 最终交付物在上级目录：`按知识点版/`（Word 成品）+ 各 Markdown 成品（见 06）。

## 目录结构

| 目录 | 内容 | 说明 |
|---|---|---|
| `01_脚本/` | parse.py、build*.py、validate.py、md2docx.py 等 24 个 | 题目解析、归类拼装、独立校验、Markdown→Word 转换的全部脚本；`md2docx.py` 可复用（用法：`python md2docx.py <md目录> <输出目录>`） |
| `02_题目数据/` | `parsed/`（13 份结构化题目 JSON）、preview/（子任务紧凑清单） | 每份 JSON 含全部题目的 no / label / etype / stem / body / answer，是所有后续加工的数据源 |
| `03_知识点整理/` | 13 份「知识点：一句话结论」清单 | 按模块归纳的考点速查，已并入成品文档开头 |
| `04_复习卡/` | 13 份模块复习卡 | 每份含考点速览 / 易错点·陷阱 / 记忆点·口诀 / 高频数字四部分，汇总成 00_总复习_全模块汇总 |
| `05_讲解稿/` | 02_企业会计准则 12 个模块的讲解稿（m01–m12） | 「先讲解后刷题」样板用的素材，含为什么层 + 生活化例子 |
| `06_Markdown成品/` | `final_md/`（13 份按知识点版）、`master_md/`（总复习汇总）、`crash_md/`（考前突击速成手册）、`sample_md/`（02 讲解版样板） | 所有 Word 的 md 源文件 |

## 关键质量记录

- 1385 题按知识点重排后与原文件**逐字比对零差异**（validate.py 独立校验，不依赖 AI 自述）
- 归类规则：每题恰好归属一个模块一次（assign JSON 可复查）
- 题型校正：大量判断题原文错放在「单选题」章节，解析时按标签前缀校正为真实题型

## 数据流

```
原始题库(xlsx→md) → parse.py 解析 → parsed JSON
    → 子任务语义归类 → assign JSON → validate.py 校验
    → build/build2.py 拼装 → final_md → md2docx.py → 按知识点版/*.docx
    → 复习卡(review) → build_master.py → 总复习汇总
    → crash_md → 考前突击速成手册
```
