# Heart Dataset EDA Project

## Dataset
Heart Failure Prediction dataset (`Heart.csv`) — 918 rows, 12 columns.
Target: `HeartDisease` (0 = no disease, 1 = disease) — classification.

## Topic 1 & 2: Loading, First Look, Data Types & Missing Values
- Loaded data with `pd.read_csv()`
- Checked `.head()`, `.shape`, `.info()`, `.describe()`
- Found `RestingBP` had a minimum of 0 (impossible value) — 1 row affected
- Checked `.dtypes`, `.isnull().sum()`, `.duplicated().sum()` — no missing values, no duplicates

## Topic 3: Handling Outliers
- Replaced `RestingBP = 0` with median of valid values
- Replaced `Cholesterol = 0` with median of valid values
- Verified both fixes — no zeros remain in either column

## Boxplot — Quick Concept

A boxplot summarizes ONE column using 5 values:
- **Median** (line in box) → middle value of all data
- **Q1** (left edge) → 25% of values are below this
- **Q3** (right edge) → 75% of values are below this
- **Box (Q1–Q3)** → where the middle 50% of values lie ("typical range")
- **Whiskers** → normal min/max range
- **Dots beyond whiskers** → outliers

A single boxplot (e.g. `sns.boxplot(x=df['Age'])`) only describes
that ONE column across ALL rows — it does NOT compare groups.
To compare groups (e.g. Age by HeartDisease), split it:
`sns.boxplot(x=df['HeartDisease'], y=df['Age'])`

## Topic 4: Univariate Analysis (`notebooks/04_univariate_analysis.ipynb`)
**Operations performed:**
- Histograms for Age, RestingBP, Cholesterol, MaxHR, Oldpeak
- Boxplots for same 5 numeric columns
- Countplots for Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope

**Findings:**
- [Note anything I actually noticed — e.g. "Sex is imbalanced, mostly Male" or "Cholesterol/Age look roughly normal after cleaning"]