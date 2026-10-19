# -*- coding: utf-8 -*-
"""图4：血管化 —— 合成组织的“最后一公里”"""
import numpy as np
import figstyle as S
from matplotlib.patches import (FancyBboxPatch, Rectangle, Circle, Polygon,
                                FancyArrowPatch, Ellipse)

plt = S.plt
fig = plt.figure(figsize=(13.6, 9.0))
gs = fig.add_gridspec(2, 3, hspace=0.34, wspace=0.14,
                      left=0.028, right=0.978, top=0.885, bottom=0.045)


def ptitle(ax, tag, title, color, sub=None):
    ax.text(0.0, 1.14, tag, transform=ax.transAxes, fontsize=14.5,
            fontweight="bold", color=color, va="bottom")
    ax.text(0.068, 1.135, title, transform=ax.transAxes, fontsize=11.8,
            fontweight="bold", color=color, va="bottom")
    if sub:
        ax.text(0.0, 1.022, sub, transform=ax.transAxes, fontsize=8.7,
                color=S.GRAY, va="bottom")


def newax(r, c):
    a = fig.add_subplot(gs[r, c]); a.set_xlim(0, 1); a.set_ylim(0, 1); a.axis("off")
    return a


def arr(ax, p1, p2, color="#8FA3B5", lw=1.6, ms=12, z=6, style="-|>"):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=ms,
                                 lw=lw, color=color, zorder=z, shrinkA=0, shrinkB=0))


# ================================================== (a) 问题：没有血管就没有厚度
ax = newax(0, 0)
ptitle(ax, "a", "问题：没有血管，组织就长不厚", S.CORAL,
       "氧只能靠扩散走 ≤ 200 µm —— 再往里，细胞开始窒息")

sx, sy, sR = 0.315, 0.575, 0.290
ax.add_patch(Circle((sx, sy), sR, fc="#FFD9D2", ec=S.CORAL, lw=1.6, zorder=2))
ax.add_patch(Circle((sx, sy), sR * 0.70, fc="#FBE3B8", ec="#E8B24A", lw=1.4, zorder=3))
ax.add_patch(Circle((sx, sy), sR * 0.365, fc="#E9A79C", ec="#C0392B", lw=1.4, zorder=4))
ax.text(sx, sy, "坏死\n核心", ha="center", va="center", fontsize=8.0,
        color="#7B241C", fontweight="bold", zorder=6, linespacing=1.4)
ax.text(sx, sy + sR * 0.845, "增殖层", ha="center", va="center", fontsize=8.2,
        color="#B03A2E", fontweight="bold", zorder=6)
ax.text(sx, sy + sR * 0.52, "静息层", ha="center", va="center", fontsize=8.0,
        color="#A9761A", zorder=6)
arr(ax, (sx + sR * 0.72, sy + sR * 0.72), (0.965, 0.965), color=S.CORAL, lw=1.4, ms=10)
ax.text(0.965, 0.985, "半径 > 200 µm\n核心就缺氧", fontsize=8.2, color="#C0392B",
        ha="right", va="bottom", linespacing=1.5, fontweight="bold")
ax.text(sx, 0.185, "细胞球（spheroid）的经典剖面", fontsize=8.4, color="#3C4E60",
        ha="center", va="center")

# 小插图：氧浓度剖面
bx0, bw = 0.585, 0.375
ax.add_patch(FancyBboxPatch((bx0, 0.235), bw, 0.50, boxstyle="round,pad=0,rounding_size=0.02",
                            fc="#F7FAFC", ec="#D6E0E9", lw=1.0, zorder=1))
rr = np.linspace(0, 1, 100)
po2 = np.clip(1 - (1 - rr) ** 0.55 * 1.0, 0, 1)
Xs = bx0 + 0.055 + rr * (bw - 0.09)
Ys = 0.30 + po2 * 0.36
ax.plot(Xs, Ys, color=S.NAVY, lw=2.4, zorder=4)
ax.fill_between(Xs, 0.30, Ys, color="#BBD9EE", alpha=.45, zorder=2)
ax.plot([Xs[0], Xs[-1]], [0.30, 0.30], color="#9FB3C4", lw=1.1, zorder=3)
ax.plot([Xs[0], Xs[0]], [0.30, 0.70], color="#9FB3C4", lw=1.1, zorder=3)
ax.add_patch(Rectangle((Xs[0], 0.30), 0.30 * (bw - 0.09), 0.40, fc=S.CORAL,
                       alpha=.10, ec="none", zorder=0))
