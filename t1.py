import dask.dataframe as dd

# Step 1: Load CSV with image column correctly handled
df = dd.read_csv("AMAZON_FASHION.csv", dtype={'image': 'object'})

# Step 2: Show first 5 rows
print("👉 Top 5 Rows:")
print(df.head())

# Step 3: Total rows
print("👉 Total Rows:")
print(df.shape[0].compute())

# Step 4: Verified vs Unverified review count
print("\n👉 Verified/Unverified Review Count:")
print(df.groupby('verified').size().compute())

# Step 5: Average rating
print("\n👉 Average Overall Rating:")
print(df['overall'].mean().compute())
