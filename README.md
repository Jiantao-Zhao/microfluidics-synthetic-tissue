# 微流控如何"造"出合成组织

> 从芯片上的通道，到会呼吸、会搏动、会长血管的活组织。

一份关于微流控与合成组织的**图文科普长文**：从层流、扩散、液滴三个物理内核出发，走过微流控纺丝、液滴组装、生物打印、器官芯片四条技术路线，最后落到血管化、合成形态发生与监管转化。

**在线阅读：** https://jiantao-zhao.github.io/microfluidics-synthetic-tissue/

---

## 内容

| 章节 | 内容 |
|---|---|
| 0 | 先看全貌：六工位装配线 |
| 1 | 为什么非要把组织"造"出来（器官缺口、动物模型、培养皿） |
| 2 | 微流控的物理内核：Re、Pe、Ca 与三条尺度律 |
| 3 | 四条技术路线：纺丝 / 液滴微凝胶 / 生物打印 / 器官芯片 |
| 4 | 血管化：合成组织的"最后一公里" |
| 5 | 合成形态发生：Turing 斑图、形态原梯度、合成细胞间信号、组装体 |
| 6–7 | 真实世界里的器官芯片，以及从实验室到病房 |
| 8 | 五道坎与正在发生的解法 |
| 9 | 如果你想上手：一页速查 |
| 10 | 术语表 |

正文含 **20 张配图**（6 张自绘原理图 + 14 张 Wikimedia Commons 素材）与 **66 条参考文献**，DOI 均经 Crossref / 出版商页面逐条核对。

## 文件结构

```
index.html                    单文件站点（图片全部内嵌为 data URI，离线可用）
source/*.md                   正文 Markdown 源
source/IMAGE_CREDITS.md       配图的作者与许可证
source/f0*.py                 6 张原理图的 Matplotlib 绘图脚本
source/build_html.py          Markdown → 单文件 HTML 的构建脚本
```

## 配图与许可

- 原理图 1–6 为本文自绘（Matplotlib），复用请注明来源。
- 摄影与机构示意图来自 Wikimedia Commons，逐张作者与许可证见 [`source/IMAGE_CREDITS.md`](source/IMAGE_CREDITS.md)；其中 CC BY / CC BY-SA 素材的使用遵循署名—相同方式共享要求。

## 关于引用

写作过程中修正了若干在科普中流传较广的错误，例如肺水肿肺芯片论文的年份、"A guide to the organ-on-a-chip" 的期刊，以及"3D 打印多血管组织 = Lee 2014 Science"这一并不存在的引用。详见正文参考文献后的说明。
