# Spotify Audio Features vs Popularity — Data Analysis

## 📌 Project Overview
This project provides a comprehensive analysis of Spotify tracks to identify the key audio features (such as danceability, energy, and acousticness) that drive track popularity. Leveraging the Python data science stack (**Pandas**, **NumPy**, **Matplotlib**, **Seaborn**), the project includes a robust ETL pipeline, exploratory data analysis (EDA), and a baseline linear regression model to quantify feature importance.

## 📂 Repository Structure
```
spotify-audio-popularity-analysis/
├── data/               # Dataset directory (user-provided CSV)
├── notebooks/          # Jupyter Notebooks for analysis
│   └── 01_spotify_eda.ipynb
├── src/                # Helper modules
│   └── utils.py        # Data cleaning and plotting utilities
├── outputs/            # Generated visualizations (PNG)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

## 🚀 Setup & Usage

### 1. Prerequisites
Ensure you have Python 3.8+ installed.

### 2. Installation
Clone the repository and install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3. Data Configuration
Download a Spotify Tracks dataset (e.g., from Kaggle's "Spotify Tracks Dataset"). The dataset should be a CSV file containing columns like `popularity`, `danceability`, `energy`, `tempo`, etc.

**Action:** Place the CSV file at `./data/spotify_tracks.csv`.

### 4. Running the Analysis
Launch the Jupyter Notebook to execute the analysis pipeline:
```bash
jupyter notebook notebooks/01_spotify_eda.ipynb
```
Run all cells to generate the insights and populate the `outputs/` directory.

## 📊 Output Visualizations
The analysis automatically generates the following visualizations in the `outputs/` directory:

| Filename | Description |
|----------|-------------|
| `popularity_distribution.png` | Histogram and KDE of the target variable `popularity`. |
| `audio_features_distribution.png` | Combined distribution plots for key audio features (danceability, energy, valence, etc.). |
| `correlation_heatmap.png` | Pearson correlation matrix showing relationships between numerical features. |
| `bivariate_scatter_plots.png` | Scatter plots with linear trendlines for top correlated features vs. popularity. |
| `tempo_outliers_comparison.png` | Boxplots demonstrating the impact of IQR outlier removal on Tempo. |
| `explicit_vs_popularity.png` | Boxplot comparison of popularity for Explicit vs. Non-Explicit tracks. |
| `mode_vs_popularity.png` | Popularity distribution across Major vs. Minor modes. |
| `hit_vs_nonhit_profile.png` | Bar chart comparing mean audio feature values for "Hits" (Pop ≥ 80) vs. others. |
| `popularity_trend_by_year.png` | Time-series analysis of average popularity over years. |

## 🔑 Key Analytical Insights
- **Correlation Analysis**: Identifies which features have the strongest positive/negative correlation with popularity.
- **Hit Profile**: "Hit" songs often exhibit distinct characteristics in terms of `loudness`, `danceability`, and `energy` compared to the general population.
- **Explicit Content**: Analysis reveals quantifiable differences in popularity distribution between explicit and clean tracks.

## 🛠 Tech Stack
- **Core**: `pandas`, `numpy`
- **Visualization**: `matplotlib`, `seaborn`
- **Modeling**: `scikit-learn` (Linear Regression baseline)
