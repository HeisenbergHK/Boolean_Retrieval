import pandas as pd

# Load the CSV file containing the dataset of Digikala comments
df = pd.read_csv("digikala_comments_dataset.csv")

# Optional: Limit the dataset to the first 100 comments to improve performance
# This is because the algorithm has O(n^2) complexity and can take a long time
df = df.head(100)

# Display the first few rows of the dataframe for inspection
print(df)

# Initialize an empty set to store all unique words from the comments
words_set = set()

# Iterate over each comment in the "Comment" column of the dataset
for comment in df["Comment"]:
    # Split each comment into individual words (by default, splitting by spaces)
    words = comment.split()
    
    # Add the words from the current comment to the set (ensures uniqueness)
    words_set.update(words)

# Create a DataFrame with the unique words as the index (rows)
words_df = pd.DataFrame(index=list(words_set))

# Name the index column as 'Word' for clarity
words_df.index.name = 'Word'

# Get the total number of comments in the dataset
num_comments = len(df)

# Create a DataFrame where each comment will be represented as a column
# The index will be the words, and the columns will be named "comment 1", "comment 2", ..., "comment n"
columns_data = pd.DataFrame(None, index=words_df.index, columns=[f"comment {i}" for i in range(1, num_comments + 1)])

# For each unique word in the words_set
for word in words_set:
    # Loop over each comment and its index in the dataset
    for index, comment in enumerate(df["Comment"]):
        # Check if the current word exists in the split comment
        if word in comment.split():
            # If the word is found in the comment, mark the cell with a 1 (word present)
            columns_data.at[word, f"comment {index + 1}"] = 1
        else:
            # If the word is not found in the comment, mark the cell with a 0 (word absent)
            columns_data.at[word, f"comment {index + 1}"] = 0

# Concatenate the original words_df with the newly created columns_data DataFrame along the columns
words_df = pd.concat([words_df, columns_data], axis=1)

# Save the final document-term matrix to a CSV file, with words as the index
words_df.to_csv('doc-term_matrix.csv', index=True)