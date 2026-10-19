# -*- coding: utf-8 -*-
"""图3：四条主流技术路线 —— 纺丝 / 液滴组装 / 生物打印 / 器官芯片"""
import numpy as np
import figstyle as S
from matplotlib.patches import (FancyBboxPatch, Rectangle, Circle, Polygon,
                                FancyArrowPatch)

plt = S.plt
fig = plt.figure(figsize=(13.6, 9.6))
gs = fig.add_gridspec(2, 2, hspace=0.30, wspace=0.11,
                      left=0.028, right=0.978, top=0.90, bottom=0.045)


def panel_title(ax, tag, title, sub, color):
    ax.text(0.0, 1.115, tag, transform=ax.transAxes, fontsize=15,
            fontweight="bold", color=color, va="bottom")
    ax.text(0.062, 1.11, title, transform=ax.transAxes, fontsize=12.5,
            fontweight="bold", color=color, va="bottom")
    ax.text(0.0, 1.012, sub, transform=ax.transAxes, fontsize=8.9,
            color=S.GRAY, va="bottom")


def keyline(ax, text, y=0.055):
    ax.text(0.5, y, text, ha="center", va="center", fontsize=9.0, color="#2B3B4C",
            linespacing=1.75,
            bbox=dict(fc="#F4F8FB", ec="#DCE4EB", boxstyle="round,pad=0.45"))


def arr(ax, p1, p2, color="#8FA3B5", lw=1.6, ms=12, z=6, style="-|>"):
    ax.add_patch(FancyArrowPatch(p1, p2, arrowstyle=style, mutation_scale=ms,
                                 lw=lw, color=color, zorder=z, shrinkA=0, shrinkB=0))


