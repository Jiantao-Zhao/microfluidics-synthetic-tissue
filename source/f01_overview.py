# -*- coding: utf-8 -*-
"""图1：微流控合成组织的总体流水线 —— 微流控处在哪一环"""
import numpy as np
import figstyle as S
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch, Ellipse
from matplotlib.lines import Line2D

plt = S.plt
fig, ax = plt.subplots(figsize=(13.2, 7.6))
ax.set_xlim(0, 132); ax.set_ylim(0, 64); ax.axis("off")

def box(x, y, w, h, fc, ec, lw=1.6, r=1.6, z=2):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec, lw=lw, zorder=z))

def arrow(x1, y1, x2, y2, color="#8FA3B5", lw=2.2, style="-|>", ms=14, z=3):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle=style,
                                 mutation_scale=ms, lw=lw, color=color, zorder=z,
                                 shrinkA=0, shrinkB=0))

def head(x, y, text, color, size=11.5):
    ax.text(x, y, text, ha="center", va="center", fontsize=size,
            color=color, fontweight="bold", zorder=6)

def note(x, y, text, color="#4A5C6E", size=9.2, ha="center", style="normal"):
    ax.text(x, y, text, ha=ha, va="center", fontsize=size, color=color,
            zorder=6, style=style)

# ============ 顶部标题条 ============
ax.text(1.5, 62.4, "微流控合成组织：一条“芯片上的装配线”", fontsize=16.5,
        color=S.NAVY, fontweight="bold", va="center")
ax.text(1.5, 59.5, "Microfluidics for synthetic tissues — 从细胞与材料，到可灌注的功能组织",
        fontsize=10.2, color=S.GRAY, va="center")

# ============ 核心逻辑带：为什么是微流控 ============
KEY = [
    ("尺度对上了", "通道 10–500 µm，与单个细胞（10–20 µm）同量级\n→ 可以在“细胞的那把尺子”上设计结构", S.NAVY),
    ("流态听你的", "Re ≪ 1 的层流：不同液体并排走不打混\n→ 界面位置、浓度梯度、剪切力都可编程", S.TEAL),
    ("组织自己会组装", "芯片只提供“条件”，细胞靠黏附与自组织\n→ 自下而上长出有序结构", S.CORAL),
]
kx = 2.0; kw = 41.6; kgap = 2.0
for i, (t, d, c) in enumerate(KEY):
    X = kx + i * (kw + kgap)
    box(X, 48.6, kw, 9.4, "#F4F8FB", "#D6E0E9", lw=1.1, r=1.2, z=1)
    ax.add_patch(Rectangle((X, 48.6), 0.8, 9.4, fc=c, ec="none", zorder=2))
    ax.text(X + 2.2, 55.3, t, fontsize=11.0, color=c, fontweight="bold",
            va="center", zorder=6)
    ax.text(X + 2.2, 51.6, d, fontsize=8.8, color="#3C4E60", va="center",
            zorder=6, linespacing=1.6)

# ============ 六个阶段 ============
Y, H, W = 20.5, 22.0, 15.4
xs = [2.0, 21.0, 40.0, 59.0, 78.0, 97.0, 116.0]
labels = ["① 细胞来源", "② 生物材料", "③ 微流控加工", "④ 组装 / 融合", "⑤ 成熟 / 灌流", "⑥ 合成组织"]
subs = ["iPSC · 原代细胞\n细胞系 · 共培养",
        "GelMA · 海藻酸\n胶原 · 脱细胞 ECM",
        "芯片尺度上的\n流体与界面控制",
        "模块拼接\n细胞自排序",
        "力学刺激\n营养与氧供给",
        "可灌注、有功能\n可测、可移植"]
cols = [S.TEAL, S.AMBER, S.NAVY, S.VIOLET, S.GREEN, S.CORAL]
fcs = ["#E7F7F4", "#FDF3E2", "#E8EEF4", "#F1EDFF", "#EAF7F1", "#FFEFEC"]

