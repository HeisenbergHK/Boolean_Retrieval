import re

import pandas as pd


# Function to extract the number from a comment string for numerical sorting
def extract_number(comment):
    match = re.search(r'\d+', comment)  # Find the first occurrence of a number in the string
    return int(match.group()) if match else 0  # Return the number or 0 if no number is found

df = pd.read_csv("doc-term_matrix.csv")

search_item = input("Search key: ")


matching_rows = df[df["Word"].str.contains(search_item, case=False, na=False)]


if not matching_rows.empty:


    list_of_comments = set()

    for index, row in matching_rows.iterrows():
        # Find all columns where the value is 1
        columns_with_one = row[row == 1].index.tolist()

        # Update the set with the found columns
        list_of_comments.update(map(str, columns_with_one))

    # Sort comments based on the extracted number from each comment
    sorted_comments = sorted(list_of_comments, key=extract_number)

    # Print the sorted comments
    print(f"Comments with the word {search_item} in them:")
    for comment in sorted_comments:
        print(comment)

else:
    print(f"No rows contain the word '{search_item}' in the column '{"Word"}'.")
