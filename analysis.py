import matplotlib.pyplot as plt

def clean_data(df):
    """
    Perform basic data cleaning on a DataFrame.

    Args:
    df (pandas.DataFrame): DataFrame to clean.

    Returns:
    pandas.DataFrame: Cleaned DataFrame.
    """
    # Dropping rows with missing values and removing duplicates
    df = df.dropna().drop_duplicates()
    return df

def analyze_data(df):
    """
    Perform basic data analysis on a DataFrame.

    Args:
    df (pandas.DataFrame): DataFrame to analyze.
    """
    # Displaying descriptive statistics for numeric columns
    print("\nDescriptive Statistics:")
    print(df.describe())

def visualize_data(df):
    """
    Visualize data in the DataFrame using Matplotlib.

    Args:
    df (pandas.DataFrame): DataFrame to visualize.
    """
    # Plotting only if DataFrame has numeric data
    if not df.empty and df.select_dtypes(include='number').any(axis=None):
        df.select_dtypes(include='number').plot(kind='line')
        plt.show()
    else:
        print("No numeric data available for visualization.")