ax.text(Xs[0] + 0.015, 0.335, "缺氧区", fontsize=7.8, color="#C0392B", va="bottom")
ax.text(bx0 + bw / 2, 0.685, "氧分压随深度下降", fontsize=8.2, color=S.NAVY,
        ha="center", va="center")
ax.text(bx0 + 0.028, 0.268, "核心", fontsize=7.6, color=S.GRAY, ha="left", va="top")
ax.text(bx0 + bw - 0.028, 0.268, "表面", fontsize=7.6, color=S.GRAY, ha="right", va="top")
ax.text(bx0 + bw / 2, 0.155, "氧供给靠扩散、消耗靠代谢：\n两者平衡的位置就是“能活多厚”的上限",
        fontsize=8.3, color="#3C4E60", ha="center", va="center", linespacing=1.7)

# ================================================== (b) 自组装
ax = newax(0, 1)
ptitle(ax, "b", "策略一：让内皮细胞自己长血管", S.TEAL,
       "血管发生（vasculogenesis）+ 血管新生（angiogenesis）")

ax.add_patch(FancyBboxPatch((0.045, 0.24), 0.91, 0.62,
                            boxstyle="round,pad=0,rounding_size=0.025",
                            fc="#EAF7F1", ec=S.GREEN, lw=1.3, zorder=1))
rng = np.random.default_rng(5)
gx = np.linspace(0.135, 0.865, 5)
gy = np.linspace(0.335, 0.775, 4)
nodes = {}
for i, xv in enumerate(gx):
    for j, yv in enumerate(gy):
        nodes[(i, j)] = (xv + rng.uniform(-0.022, 0.022),
                         yv + rng.uniform(-0.022, 0.022))
for (i, j), (x1, y1) in nodes.items():
    for di, dj in ((1, 0), (0, 1)):
        if (i + di, j + dj) in nodes:
            x2, y2 = nodes[(i + di, j + dj)]
            ax.plot([x1, x2], [y1, y2], color="#C0392B", lw=rng.uniform(2.0, 3.4),
                    zorder=3, alpha=.85, solid_capstyle="round")
    if i < 4 and j < 3 and rng.random() < 0.30:
        x2, y2 = nodes[(i + 1, j + 1)]
        ax.plot([x1, x2], [y1, y2], color="#C0392B", lw=rng.uniform(1.3, 2.0),
                zorder=3, alpha=.65, solid_capstyle="round")
for (x1, y1) in nodes.values():
    ax.add_patch(Circle((x1, y1), 0.016, fc=S.PINK, ec="white", lw=0.6, zorder=4))
ax.plot([0.075, nodes[(0, 1)][0]], [0.55, nodes[(0, 1)][1]], color="#C0392B",
        lw=3.4, zorder=3, solid_capstyle="round")
# 灌注入口
arr(ax, (0.020, 0.55), (0.070, 0.55), color="#C0392B", lw=3.0, ms=15, z=5)
ax.text(0.075, 0.475, "与宿主血管接通", fontsize=8.0, color="#C0392B", ha="center", va="top")
ax.text(0.50, 0.185, "优点：全生物、可长成毛细血管级（5–10 µm）\n"
                     "难点：随机、慢、无法保证连到灌注源",
        fontsize=8.4, color="#3C4E60", ha="center", va="center", linespacing=1.8)

# ================================================== (c) 模板法
ax = newax(0, 2)
ptitle(ax, "c", "策略二：先用“模板”占位，再抽掉", S.VIOLET,
       "牺牲模板 / 3D 打印血管网 —— 血管位置由设计图决定")

