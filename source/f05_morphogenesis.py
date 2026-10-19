# -*- coding: utf-8 -*-
"""图5：合成形态发生 —— 让组织“被编程”地长出来"""
import numpy as np
import figstyle as S
from matplotlib.patches import (FancyBboxPatch, Rectangle, Circle, Polygon,
                                FancyArrowPatch)

plt = S.plt
rng = np.random.default_rng(42)


# ---------- Gray–Scott 反应扩散：真实的 Turing 斑图数值解 ----------
def gray_scott(n=128, steps=9000, F=0.0367, k=0.0649, Du=0.16, Dv=0.08, dt=1.0):
    u = np.ones((n, n), dtype=np.float32)
    v = np.zeros((n, n), dtype=np.float32)
    u += 0.02 * rng.standard_normal((n, n)).astype(np.float32)
    v += 0.02 * rng.standard_normal((n, n)).astype(np.float32)
    r = int(n * 0.10)
    c = n // 2
    u[c - r:c + r, c - r:c + r] = 0.50
    v[c - r:c + r, c - r:c + r] = 0.25
    snaps = {}
    for s in range(steps):
        Lu = (np.roll(u, 1, 0) + np.roll(u, -1, 0) +
              np.roll(u, 1, 1) + np.roll(u, -1, 1) - 4 * u)
        Lv = (np.roll(v, 1, 0) + np.roll(v, -1, 0) +
              np.roll(v, 1, 1) + np.roll(v, -1, 1) - 4 * v)
        uvv = u * v * v
        u += dt * (Du * Lu - uvv + F * (1.0 - u))
        v += dt * (Dv * Lv + uvv - (F + k) * v)
        if s + 1 in (60, 900, steps):
            snaps[s + 1] = v.copy()
    return snaps


snaps = gray_scott()

fig = plt.figure(figsize=(13.6, 9.2))
gs = fig.add_gridspec(3, 2, height_ratios=[1, 1, 0.30], hspace=0.34, wspace=0.13,
                      left=0.028, right=0.978, top=0.885, bottom=0.045)


def ptitle(ax, tag, title, color, sub=None):
    ax.text(0.0, 1.135, tag, transform=ax.transAxes, fontsize=14.5,
            fontweight="bold", color=color, va="bottom")
    ax.text(0.068, 1.13, title, transform=ax.transAxes, fontsize=11.8,
            fontweight="bold", color=color, va="bottom")
    if sub:
        ax.text(0.0, 1.015, sub, transform=ax.transAxes, fontsize=8.7,
                color=S.GRAY, va="bottom")


def arr(ax, p1, p2, color="#8FA3B5", lw=1.6, ms=12, z=6, style="-|>"):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=ms,
                                 lw=lw, color=color, zorder=z, shrinkA=0, shrinkB=0))