BW = 13.6
for i, x in enumerate(xs[:6]):
    box(x, Y, BW, H, fcs[i], cols[i], lw=1.8)
    # 顶部色条
    ax.add_patch(Rectangle((x + 0.9, Y + H - 1.5), BW - 1.8, 1.0,
                           fc=cols[i], ec="none", zorder=4))
    head(x + BW / 2, Y + H - 4.2, labels[i], cols[i], 11.5)
    note(x + BW / 2, Y + H - 9.0, subs[i], "#3C4E60", 8.9)

# 箭头
for i in range(5):
    arrow(xs[i] + BW + 0.35, Y + H / 2, xs[i + 1] - 0.35, Y + H / 2)

# ============ 各阶段内的小插画 ============
np.random.seed(7)

# ① 细胞
cx0 = xs[0] + BW / 2
for (dx, dy, c) in [(-2.6, 3.2, S.TEAL), (0.2, 4.0, S.PINK), (2.7, 3.0, S.GREEN),
                    (-1.4, 6.0, S.AMBER), (1.6, 6.2, S.VIOLET), (2.9, 6.1, S.TEAL)]:
    ax.add_patch(Circle((cx0 + dx, Y + dy), 1.05, fc=c, ec="white", lw=1.0, zorder=5, alpha=.92))

# ② 材料网络
cx1 = xs[1] + BW / 2
ax.add_patch(FancyBboxPatch((cx1 - 4.0, Y + 2.6), 8.0, 5.6,
                            boxstyle="round,pad=0,rounding_size=2.0",
                            fc="#F6D9A0", ec=S.AMBER, lw=1.4, zorder=4))
rng = np.random.default_rng(3)
for _ in range(16):
    a = rng.uniform(0, np.pi); b = rng.uniform(0, np.pi)
    x1 = cx1 + rng.uniform(-3.4, 3.4); y1 = Y + 3.2 + rng.uniform(0, 4.4)
    ax.plot([x1, x1 + 1.7 * np.cos(a)], [y1, y1 + 1.7 * np.sin(a)],
            color="#B87C1E", lw=0.9, zorder=5, alpha=.85)

# ③ 芯片
cx2 = xs[2] + BW / 2
box(cx2 - 5.1, Y + 2.4, 10.2, 6.2, "#DCE6EF", S.NAVY, lw=1.5, r=1.1, z=4)
ax.plot([cx2 - 5.1, cx2 - 2.6], [Y + 5.5, Y + 5.5], color=S.NAVY, lw=1.6, zorder=5)
for k in range(3):
    yy = Y + 3.9 + k * 1.6
    ax.plot([cx2 - 2.6, cx2 + 2.2], [Y + 5.5, yy], color=S.NAVY, lw=1.5, zorder=5)
    ax.plot([cx2 + 2.2, cx2 + 5.1], [yy, yy], color=S.NAVY, lw=1.6, zorder=5)
ax.add_patch(Circle((cx2 - 5.5, Y + 5.5), 0.8, fc=S.CORAL, ec="none", zorder=6))

# ④ 组装
cx3 = xs[3] + BW / 2
for k in range(4):
    ax.add_patch(FancyBboxPatch((cx3 - 4.2 + k * 0.9, Y + 2.6 + k * 1.25), 3.0, 1.05,
                                boxstyle="round,pad=0,rounding_size=0.5",
                                fc=[S.TEAL, S.PINK, S.VIOLET, S.GREEN][k],
                                ec="white", lw=0.9, zorder=4 + k, alpha=.9))

# ⑤ 灌流
cx4 = xs[4] + BW / 2
ax.add_patch(FancyBboxPatch((cx4 - 4.6, Y + 4.0), 9.2, 4.6,
                            boxstyle="round,pad=0,rounding_size=1.6",
                            fc="#D7EFE3", ec=S.GREEN, lw=1.4, zorder=4))
for k in range(3):
    yy = Y + 5.0 + k * 1.3
    ax.annotate("", xy=(cx4 + 3.7, yy), xytext=(cx4 - 3.7, yy),
                arrowprops=dict(arrowstyle="-|>", color=S.GREEN, lw=1.5,
                                mutation_scale=9), zorder=5)
