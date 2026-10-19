#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 Markdown 长文编译成单文件、自包含（图片内嵌）的图文 HTML。"""
import base64
import html as ihtml
import mimetypes
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.abspath(__file__))
MD = os.path.join(ROOT, "微流控合成组织-科普.md")
FRAG = os.path.join(ROOT, "web", "_body.html")
OUT = os.path.join(ROOT, "微流控合成组织-科普.html")
CSS = os.path.join(ROOT, "web", "style.css")
HERO = "web/assets/lung_on_a_chip_wyss.jpg"

# ---------------------------------------------------------------- 1. 源码预处理
src = open(MD, encoding="utf-8").read()
src = re.sub(r"\A---\n.*?\n---\n", "", src, flags=re.S)
src = re.sub(r"^#\s+.*?\n", "", src, count=1, flags=re.M)
src = re.sub(r"^###\s+——.*?\n", "", src, count=1, flags=re.M)


def remap(m):
    base = os.path.splitext(m.group(1))[0]
    base = base.replace("figures/", "web/figures/").replace("assets/", "web/assets/")
    return "](" + base + ".jpg)"


src = re.sub(r"\]\(((?:figures|assets)/[^)]+\.(?:png|jpg|jpeg|tif|tiff))\)", remap, src)
tmpp = os.path.join(ROOT, "web", "_src.md")
open(tmpp, "w", encoding="utf-8").write(src)

# ---------------------------------------------------------------- 2. pandoc
subprocess.run(
    ["pandoc", tmpp, "-f",
     "markdown+pipe_tables+tex_math_dollars-implicit_figures",
     "-t", "html", "--mathml", "--wrap=none", "--no-highlight", "-o", FRAG],
    check=True)
doc = open(FRAG, encoding="utf-8").read()

# ---------------------------------------------------------------- 3. 目录
heads = re.findall(r'<h([23]) id="([^"]+)">(.*?)</h\1>', doc, flags=re.S)
toc_items = []
for lvl, hid, txt in heads:
    t = re.sub(r"<[^>]+>", "", txt).strip()
    toc_items.append((int(lvl), hid, t))
toc_html = ['<div class="toc-title">目 录</div>',
            '<nav id="TOC" role="doc-toc"><ul>']
for i, (lvl, hid, t) in enumerate(toc_items):
    if lvl == 2:
        toc_html.append(f'<li class="l2"><a href="#{hid}">{ihtml.escape(t)}</a>')
        # 若下一项是 h3，则开启子列表
        if i + 1 < len(toc_items) and toc_items[i + 1][0] == 3:
            toc_html.append("<ul>")
        else:
            toc_html.append("</li>")
    else:
        toc_html.append(f'<li class="l3"><a href="#{hid}">{ihtml.escape(t)}</a></li>')
        if i + 1 >= len(toc_items) or toc_items[i + 1][0] == 2:
            toc_html.append("</ul></li>")
toc_html.append("</ul></nav>")
toc = "".join(toc_html)

# ---------------------------------------------------------------- 4. 图注结构化
# 4a. 图 + 紧随其后的 *署名* 段落
doc = re.sub(
    r'<p>\s*(<img[^>]*?/>)\s*</p>\s*<p>\s*<em>(.*?)</em>\s*</p>',
    lambda m: f'<figure>{m.group(1)}<figcaption>{m.group(2)}</figcaption></figure>',
    doc, flags=re.S)


def solo(m):
    tag = m.group(1)
    a = re.search(r'alt="([^"]*)"', tag)
    cap = (a.group(1) if a else "").strip()
    return (f'<figure>{tag}<figcaption>{cap}</figcaption></figure>' if cap
            else f'<figure>{tag}</figure>')


doc = re.sub(r'<p>\s*(<img[^>]*?/>)\s*</p>', solo, doc, flags=re.S)
doc = doc.replace(' aria-hidden="true"', "")

# 表格包一层以便横向滚动
doc = re.sub(r'(<table>.*?</table>)',
             lambda m: '<div class="tablewrap">' + m.group(1) + "</div>",
             doc, flags=re.S)

