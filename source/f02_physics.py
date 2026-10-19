# -*- coding: utf-8 -*-
"""图2：微流控的四条“物理杠杆”——层流、梯度、液滴、扩散尺度"""
import numpy as np
import figstyle as S
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, Polygon
from matplotlib.colors import to_rgb

plt = S.plt
fig = plt.figure(figsize=(13.4, 8.8))
gs = fig.add_gridspec(2, 2, hspace=0.34, wspace=0.19,
                      left=0.035, right=0.975, top=0.895, bottom=0.055)

def panel_title(ax, tag, title, sub):
    ax.text(0.0, 1.11, tag, transform=ax.transAxes, fontsize=15,
            fontweight="bold", color=S.NAVY, va="bottom")
    ax.text(0.062, 1.105, title, transform=ax.transAxes, fontsize=12.4,
            fontweight="bold", color=S.NAVY, va="bottom")
    ax.text(0.0, 1.012, sub, transform=ax.transAxes, fontsize=8.9,
            color=S.GRAY, va="bottom")

# ============================================================ (a) 层流
ax = fig.add_subplot(gs[0, 0]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
panel_title(ax, "a", "层流：并排走，不打架",
            "Re = ρvL/μ ≪ 1 → 黏性主导，流线彼此平行，两股液体只能靠扩散“认识”")

TEAL_L, AMBER_L = "#9FD9CF", "#F3D69B"
# 两股入口
ax.add_patch(Polygon([(0.03, 0.50), (0.30, 0.50), (0.38, 0.48), (0.38, 0.66),
                     (0.30, 0.62), (0.03, 0.62)],
                     fc=TEAL_L, ec="#8FA3B5", lw=1.2, zorder=2))
ax.add_patch(Polygon([(0.03, 0.34), (0.30, 0.34), (0.38, 0.30), (0.38, 0.48),
                     (0.30, 0.46), (0.03, 0.46)],
                     fc=AMBER_L, ec="#8FA3B5", lw=1.2, zorder=2))
# 汇合主通道（扩散混合场）
nx, ny = 300, 160
Xf = np.linspace(0, 1, nx); Yc = np.linspace(0, 1, ny)
w = 0.012 + 0.330 * Xf ** 1.55
frac = 0.5 * (1 + np.tanh((Yc[None, :] - 0.5) / w[:, None]))     # (nx, ny)
c1 = np.array(to_rgb(S.TEAL)); c2 = np.array(to_rgb("#E8B24A"))
img = (frac[..., None] * c1 + (1 - frac[..., None]) * c2).transpose(1, 0, 2)
ax.imshow(img, extent=(0.38, 0.965, 0.30, 0.66), origin="lower",
          aspect="auto", zorder=3, interpolation="bilinear")
ax.add_patch(Polygon([(0.38, 0.30), (0.965, 0.30), (0.965, 0.66), (0.38, 0.66)],
                     fc="none", ec="#8FA3B5", lw=1.6, zorder=4))
ax.annotate("", xy=(0.95, 0.78), xytext=(0.40, 0.78),
            arrowprops=dict(arrowstyle="-|>", color=S.NAVY, lw=1.5, mutation_scale=12))
ax.text(0.675, 0.825, "流动方向", ha="center", fontsize=9, color=S.NAVY)
ax.text(0.155, 0.575, "液体 A", ha="center", fontsize=9, color="#0E7C70")
ax.text(0.155, 0.375, "液体 B", ha="center", fontsize=9, color="#A9761A")
ax.text(0.675, 0.215, "混合带宽度 ∝ √(D·t)：界面只会变模糊，永远不会被“搅开”",
        ha="center", fontsize=9.1, color="#3C4E60")
ax.text(0.985, 0.48, "混合带", ha="left", fontsize=8.2, color=S.GRAY, va="center")
ax.text(0.03, 0.905, "典型值：通道 100 µm、流速 1 mm/s、水 —— Re ≈ 0.1（粘性完全统治）",
        fontsize=8.9, color=S.NAVY, va="center",
        bbox=dict(fc="#F4F8FB", ec="#D6E0E9", boxstyle="round,pad=0.4"))

# ============================================================ (b) 圣诞树梯度发生器
ax = fig.add_subplot(gs[0, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
panel_title(ax, "b", "梯度发生器：把浓度“劈”成一把尺",
            "网络里反复做 1:1 合并，出口就得到等间距的浓度阶梯（Whitesides 组经典设计）")

stages = [
    (0.045, [0.560, 0.440]),
    (0.275, [0.620, 0.500, 0.380]),
    (0.505, [0.680, 0.560, 0.440, 0.320]),
    (0.735, [0.740, 0.620, 0.500, 0.380, 0.260]),
]
for k in range(len(stages) - 1):
    xa, ya = stages[k]; xb, yb = stages[k + 1]
    for i, yv in enumerate(ya):
        for j in (i, i + 1):
            if j < len(yb):
                ax.plot([xa, xb], [yv, yb[j]], color="#9FB3C4", lw=1.35,
                        zorder=1, solid_capstyle="round")
# 入口标注
ax.text(0.028, 0.560, "缓冲液", fontsize=8.8, color=S.NAVY, ha="right", va="center")
ax.text(0.028, 0.440, "样品", fontsize=8.8, color=S.NAVY, ha="right", va="center")
for yv in stages[0][1]:
    ax.plot([0.028, 0.045], [yv, yv], color="#9FB3C4", lw=1.6, zorder=1)
# 出口
ramp = ["#EFF6F4", "#C8E5DF", "#9BD3C8", "#54B7A8", "#0E7C70"]
xl = stages[-1][0]
for yv, c in zip(stages[-1][1], ramp):
    ax.plot([xl, 0.955], [yv, yv], color=c, lw=7.0, solid_capstyle="butt", zorder=3)
for yv, lab in zip(stages[-1][1], ["0", "25%", "50%", "75%", "100%"]):
    ax.text(0.972, yv, lab, fontsize=8.5, color="#3C4E60", va="center", ha="left")
ax.text(0.50, 0.135, "一次实验 = 一整条浓度谱；再叠一维流速就得到“浓度 × 时间”图谱。\n"
                     "它同时是形态原梯度实验的标准工具（见后文“合成形态发生”）。",
        ha="center", fontsize=9.0, color="#3C4E60", linespacing=1.75)
ax.text(0.50, 0.045, "示意图：实际器件的流道长度与混合蛇形段经过专门设计，以保证出口等间距",
        ha="center", fontsize=8.0, color=S.GRAY, style="italic")

# ============================================================ (c) 液滴三构型
ax = fig.add_subplot(gs[1, 0]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
panel_title(ax, "c", "液滴：把“一口反应器”缩到皮升级",
            "连续相把分散相剪断 → 单分散液滴；尺寸由流量比与毛细数 Ca = μv/γ 决定")

CW, CH, BY = 0.288, 0.47, 0.36
X1, X2, X3 = 0.030, 0.356, 0.682
CONT, DISP = "#BFDCEC", "#F0CE86"
DR = "#E8B24A"; DRE = "#B87C1E"
BM = 0.030                                    # 主通道半高

def frame(X, lab):
    ax.add_patch(FancyBboxPatch((X, BY), CW, CH, boxstyle="round,pad=0,rounding_size=0.012",
                                fc="#F7FAFC", ec="#C9D3DD", lw=1.1, zorder=0))
    ax.text(X + CW / 2, BY - 0.045, lab, ha="center", fontsize=9.8,
            color=S.NAVY, fontweight="bold")

def droplets(x0, y, n=4, step=0.043, r=0.0195):
    for i in range(n):
        ax.add_patch(Circle((x0 + i * step, y), r, fc=DR, ec=DRE, lw=0.7, zorder=4))

# --- T 型 ---
frame(X1, "T 型接头")
yC = BY + CH * 0.66
ax.add_patch(Rectangle((X1 + 0.022, yC - BM), CW - 0.044, 2 * BM, fc=CONT, ec="none", zorder=2))
ax.add_patch(Rectangle((X1 + 0.022, BY + 0.055), 0.034, yC - BM - (BY + 0.055),
                       fc=DISP, ec="none", zorder=2))
droplets(X1 + 0.125, yC, 4)
ax.text(X1 + CW - 0.028, yC + BM + 0.028, "连续相", fontsize=7.6, color="#2C6E8F",
        ha="right", va="center")
ax.text(X1 + 0.030, BY + 0.048, "分散相", fontsize=7.6, color="#A9761A", ha="left", va="top")

# --- 流动聚焦 ---
frame(X2, "流动聚焦")
yC = BY + CH * 0.50
ax.add_patch(Rectangle((X2 + 0.022, yC - BM), CW - 0.044, 2 * BM, fc=CONT, ec="none", zorder=2))
ax.add_patch(Rectangle((X2 + CW / 2 - 0.017, BY + 0.048), 0.034, yC - BM - (BY + 0.048),
                       fc=DISP, ec="none", zorder=3))
ax.add_patch(Rectangle((X2 + CW / 2 - 0.017, yC + BM), 0.034, BY + CH - 0.048 - (yC + BM),
                       fc=CONT, ec="none", zorder=3))
droplets(X2 + 0.145, yC, 3, step=0.046)
ax.text(X2 + 0.028, yC + BM + 0.030, "连续相", fontsize=7.6,
        color="#2C6E8F", ha="left", va="bottom")
ax.text(X2 + 0.028, BY + 0.040, "分散相", fontsize=7.6, color="#A9761A", ha="left", va="bottom")

# --- 共轴 ---
frame(X3, "共轴 / 毛细管")
yC = BY + CH * 0.50
ax.add_patch(Rectangle((X3 + 0.022, yC - 0.052), CW - 0.044, 0.104, fc=CONT, ec="none", zorder=2))
ax.add_patch(Rectangle((X3 + 0.022, yC - 0.014), 0.105, 0.028, fc=DISP, ec="none", zorder=3))
droplets(X3 + 0.165, yC, 3, step=0.046)
ax.text(X3 + 0.028, yC + 0.075, "连续相（鞘流）", fontsize=7.6, color="#2C6E8F", va="bottom")
ax.text(X3 + 0.030, yC - 0.030, "分散相", fontsize=7.6, color="#A9761A", va="top")

ax.text(0.50, 0.245, r"液滴直径 $d \propto Q_d/Q_c$（流量比控制）    ·    "
                     r"$Ca=\mu v/\gamma$ 决定是“挤断”还是“滴落”",
        ha="center", fontsize=9.5, color="#3C4E60")
ax.text(0.50, 0.115, "通量：单通道每秒 10²–10⁴ 个液滴，直径变异系数 CV < 3%\n"
                     "每个液滴 = 一个独立微反应器 / 一个细胞球 / 一块微凝胶积木",
        ha="center", fontsize=9.0, color="#3C4E60", linespacing=1.75)

# ============================================================ (d) 扩散时间
axx = fig.add_subplot(gs[1, 1])
L = np.logspace(np.log10(0.05), np.log10(3000), 400)
D = 500.0
axx.loglog(L, L ** 2 / (2 * D), color=S.VIOLET, lw=2.8, zorder=3)
axx.set_xlabel("扩散距离 L（µm）", fontsize=10)
axx.set_ylabel("达到均一所需时间 t ≈ L²/2D（s）", fontsize=10)
axx.grid(True, which="both", ls=":", color="#DCE4EB", zorder=0)
axx.set_ylim(1e-7, 2e4); axx.set_xlim(0.05, 3000)

for Lv, lab, c, off in [(1, "1 µm\n单个细菌", "#3C4E60", (12, 10)),
                        (10, "10 µm\n一个细胞", S.TEAL, (12, 10)),
                        (100, "100 µm\n毛细血管间距", S.AMBER, (-14, -34)),
                        (1000, "1 mm\n厚组织", S.CORAL, (12, -30))]:
    tv = Lv ** 2 / (2 * D)
    axx.plot([Lv], [tv], "o", ms=8.5, color=c, zorder=4, mec="white", mew=1.5)
    axx.annotate(lab, (Lv, tv), textcoords="offset points", xytext=off,
                 fontsize=8.8, color=c, fontweight="bold", linespacing=1.5)

axx.axvspan(100, 200, color=S.CORAL, alpha=0.10, zorder=0)
axx.axvline(200, color=S.CORAL, ls="--", lw=1.5, zorder=1)
axx.text(232, 2.2e-6, "无血管组织\n氧扩散极限\n≈ 100–200 µm", fontsize=8.5,
         color="#C0392B", va="bottom", fontweight="bold", linespacing=1.6)
axx.text(0.75, 3.5e2, "尺度越小，扩散越快。\n这既是微流控能“养活”厚组织的原因，\n"
                      "也是它能把化学信号精确排布的原因。",
         fontsize=9.1, color=S.NAVY, va="center", linespacing=1.75,
         bbox=dict(fc="#F4F8FB", ec="#D6E0E9", boxstyle="round,pad=0.45"))
for sp in ("top", "right"):
    axx.spines[sp].set_visible(False)
panel_title(axx, "d", "扩散：微尺度里唯一的“混合器”",
            "小分子在水中 D ≈ 500 µm²/s —— 距离翻倍，等待时间变成 4 倍")

S.save(fig, "figures/fig02_physics.png")
