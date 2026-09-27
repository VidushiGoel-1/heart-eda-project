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