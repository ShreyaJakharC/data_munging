# Raw Data Munging

## Overview

A pair of Python scripts that transform NASA’s fixed-width historic surface temperature anomaly data into a clean CSV and then compute decadal average anomalies in °F for easy analysis.

## Features

- **Raw → CSV:** Removes header/footer notes, extra headings, blank lines, and handles `***` missing values
- **Unit Conversion:** Translates 0.01 °C anomaly values to °F (formatted to one decimal place)
- **Decadal Analysis:** Calculates average anomaly for each decade from 1880 onward
- **Repeatable Workflow:** One-step munge (`munge.py`) and one-step analysis (`analyze.py`)

## Tech & Tools

- **Language:** Python 3
- **Libraries:** — (built-in csv module only)
- **Data Source:** NASA GISS Surface Temperature Analysis

## Quick Start

```bash
git clone https://github.com/yourusername/raw-data-munging.git
cd raw-data-munging
# Munge raw NASA data into CSV
python munge.py data/GLB.Ts+dSST.txt
# Analyze the cleaned CSV and print decadal averages
python analyze.py data/clean_data.csv
```

## Results & Key Takeaways

- Successfully converted unstructured raw data into an analyzable CSV format.
- Computed historical temperature trends, highlighting long-term climate changes.
- Provided a foundation for further statistical modeling and visualization.

## Skills Gained

Data Cleaning & Preprocessing, Python Programming, CSV Data Processing, Algorithmic Thinking: Automating repetitive data transformations and decadal aggregations and Statistical Analysis: Calculating decadal averages to reveal long-term climate trends.
