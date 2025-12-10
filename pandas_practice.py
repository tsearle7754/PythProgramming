import pandas as pd

data = {
    'student': ['Amy', 'Ben', 'Chris', 'Dana'],
    'grade': [87, 92, 74, 88],
    'major': ['CS', 'CS', 'History', 'Math']
}

df = pd.DataFrame(data)

print(df.head())
print(df.describe())
print(df[df['grade'] > 85])
df['curved'] = df['grade'] + 5
print(df)