for k, (bx, lab) in enumerate([(0.045, "① 打印可溶模板"), (0.520, "② 抽掉模板 + 种内皮")]):
    ax.add_patch(FancyBboxPatch((bx, 0.34), 0.435, 0.50,
                                boxstyle="round,pad=0,rounding_size=0.02",
                                fc="#F1EDFF" if k == 0 else "#FFE9E4",
                                ec=S.VIOLET if k == 0 else S.CORAL, lw=1.3, zorder=1))
    ax.text(bx + 0.2175, 0.905, lab, fontsize=8.6,
            color=S.VIOLET if k == 0 else S.CORAL, ha="center", va="center",
            fontweight="bold")
    cx, cy = bx + 0.2175, 0.585
    for (dx, dy, w, h) in [(0, 0, 0.30, 0.055), (-0.085, -0.105, 0.055, 0.16),
                           (0.085, -0.105, 0.055, 0.16), (0, 0.115, 0.055, 0.14)]:
        if k == 0:
            ax.add_patch(Rectangle((cx + dx - w / 2, cy + dy - h / 2), w, h,
                                   fc="#C0392B", ec="none", zorder=3))
        else:
            ax.add_patch(Rectangle((cx + dx - w / 2, cy + dy - h / 2), w, h,
                                   fc="#FFD3CB", ec="#C0392B", lw=1.2, zorder=3))
            if w > h:
                ax.plot([cx + dx - w / 2 + 0.012, cx + dx + w / 2 - 0.012],
                        [cy + dy + h / 2 - 0.011, cy + dy + h / 2 - 0.011],
                        color=S.PINK, lw=2.0, zorder=5)
                ax.plot([cx + dx - w / 2 + 0.012, cx + dx + w / 2 - 0.012],
                        [cy + dy - h / 2 + 0.011, cy + dy - h / 2 + 0.011],
                        color=S.PINK, lw=2.0, zorder=5)
            else:
                ax.plot([cx + dx + w / 2 - 0.011, cx + dx + w / 2 - 0.011],
                        [cy + dy - h / 2 + 0.012, cy + dy + h / 2 - 0.012],
                        color=S.PINK, lw=2.0, zorder=5)
                ax.plot([cx + dx - w / 2 + 0.011, cx + dx - w / 2 + 0.011],
                        [cy + dy - h / 2 + 0.012, cy + dy + h / 2 - 0.012],
                        color=S.PINK, lw=2.0, zorder=5)
arr(ax, (0.485, 0.585), (0.515, 0.585), color=S.GRAY, lw=1.8, ms=12)
ax.text(0.50, 0.240, "优点：血管位置、直径、分支可精确设计\n"
                     "难点：模板必须对细胞无毒、能被完全清掉",
        fontsize=8.4, color="#3C4E60", ha="center", va="center", linespacing=1.8)

# ================================================== (d) 芯片法
ax = newax(1, 0)
ptitle(ax, "d", "策略三：器官芯片里的跨膜血管床", S.NAVY,
       "把“血管侧”和“组织侧”做成两条可独立灌流的通道")

CX, CY, CW, CH = 0.075, 0.30, 0.85, 0.55
ax.add_patch(FancyBboxPatch((CX, CY), CW, CH, boxstyle="round,pad=0,rounding_size=0.02",
                            fc="#E9EEF3", ec="#8FA3B5", lw=1.3, zorder=1))
yU, yL, mh = CY + 0.360, CY + 0.175, 0.070
ax.add_patch(Rectangle((CX + 0.035, yU - mh / 2), CW - 0.07, mh, fc="#FFE4DE",
                       ec="none", zorder=3))
for i in range(12):
    ax.add_patch(Circle((CX + 0.075 + i * 0.062, yU + mh / 2 - 0.010), 0.016,
                        fc="#C0392B", ec="white", lw=0.5, zorder=4))
ax.text(CX + CW / 2, yU + 0.062, "血管侧：内皮细胞铺成管腔 → 可灌注全血 / 培养液",
        fontsize=8.1, color="#C0392B", ha="center", va="center")
ax.add_patch(Rectangle((CX + 0.035, yL - mh / 2), CW - 0.07, mh, fc="#D9EEF7",
                       ec="none", zorder=3))
for i in range(12):
    ax.add_patch(Circle((CX + 0.075 + i * 0.062, yL - mh / 2 + 0.010), 0.016,
                        fc=S.TEAL, ec="white", lw=0.5, zorder=4))
ax.text(CX + CW / 2, yL - 0.062, "组织侧：上皮 / 肝细胞 / 肿瘤等目标细胞",
        fontsize=8.1, color="#0E7C70", ha="center", va="center")
ax.plot([CX + 0.035, CX + CW - 0.035], [CY + 0.268, CY + 0.268], color="#7A8A99",
        lw=2.2, zorder=5, ls=(0, (4, 2)))
ax.text(CX + CW / 2, CY + 0.280, "多孔膜：细胞可跨膜互访，血管不会“漏”过去",
        fontsize=7.9, color="#4A5C6E", ha="center", va="bottom", zorder=6)
for yy in (yU, yL):
    arr(ax, (CX + 0.008, yy), (CX + 0.062, yy), color=S.NAVY, lw=1.8, ms=11, z=6)
    arr(ax, (CX + CW - 0.008, yy), (CX + CW - 0.150, yy), color=S.NAVY, lw=1.8, ms=11, z=6)
