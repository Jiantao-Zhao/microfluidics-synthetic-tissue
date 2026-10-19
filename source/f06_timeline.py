# -*- coding: utf-8 -*-
"""图6：二十年路线图 —— 里程碑、应用版图与五道坎"""
import numpy as np
import figstyle as S
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch

plt = S.plt
fig = plt.figure(figsize=(13.6, 8.3))
gs = fig.add_gridspec(2, 3, height_ratios=[1.06, 1.0], hspace=0.30, wspace=0.13,
                      left=0.028, right=0.978, top=0.885, bottom=0.045)


def ptitle(ax, tag, title, color, sub=None):
    ax.text(0.0, 1.115, tag, transform=ax.transAxes, fontsize=14.5,
            fontweight="bold", color=color, va="bottom")
    ax.text(0.075, 1.11, title, transform=ax.transAxes, fontsize=11.8,
            fontweight="bold", color=color, va="bottom")
    if sub:
        ax.text(0.0, 1.010, sub, transform=ax.transAxes, fontsize=8.7,
                color=S.GRAY, va="bottom")


# ================================================== 时间线
ax = fig.add_subplot(gs[0, :]); ax.set_xlim(1997, 2027); ax.set_ylim(0, 1); ax.axis("off")
ptitle(ax, "", "二十年路线图：从“芯片上的通道”到“芯片上的器官”", S.NAVY,
       "每一格都代表一次“原来还能这样做”的转折")

ax.plot([1998, 2026], [0.50, 0.50], color="#C9D3DD", lw=3.0, zorder=1,
        solid_capstyle="round")
for yr in range(1998, 2027, 2):
    ax.plot([yr, yr], [0.487, 0.513], color="#C9D3DD", lw=1.2, zorder=1)

MILES = [
    (1998, "软光刻与 PDMS\n微流控走向普及", S.NAVY, 1),
    (2002, "梯度发生器\n浓度变成几何问题", S.VIOLET, -1),
    (2006, "液滴微流控\n皮升级反应器", S.VIOLET, 1),
    (2010, "肺芯片\n组织第一次会呼吸", S.NAVY, -1),
    (2013, "米级细胞微纤维\n可编织成组织", S.AMBER, 1),
    (2016, "血管化 3D 打印\n+ 微孔颗粒凝胶", S.TEAL, -1),
    (2019, "器官级血管树\n合成细胞间信号", S.AMBER, 1),
    (2021, "微流控 WNT 梯度\n24 小时建出体轴", S.GREEN, -1),
    (2024, "组装体与生物机器人\n监管开始转向", S.CORAL, 1),
]
for yr, lab, c, side in MILES:
    yy = 0.50 + side * 0.070
    ax.plot([yr, yr], [0.50, yy], color=c, lw=1.4, zorder=2, alpha=.75)
    ax.add_patch(Circle((yr, 0.50), 0.0080, fc=c, ec="white", lw=1.3, zorder=4))
    ty = yy + side * 0.050
    ax.add_patch(FancyBboxPatch((yr - 1.25, ty), 2.50, 0.285,
                                boxstyle="round,pad=0,rounding_size=0.05",
                                fc="white", ec=c, lw=1.1, zorder=3))
    ax.text(yr, ty + 0.140, lab, fontsize=8.2, color=c, ha="center", va="center",
            zorder=5, linespacing=1.55)
    ax.text(yr, yy + side * 0.020, f"{yr}", fontsize=9.0, color=c, ha="center",
            va="center", zorder=5, fontweight="bold",
            bbox=dict(fc="white", ec="none", pad=0.9))

