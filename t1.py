import dask.dataframe as dd

#Load CSV with image column correctly handled
df = dd.read_csv("AMAZON_FASHION.csv", dtype={'image': 'object'})

#Show first 5 rows
print("👉 Top 5 Rows:")
print(df.head())

#Total rows
print("👉 Total Rows:")
print(df.shape[0].compute())

#Verified vs Unverified review count
print("\n👉 Verified/Unverified Review Count:")
print(df.groupby('verified').size().compute())

Average rating
print("\n👉 Average Overall Rating:")
print(df['overall'].mean().compute())