def newax():
    a = fig.add_subplot(gs[len(newax.n) // 2, len(newax.n) % 2])
    newax.n.append(1)
    a.set_xlim(0, 1); a.set_ylim(0, 1); a.axis("off")
    return a

newax.n = []

# ==================================================== ① 微流控纺丝
ax = newax()
panel_title(ax, "①", "微流控纺丝：把组织拉成“线”",
            "共轴层流不打混 → 芯层细胞被鞘层包住，出孔即固化成核壳纤维", S.AMBER)

# --- 共轴喷头（垂直）---
DX0, DX1 = 0.055, 0.275
ax.add_patch(Rectangle((DX0, 0.585), DX1 - DX0, 0.335, fc="#E4EBF1", ec="#8FA3B5",
                       lw=1.3, zorder=1))
ax.add_patch(Rectangle((DX0 + 0.012, 0.597), DX1 - DX0 - 0.024, 0.311,
                       fc="#D9EEF7", ec="none", zorder=2))
ax.add_patch(Rectangle((DX0 + 0.012, 0.597), 0.072, 0.311, fc="#CFE8F4", ec="none", zorder=2))
ax.add_patch(Rectangle((DX0 + 0.136, 0.597), 0.072, 0.311, fc="#CFE8F4", ec="none", zorder=2))
# 内针
ax.add_patch(Rectangle((DX0 + 0.080, 0.700), 0.060, 0.255, fc="#F0CE86",
                       ec="#B87C1E", lw=1.1, zorder=3))
ax.add_patch(Polygon([(DX0 + 0.080, 0.700), (DX0 + 0.140, 0.700),
                      (DX0 + 0.110, 0.640)], fc="#F0CE86", ec="#B87C1E", lw=1.1, zorder=3))
ax.text(DX0 + 0.110, 0.963, "芯层：细胞 + 基质", fontsize=7.9, color="#A9761A",
        ha="center", va="bottom")
ax.text(0.300, 0.930, "鞘流：海藻酸钠 / 胶原", fontsize=7.9, color="#2C6E8F",
        ha="left", va="center")
ax.text(DX0 + 0.110, 0.565, "同轴针头", fontsize=7.8, color=S.GRAY, ha="center", va="top")

# --- 出孔成纤 ---
ax.add_patch(Rectangle((DX0 + 0.080, 0.395), 0.060, 0.150, fc="#F0CE86",
                       ec="#B87C1E", lw=0.9, zorder=3))
ax.add_patch(Rectangle((DX0 + 0.068, 0.395), 0.012, 0.150, fc="#BFDFF0", ec="none", zorder=2))
ax.add_patch(Rectangle((DX0 + 0.140, 0.395), 0.012, 0.150, fc="#BFDFF0", ec="none", zorder=2))
arr(ax, (DX0 + 0.110, 0.385), (DX0 + 0.110, 0.325), color=S.AMBER, lw=2.0, ms=13)
ax.text(0.135, 0.360, "出孔即固化（Ca²⁺ / 光 / 酶）", fontsize=8.0,
        color="#A9761A", ha="left", va="center")

# --- 核壳截面 ---
fx, fy, fr = 0.450, 0.790, 0.072
ax.add_patch(Circle((fx, fy), fr, fc="#D9EEF7", ec="#2C6E8F", lw=1.5, zorder=4))
ax.add_patch(Circle((fx, fy), fr * 0.55, fc="#F0CE86", ec="#B87C1E", lw=1.2, zorder=5))
for a in np.linspace(0.3, 2 * np.pi + 0.3, 6, endpoint=False):
    ax.add_patch(Circle((fx + fr * 0.36 * np.cos(a), fy + fr * 0.36 * np.sin(a)),
                        0.0125, fc=S.PINK, ec="white", lw=0.6, zorder=6))
ax.text(fx, fy - fr - 0.048, "核壳纤维截面", fontsize=8.2, color="#3C4E60", ha="center",
        va="top")
arr(ax, (0.545, 0.790), (0.610, 0.790), color=S.AMBER, lw=1.9)

# --- 取向纤维束 ---
for i in range(5):
    yy = 0.660 + i * 0.055
    c = ["#F0CE86", "#E8B24A", "#F0CE86", "#D9A93A", "#F0CE86"][i]
    ax.plot([0.640, 0.985], [yy, yy], color=c, lw=6.0, solid_capstyle="round", zorder=3)
    ax.plot([0.640, 0.985], [yy, yy], color="#B87C1E", lw=0.9, zorder=4, alpha=.55)
ax.text(0.812, 0.945, "取向纤维束 → 肌肉 / 神经 / 肌腱", fontsize=8.5,
        color="#3C4E60", ha="center", va="center")
ax.text(0.812, 0.585, "再进一步：编织 / 缠绕成 3D 支架", fontsize=8.5,
        color=S.GRAY, ha="center", va="center", style="italic")

# --- 左下要点 ---
ax.text(0.030, 0.195, "单根纤维直径 10–1000 µm，可细到\n只容纳 1–2 个细胞", fontsize=8.4,
        color="#3C4E60", ha="left", va="center", linespacing=1.7)
ax.text(0.985, 0.195, "层流界面不打混 → 核-壳、Janus、多腔、\n中空纤维都能一次成型；细胞存活率通常 > 90%",
        fontsize=8.4, color="#3C4E60", ha="right", va="center", linespacing=1.7,
        bbox=dict(fc="#FDF6E8", ec="#F0DDB4", boxstyle="round,pad=0.45"))
keyline(ax, "纤维直径 10–1000 µm · 细胞存活率通常 > 90% · 可连续收丝（m/min 量级）")

# ==================================================== ② 液滴与微凝胶
ax = newax()
panel_title(ax, "②", "液滴与微凝胶：把组织拆成“积木”再拼回来",
            "自下而上（bottom-up）：先做均一模块，再让模块自己融合、排序", S.VIOLET)

# --- 顶部流程 ---
ax.add_patch(Rectangle((0.045, 0.760), 0.085, 0.045, fc="#BFDCEC", ec="none", zorder=2))
ax.add_patch(Rectangle((0.045, 0.680), 0.026, 0.100, fc="#F0CE86", ec="none", zorder=3))
for i in range(3):
    ax.add_patch(Circle((0.152 + i * 0.034, 0.782), 0.0165, fc="#E8B24A",
                        ec="#B87C1E", lw=0.7, zorder=4))
ax.text(0.075, 0.645, "① 液滴生成\n10²–10⁴ 个/秒", fontsize=8.0, color="#3C4E60",
        ha="center", va="top", linespacing=1.5)
arr(ax, (0.262, 0.782), (0.300, 0.782), color=S.VIOLET, lw=1.8)

for i in range(3):
    cx = 0.345 + i * 0.052
    ax.add_patch(Circle((cx, 0.782), 0.0235, fc="#D8CFFB", ec=S.VIOLET, lw=1.3, zorder=4))
    for a in np.linspace(0.5, 2 * np.pi + 0.5, 4, endpoint=False):
        ax.add_patch(Circle((cx + 0.011 * np.cos(a), 0.782 + 0.011 * np.sin(a)),
                            0.006, fc=S.PINK, ec="none", zorder=5))
ax.text(0.397, 0.645, "② 固化成微凝胶\n50–300 µm，CV < 3%", fontsize=8.0,
        color="#3C4E60", ha="center", va="top", linespacing=1.5)
arr(ax, (0.520, 0.782), (0.558, 0.782), color=S.VIOLET, lw=1.8)

ax.add_patch(FancyBboxPatch((0.560, 0.720), 0.145, 0.125,
                            boxstyle="round,pad=0,rounding_size=0.018",
                            fc="#F1EDFF", ec=S.VIOLET, lw=1.3, zorder=1))
rng = np.random.default_rng(11)
cols = [S.PINK, S.TEAL, S.AMBER, "#B9A8F5", S.GREEN]
for i in range(20):
    ax.add_patch(Circle((0.575 + rng.uniform(0, 0.115), 0.735 + rng.uniform(0, 0.095)),
                        rng.uniform(0.013, 0.021), fc=cols[i % 5], ec="white",
                        lw=0.6, zorder=3, alpha=.92))
ax.text(0.6325, 0.645, "③ 堆积 → 融合成一体", fontsize=8.0, color="#3C4E60",
        ha="center", va="top")
arr(ax, (0.740, 0.782), (0.778, 0.782), color=S.VIOLET, lw=1.8)

ax.add_patch(FancyBboxPatch((0.780, 0.700), 0.195, 0.165,
                            boxstyle="round,pad=0,rounding_size=0.018",
                            fc="#EAF7F1", ec=S.GREEN, lw=1.3, zorder=1))
for k in range(3):
    ax.add_patch(Rectangle((0.795, 0.735 + k * 0.040), 0.165, 0.028,
                           fc=["#9BD3C8", "#BFE3DC", "#9BD3C8"][k], ec="white",
                           lw=0.8, zorder=3))
ax.plot([0.877, 0.877], [0.725, 0.845], color="#C0392B", lw=2.4, zorder=4,
        solid_capstyle="round")
ax.text(0.877, 0.645, "④ 成熟：自排序、\n血管长入、出现功能", fontsize=8.0,
        color="#2E7D5B", ha="center", va="top", linespacing=1.5)

# --- 左下：融合与差异黏附 ---
fy = 0.345
ax.add_patch(Circle((0.105, fy), 0.070, fc=S.PINK, ec="white", lw=1.2, zorder=3, alpha=.9))
ax.add_patch(Circle((0.215, fy), 0.070, fc=S.TEAL, ec="white", lw=1.2, zorder=3, alpha=.9))
arr(ax, (0.140, fy), (0.180, fy), color=S.GRAY, lw=1.6, ms=11, style="<|-|>")
ax.add_patch(Circle((0.335, fy), 0.090, fc=S.TEAL, ec="white", lw=1.2, zorder=3, alpha=.9))
for dx, dy, r in [(0, 0.055, 0.045), (-0.038, -0.050, 0.038), (0.042, -0.046, 0.036)]:
    ax.add_patch(Circle((0.335 + dx, fy + dy), r, fc=S.PINK, ec="white", lw=1.0,
                        zorder=4, alpha=.92))
ax.text(0.245, 0.185, "差异黏附：黏得紧的往里钻，黏得松的摊在外层\n→ 不用模板，也能自发形成“核-壳”式分层",
        fontsize=8.4, color="#3C4E60", ha="center", va="center", linespacing=1.9)

# --- 右下：要点 ---
ax.text(0.985, 0.345, "为什么要模块化？", fontsize=9.4, color=S.VIOLET,
        fontweight="bold", ha="right", va="top")
ax.text(0.985, 0.255, "• 每个模块的尺寸、组成、刚度都能独立设定\n"
                      "• 模块本身很薄，天然绕开“氧气送不进厚组织”的难题\n"
                      "• 可批量生产、冻存，像零件一样按需拼装",
        fontsize=8.3, color="#3C4E60", ha="right", va="top", linespacing=2.1)
keyline(ax, "液滴通量 10²–10⁴ 个/秒/通道 · 微凝胶 50–300 µm · 融合时间 数小时–数天")

# ==================================================== ③ 微流控生物打印
ax = newax()
panel_title(ax, "③", "微流控生物打印：按图纸“点”出组织",
            "把微流控喷头装到运动平台上：多材料同时挤出，逐点 / 逐层，甚至体积一次成型", S.TEAL)

# --- 打印头 ---
hx, hy, hw, hh = 0.020, 0.640, 0.280, 0.275
ax.add_patch(FancyBboxPatch((hx, hy), hw, hh, boxstyle="round,pad=0,rounding_size=0.015",
                            fc="#E9EEF3", ec="#8FA3B5", lw=1.3, zorder=2))
for i, (c, lab) in enumerate([(S.TEAL, "墨水 A"), (S.AMBER, "墨水 B"), (S.PINK, "细胞")]):
    X = hx + 0.030 + i * 0.080
    ax.add_patch(Rectangle((X, hy + 0.085), 0.044, 0.140, fc=c, ec="none", zorder=3, alpha=.85))
    ax.text(X + 0.022, hy + 0.232, lab, fontsize=7.5, color="#3C4E60", ha="center", va="bottom")
    ax.plot([X + 0.022, hx + 0.140], [hy + 0.085, hy - 0.052], color=c, lw=1.6, zorder=4)
ax.add_patch(Polygon([(hx + 0.112, hy - 0.048), (hx + 0.168, hy - 0.048),
                      (hx + 0.153, hy - 0.112), (hx + 0.127, hy - 0.112)],
                     fc="#DCE6EF", ec="#8FA3B5", lw=1.1, zorder=5))
arr(ax, (hx + 0.140, hy - 0.118), (hx + 0.140, hy - 0.176), color="#3C4E60", lw=2.0, ms=13)
ax.text(hx + 0.140, hy - 0.198, "挤出丝径 100–400 µm", fontsize=8.1, color=S.GRAY,
        ha="center", va="top")
for k in range(4):
    ax.add_patch(FancyBboxPatch((0.028 + k * 0.006, 0.240 + k * 0.040), 0.272 - k * 0.012, 0.030,
                                boxstyle="round,pad=0,rounding_size=0.008",
                                fc=[S.TEAL, "#8FD1C4", S.AMBER, "#F3D69B"][k],
                                ec="white", lw=1.0, zorder=3, alpha=.92))
ax.text(0.164, 0.200, "逐层堆叠（也可以投影 / 体积一次成型）", fontsize=8.3,
        color="#3C4E60", ha="center", va="top")
ax.text(0.020, 0.135, "微流控喷头的价值：把“配比”从手艺变成可编程参数。",
        fontsize=8.3, color="#3C4E60", ha="left", va="center")

ax.add_patch(FancyBboxPatch((0.400, 0.250), 0.255, 0.665,
                            boxstyle="round,pad=0,rounding_size=0.018",
                            fc="#EAF7F1", ec=S.GREEN, lw=1.3, zorder=1))
ax.plot([0.440, 0.615], [0.560, 0.560], color="#C0392B", lw=6.0, zorder=4,
        solid_capstyle="round")
ax.plot([0.528, 0.528], [0.560, 0.700], color="#C0392B", lw=4.4, zorder=4,
        solid_capstyle="round")
ax.plot([0.528, 0.528], [0.560, 0.420], color="#C0392B", lw=4.4, zorder=4,
        solid_capstyle="round")
for i in range(6):
    ax.add_patch(Circle((0.448 + i * 0.030, 0.665), 0.011, fc=S.PINK, ec="white",
                        lw=0.5, zorder=5))
    ax.add_patch(Circle((0.448 + i * 0.030, 0.455), 0.011, fc=S.PINK, ec="white",
                        lw=0.5, zorder=5))
ax.text(0.528, 0.850, "牺牲模板：打印可溶“血管芯”", fontsize=8.3, color="#2E7D5B",
        ha="center", va="center")
ax.text(0.528, 0.360, "溶解 → 留下中空管腔 → 灌注\n→ 内皮细胞铺满管壁",
        fontsize=8.1, color="#2E7D5B", ha="center", va="center", linespacing=1.8)

ax.text(0.985, 0.860, "生物打印的“三难”", fontsize=9.4, color=S.TEAL,
        fontweight="bold", ha="right", va="center")
ax.text(0.985, 0.620, "① 分辨率 ↔ 速度\n"
                      "② 力学强度 ↔ 细胞存活\n"
                      "　（喷嘴处剪切要 < 5 kPa）\n"
                      "③ 形状自由 ↔ 血管化\n"
                      "　（> 200 µm 就必须有血管）",
        fontsize=8.3, color="#3C4E60", ha="right", va="center", linespacing=2.1)
ax.text(0.985, 0.315, "微流控喷头：多路墨水在喷口前汇合，\n流量与剪切实时可调，配方随时切换。",
        fontsize=8.2, color="#3C4E60", ha="right", va="center", linespacing=1.8,
        bbox=dict(fc="#EAF7F1", ec="#BFE3DC", boxstyle="round,pad=0.45"))
keyline(ax, "面内分辨率 50–500 µm · 喷嘴 100–400 µm · 打印后 24 h 细胞存活率通常 85–95%")

# ==================================================== ④ 器官芯片
ax = newax()
panel_title(ax, "④", "器官芯片：让组织“活在有条件的房间里”",
            "在同一块芯片上同时给出灌流、机械力与化学梯度，并把功能实时读出来", S.NAVY)

CX, CY, CW, CH = 0.115, 0.235, 0.455, 0.615
ax.add_patch(FancyBboxPatch((CX, CY), CW, CH, boxstyle="round,pad=0,rounding_size=0.018",
                            fc="#E9EEF3", ec="#8FA3B5", lw=1.4, zorder=1))
yU, yL, mh = CY + 0.430, CY + 0.185, 0.036
ax.add_patch(Rectangle((CX + 0.028, yU - mh / 2), CW - 0.056, mh, fc="#D9EEF7",
                       ec="none", zorder=3))
for i in range(10):
    ax.add_patch(Circle((CX + 0.048 + i * 0.040, yU - mh / 2 + 0.006), 0.0135,
                        fc=S.TEAL, ec="white", lw=0.5, zorder=4))
ax.add_patch(Rectangle((CX + 0.028, yL - mh / 2), CW - 0.056, mh, fc="#FFE4DE",
                       ec="none", zorder=3))
for i in range(10):
    ax.add_patch(Circle((CX + 0.048 + i * 0.040, yL + mh / 2 - 0.006), 0.0135,
                        fc=S.CORAL, ec="white", lw=0.5, zorder=4))
ax.plot([CX + 0.028, CX + CW - 0.028], [CY + 0.305, CY + 0.305], color="#7A8A99",
        lw=2.2, zorder=5, ls=(0, (4, 2)))
ax.text(CX + CW / 2, CY + 0.318, "多孔膜（0.4–10 µm 孔）", fontsize=7.9, color="#4A5C6E",
        ha="center", va="bottom", zorder=6)
for sx, inward in ((CX - 0.055, 1), (CX + CW + 0.010, -1)):
    ax.add_patch(FancyBboxPatch((sx, CY + 0.075), 0.045, 0.465,
                                boxstyle="round,pad=0,rounding_size=0.016",
                                fc="#DCE6EF", ec="#8FA3B5", lw=1.2, zorder=1))
    ax.text(sx + 0.0225, CY + 0.305, "负压侧腔", fontsize=7.3, color="#4A5C6E",
            rotation=90, ha="center", va="center", zorder=6)
    for dy in (-0.135, 0, 0.135):
        arr(ax, (sx + 0.0225, CY + 0.305 + dy),
            (sx + 0.0225 + inward * 0.038, CY + 0.305 + dy),
            color=S.CORAL, lw=1.3, ms=9, z=6)
for yy in (yU, yL):
    arr(ax, (CX + 0.006, yy), (CX + 0.052, yy), color=S.NAVY, lw=1.7, ms=11, z=6)
    arr(ax, (CX + CW - 0.006, yy), (CX + CW - 0.152, yy), color=S.NAVY, lw=1.7, ms=11, z=6)
ax.text(CX + CW / 2, CY + CH - 0.030, "灌流：氧气 + 营养 + 剪切力", fontsize=8.5,
        color=S.NAVY, ha="center", va="center")
ax.text(CX + CW / 2, CY + 0.045, "上皮 / 内皮界面 · 跨膜运输 · 屏障功能",
        fontsize=8.1, color="#3C4E60", ha="center", va="center")

ax.text(0.985, 0.850, "能读出来的功能", fontsize=9.4, color=S.NAVY,
        fontweight="bold", ha="right", va="center")
ax.text(0.985, 0.590, "• 跨膜电阻 TEER\n• 屏障通透性\n• 收缩力 / 搏动频率\n"
                      "• 分泌与代谢产物\n• 免疫细胞浸润\n• 基因表达与组学",
        fontsize=8.3, color="#3C4E60", ha="right", va="center", linespacing=2.1)
ax.text(0.985, 0.245, "本质：把培养皿里\n“看不见的条件”\n变成可编程、\n可测量的参数",
        fontsize=8.3, color=S.NAVY, ha="right", va="center", linespacing=1.9,
        bbox=dict(fc="#EEF3F7", ec="#D6E0E9", boxstyle="round,pad=0.45"))
keyline(ax, "通道 100–1000 µm 宽 × 100–200 µm 高 · 剪切力 0.01–1 dyn/cm² · 牵张 5–10% · 可连续培养数周")

S.save(fig, "figures/fig03_routes.png")
