# -*- coding: utf-8 -*-
"""统一绘图样式：中文标签 + 一致配色（科普长文配图专用）"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

CJK = "Heiti TC"          # 系统中文字体
for cand in ("Heiti TC", "PingFang HK", "Songti SC", "Arial Unicode MS", "STHeiti"):
    try:
        fm.findfont(cand, fallback_to_default=False)
        CJK = cand
        break
    except Exception:
        continue

plt.rcParams.update({
    "font.family": [CJK, "DejaVu Sans"],
    "axes.unicode_minus": False,
    "figure.dpi": 200,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "savefig.facecolor": "white",
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": "#C9D3DD",
    "axes.linewidth": 1.0,
    "text.color": "#12283D",
    "axes.labelcolor": "#12283D",
    "xtick.color": "#4A5C6E",
    "ytick.color": "#4A5C6E",
    "font.size": 10.5,
})

# ---- 调色板 ----
NAVY   = "#0F2A44"   # 主色：微流控/芯片
TEAL   = "#12A594"   # 细胞/生物
CORAL  = "#FF6B5B"   # 强调/警示
AMBER  = "#F2A93B"   # 材料/墨水
VIOLET = "#7C5CFF"   # 信号/梯度
GRAY   = "#6B7A8F"
LIGHT  = "#EEF3F7"
GREEN  = "#3FB27F"
PINK   = "#F27BA8"

def save(fig, path):
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white", pad_inches=0.18)
    plt.close(fig)
    print("saved", path)
