# Wilke Dataviz Matplotlib

Matplotlib implementations of data visualization concepts from Wilke's Fundamentals of Data Visualization (Ch. 2 to 5) covering aesthetic mappings, coordinate systems, color scales, and chart types for amounts, distributions, proportions, and relationships.

**Course:** DATA230 Data Visualization
**Institution:** San Jose State University
**Author:** Anees Saheba Guddi
**Repo:** https://github.com/aneessaheba/wilke-dataviz-matplotlib

## Overview

This notebook walks through core visualization principles from Claus O. Wilke's textbook using Python and Matplotlib. Each chapter section includes working code examples and findings.

## Chapter 2 Aesthetic Mappings

Demonstrates how data values map to visual properties: position, color, shape, size, line width, and line type.

**Visualizations:**
- Scatterplots using position only, position + color, position + shape, position + size, and all aesthetics combined
- Line plots varying line type and line width

**Key Finding:** Each aesthetic adds an independent dimension of information. Color and shape distinguish categories; size encodes continuous variables. Line type is useful for colorblind accessible figures.

## Chapter 3 Coordinate Systems and Axes

Covers Cartesian vs polar coordinate systems, linear vs logarithmic scales, and the effect of aspect ratio on perception.

**Visualizations:**
- Monthly temperature in Cartesian and polar coordinates
- GDP per capita bar chart on linear vs log scale
- Temperature trend shown at three different aspect ratios

**Key Finding:** Polar plots reveal cyclic patterns. Log scale surfaces proportional differences across wide numeric ranges. Aspect ratio affects perceived slope and variability.

## Chapter 4 Color Scales

Explores the three roles of color in visualization: distinguishing categories (qualitative), encoding magnitude (sequential), and showing deviation from a midpoint (diverging).

**Visualizations:**
- Qualitative color scale: US state population growth by region
- Sequential color scale: monthly temperature heatmap across cities
- Diverging color scale: correlation matrix
- Highlight color: single accent bar chart

**Key Finding:** Each use case requires a different palette type. Diverging palettes center on zero; sequential palettes encode magnitude; qualitative palettes avoid implying order.

## Chapter 5 Directory of Visualizations

Surveys visualization types organized by data category: Amounts, Distributions, Proportions, Relationships, and Time Series.

**Visualizations:**
- Amounts: grouped bar, stacked bar, dot plot
- Distributions: histogram, density plot, boxplot, violin plot
- Proportions: pie chart, stacked area chart
- Relationships: scatter with regression, bubble chart, 2D histogram
- Time Series: line with area fill, color coded profit bars

**Key Finding:** Matching the chart type to the data type and question is critical. Each chart type has strengths suited to specific comparisons.

## Summary Table

| Chapter | Key Concept | Visualizations | Finding |
|---|---|---|---|
| Ch 2 | Aesthetic Mappings | Scatterplot grid, line plots | Each aesthetic adds a dimension of information |
| Ch 3 | Coordinate Systems and Scale | Cartesian vs Polar, Log scale, Aspect ratio | Coordinate choice shapes perception |
| Ch 4 | Color Scales | Qualitative, Sequential, Diverging, Highlight | Each color use case needs a different palette |
| Ch 5 | Directory of Visualizations | Bars, distributions, proportions, scatter, time series | Chart type must match data type |

## Requirements

```
numpy
pandas
matplotlib
scipy
```

Install with:

```
pip install numpy pandas matplotlib scipy
```

## Files

| File | Description |
|---|---|
| wilke_dataviz_ch2_to_ch5.ipynb | Main notebook with all chapter implementations |
| ch2_aesthetics.png | Chapter 2 aesthetic mapping plots |
| ch2_line_aesthetics.png | Chapter 2 line aesthetics |
| ch3_coordinate_systems.png | Chapter 3 Cartesian vs polar |
| ch3_log_vs_linear.png | Chapter 3 log vs linear scale |
| ch3_aspect_ratio.png | Chapter 3 aspect ratio comparison |
| ch4_qualitative_color.png | Chapter 4 qualitative color scale |
| ch4_sequential_color.png | Chapter 4 sequential color heatmap |
| ch4_diverging_color.png | Chapter 4 diverging correlation matrix |
| ch4_highlight_color.png | Chapter 4 highlight accent color |
| ch5_amounts.png | Chapter 5 amount visualizations |
| ch5_distributions.png | Chapter 5 distribution visualizations |
| ch5_proportions.png | Chapter 5 proportion visualizations |
| ch5_relationships.png | Chapter 5 relationship visualizations |
| ch5_timeseries.png | Chapter 5 time series visualizations |
