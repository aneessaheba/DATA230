"""
HW3 - Chapter 6: Visualizing Amounts
Textbook: Fundamentals of Data Visualization (Claus O. Wilke)

Concepts implemented:
  1. Vertical vs Horizontal Bar Plot  (Ch6 - bar ordering & label readability)
  2. Grouped Bar Plot                 (Ch6 - two categorical variables)
  3. Stacked Bar Plot                 (Ch6 - showing totals and composition)
  4. Dot Plot                         (Ch6 - better than bars for narrow ranges)
  5. Heatmap                          (Ch6 - two categorical + one quantitative)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import seaborn as sns

plt.rcParams.update({"font.size": 11})

# ── Dataset: Titanic (used across multiple figures) ──────────────────────────
titanic = sns.load_dataset("titanic")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 1  ·  Vertical (bad) vs Horizontal (good) bar plot
#   Key concept: long category labels → horizontal bars are easier to read.
# ═══════════════════════════════════════════════════════════════════════════
languages = [
    "Python", "JavaScript", "Java", "C#", "C++",
    "TypeScript", "PHP", "Swift", "Kotlin", "Rust",
]
popularity = [30.3, 13.4, 11.6, 7.5, 6.8, 5.9, 5.0, 4.5, 3.9, 2.1]

df_lang = pd.DataFrame({"Language": languages, "Popularity (%)": popularity})
df_lang_sorted = df_lang.sort_values("Popularity (%)")   # ascending → natural for barh

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle(
    "Figure 1 · Vertical vs Horizontal Bar Plot\n"
    "Most Popular Programming Languages (Stack Overflow Survey 2023)",
    fontsize=13, fontweight="bold",
)

# (a) Vertical with rotated labels – avoid this
ax1.bar(df_lang["Language"], df_lang["Popularity (%)"], color="steelblue")
ax1.set_xticks(range(len(df_lang)))
ax1.set_xticklabels(df_lang["Language"], rotation=45, ha="right")
ax1.set_title("(a) Vertical Bars – Rotated Labels\n[Harder to read — avoid]", color="firebrick")
ax1.set_ylabel("Popularity (%)")

# (b) Horizontal sorted – preferred
ax2.barh(df_lang_sorted["Language"], df_lang_sorted["Popularity (%)"], color="steelblue")
ax2.set_title("(b) Horizontal Bars – Sorted by Value\n[Preferred]", color="darkgreen")
ax2.set_xlabel("Popularity (%)")

plt.tight_layout()
plt.savefig("ch6_fig1_bar_orientation.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch6_fig1_bar_orientation.png")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 2  ·  Grouped Bar Plot
#   Key concept: compare two categorical dimensions simultaneously.
# ═══════════════════════════════════════════════════════════════════════════
# 2016 US median household income by age group and education (approximate)
age_groups = ["25–34", "35–44", "45–54", "55–64"]
bachelor  = [65_000, 80_000, 85_000, 78_000]
masters   = [75_000, 95_000, 100_000, 90_000]

x = np.arange(len(age_groups))
width = 0.35

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(x - width / 2, bachelor, width, label="Bachelor's degree", color="steelblue")
ax.bar(x + width / 2, masters,  width, label="Master's degree",   color="darkorange")
ax.set_title(
    "Figure 2 · Grouped Bar Plot\n"
    "Median Household Income by Age Group & Education Level (2016)",
    fontweight="bold",
)
ax.set_xlabel("Age Group")
ax.set_ylabel("Median Income (USD)")
ax.set_xticks(x)
ax.set_xticklabels(age_groups)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"${v:,.0f}"))
ax.legend()
ax.set_ylim(0, 115_000)

plt.tight_layout()
plt.savefig("ch6_fig2_grouped_bar.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch6_fig2_grouped_bar.png")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 3  ·  Stacked Bar Plot
#   Key concept: stacking works when summing sub-groups is meaningful.
# ═══════════════════════════════════════════════════════════════════════════
counts = (
    titanic.groupby(["pclass", "sex"])
    .size()
    .unstack(fill_value=0)
)
class_labels = ["1st Class", "2nd Class", "3rd Class"]
male_cnt   = counts["male"].values
female_cnt = counts["female"].values
x = np.arange(len(class_labels))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))
fig.suptitle(
    "Figure 3 · Grouped vs Stacked Bar Plot\n"
    "Titanic Passengers by Class and Gender",
    fontsize=13, fontweight="bold",
)

# Grouped
ax1.bar(x - 0.2, male_cnt,   0.4, label="Male",   color="steelblue")
ax1.bar(x + 0.2, female_cnt, 0.4, label="Female", color="salmon")
ax1.set_title("(a) Grouped – compare within class")
ax1.set_xticks(x); ax1.set_xticklabels(class_labels)
ax1.set_ylabel("Number of Passengers")
ax1.legend()

# Stacked
ax2.bar(x, male_cnt,   0.6, label="Male",   color="steelblue")
ax2.bar(x, female_cnt, 0.6, bottom=male_cnt, label="Female", color="salmon")
ax2.set_title("(b) Stacked – shows totals per class")
ax2.set_xticks(x); ax2.set_xticklabels(class_labels)
ax2.set_ylabel("Number of Passengers")
ax2.legend()

plt.tight_layout()
plt.savefig("ch6_fig3_stacked_bar.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch6_fig3_stacked_bar.png")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 4  ·  Dot Plot vs Bar Plot
#   Key concept: when data values are far from zero, dots convey differences
#                better than bars that require a tall, mostly-empty axis.
# ═══════════════════════════════════════════════════════════════════════════
life_exp = {
    "Canada": 80.7, "United States": 78.2, "Chile": 78.6,
    "Mexico": 76.1, "Brazil": 73.0, "Colombia": 72.3,
    "Peru": 71.4, "Venezuela": 70.4, "Ecuador": 69.3,
    "Paraguay": 67.7, "Bolivia": 60.3, "Haiti": 57.1,
}
df_le = (pd.DataFrame.from_dict(life_exp, orient="index", columns=["LifeExp"])
           .reset_index()
           .rename(columns={"index": "Country"})
           .sort_values("LifeExp"))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
fig.suptitle(
    "Figure 4 · Dot Plot vs Bar Plot\n"
    "Life Expectancy in the Americas (2007)",
    fontsize=13, fontweight="bold",
)

# Dot plot (preferred for narrow data range)
for _, row in df_le.iterrows():
    ax1.plot([55, row["LifeExp"]], [row["Country"], row["Country"]],
             color="lightgray", linewidth=1, zorder=1)
ax1.scatter(df_le["LifeExp"], df_le["Country"],
            color="steelblue", s=90, zorder=3)
ax1.set_title("(a) Dot Plot – highlights differences")
ax1.set_xlabel("Life Expectancy (years)")
ax1.set_xlim(50, 86)
ax1.grid(axis="x", linestyle="--", alpha=0.4)

# Bar plot (harder to compare when bars all ~70-80 years)
ax2.barh(df_le["Country"], df_le["LifeExp"], color="steelblue")
ax2.set_title("(b) Bar Plot – long bars obscure differences")
ax2.set_xlabel("Life Expectancy (years)")
ax2.set_xlim(0, 86)

plt.tight_layout()
plt.savefig("ch6_fig4_dot_plot.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch6_fig4_dot_plot.png")


# ═══════════════════════════════════════════════════════════════════════════
# Figure 5  ·  Heatmap
#   Key concept: show a quantitative value across two categorical dimensions.
# ═══════════════════════════════════════════════════════════════════════════
pivot = (
    titanic.groupby(["pclass", "sex"])["fare"]
    .mean()
    .unstack()
    .rename(index={1: "1st Class", 2: "2nd Class", 3: "3rd Class"})
)

fig, ax = plt.subplots(figsize=(6, 4))
im = ax.imshow(pivot.values, cmap="YlOrRd", aspect="auto")
ax.set_xticks([0, 1])
ax.set_xticklabels(pivot.columns.str.capitalize())
ax.set_yticks([0, 1, 2])
ax.set_yticklabels(pivot.index)
ax.set_title(
    "Figure 5 · Heatmap\nMean Titanic Fare by Passenger Class & Gender",
    fontweight="bold",
)
for i in range(pivot.shape[0]):
    for j in range(pivot.shape[1]):
        ax.text(j, i, f"${pivot.values[i, j]:.0f}",
                ha="center", va="center", fontsize=12, fontweight="bold",
                color="black" if pivot.values[i, j] < 80 else "white")
plt.colorbar(im, ax=ax, label="Mean Fare (USD)")
plt.tight_layout()
plt.savefig("ch6_fig5_heatmap.png", dpi=150, bbox_inches="tight")
plt.show()
print("Saved: ch6_fig5_heatmap.png")


# ─── Summary ────────────────────────────────────────────────────────────────
print("""
╔══════════════════════════════════════════════════════════════════════════╗
║  Chapter 6 Key Findings                                                  ║
╠══════════════════════════════════════════════════════════════════════════╣
║  • Horizontal bars are preferred when category labels are long.          ║
║  • Sort bars by data value unless the order is naturally meaningful.     ║
║  • Grouped bars compare sub-groups; stacked bars reveal totals.          ║
║  • Dot plots outperform bars when values are far from zero, because      ║
║    they highlight differences rather than absolute magnitudes.           ║
║  • Heatmaps efficiently encode a numeric value across two categories.    ║
╚══════════════════════════════════════════════════════════════════════════╝
""")
