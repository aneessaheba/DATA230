"""
HW3 - Chapter 7: Visualizing Distributions – Histograms and Density Plots
Textbook: Fundamentals of Data Visualization (Claus O. Wilke)

Concepts implemented:
  1. Histogram with varying bin widths     (effect of bin-width choice)
  2. Kernel Density Estimate (KDE)         (continuous distribution estimate)
  3. Overlapping density plots             (comparing two groups)
  4. Age Pyramid (mirrored histogram)      (comparing two distributions)
  5. Multi-group density plot              (comparing several groups)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import gaussian_kde

plt.rcParams.update({"font.size": 11})

# ── Dataset: Titanic passenger ages ──────────────────────────────────────────
titanic = sns.load_dataset("titanic")
ages    = titanic["age"].dropna().values
male_ages   = titanic.loc[titanic["sex"] == "male",   "age"].dropna().values
female_ages = titanic.loc[titanic["sex"] == "female", "age"].dropna().values


# ═══════════════════════════════════════════════════════════════════════════
# Figure 1  ·  Histograms with different bin widths
#   Key concept: bin width dramatically changes apparent shape of distribution.
#   Always explore multiple bin widths before settling on one.
# ═══════════════════════════════════════════════════════════════════════════
bin_widths = [1, 3, 5, 15]
bin_labels = ["(a) bin width = 1 yr\n[too narrow – noisy]",
              "(b) bin width = 3 yrs\n[good balance]",
              "(c) bin width = 5 yrs\n[reasonable]",
              "(d) bin width = 15 yrs\n[too wide – loses detail]"]

fig, axes = plt.subplots(1, 4, figsize=(16, 4), sharey=False)
fig.suptitle(
    "Figure 1 · Histograms Depend on Bin Width\n"
    "Age Distribution of Titanic Passengers",
    fontsize=13, fontweight="bold",
)
for ax, bw, label in zip(axes, bin_widths, bin_labels):
    bins = np.arange(0, 80 + bw, bw)
    ax.hist(ages, bins=bins, color="steelblue", edgecolor="white", linewidth=0.4)
    ax.set_title(label, fontsize=10)
    ax.set_xlabel("Age (years)")
    ax.set_ylabel("Count")
    ax.set_xlim(0, 80)

plt.tight_layout()
plt.savefig("ch7_fig1_histogram_binwidths.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch7_fig1_histogram_binwidths.png")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 2  ·  Histogram vs Kernel Density Estimate (KDE)
#   Key concept: KDE gives a smooth, parameter-dependent continuous curve.
#   The curve area integrates to 1 (probability density).
# ═══════════════════════════════════════════════════════════════════════════
x_range = np.linspace(0, 80, 500)
kde_func = gaussian_kde(ages, bw_method=0.25)   # bandwidth ~2 years equivalent

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4))
fig.suptitle(
    "Figure 2 · Histogram vs Kernel Density Estimate\n"
    "Age Distribution of Titanic Passengers",
    fontsize=13, fontweight="bold",
)

# Histogram (density=True so y-axis matches KDE scale)
ax1.hist(ages, bins=np.arange(0, 80, 5), color="steelblue",
         edgecolor="white", linewidth=0.5, density=True, alpha=0.7)
ax1.set_title("(a) Histogram (bin width = 5 yrs)")
ax1.set_xlabel("Age (years)"); ax1.set_ylabel("Density")

# KDE
ax2.fill_between(x_range, kde_func(x_range), alpha=0.3, color="steelblue")
ax2.plot(x_range, kde_func(x_range), color="steelblue", linewidth=2)
ax2.set_title("(b) Kernel Density Estimate (KDE)\nbandwidth = 0.25 (Gaussian)")
ax2.set_xlabel("Age (years)"); ax2.set_ylabel("Density")
ax2.set_xlim(0, 80)

plt.tight_layout()
plt.savefig("ch7_fig2_histogram_kde.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch7_fig2_histogram_kde.png")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 3  ·  Effect of KDE bandwidth choice
#   Key concept: too-narrow bandwidth → spiky; too-wide → over-smoothed.
# ═══════════════════════════════════════════════════════════════════════════
bandwidths = [0.05, 0.15, 0.4, 1.0]
bw_labels  = ["(a) bw = 0.05\n[too narrow]",
               "(b) bw = 0.15\n[good]",
               "(c) bw = 0.40\n[slightly wide]",
               "(d) bw = 1.00\n[too wide]"]

fig, axes = plt.subplots(1, 4, figsize=(16, 4), sharey=False)
fig.suptitle(
    "Figure 3 · KDE Depends on Bandwidth Choice\n"
    "Age Distribution of Titanic Passengers",
    fontsize=13, fontweight="bold",
)
for ax, bw, label in zip(axes, bandwidths, bw_labels):
    kde = gaussian_kde(ages, bw_method=bw)
    ax.fill_between(x_range, kde(x_range), alpha=0.25, color="steelblue")
    ax.plot(x_range, kde(x_range), color="steelblue", linewidth=2)
    ax.set_title(label, fontsize=10)
    ax.set_xlabel("Age (years)"); ax.set_ylabel("Density")
    ax.set_xlim(0, 80)

plt.tight_layout()
plt.savefig("ch7_fig3_kde_bandwidth.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch7_fig3_kde_bandwidth.png")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 4  ·  Overlapping Density Plots (Male vs Female)
#   Key concept: overlapping KDEs work better than overlapping histograms
#   because the continuous lines help the eye distinguish groups.
# ═══════════════════════════════════════════════════════════════════════════
kde_male   = gaussian_kde(male_ages,   bw_method=0.25)
kde_female = gaussian_kde(female_ages, bw_method=0.25)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4))
fig.suptitle(
    "Figure 4 · Overlapping Histograms vs Overlapping Density Plots\n"
    "Titanic Passenger Ages by Gender",
    fontsize=13, fontweight="bold",
)

# (a) Overlapping histograms – problematic
ax1.hist(male_ages,   bins=np.arange(0, 80, 5), alpha=0.5,
         color="steelblue", edgecolor="white", label="Male")
ax1.hist(female_ages, bins=np.arange(0, 80, 5), alpha=0.5,
         color="salmon",    edgecolor="white", label="Female")
ax1.set_title("(a) Overlapping Histograms\n[Ambiguous – avoid]", color="firebrick")
ax1.set_xlabel("Age (years)"); ax1.set_ylabel("Count")
ax1.legend()

# (b) Overlapping KDEs – cleaner
# Scale by group size so area reflects count, not fraction
scale_m = len(male_ages)
scale_f = len(female_ages)
ax2.fill_between(x_range, kde_male(x_range)   * scale_m,
                 alpha=0.3, color="steelblue", label=f"Male (n={scale_m})")
ax2.fill_between(x_range, kde_female(x_range) * scale_f,
                 alpha=0.3, color="salmon",    label=f"Female (n={scale_f})")
ax2.plot(x_range, kde_male(x_range)   * scale_m, color="steelblue", linewidth=2)
ax2.plot(x_range, kde_female(x_range) * scale_f, color="salmon",    linewidth=2)
ax2.set_title("(b) Overlapping Density Plots\n[Preferred – groups stay distinct]",
              color="darkgreen")
ax2.set_xlabel("Age (years)"); ax2.set_ylabel("Count (scaled)")
ax2.set_xlim(0, 80)
ax2.legend()

plt.tight_layout()
plt.savefig("ch7_fig4_overlapping_distributions.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch7_fig4_overlapping_distributions.png")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 5  ·  Age Pyramid (mirrored histogram)
#   Key concept: two distributions can be directly compared face-to-face.
#   Only works for exactly two groups.
# ═══════════════════════════════════════════════════════════════════════════
bin_edges = np.arange(0, 85, 5)
male_hist,   _ = np.histogram(male_ages,   bins=bin_edges)
female_hist, _ = np.histogram(female_ages, bins=bin_edges)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

fig, ax = plt.subplots(figsize=(8, 7))
ax.barh(bin_centers, -male_hist,   height=4.5, color="steelblue",
        label="Male",   align="center")
ax.barh(bin_centers,  female_hist, height=4.5, color="salmon",
        label="Female", align="center")
ax.set_xlabel("Count")
ax.set_ylabel("Age (years)")
ax.set_title(
    "Figure 5 · Age Pyramid – Titanic Passengers by Gender",
    fontweight="bold",
)
# Relabel x-axis to show positive values on both sides
x_ticks = ax.get_xticks()
ax.set_xticklabels([str(abs(int(t))) for t in x_ticks])
ax.axvline(0, color="black", linewidth=0.8)
ax.legend(loc="lower right")

plt.tight_layout()
plt.savefig("ch7_fig5_age_pyramid.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch7_fig5_age_pyramid.png")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 6  ·  Multi-group density plot
#   Key concept: density plots scale to multiple groups better than histograms.
# ═══════════════════════════════════════════════════════════════════════════
iris = sns.load_dataset("iris")
species_colors = {"setosa": "#E69F00", "versicolor": "#56B4E9", "virginica": "#009E73"}

fig, ax = plt.subplots(figsize=(9, 5))
x_r = np.linspace(0, 8, 500)
for species, color in species_colors.items():
    data = iris.loc[iris["species"] == species, "petal_length"].values
    kde  = gaussian_kde(data, bw_method=0.35)
    ax.fill_between(x_r, kde(x_r), alpha=0.25, color=color, label=species.capitalize())
    ax.plot(x_r, kde(x_r), color=color, linewidth=2)

ax.set_title(
    "Figure 6 · Multi-Group Density Plot\nIris Petal Length Distribution by Species",
    fontweight="bold",
)
ax.set_xlabel("Petal Length (cm)")
ax.set_ylabel("Density")
ax.legend()

plt.tight_layout()
plt.savefig("ch7_fig6_multigroup_kde.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch7_fig6_multigroup_kde.png")


# ─── Summary ────────────────────────────────────────────────────────────────
print("""
╔══════════════════════════════════════════════════════════════════════════╗
║  Chapter 7 Key Findings                                                  ║
╠══════════════════════════════════════════════════════════════════════════╣
║  • Titanic age distribution peaks in the 20-30 range with a small        ║
║    secondary peak for children (~5 yrs). Most passengers were adults.    ║
║  • Bin width and KDE bandwidth both strongly affect perceived shape —    ║
║    always try several values (Fig 1 & 3).                                ║
║  • Male passengers were slightly older on average than female.           ║
║  • Overlapping KDEs are cleaner than overlapping histograms (Fig 4).     ║
║  • Iris species are cleanly separable in petal length (Fig 6):           ║
║    setosa ≈ 1.5 cm, versicolor ≈ 4.3 cm, virginica ≈ 5.5 cm.            ║
╚══════════════════════════════════════════════════════════════════════════╝
""")