# ================================================== (a) Turing 斑图
ax = fig.add_subplot(gs[0, 0]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
ptitle(ax, "a", "Turing 斑图：位置信息可以是“自发涌现”的", S.VIOLET,
       "两种分子（短程激活 + 长程抑制）互相追逐，就从均匀里长出周期结构")

boxes = [(0.030, "① 初始：均匀"), (0.345, "② 早期：失稳"), (0.660, "③ 成熟：周期斑图")]
BW, BH = 0.305, 0.640
imgs = [snaps[60], snaps[900], snaps[9000]]
for (bx, lab), im in zip(boxes, imgs):
    ax.imshow(im, extent=(bx, bx + BW, 0.185, 0.185 + BH), origin="lower",
              cmap="magma", aspect="auto", zorder=2,
              vmin=0, vmax=max(0.42, float(im.max())))
    ax.add_patch(Rectangle((bx, 0.185), BW, BH, fc="none", ec="#C9D3DD",
                           lw=1.2, zorder=3))
    ax.text(bx + BW / 2, 0.862, lab, fontsize=8.8, color=S.VIOLET,
            ha="center", va="center", fontweight="bold")
for bx in (0.345, 0.660):
    arr(ax, (bx - 0.032, 0.505), (bx - 0.006, 0.505), color=S.VIOLET, lw=1.8)
ax.text(0.5, 0.060, "上图为 Gray–Scott 模型（F = 0.0367, k = 0.0649）的实时数值解："
                    "没有模板，也没有“指挥中心”。",
        fontsize=8.2, color="#3C4E60", ha="center", va="center")

# ================================================== (b) 形态原梯度建体轴
ax = fig.add_subplot(gs[0, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
ptitle(ax, "b", "形态原梯度：把“体轴”写进培养液", S.GREEN,
       "微流控能给出一段稳定的浓度斜坡 —— 这正是胚胎里决定“头尾”的那类信号")

gy0, gh = 0.540, 0.085
# 梯度通道
grad = np.linspace(0, 1, 400)
img = np.tile(grad, (40, 1))
ax.imshow(img, extent=(0.075, 0.955, gy0, gy0 + gh), origin="lower", cmap="YlGn",
          aspect="auto", zorder=2, vmin=0, vmax=1)
ax.add_patch(Rectangle((0.075, gy0), 0.88, gh, fc="none", ec="#9FB3C4", lw=1.3, zorder=3))
ax.text(0.075, gy0 + gh + 0.028, "WNT 浓度：低", fontsize=8.0, color="#2E7D5B",
        ha="left", va="bottom")
ax.text(0.955, gy0 + gh + 0.028, "高", fontsize=8.0, color="#2E7D5B",
        ha="right", va="bottom")
arr(ax, (0.020, gy0 + gh / 2), (0.068, gy0 + gh / 2), color="#2E7D5B", lw=1.8)
ax.text(0.020, gy0 + gh / 2 + 0.045, "灌流", fontsize=7.8, color="#2E7D5B", ha="left")

# 梯度下方的细胞带
bands = [("#F6E7A8", "后脑 / 脊髓"), ("#BFE3C8", "中脑"), ("#8FD1C4", "前脑"),
         ("#4FAE9E", "端脑")]
bx = 0.075
for i, (c, lab) in enumerate(bands):
    w = 0.88 / 4
    ax.add_patch(Rectangle((bx, 0.345), w, 0.115, fc=c, ec="white", lw=1.2, zorder=3))
    ax.text(bx + w / 2, 0.4025, lab, fontsize=7.9, color="#1F4E45", ha="center",
            va="center", zorder=5)
    bx += w
ax.text(0.515, 0.225, "同一群干细胞，凭位置读到不同浓度的信号，\n"
                      "于是分化成不同脑区 —— 24 h 建立体轴，48 h 出现分化标志",
        fontsize=8.4, color="#3C4E60", ha="center", va="center", linespacing=1.8)
arr(ax, (0.515, gy0 - 0.012), (0.515, 0.470), color="#9FB3C4", lw=1.6, ms=12)
ax.text(0.985, 0.845, "微流控的独特贡献：\n把梯度变成可设定、\n可维持、可撤销的“参数”",
        fontsize=8.3, color="#2E7D5B", ha="right", va="center", linespacing=1.9,
        bbox=dict(fc="#EAF7F1", ec="#BFE3DC", boxstyle="round,pad=0.45"))

# ================================================== (c) 合成细胞间信号
ax = fig.add_subplot(gs[1, 0]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
ptitle(ax, "c", "合成细胞间信号：给细胞装一个“如果…就…”", S.CORAL,
       "synNotch 之类的工程受体：一旦接到邻居的信号，就打开指定的黏附分子")

BX, BY, BW2, BH2 = 0.045, 0.360, 0.415, 0.540
for k, (lab, sub) in enumerate([("改造前：混在一起", "两种细胞随机混杂"),
                                ("改造后：自己分层", "黏附差异驱动细胞排序")]):
    x = BX + k * 0.500
    ax.add_patch(FancyBboxPatch((x, BY), BW2, BH2,
                                boxstyle="round,pad=0,rounding_size=0.02",
                                fc="#F7FAFC", ec="#C9D3DD", lw=1.2, zorder=1))
    ax.text(x + BW2 / 2, BY + BH2 + 0.035, lab, fontsize=8.9, color=S.CORAL,
            ha="center", va="center", fontweight="bold")
    ax.text(x + BW2 / 2, BY - 0.030, sub, fontsize=8.0, color=S.GRAY,
            ha="center", va="center")
    if k == 0:
        for i in range(30):
            ax.add_patch(Circle((x + rng.uniform(0.045, BW2 - 0.045),
                                 BY + rng.uniform(0.045, BH2 - 0.045)), 0.021,
                                fc=S.TEAL if i % 2 else S.PINK, ec="white",
                                lw=0.6, zorder=3))
    else:
        ax.add_patch(Circle((x + BW2 / 2, BY + BH2 * 0.42), 0.135, fc=S.TEAL,
                            ec="white", lw=1.2, zorder=3, alpha=.92))
        for a in np.linspace(0, 2 * np.pi, 12, endpoint=False):
            ax.add_patch(Circle((x + BW2 / 2 + 0.185 * np.cos(a),
                                 BY + BH2 * 0.42 + 0.185 * np.sin(a)), 0.021,
                                fc=S.PINK, ec="white", lw=0.6, zorder=4))
arr(ax, (BX + BW2 + 0.012, BY + BH2 / 2), (BX + 0.488, BY + BH2 / 2),
    color=S.CORAL, lw=2.0, ms=13)

# 信号回路小图
ax.text(0.055, 0.195, "信号 →", fontsize=8.2, color=S.CORAL, va="center")
ax.add_patch(FancyBboxPatch((0.145, 0.150), 0.230, 0.090,
                            boxstyle="round,pad=0,rounding_size=0.012",
                            fc="#FFEFEC", ec=S.CORAL, lw=1.1, zorder=2))
ax.text(0.260, 0.195, "受体被切开 → 释放转录因子", fontsize=8.0, color="#8C3A2E",
        ha="center", va="center", zorder=3)
arr(ax, (0.380, 0.195), (0.425, 0.195), color=S.CORAL, lw=1.6, ms=11)
ax.add_patch(FancyBboxPatch((0.430, 0.150), 0.240, 0.090,
                            boxstyle="round,pad=0,rounding_size=0.012",
                            fc="#FFEFEC", ec=S.CORAL, lw=1.1, zorder=2))
ax.text(0.550, 0.195, "开启钙黏蛋白 → 改变黏附", fontsize=8.0, color="#8C3A2E",
        ha="center", va="center", zorder=3)
ax.text(0.985, 0.195, "最简回路\n足以造出多域结构", fontsize=8.2, color=S.CORAL,
        ha="right", va="center", linespacing=1.7)

# ================================================== (d) 组装体
ax = fig.add_subplot(gs[1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
ptitle(ax, "d", "组装体：把几块类器官“焊”成一个回路", S.NAVY,
       "不同脑区 / 不同器官的类器官贴在一起，能长出跨区域的连接")

# 两个类器官
for (cx, cy, c, lab) in [(0.185, 0.640, S.VIOLET, "运动皮层"),
                         (0.185, 0.360, S.TEAL, "脊髓")]:
    ax.add_patch(Circle((cx, cy), 0.098, fc=c, ec="white", lw=1.4, zorder=3, alpha=.85))
    for a in np.linspace(0.4, 2 * np.pi + 0.4, 7, endpoint=False):
        ax.add_patch(Circle((cx + 0.055 * np.cos(a), cy + 0.055 * np.sin(a)), 0.014,
                            fc="white", ec="none", lw=0.6, zorder=4, alpha=.75))
    ax.text(cx - 0.110, cy, lab, fontsize=8.2, color=c, ha="right", va="center")
arr(ax, (0.285, 0.640), (0.300, 0.640), color=S.GRAY, lw=1.5, ms=11)
arr(ax, (0.285, 0.360), (0.300, 0.360), color=S.GRAY, lw=1.5, ms=11)

# 融合体
ax.add_patch(FancyBboxPatch((0.310, 0.265), 0.330, 0.470,
                            boxstyle="round,pad=0,rounding_size=0.05",
                            fc="#F4F8FB", ec="#C9D3DD", lw=1.2, zorder=1))
ax.add_patch(Circle((0.415, 0.595), 0.088, fc=S.VIOLET, ec="white", lw=1.2,
                    zorder=3, alpha=.85))
ax.add_patch(Circle((0.415, 0.410), 0.088, fc=S.TEAL, ec="white", lw=1.2,
                    zorder=3, alpha=.85))
ax.add_patch(Rectangle((0.388, 0.415), 0.054, 0.175, fc="#9B8BE8", ec="none",
                       zorder=2, alpha=.85))
for i in range(5):
    ax.plot([0.395 + i * 0.013, 0.395 + i * 0.013], [0.425, 0.580],
            color="#C0392B", lw=1.2, zorder=4, alpha=.8)
ax.text(0.475, 0.500, "跨区连接\n（轴突长过去）", fontsize=8.0, color="#C0392B",
        ha="left", va="center", linespacing=1.6)
ax.text(0.475, 0.285, "组装体可稳定\n数周以上", fontsize=8.0, color=S.GRAY,
        ha="left", va="center", linespacing=1.6)

# 放电曲线
sx0, sy0, sw, sh = 0.690, 0.400, 0.290, 0.220
ax.add_patch(FancyBboxPatch((sx0, sy0), sw, sh, boxstyle="round,pad=0,rounding_size=0.015",
                            fc="white", ec="#D6E0E9", lw=1.0, zorder=1))
tt = np.linspace(0, 1, 600)
sig = np.zeros_like(tt)
for _ in range(7):
    p = rng.uniform(0.03, 0.95)
    sig += 0.9 * np.exp(-((tt - p) / 0.012) ** 2) * rng.uniform(0.55, 1.0)
ax.plot(sx0 + 0.022 + tt * (sw - 0.044), sy0 + 0.045 + sig * (sh - 0.095),
        color=S.NAVY, lw=1.4, zorder=3)
ax.text(sx0 + sw / 2, sy0 + sh + 0.028, "自发同步放电 = 回路真的接上了",
        fontsize=8.2, color=S.NAVY, ha="center", va="bottom")
ax.text(0.985, 0.870, "进一步：从成人细胞自建\n的“移动生物机器人”\n（Anthrobot，30–500 µm）",
        fontsize=8.1, color=S.VIOLET, ha="right", va="center", linespacing=1.85,
        bbox=dict(fc="#F1EDFF", ec="#DCCFF7", boxstyle="round,pad=0.45"))

# ================================================== 底部要点带
axb = fig.add_subplot(gs[2, :]); axb.set_xlim(0, 1); axb.set_ylim(0, 1); axb.axis("off")
pts = [("反直觉 ①", "细胞球并不真的像液滴：\n表观表面张力更低的细胞球，融合反而更快", S.CORAL),
       ("反直觉 ②", "形态原不必是天然分子：\n只要能被捕获限漏，惰性蛋白 GFP 也能当形态原", S.VIOLET),
       ("反直觉 ③", "微流控的贡献不是“更好的培养皿”，\n而是提供体轴与位置信息", S.NAVY)]
for i, (tag, txt, c) in enumerate(pts):
    x = 0.008 + i * 0.332
    axb.add_patch(FancyBboxPatch((x, 0.08), 0.322, 0.84,
                                 boxstyle="round,pad=0,rounding_size=0.02",
                                 fc="#F7FAFC", ec="#D6E0E9", lw=1.0, zorder=1))
    axb.add_patch(Rectangle((x, 0.08), 0.008, 0.84, fc=c, ec="none", zorder=2))
    axb.text(x + 0.028, 0.72, tag, fontsize=9.2, color=c, fontweight="bold",
             va="center", zorder=3)
    axb.text(x + 0.028, 0.36, txt, fontsize=8.3, color="#3C4E60", va="center",
             linespacing=1.8, zorder=3)

S.save(fig, "figures/fig05_morphogenesis.png")
