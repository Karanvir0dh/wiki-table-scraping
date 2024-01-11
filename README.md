# Wikipedia Table Scraper

## Project Description
This Python-based web scraper extracts tables from Wikipedia articles and performs basic data analysis and visualization. It is designed to demonstrate web scraping, data cleaning, analysis, and visualization capabilities.

## Features
- **Web Scraping**: Extract tables from any Wikipedia article.
- **Data Cleaning**: Handle missing values and duplicates.
- **Data Analysis**: Perform basic statistical analysis.
- **Data Visualization**: Generate line plots for numerical data.
- **Custom Output**: Save scraped tables as CSV files with user-defined filenames.

## Installation
Ensure you have Python installed on your system. Install required libraries using:
```
pip install requests beautifulsoup4 pandas matplotlib
```

## Usage
1. Run `main.py`.
2. Enter the URL of a Wikipedia article when prompted.
3. Select the table number to scrape (if multiple are available).
4. View the basic analysis output in the console.
5. Enter a desired filename to save the table as a CSV.

## Code Structure
- `scraper.py`: Handles scraping of Wikipedia pages.
- `analysis.py`: Contains data cleaning, analysis, and visualization functions.
- `main.py`: The user interface for the scraper and analysis tools.
