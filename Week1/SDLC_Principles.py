# Step 1: Raw / Messy Code (Before Principles)

# Messy code – not modular, not reusable, hard to maintain
import pandas as pd
from typing import List, cast
import random

numbers = [random.randint(1, 100) for _ in range(10)]
print("Generated numbers:", numbers)

# Calculate average
total = 0
for n in numbers:
    total += n
average = total / len(numbers)
print("Average:", average)

# Find max
max_num = numbers[0]
for n in numbers:
    if n > max_num:
        max_num = n
print("Max:", max_num)


"""
🔴 Problems:

No functions (not modular).

Can’t reuse logic elsewhere.

Hard to extend (e.g., adding min/median).

Not scalable (works only for small lists).

No error handling (reliability issue).

No comments/documentation.
"""

# Step 2: Refactored Code (With Principles)


def generate_numbers(count: int, lower: int = 1, upper: int = 100) -> List[int]:
    """Generate a list of random integers."""
    return [random.randint(lower, upper) for _ in range(count)]


def calculate_average(numbers: List[int]) -> float:
    """Return the average of a list of numbers."""
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    return sum(numbers) / len(numbers)


def find_max(numbers: List[int]) -> int:
    """Return the maximum number from a list."""
    if not numbers:
        raise ValueError("List of numbers cannot be empty")
    return max(numbers)


if __name__ == "__main__":
    # Example workflow (can be reused in other projects)
    nums = generate_numbers(10)
    print("Generated numbers:", nums)
    print("Average:", calculate_average(nums))
    print("Max:", find_max(nums))

"""
✅ Improvements:

Modularity: Code broken into functions.

Reusability: Functions can be used in any project.

Maintainability: Easy to add min/median later.

Scalability: Can handle larger datasets (just change count).

Reliability & Quality: Error handling included.

Security & Trust: Checks against empty input.

Collaboration: Docstrings/comments make it understandable for teams.
"""

# Classroom Activity

# Step 1: Raw / Messy Pandas Code


# Load CSV
df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Print average sepal length
avg = df['sepal_length'].mean()
print("Average sepal length:", avg)

# Print max petal width
mx = df['petal_width'].max()
print("Max petal width:", mx)

# Filter rows where species is setosa
print(df[df['species'] == 'setosa'].head())

"""
🔴 Problems:

All logic in one block → not modular.

Hard to reuse functions for other datasets.

No error handling → breaks if column names change.

Not scalable (imagine working on multiple CSVs).

No documentation → not good for collaboration.
"""

# Step 2: Refactored Pandas Code (With Principles)
# I'm applying the same idea as the numbers example above: instead of one
# big block of code, I split each task into its own function so it's
# easier to read, test, and reuse with a different CSV/columns later.


def load_dataset(url: str) -> pd.DataFrame:
    """Load a CSV file from a URL into a DataFrame."""
    return pd.read_csv(url)


def column_average(df: pd.DataFrame, column: str) -> float:
    """Return the mean of a numeric column."""
    # Checking the column exists first, otherwise pandas throws a
    # confusing KeyError that doesn't say what actually went wrong.
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataset")
    return df[column].mean()


def column_max(df: pd.DataFrame, column: str) -> float:
    """Return the maximum value of a numeric column."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataset")
    return df[column].max()


def filter_by_value(df: pd.DataFrame, column: str, value: str) -> pd.DataFrame:
    """Return only the rows where `column` equals `value`."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in dataset")
    # loc[] is typed by pandas-stubs as Series | DataFrame even though a
    # DataFrame boolean mask always returns a DataFrame here, so I cast it.
    return cast(pd.DataFrame, df.loc[df[column] == value])


if __name__ == "__main__":
    # Same workflow as before, just using the functions instead of
    # writing the logic inline. If I get a different dataset later
    # (not iris), I just change these variables/URL, not the functions.
    IRIS_URL = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

    iris_df = load_dataset(IRIS_URL)
    print("Average sepal length:", column_average(iris_df, "sepal_length"))
    print("Max petal width:", column_max(iris_df, "petal_width"))
    print(filter_by_value(iris_df, "species", "setosa").head())

"""
✅ Improvements (same principles as the numbers example):

Modularity: Loading, aggregating and filtering are now separate functions.

Reusability: Same functions work with any CSV, not just iris.csv.

Maintainability: If I need median/min later, I just add one more function.

Scalability: Easy to loop this over multiple CSV files/columns.

Reliability & Quality: Raises a clear error if a column name doesn't exist.

Collaboration: Docstrings explain what each function does for teammates.
"""
