import pandas as pd

def createCountryDataframes(country_list, dataframes_list):
    """
    Create a DataFrame for each country with indicators as rows and years as columns.

    Parameters:
    - country_list: List of country names.
    - dataframes_list: List of DataFrames, each containing data for one indicator.

    Returns:
    - country_dfs: Dictionary where keys are country names and values are DataFrames with indicators as rows.
    """
    # Initialize a dictionary to hold the DataFrames for each country
    country_dfs = {}

    # Iterate over each country
    for country in country_list:
        # Create a list to hold series/data for the current country from each DataFrame
        country_data = []

        # Iterate over each DataFrame
        for df in dataframes_list:
            # Extract the row corresponding to the current country
            country_row = df[df['Country Name'] == country]

            if not country_row.empty:
                # Extract the series name and the yearly data
                series_name = country_row['Series Name'].values[0]
                data = country_row.drop(['Country Name','Series Name'], axis=1)

                # Create a DataFrame for this indicator
                indicator_df = pd.DataFrame(data.values, index=[series_name], columns=data.columns)
                country_data.append(indicator_df)

        # Concatenate all the data for the current country into a single DataFrame
        if country_data:
            combined_df = pd.concat(country_data)
            # Store the resulting DataFrame in the dictionary
            country_dfs[country] = combined_df

    return country_dfs