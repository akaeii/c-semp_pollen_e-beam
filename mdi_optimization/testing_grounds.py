import pandas as pd

df1 = pd.DataFrame(
    data={
        "wave_no": [i for i in range(1, 11, 1)],
        "abs_1": [i for i in range(10, 110, 10)],
    }
)
df2 = pd.DataFrame(
    data={
        "wave_no": [i for i in range(1, 11, 1)],
        "abs_2": [i for i in range(20, 220, 20)],
    }
)

concatenated = pd.DataFrame()
concatenated = df1

concatenated = pd.merge(
    left=concatenated,
    right=df2,
    on="wave_no",
)

print(concatenated.head())
