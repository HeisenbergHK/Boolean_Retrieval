import pandas as pd

df = pd.read_csv("data.csv")

print(df)

print(df.isnull().sum())

print(df.columns)

with open("raw data.txt", "w", encoding='utf-8') as file:
    for index, row in df.iterrows():
        file.write(f"comment {index}\n")
        file.write(row["Text"])
        file.write("\n")

df = df.drop(columns=["Score", "Suggestion"])

df = df.rename(columns={"Text": "Comment"})

df.to_csv("digikala_comments_dataset.csv", index=False)