# ---------------------------------------------------------------- 5. 引言块
mm = re.search(r"<blockquote>(.*?)</blockquote>", doc, flags=re.S)
lede = mm.group(1).strip() if mm else ""
if mm:
    doc = doc.replace(mm.group(0), "", 1)

# ---------------------------------------------------------------- 6. 图片内嵌
def datauri(rel):
    p = os.path.join(ROOT, rel)
    mt = mimetypes.guess_type(p)[0] or "image/jpeg"
    b = base64.b64encode(open(p, "rb").read()).decode()
    return f"data:{mt};base64,{b}"


used = sorted(set(re.findall(r'src="(web/[^"]+)"', doc)))
for rel in used:
    doc = doc.replace(f'src="{rel}"', f'src="{datauri(rel)}"')
hero_uri = datauri(HERO)
css = open(CSS, encoding="utf-8").read()
n_fig = doc.count("<figure>")
n_tab = doc.count("<table>")

# ---------------------------------------------------------------- 7. 输出
page = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>微流控如何"造"出合成组织 · 图文科普长文</title>
<meta name="description" content="基于微流控合成合成组织（synthetic tissues）的图文科普长文：物理原理、四条技术路线、血管化、合成形态发生、器官芯片与产业化挑战。">
<link rel="license" href="https://creativecommons.org/licenses/by/4.0/">
<style>
{css}
</style>
</head>
<body>

<header class="hero">
  <img src="{hero_uri}" alt="">
  <div class="veil"></div>
  <div class="credit">图：Wyss Institute, Harvard / Wikimedia Commons / CC BY 2.0</div>
  <div class="cap"><div class="inner">
    <div class="kicker">Microfluidics &times; Synthetic Tissues</div>
    <h1>微流控如何"造"出合成组织</h1>
    <p class="sub">从芯片上的通道，到会呼吸、会搏动、会长血管的活组织</p>
  </div></div>
</header>

<section class="lede">
  <div class="tldr">{lede}</div>
</section>

<div class="layout">
  <main>
{doc}
  </main>
  <aside class="tocbox">{toc}</aside>
</div>

<footer><div class="fi">
  <p><b>关于本文</b>　本文为科普长文，6 张原理图由本文用 Matplotlib 自绘（其中 Turing 斑图为 Gray–Scott 模型的实时数值解）；其余摄影与示意图素材来自 Wikimedia Commons，作者与许可证详见随附的 <code>source/IMAGE_CREDITS.md</code>。</p>
  <p><b>关于引用</b>　全部文献 DOI 均已逐条核对。文中标注并修正了若干流传较广的错误引用与过度简化的说法（例如"挤出剪切超过 5–10 kPa 细胞就会死"），详见文末说明。</p>
  <p><b>生成方式</b>　Markdown 源文件经 pandoc 编译为自包含单文件 HTML，图片以 base64 内嵌，可离线阅读。</p>
  <p><b>许可</b>　本文文字与图 1–6 采用 <a href="https://creativecommons.org/licenses/by/4.0/" rel="license">CC BY 4.0</a> 许可：转载、翻译、改编、商用均可，须署名 <i>Jiantao Zhao</i>、标注标题《微流控如何“造”出合成组织》、给出<a href="https://jiantao-zhao.github.io/microfluidics-synthetic-tissue/">原文链接</a>与许可证链接，改动处须注明；不得暗示作者背书，不得附加额外限制。绘图与构建脚本另按 MIT 许可。文中 14 张来自 Wikimedia Commons 的摄影与示意图不在该许可范围内，各自按原许可证使用（含 CC0 / CC BY / CC BY-SA），逐张署名见 <a href="https://github.com/Jiantao-Zhao/microfluidics-synthetic-tissue/blob/main/source/IMAGE_CREDITS.md">IMAGE_CREDITS.md</a>。</p>
</div></footer>

</body>
</html>
"""
open(OUT, "w", encoding="utf-8").write(page)
print(f"✅ {OUT}")
print(f"   图片 {len(used)} 张内嵌 · 图 {n_fig} 幅 · 表 {n_tab} 个 · "
      f"目录 {len(toc_items)} 项 · {os.path.getsize(OUT)/1024/1024:.2f} MB")
