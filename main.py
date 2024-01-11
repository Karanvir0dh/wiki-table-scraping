from scraper import scrape_all_tables, save_table_to_csv
from analysis import clean_data, analyze_data, visualize_data

def main():
    print("Web Scraper for Wikipedia Tables")
    url = input("Enter the URL of the Wikipedia page: ")

    tables = scrape_all_tables(url)

    if tables:
        print(f"{len(tables)} tables found. Enter the number of the table to save (1-{len(tables)}):")
        table_number = int(input()) - 1

        if 0 <= table_number < len(tables):
            table_df = tables[table_number]
            print("\nSelected Table Preview:")
            print(table_df.head())

            # Data cleaning and analysis
            cleaned_df = clean_data(table_df)
            analyze_data(cleaned_df)
            visualize_data(cleaned_df)

            # Saving the table to CSV
            filename = input("Enter the desired name for the output file (without extension): ") + '.csv'
            save_table_to_csv(cleaned_df, filename)
        else:
            print("Invalid table number.")
    else:
        print("Failed to scrape tables from the provided URL.")

if __name__ == "__main__":
    main()
