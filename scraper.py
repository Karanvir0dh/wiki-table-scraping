import requests
from bs4 import BeautifulSoup
from io import StringIO
import pandas as pd

def scrape_all_tables(url, table_class="wikitable"):
    """
    Scrape all tables from a given Wikipedia URL.
    
    Args:
    url (str): URL of the Wikipedia page to scrape.
    table_class (str): Class name of the tables to scrape.

    Returns:
    list of pandas.DataFrame: List of all scraped tables as DataFrames.
    """
    try:
        # Sending a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Checks if the request was successful

        # Parsing the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Finding all tables with the specified class
        tables = soup.find_all('table', {'class': table_class})
        if not tables:
            raise ValueError("No tables found with the specified class")

        # Converting each HTML table to a pandas DataFrame
        return [pd.read_html(StringIO(str(table)))[0] for table in tables]
    except requests.exceptions.RequestException as e:
        print(f"Error while requesting the webpage: {e}")
        return None
    except ValueError as ve:
        print(ve)
        return None

def save_table_to_csv(df, filename):
    """
    Save a DataFrame to a CSV file.

    Args:
    df (pandas.DataFrame): DataFrame to save.
    filename (str): Name of the file to save the DataFrame.
    """
    df.to_csv(filename, index=False, encoding='utf-8-sig')
    print(f"Table saved to {filename}")
