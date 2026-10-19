# 许可范围 / License Scope

本项目采用**分层许可**：正文、自绘插图与代码各自适用不同条款，第三方素材保留其原有许可。

- **CC BY 4.0 完整法律文本**：[`LICENSE`](LICENSE)（本文件只说明"哪些部分适用哪一条款"）
- **代码许可**：见第 2 节
- **第三方配图**：见第 3 节与 [`source/IMAGE_CREDITS.md`](source/IMAGE_CREDITS.md)

---

## 1. 正文文字与自绘原理图 —— CC BY 4.0

适用范围：

- `index.html` 中的全部**文字内容**（正文、图注、表格、术语表、参考文献说明）
- `source/微流控合成组织-科普.md`
- **图 1–图 6** 六张自绘原理图（由 `source/f0*.py` 用 Matplotlib 生成，含图 5a 的 Gray–Scott 数值解）

许可：**Creative Commons Attribution 4.0 International (CC BY 4.0)**
法律文本：https://creativecommons.org/licenses/by/4.0/legalcode
人类可读摘要：https://creativecommons.org/licenses/by/4.0/

### 你可以做什么

复制、转载、翻译、改编、汇编、商用——**无需事先取得许可**。

### 你必须做什么（CC BY 4.0 的四项署名要求）

1. **署名**：标注原作者 Jiantao Zhao。
2. **标注标题**：给出作品名称《微流控如何"造"出合成组织》。
3. **给出链接**：同时给出来源链接与许可证链接。
4. **说明改动**：若作了修改，须注明"本文基于原作修改"。

且**不得附加额外限制**（例如不得对转载件再加 DRM 或更严格的条款），**不得暗示原作者为你或你的用途背书**。

### 建议署名格式

网页 / 文章：

> Jiantao Zhao，《微流控如何"造"出合成组织》，CC BY 4.0。
> 来源：https://jiantao-zhao.github.io/microfluidics-synthetic-tissue/

图片（复用图 1–6 时）：

> 图：Jiantao Zhao，《微流控如何"造"出合成组织》，CC BY 4.0。

---

## 2. 代码 —— MIT

适用范围：`source/*.py`（含 `build_html.py`、`figstyle.py`、`f01`–`f06` 绘图脚本）。

```
MIT License

Copyright (c) 2026 Jiantao Zhao

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 3. 第三方素材 —— 不在上述许可范围内

`index.html` 中另有 **14 张摄影与机构示意图**来自 Wikimedia Commons，其著作权属于各自作者，按原许可证提供（多为 CC0 / CC BY 2.0–4.0 / CC BY-SA 4.0）。

- **逐张的作者、原始链接与许可证**：见 [`source/IMAGE_CREDITS.md`](source/IMAGE_CREDITS.md)
- **CC BY / CC BY-SA** 素材：转载时须保留图注中的署名与许可证，并链接到许可证原文
- **CC BY-SA** 素材：若对其作改编，改编件须以相同许可证（SA）发布——此要求**不传染**到本项目其余部分，仅约束该图的改编件
- **CC0 / Public Domain** 素材：无署名义务，但本项目仍保留署名以示尊重

**简言之**：本文的 CC BY 4.0 只覆盖"我写的字和我画的图"，不覆盖"我引的图"。

---

## 4. 引用的文献

参考文献中的论文标题、数据与结论归原作者与出版方所有，本文仅作引用与转述。引用条目按学术惯例列出，不构成对原文的再许可。

---

## 5. 免责声明

本文为科普作品，所述参数与结论力求准确但**不构成实验操作、医疗或监管建议**。依本文内容开展实验（尤其是涉及细胞、溴酸盐等化学品或生物材料）所产生的风险与合规责任由操作者自负。
