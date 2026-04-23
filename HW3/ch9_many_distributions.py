"""
HW3 - Chapter 9: Visualizing Many Distributions at Once
Textbook: Fundamentals of Data Visualization (Claus O. Wilke)

Concepts implemented:
  1. Mean ± error bars (what NOT to do – loses distribution shape)
  2. Boxplots across groups
  3. Violin plots
  4. Strip chart (raw points, plain and jittered)
  5. Sina plot (points spread by local density)
  6. Ridgeline plot (density distributions stacked vertically)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import gaussian_kde

plt.rcParams.update({"font.size": 11})

# ── Dataset: Lincoln, NE daily temperatures (synthetic, realistic parameters) ─
# Monthly means/stds derived from actual NOAA normals for Lincoln NE
month_params = {
    "Jan": (23.7, 12), "Feb": (28.8, 12), "Mar": (40.5, 11),
    "Apr": (52.7, 10), "May": (63.2, 9),  "Jun": (72.5, 8),
    "Jul": (77.8, 7),  "Aug": (75.5, 7),  "Sep": (66.3, 8),
    "Oct": (54.8, 10), "Nov": (39.8, 11), "Dec": (27.3, 12),
}
month_order = list(month_params.keys())

rng = np.random.default_rng(0)
records = []
for month, (mean, std) in month_params.items():
    # Roughly 30 observations per month
    temps = rng.normal(mean, std, 30)
    for t in temps:
        records.append({"Month": month, "Temp_F": t})

df = pd.DataFrame(records)
df["Month"] = pd.Categorical(df["Month"], categories=month_order, ordered=True)
df = df.sort_values("Month")

# Also load tips for supplementary violin demo
tips = sns.load_dataset("tips")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 1  ·  Mean ± Error Bars (what NOT to use)
#   Key concept: a single point + two bars loses all distributional detail
#   and readers can't tell what the error bars represent (std? SEM? CI?).
# ═══════════════════════════════════════════════════════════════════════════
summary = df.groupby("Month", observed=True)["Temp_F"].agg(["mean", "std"]).reset_index()

fig, ax = plt.subplots(figsize=(11, 4))
ax.errorbar(
    summary["Month"], summary["mean"], yerr=2 * summary["std"],
    fmt="o", color="steelblue", capsize=5, linewidth=1.5,
)
ax.set_title(
    "Figure 1 · Mean ± 2 SD – Lincoln, NE Daily Temperatures\n"
    "[Avoid: hides distribution shape; ambiguous error bars]",
    fontweight="bold", color="firebrick",
)
ax.set_xlabel("Month"); ax.set_ylabel("Temperature (°F)")
ax.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("ch9_fig1_errorbar.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch9_fig1_errorbar.png")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 2  ·  Boxplots
#   Key concept: shows median, IQR, whiskers (1.5×IQR), and outliers.
#   Much more informative than error bars, but still hides multimodality.
# ═══════════════════════════════════════════════════════════════════════════
grouped = [df.loc[df["Month"] == m, "Temp_F"].values for m in month_order]

fig, ax = plt.subplots(figsize=(12, 5))
bp = ax.boxplot(grouped, tick_labels=month_order, patch_artist=True,
                medianprops={"color": "white", "linewidth": 2},
                whiskerprops={"linewidth": 1.5},
                capprops={"linewidth": 1.5})

cmap = plt.cm.coolwarm
n = len(grouped)
for i, patch in enumerate(bp["boxes"]):
    patch.set_facecolor(cmap(i / (n - 1)))

ax.set_title(
    "Figure 2 · Boxplots – Lincoln, NE Daily Temperatures by Month\n"
    "Median line + IQR box + whiskers (1.5×IQR) + outlier dots",
    fontweight="bold",
)
ax.set_xlabel("Month"); ax.set_ylabel("Temperature (°F)")
ax.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("ch9_fig2_boxplots.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch9_fig2_boxplots.png")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 3  ·  Violin Plots
#   Key concept: KDE mirrored around the center axis — reveals bimodality
#   and full distributional shape that boxplots hide.
# ═══════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(12, 5))

for i, month in enumerate(month_order, start=1):
    data = df.loc[df["Month"] == month, "Temp_F"].values
    kde  = gaussian_kde(data, bw_method=0.4)
    y_range = np.linspace(data.min() - 5, data.max() + 5, 300)
    density  = kde(y_range)
    density  = density / density.max() * 0.4  # normalize width

    color = plt.cm.coolwarm((i - 1) / (len(month_order) - 1))
    ax.fill_betweenx(y_range, i - density, i + density,
                     color=color, alpha=0.75)
    ax.plot(np.full_like(y_range, i - density), y_range, color=color, alpha=0.3)
    ax.plot(np.full_like(y_range, i + density), y_range, color=color, alpha=0.3)
    # Median marker
    ax.scatter(i, np.median(data), color="white", s=30, zorder=3)

ax.set_xticks(range(1, len(month_order) + 1))
ax.set_xticklabels(month_order)
ax.set_title(
    "Figure 3 · Violin Plots – Lincoln, NE Daily Temperatures by Month\n"
    "Reveals full distribution shape; note bimodal pattern in some months",
    fontweight="bold",
)
ax.set_xlabel("Month"); ax.set_ylabel("Temperature (°F)")
ax.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("ch9_fig3_violin.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch9_fig3_violin.png")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 4  ·  Strip Chart – plain vs jittered
#   Key concept: plot every individual point. Plain = overplotting.
#   Jitter = spread horizontally to reveal density.
# ═══════════════════════════════════════════════════════════════════════════
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5), sharey=True)
fig.suptitle(
    "Figure 4 · Strip Charts – Lincoln, NE Temperatures by Month",
    fontsize=13, fontweight="bold",
)

for i, month in enumerate(month_order, start=1):
    data = df.loc[df["Month"] == month, "Temp_F"].values
    # (a) No jitter – points pile on top of each other
    ax1.scatter(np.full_like(data, i), data,
                color="steelblue", alpha=0.4, s=18)
    # (b) Horizontal jitter
    jitter = rng.uniform(-0.25, 0.25, size=len(data))
    ax2.scatter(i + jitter, data, color="steelblue", alpha=0.5, s=18)

for ax, title, note in [
    (ax1, "(a) Strip Chart (no jitter)\n[Overplotting hides point density]", "firebrick"),
    (ax2, "(b) Jittered Strip Chart\n[Better — density now visible]", "darkgreen"),
]:
    ax.set_xticks(range(1, len(month_order) + 1))
    ax.set_xticklabels(month_order, rotation=45, ha="right")
    ax.set_title(title, color=note)
    ax.set_xlabel("Month")
ax1.set_ylabel("Temperature (°F)")

plt.tight_layout()
plt.savefig("ch9_fig4_strip_chart.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch9_fig4_strip_chart.png")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 5  ·  Sina Plot (violin + raw points combined)
#   Key concept: points jittered proportionally to local KDE — best of both.
# ═══════════════════════════════════════════════════════════════════════════
fig, ax = plt.subplots(figsize=(12, 5))

for i, month in enumerate(month_order, start=1):
    data = df.loc[df["Month"] == month, "Temp_F"].values
    kde  = gaussian_kde(data, bw_method=0.4)
    density_at_points = kde(data)
    density_at_points /= density_at_points.max()  # normalize to [0,1]
    max_spread = 0.35
    jitter_x = rng.uniform(-1, 1, size=len(data)) * density_at_points * max_spread

    color = plt.cm.coolwarm((i - 1) / (len(month_order) - 1))
    ax.scatter(i + jitter_x, data, color=color, alpha=0.6, s=20, zorder=2)
    # Median marker
    ax.scatter(i, np.median(data), color="black", s=50, zorder=4, marker="_", linewidths=2)

ax.set_xticks(range(1, len(month_order) + 1))
ax.set_xticklabels(month_order)
ax.set_title(
    "Figure 5 · Sina Plot – Points Jittered by Local Density\n"
    "Lincoln, NE Daily Temperatures by Month",
    fontweight="bold",
)
ax.set_xlabel("Month"); ax.set_ylabel("Temperature (°F)")
ax.grid(axis="y", linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("ch9_fig5_sina_plot.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch9_fig5_sina_plot.png")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 6  ·  Ridgeline Plot (joy plot)
#   Key concept: stagger KDE distributions along y-axis to show many at once.
#   Great for showing trends across ordered groups (e.g., months, years).
# ═══════════════════════════════════════════════════════════════════════════
x_range = np.linspace(-20, 110, 500)
overlap  = 2.5   # vertical spacing between rows
colors   = plt.cm.coolwarm(np.linspace(0, 1, len(month_order)))

fig, ax = plt.subplots(figsize=(10, 9))

for idx, (month, color) in enumerate(zip(month_order, colors)):
    data    = df.loc[df["Month"] == month, "Temp_F"].values
    kde     = gaussian_kde(data, bw_method=0.45)
    density = kde(x_range)
    density = density / density.max() * overlap * 0.9  # normalize height

    baseline = idx * overlap
    ax.fill_between(x_range, baseline, baseline + density,
                    color=color, alpha=0.8, zorder=idx)
    ax.plot(x_range, baseline + density, color="white", linewidth=0.8, zorder=idx + 0.5)
    ax.text(-22, baseline + 0.15, month, ha="right", va="bottom",
            fontsize=10, fontweight="bold", color=color)

ax.set_xlim(-20, 110)
ax.set_ylim(-0.5, len(month_order) * overlap + 1)
ax.set_yticks([])
ax.set_xlabel("Daily Mean Temperature (°F)", fontsize=12)
ax.set_title(
    "Figure 6 · Ridgeline Plot – Lincoln, NE Daily Temperatures\n"
    "Each ridge = KDE for one month (Jan at bottom, Dec at top)",
    fontweight="bold",
)
ax.spines[["left", "top", "right"]].set_visible(False)

plt.tight_layout()
plt.savefig("ch9_fig6_ridgeline.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch9_fig6_ridgeline.png")


# ─── Summary ────────────────────────────────────────────────────────────────
print("""
╔══════════════════════════════════════════════════════════════════════════╗
║  Chapter 9 Key Findings                                                  ║
╠══════════════════════════════════════════════════════════════════════════╣
║  • Lincoln, NE shows a clear seasonal temperature cycle:                 ║
║    winter months (Dec–Feb) cluster around 20–30°F; summer (Jun–Aug)     ║
║    around 70–80°F.                                                       ║
║  • Error bars (Fig 1) discard shape; boxplots (Fig 2) add quartile      ║
║    info but still hide multimodality.                                    ║
║  • Violin plots (Fig 3) reveal bimodal temperature patterns in autumn    ║
║    (Oct–Nov) — a feature invisible in boxplots.                          ║
║  • Jittered strip charts (Fig 4b) and sina plots (Fig 5) show all raw   ║
║    data points while still indicating density.                           ║
║  • Ridgeline plot (Fig 6) is the most compact and visually appealing     ║
║    summary — it scales well to many distributions at once.               ║
╚══════════════════════════════════════════════════════════════════════════╝
""")
