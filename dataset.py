import pandas as pd
df=pd.read_csv("Bengaluru_House_Data.csv")
print(df.head())

print("Shape:", df.shape)
print("Columns:", df.columns)


print(df.info())

print(df.isnull().sum())

print(df['society'].nunique()) 
print(df['availability'].unique())


df = df.drop(['society', 'availability'], axis=1)

df = df.dropna()


df.isnull().sum()

df['BHK'] = df['size'].apply(lambda x: int(x.split(' ')[0]) if isinstance(x, str) else None)


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
print(df['price'].head())
df.to_csv("cleaned_bengaluru_house_data.csv", index=False)