ax.text(0.50, 0.205, "这是目前最能“同时管住两种细胞 + 灌流 + 读数”的方案",
        fontsize=8.4, color="#3C4E60", ha="center", va="center")

# ================================================== (e) 纺丝法
ax = newax(1, 1)
ptitle(ax, "e", "策略四：纺出中空纤维当血管", S.AMBER,
       "共轴纺丝直接做中空 / 多腔纤维，本身就是一根可灌注的管子")

for k in range(3):
    yy = 0.75 - k * 0.155
    ax.add_patch(Rectangle((0.075, yy - 0.055), 0.72, 0.110, fc="#F3E2BE",
                           ec="#B87C1E", lw=1.3, zorder=2))
    ax.add_patch(Rectangle((0.095, yy - 0.032), 0.680, 0.064, fc="#FFF6E4",
                           ec="#E8B24A", lw=1.0, zorder=3))
    for i in range(9):
        ax.add_patch(Circle((0.135 + i * 0.076, yy + 0.032), 0.0105, fc=S.PINK,
                            ec="white", lw=0.5, zorder=5))
        ax.add_patch(Circle((0.135 + i * 0.076, yy - 0.032), 0.0105, fc=S.PINK,
                            ec="white", lw=0.5, zorder=5))
arr(ax, (0.030, 0.750), (0.190, 0.750), color="#C0392B", lw=2.6, ms=14, z=6)
ax.text(0.030, 0.815, "灌注", fontsize=8.2, color="#C0392B", ha="left", va="center")
ax.text(0.795, 0.845, "管腔", fontsize=8.0, color="#B87C1E", ha="left", va="center")
ax.text(0.50, 0.190, "优点：管腔尺寸由模具/流速决定，天然可灌注、可并行排布\n"
                     "难点：分支与逐级变细仍难，管壁厚度限制氧气外送",
        fontsize=8.4, color="#3C4E60", ha="center", va="center", linespacing=1.8)

# ================================================== (f) 对比表
ax = newax(1, 2)
ptitle(ax, "f", "五条路线怎么选？", S.NAVY, "以“血管直径 / 可灌注性 / 可及厚度”三把尺子衡量")
rows = [
    ("自组装", "5–50 µm", "需再接通", "≤ 1 mm", S.TEAL),
    ("牺牲模板", "50–500 µm", "直接可灌注", "数 mm", S.VIOLET),
    ("跨膜血管床", "5–50 µm", "芯片内灌注", "≤ 1 mm", S.NAVY),
    ("中空纤维", "100–1000 µm", "直接可灌注", "纤维束级", S.AMBER),
    ("器官级血管树", "10 µm–1 mm", "多级可灌注", "厘米级", S.CORAL),
]
ytop, rh = 0.845, 0.128
ax.text(0.020, ytop + 0.075, "路线", fontsize=8.4, color=S.GRAY, fontweight="bold")
ax.text(0.285, ytop + 0.075, "血管直径", fontsize=8.4, color=S.GRAY, fontweight="bold")
ax.text(0.520, ytop + 0.075, "可灌注性", fontsize=8.4, color=S.GRAY, fontweight="bold")
ax.text(0.780, ytop + 0.075, "可及厚度", fontsize=8.4, color=S.GRAY, fontweight="bold")
for i, (a, b, c, d, col) in enumerate(rows):
    y = ytop - i * rh
    ax.add_patch(Rectangle((0.012, y - 0.045), 0.976, 0.090,
                           fc="#F7FAFC" if i % 2 == 0 else "white", ec="none", zorder=1))
    ax.add_patch(Rectangle((0.012, y - 0.045), 0.008, 0.090, fc=col, ec="none", zorder=2))
    ax.text(0.030, y, a, fontsize=8.5, color=col, va="center", fontweight="bold", zorder=3)
    ax.text(0.285, y, b, fontsize=8.3, color="#3C4E60", va="center", zorder=3)
    ax.text(0.520, y, c, fontsize=8.3, color="#3C4E60", va="center", zorder=3)
    ax.text(0.780, y, d, fontsize=8.3, color="#3C4E60", va="center", zorder=3)
ax.text(0.5, 0.115, "现实做法通常是组合拳：先用模板/纤维搭出主干，\n"
                    "再让内皮细胞自己把毛细血管补满。",
        ha="center", va="center", fontsize=8.5, color=S.NAVY, linespacing=1.8,
        bbox=dict(fc="#EEF3F7", ec="#D6E0E9", boxstyle="round,pad=0.45"))

S.save(fig, "figures/fig04_vascular.png")
