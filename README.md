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

-> What a correlation HEATMAP shows:

It's a grid where every numeric column is compared against every other numeric column, and each cell shows a number between -1 and +1 telling you how strongly those two columns move together:

+1 → perfect positive relationship (as one goes up, the other always goes up too)
0  → no relationship at all
-1 → perfect negative relationship (as one goes up, the other always goes down)
Values in between (like 0.3 or -0.6) → weaker versions of the same idea

The color (cmap='coolwarm') is just a visual shortcut so you don't have to read every number — typically red/warm = positive correlation, blue/cool = negative correlation, and the intensity of the color shows how strong it is.

The annot=True part is what prints the actual number inside each cell (without it, you'd only get colors with no numbers — less precise).

## Topic 5: Bivariate Analysis (`notebooks/05_bivariate_analysis.ipynb`)
**Operations performed:**
- Boxplot: Age by HeartDisease status
- Correlation heatmap across all numeric columns

**Findings:**
- Patients with HeartDisease tend to be slightly older (median ~50-60) vs without (~45-58)
- Oldpeak shows positive correlation with HeartDisease (higher Oldpeak → more likely disease)
- MaxHR shows negative correlation with HeartDisease (lower MaxHR → more likely disease)