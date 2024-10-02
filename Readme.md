# Boolean Retrieval and Document-Term Matrix Project

This repository contains a project that involves creating a document-term matrix from a dataset of comments and performing boolean retrieval on it. The dataset consists of user comments from Digikala, and the project includes scripts for data pre-processing and matrix generation.

## Project Structure

* __boolean_retrieval.py:__ Script to perform boolean retrieval on the document-term matrix.
* __data.csv:__ Raw dataset containing the original comments.
* __digikala_comments_dataset.csv:__ Cleaned and processed version of the dataset.
* __doc-term_matrix.csv:__ The generated document-term matrix where rows represent unique words and columns represent comments.
* __doc-term_matrix_creation.py:__ Script that creates the document-term matrix from the dataset.
* __pre_processing_data.py:__ Script for pre-processing the data, including cleaning and organizing the raw text data.
* __raw data.txt:__ Text file containing the raw comments extracted from data.csv for reference.
* __requirement.txt:__ Lists the Python libraries and dependencies required to run the project.

## Installation

### 1. __Clone the repository:__
```
git clone https://github.com/your_username/your_project_name.git
cd your_project_name
```

### 2. Install required packages:
Make sure you have Python installed. You can install the required dependencies by running:
```
pip install -r requirement.txt
```

## Usage
Use boolean_retrieval.py to search for terms in the document-term matrix.
```
python pre_processing_data.py
```

__Note:__ You can use _pre_processing_data.py_ and _doc-term_matrix_creation.py_ for cleaning your own datasets from the internet, it will give you insights.

## Future Work
* Enhance the boolean retrieval algorithm for more complex queries (e.g., phrase search, proximity search).
* Implement additional pre-processing techniques like stemming and stop-word removal.
* Extend the dataset and test scalability.
