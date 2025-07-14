import pandas as pd
df=pd.read_csv("Bengaluru_House_Data.csv")
print(df.head())
# Check shape and column names
print("Shape:", df.shape)
print("Columns:", df.columns)

# Summary of data types and missing values
print(df.info())

# Count of missing values
print(df.isnull().sum())
# Check unique values in 'society' and 'availability'
print(df['society'].nunique())  # likely many missing or useless
print(df['availability'].unique())

# Drop 'society', 'availability', 'balcony' (if needed)
df = df.drop(['society', 'availability'], axis=1)
# Drop rows with too many nulls
df = df.dropna()

# Check again
df.isnull().sum()
# Example: '2 BHK' -> 2
df['BHK'] = df['size'].apply(lambda x: int(x.split(' ')[0]) if isinstance(x, str) else None)

# Drop original size column
df = df.drop(['size'], axis=1)
def convert_sqft(x):
    try:
        if '-' in x:
            nums = x.split('-')
            return (float(nums[0]) + float(nums[1])) / 2
        return float(x)
    except:
        return None

df['total_sqft'] = df['total_sqft'].apply(convert_sqft)
df = df[df['total_sqft'].notnull()]
print(df['price'].head())  # Already numeric, no need to convert
df.to_csv("cleaned_bengaluru_house_data.csv", index=False)
