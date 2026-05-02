# DATA 230 · Data Visualization

**Course:** DATA 230 — Data Visualization
**Institution:** San Jose State University
**Author:** Anees Saheba Guddi (018205330)
**Textbook:** *Fundamentals of Data Visualization* — Claus O. Wilke (O'Reilly, 2019)

---

## Repository Structure

```
DATA230/
├── HW1/    Global Sales Visualization (Matplotlib · Pandas · Tableau)
├── HW2/    Wilke Ch 2–5  (Aesthetics · Coordinates · Color · Chart Survey)
├── HW3/    Wilke Ch 6–9  (Amounts · Distributions · ECDFs · Many Distributions)
└── HW4/    Wilke Ch 10–13 (Proportions · Nested Proportions · Associations · Time Series)
```

---

## HW1 · Global Sales Visualization

**Tools:** Python (Pandas, Matplotlib), Tableau Public

End-to-end exploratory data analysis of a synthetic global retail sales dataset — 5,000 transactions across 5 regions, 5 product categories, 3 customer segments, and 3 sales channels (2021–2024).

### Visualizations

| # | Chart | Key Finding |
|---|-------|-------------|
| 1 | Annual Revenue Trend (line + shaded area) | Revenue peaked at $2.28M in 2021, dipped –3.95% in 2022, partially recovered by 2024 (CAGR –0.7%) |
| 2 | Revenue by Region (horizontal bar) | North America (37%) + Europe (26%) = 63% of global revenue; MEA at just $0.5M is heavily underpenetrated |
| 3 | Revenue Share by Category (pie) | Electronics alone = 63% of total revenue — a significant concentration risk |
| 4 | Monthly Revenue Heatmap | October is the weakest month every year; August–September 2023 were peak months |
| 5 | Profit Margin by Category (boxplot) | All five categories cluster near ~40% median margin — no category commands a premium |
| 6 | Revenue by Region × Channel (stacked bar) | Mobile App is the #1 channel in every region — a global, not regional, shift |
| 7 | Discount Rate vs Profit Margin (scatter) | Pearson r = 0.01 — discounts have no measurable effect on margin |
| 8 | Quarterly Revenue YoY (grouped bar) | Q3 is the peak quarter every year; Q1 2021 was an unrepeated outlier |

**Tableau Dashboard:** [Retail Sales Analytics on Tableau Public](https://public.tableau.com/app/profile/anees.saheba.guddi/viz/RetailSalesAnalysis_17726585418550/RetailSalesAnalytics)

**Files:** [`HW1/`](HW1/)

---

## HW2 · Wilke Ch 2–5 · Core Visualization Principles

**Tools:** Python (Matplotlib, NumPy, Pandas)
**Notebook:** [`HW2/wilke_dataviz_ch2_to_ch5.ipynb`](HW2/wilke_dataviz_ch2_to_ch5.ipynb)

### Chapter 2 · Aesthetic Mappings

Demonstrates how data values map to visual channels: position, color, shape, size, line width, and line type.

| Visualization | Key Finding |
|---------------|-------------|
| Scatterplot grid (position, color, shape, size, combined) | Each aesthetic adds an independent dimension of information |
| Line plots (line type, line width) | Line type enables colorblind-accessible multi-group figures |

### Chapter 3 · Coordinate Systems and Axes

| Visualization | Key Finding |
|---------------|-------------|
| Monthly temperature: Cartesian vs polar | Polar coordinates reveal cyclic seasonal patterns more naturally |
| GDP per capita: linear vs log scale | Log scale surfaces proportional differences across wide numeric ranges |
| Temperature trend at three aspect ratios | Aspect ratio dramatically affects perceived slope magnitude |

### Chapter 4 · Color Scales

| Visualization | Key Finding |
|---------------|-------------|
| Qualitative scale — US population growth by region | Categorical color avoids implying order between groups |
| Sequential scale — monthly temperature heatmap | Sequential palettes encode magnitude; single-hue ramps minimize distraction |
| Diverging scale — correlation matrix | Diverging palettes center visually on zero; positive/negative asymmetry is clear |
| Highlight color — accent bar chart | A single accent color draws attention without overwhelming the chart |

### Chapter 5 · Directory of Visualizations

Survey of chart types by data category: Amounts, Distributions, Proportions, Relationships, and Time Series.

| Category | Charts | Key Finding |
|----------|--------|-------------|
| Amounts | Grouped bar, stacked bar, dot plot | Dot plots outperform bars when data ranges are narrow and far from zero |
| Distributions | Histogram, KDE, boxplot, violin | Violin plots reveal bimodality that boxplots hide |
| Proportions | Pie, stacked area | Pie works for ≤5 distinct slices; stacked area handles change over time |
| Relationships | Scatter + regression, bubble, 2D histogram | Bubble charts encode a third variable as circle area |
| Time Series | Line + area fill, color-coded profit bars | Filled area emphasizes cumulative magnitude; line emphasizes rate of change |

**Files:** [`HW2/`](HW2/)

---

## HW3 · Wilke Ch 6–9 · Distributions and Amounts

**Tools:** Python (Matplotlib, Seaborn, SciPy, NumPy, Pandas)
**Notebook:** [`HW3/HW3_Solutions.ipynb`](HW3/HW3_Solutions.ipynb)

### Chapter 6 · Visualizing Amounts

| Figure | Key Finding |
|--------|-------------|
| Vertical vs horizontal bar (programming language popularity) | Horizontal bars are preferred when category labels are long |
| Grouped bar (income by age × education) | Grouped bars compare sub-groups; stacked bars reveal totals |
| Grouped vs stacked bar (Titanic class × gender) | Stacked bars show that 3rd class had the most passengers by total |
| Dot plot vs bar (life expectancy, Americas) | Dot plots highlight differences better when values are far from zero |
| Heatmap (Titanic fare by class × gender) | 1st-class females paid >3× more than 3rd-class males on average |

### Chapter 7 · Histograms and Density Plots

| Figure | Key Finding |
|--------|-------------|
| Histograms at different bin widths | Bin width is the most important parameter — too narrow is noisy, too wide hides features |
| Histogram vs KDE | KDE provides a smooth density estimate but requires a bandwidth choice |
| Effect of KDE bandwidth | Wide bandwidth over-smooths; narrow bandwidth shows spurious peaks |
| Overlapping histograms vs KDEs | Overlapping KDEs are cleaner for comparing two groups |
| Age pyramid (mirrored histogram) | Works only for two groups; makes direct comparison intuitive |
| Multi-group KDE (Iris sepal length) | Setosa is clearly separated; versicolor and virginica overlap substantially |

### Chapter 8 · ECDFs and Q-Q Plots

| Figure | Key Finding |
|--------|-------------|
| ECDF of exam scores | ECDF shows every data point once with no binning parameter needed |
| Skewed data: raw vs log-transformed ECDF | Log transform reveals structure hidden in right-skewed distributions |
| Q-Q plot vs normal distribution | Points along the diagonal confirm normality; deviations show tail behavior |
| Log-normal and power-law Q-Q plots | Log-normal and power-law data show characteristic curves on a normal Q-Q plot |

### Chapter 9 · Visualizing Many Distributions

Dataset: synthetic daily temperatures for Lincoln, NE (NOAA normals, 12 months × 30 days)

| Figure | Key Finding |
|--------|-------------|
| Mean ± error bars | Avoid: hides distribution shape; error bar meaning is ambiguous |
| Boxplots by month | Shows seasonal cycle clearly; summer median ~78°F, winter ~27°F |
| Violin plots | Reveals bimodal patterns in October–November invisible in boxplots |
| Strip chart: plain vs jittered | Jitter is essential — plain strip charts stack points into meaningless columns |
| Sina plot | Best of both: points jittered proportionally to local KDE density |
| Ridgeline plot | Most compact view; seasonal temperature shift reads as a flowing wave |

**Files:** [`HW3/`](HW3/)

---

## HW4 · Wilke Ch 10–13 · Proportions, Associations, and Time Series

**Tools:** Python (Matplotlib, Seaborn, SciPy, NumPy, Pandas)
**Notebook:** [`HW4/HW4_Solutions.ipynb`](HW4/HW4_Solutions.ipynb)

### Chapter 10 · Visualizing Proportions

| Figure | Key Finding |
|--------|-------------|
| Pie chart: 4 vs 10 categories | Pie works only with ≤4–5 clearly distinct slices; 10 categories make angles indistinguishable |
| Pie vs stacked bar (Bundestag 2021) | Stacked bar immediately reveals that SPD barely leads CDU/CSU (206 vs 196 seats) |
| 100% stacked bar (Titanic survival by class) | 1st class: 63% survival vs 3rd class: 24% — stark disparity invisible in raw counts |
| Side-by-side proportional bars (class × sex) | Female 1st-class survival: 97%; male 1st-class: 37% — largest gender gap of any class |
| Waffle chart (US electricity by source) | Each cell = 1%; Natural Gas + Coal together occupy >half the grid |

### Chapter 11 · Visualizing Nested Proportions

| Figure | Key Finding |
|--------|-------------|
| Mosaic plot (Titanic class × survival) | Width encodes class size; height encodes survival rate — 3rd class was largest but least safe |
| Treemap (world GDP by region + country) | USA's tile alone is larger than all of Europe — size disparity is immediately clear |
| Nested donut vs horizontal bar | Nested donuts distort inner arc lengths — bars are always a better alternative |
| Sunburst (global CO₂ by sector) | Energy dominates at 51%; Electricity and Transport are the two largest sub-sectors |
| Parallel sets (Titanic class → sex → outcome) | Female passengers had wide green survival ribbons; male 3rd-class ribbons are almost entirely red |

### Chapter 12 · Visualizing Associations Among Quantitative Variables

| Figure | Key Finding |
|--------|-------------|
| Scatter + OLS trend (weight vs mpg) | r = −0.83; each extra 1,000 lbs costs ≈ 7.7 mpg |
| Overplotting: opaque → alpha → alpha + contours | Contour overlay is the best fix — reveals the bimodal X distribution hidden under solid dots |
| Bubble chart (GDP/capita vs life expectancy) | S-shaped relationship: gains plateau above ~$15K/capita even as GDP keeps rising |
| Scatter matrix / pair plot (Iris) | Petal dimensions perfectly separate species; sepal dimensions overlap heavily |
| Correlogram (Auto MPG) | Weight, displacement, and cylinders form a near-perfect correlation cluster (r ≈ 0.9) |
| 2-D histogram vs hexbin (Tips) | Hexbin reduces square-grid boundary artifacts; tip cluster is at $15–$20 bill / $2–$3 tip |

### Chapter 13 · Visualizing Time Series

| Figure | Key Finding |
|--------|-------------|
| Basic line chart (monthly temperature) | Line implies continuity; smooth seasonal cycle from 24°F (Jan) to 78°F (Jul) |
| Multiple time series (4 stock sectors) | Tech recovered fastest after the 2020 COVID dip; Energy lagged all other sectors |
| Area chart (10-year temperature) | Filled area highlights seasonal amplitude (~55°F peak-to-trough swing) |
| Stacked area chart (energy mix 2000–2023) | Coal collapsed from 52% → 20%; Wind + Solar grew from <2% → ~20% |
| Smoothed trend + confidence band | 12-month rolling mean separates the seasonal signal from a ~+1°F/decade warming drift |
| Aspect ratio and banking to 45° | Wide/short charts hide trends; banking to 45° gives proportional slope perception |

**Files:** [`HW4/`](HW4/)

---

## Requirements

```
numpy
pandas
matplotlib
seaborn
scipy
jupyter
```

Install with:

```bash
pip install numpy pandas matplotlib seaborn scipy jupyter
```

---

## How to Run

Each homework folder contains a self-contained Jupyter notebook. Open any of them and run all cells top to bottom — all data is either generated inline or loaded from seaborn's built-in datasets (no external downloads needed).

```bash
jupyter notebook HW1/retail_sales_analysis.ipynb
jupyter notebook HW2/wilke_dataviz_ch2_to_ch5.ipynb
jupyter notebook HW3/HW3_Solutions.ipynb
jupyter notebook HW4/HW4_Solutions.ipynb
```