# ================================================== 应用版图
ax = fig.add_subplot(gs[1, 0]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
ptitle(ax, "", "已经用起来的地方", S.TEAL, "不是未来时，很多已经是现在进行时")
APPS = [
    ("药物筛选与毒性", "先在人源组织上看到肝毒性、心脏毒性", S.TEAL, "①"),
    ("疾病建模", "遗传病、感染、肿瘤微环境、罕见病", S.NAVY, "②"),
    ("再生医学与移植", "可移植的胰岛、皮肤、软骨、血管", S.CORAL, "③"),
    ("个性化医疗", "用患者自己的细胞试药，再决定方案", S.VIOLET, "④"),
    ("特殊环境", "太空辐射、微重力、环境毒理", S.AMBER, "⑤"),
]
for i, (t, d, c, num) in enumerate(APPS):
    y = 0.845 - i * 0.175
    ax.add_patch(FancyBboxPatch((0.020, y - 0.070), 0.960, 0.140,
                                boxstyle="round,pad=0,rounding_size=0.015",
                                fc="#F7FAFC", ec="#DCE4EB", lw=1.0, zorder=1))
    ax.add_patch(Rectangle((0.020, y - 0.070), 0.010, 0.140, fc=c, ec="none", zorder=2))
    ax.add_patch(Circle((0.085, y), 0.042, fc=c, ec="none", zorder=3, alpha=.14))
    ax.text(0.085, y, num, fontsize=10.5, color=c, ha="center", va="center",
            fontweight="bold", zorder=4)
    ax.text(0.150, y + 0.030, t, fontsize=9.4, color=c, ha="left", va="center",
            fontweight="bold", zorder=4)
    ax.text(0.150, y - 0.032, d, fontsize=8.2, color="#3C4E60", ha="left",
            va="center", zorder=4)

# ================================================== 五道坎
ax = fig.add_subplot(gs[1, 1]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
ptitle(ax, "", "五道坎", S.CORAL, "卡住产业化的不是想象力，是这些具体问题")
BARS = [
    ("血管化与尺度放大", 5, "厚组织送不进氧，毫米以上就是坎", S.CORAL),
    ("标准化与可重复性", 4, "PDMS 会吸走小分子，批次间差异大", S.CORAL),
    ("免疫与长期培养", 4, "培养几周后，细胞就不太“像”原来的器官", S.AMBER),
    ("通量与成本", 3, "单次实验便宜，规模化并不便宜", S.AMBER),
    ("监管与证据链", 3, "需要证明它比动物模型更能预测人", S.VIOLET),
]
ax.text(0.985, 0.930, "难度（定性）", fontsize=8.0, color=S.GRAY, ha="right",
        va="center")
for i, (t, rate, d, c) in enumerate(BARS):
    y = 0.845 - i * 0.175
    ax.add_patch(FancyBboxPatch((0.020, y - 0.075), 0.960, 0.150,
                                boxstyle="round,pad=0,rounding_size=0.015",
                                fc="#F7FAFC", ec="#DCE4EB", lw=1.0, zorder=1))
    ax.add_patch(Rectangle((0.020, y - 0.075), 0.010, 0.150, fc=c, ec="none", zorder=2))
    ax.text(0.050, y + 0.035, t, fontsize=9.3, color="#2B3B4C", ha="left",
            va="center", fontweight="bold", zorder=4)
    for k in range(5):
        filled = k < rate
        ax.add_patch(Circle((0.775 + k * 0.044, y + 0.035), 0.0165,
                            fc=c if filled else "#E3EAF0", ec="none", zorder=4))
    ax.text(0.050, y - 0.038, d, fontsize=8.1, color="#4A5C6E", ha="left",
            va="center", zorder=4)

# ================================================== 正在发生的解法
ax = fig.add_subplot(gs[1, 2]); ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.axis("off")
ptitle(ax, "", "正在发生的解法", S.VIOLET, "每道坎都已经有一条看得见的路")
FIX = [
    ("颗粒水凝胶 / 模块化", "把“厚”拆成“薄”，绕开扩散极限"),
    ("热塑性 / 玻璃芯片", "替代 PDMS，吸附与变形都更小"),
    ("AI + 自动化闭环", "机器设计、机器做、机器读数据"),
    ("多器官串联 + 免疫", "身体是网络，模型也必须是网络"),
    ("监管新通道", "用“人源证据”换取审评路径"),
]
for i, (t, d) in enumerate(FIX):
    y = 0.845 - i * 0.175
    ax.add_patch(FancyBboxPatch((0.020, y - 0.070), 0.960, 0.140,
                                boxstyle="round,pad=0,rounding_size=0.015",
                                fc="#F9F7FF", ec="#DCCFF7", lw=1.0, zorder=1))
    ax.add_patch(Circle((0.078, y), 0.026, fc=S.VIOLET, ec="white", lw=0.8, zorder=3))
    ax.text(0.078, y, "→", fontsize=9.5, color="white", ha="center", va="center",
            zorder=4, fontweight="bold")
    ax.text(0.132, y + 0.030, t, fontsize=9.3, color=S.VIOLET, ha="left",
            va="center", fontweight="bold", zorder=4)
    ax.text(0.132, y - 0.032, d, fontsize=8.2, color="#3C4E60", ha="left",
            va="center", zorder=4)

S.save(fig, "figures/fig06_timeline.png")