ax.text(cx4, Y + 2.3, "流动 = 氧气 + 营养 + 剪切", ha="center", va="center",
        fontsize=7.6, color="#2E7D5B", zorder=6)

# ⑥ 合成组织
cx5 = xs[5] + BW / 2
ax.add_patch(FancyBboxPatch((cx5 - 4.6, Y + 2.4), 9.2, 5.8,
                            boxstyle="round,pad=0,rounding_size=2.2",
                            fc="#FFDCD5", ec=S.CORAL, lw=1.5, zorder=4))
ax.plot([cx5, cx5], [Y + 7.6, Y + 4.2], color="#C0392B", lw=2.2, zorder=5,
        solid_capstyle="round")
ax.plot([cx5, cx5 - 2.6], [Y + 5.6, Y + 3.4], color="#C0392B", lw=1.6, zorder=5,
        solid_capstyle="round")
ax.plot([cx5, cx5 + 2.6], [Y + 5.6, Y + 3.4], color="#C0392B", lw=1.6, zorder=5,
        solid_capstyle="round")
for (dx, dy) in [(-3.0, 6.6), (3.0, 6.6), (0, 2.9), (-3.2, 3.0), (3.2, 3.0)]:
    ax.add_patch(Circle((cx5 + dx, Y + dy), 0.85, fc=S.PINK, ec="white",
                        lw=0.8, zorder=6, alpha=.9))

# ============ 中间放大带：四条技术路线 ============
BY = 6.6
box(1.6, BY - 1.4, 128.8, 13.0, "#F7FAFC", "#C9D3DD", lw=1.2, r=1.2, z=1)
ax.text(3.4, BY + 9.6, "微流控提供的四把“工具”", fontsize=10.6,
        color=S.NAVY, fontweight="bold", va="center", zorder=6)

tools = [
    ("微流控纺丝", "层流共轴 → 核壳 / 中空纤维", S.AMBER, "纤维、血管、肌束"),
    ("液滴 / 微凝胶", "每秒数千个均一液滴 → 模块", S.VIOLET, "细胞球、类器官积木"),
    ("微流控生物打印", "按图逐点 / 逐层（或体积）沉积", S.TEAL, "任意 3D 构型"),
    ("器官芯片", "灌流 + 力学 + 梯度 的 3D 培养腔", S.NAVY, "可测功能的微器官"),
]
tw, gap = 30.0, 2.1
x0 = 3.0
for i, (t, d, c, tag) in enumerate(tools):
    X = x0 + i * (tw + gap)
    box(X, BY, tw, 8.2, "white", c, lw=1.5, r=1.1, z=3)
    ax.add_patch(Rectangle((X, BY), 0.75, 8.2, fc=c, ec="none", zorder=4))
    ax.text(X + 2.0, BY + 6.3, t, fontsize=10.6, color=c, fontweight="bold",
            va="center", zorder=6)
    ax.text(X + 2.0, BY + 4.1, d, fontsize=8.6, color="#3C4E60", va="center", zorder=6)
    ax.text(X + 2.0, BY + 1.7, "→ " + tag, fontsize=8.6, color=c, va="center",
            zorder=6, style="italic")

# 工具带 → 阶段③ 的单条连接（避免扇形交叉线）
ax.add_patch(FancyArrowPatch((xs[2] + BW / 2, BY + 8.5), (xs[2] + BW / 2, Y - 0.55),
                             arrowstyle="-|>", mutation_scale=17, lw=2.4,
                             color=S.NAVY, zorder=3, shrinkA=0, shrinkB=0))
ax.text(xs[2] + BW / 2 + 1.4, (BY + 8.5 + Y) / 2, "即下方四种加工方式",
        fontsize=8.6, color=S.NAVY, va="center", ha="left", zorder=6,
        bbox=dict(fc="white", ec="none", pad=1.2))

# 底部注释
ax.text(66, 2.3, "所有路线共享同一个物理前提：微米尺度下 Re ≪ 1 的层流世界 —— 流体不打混、界面可设计、传质靠扩散。",
        ha="center", va="center", fontsize=9.0, color=S.GRAY, style="italic")

S.save(fig, "figures/fig01_overview.png")
