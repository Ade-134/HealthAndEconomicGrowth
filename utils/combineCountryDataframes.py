import pandas as pd

def combineCountryDataframes(country_dfs):
    """
    Combine country DataFrames into a single DataFrame with 'Country Name', 'Country Code', 'Year', and indicators as columns.

    Parameters:
    - country_dfs: Dictionary where keys are country names and values are DataFrames with indicators as rows, and 'Country Code' as a column.

    Returns:
    - combined_df: A combined DataFrame with 'Country Name', 'Country Code', 'Year', and indicators as columns.
    """
    # List to store DataFrames
    dataframes = []

    # Iterate over each country and its DataFrame
    for country, df in country_dfs.items():
        # Reset index to get indicators as a column
        df_reset = df.reset_index()

        # Melt the DataFrame to have 'Year' as a column
        df_long = df_reset.melt(id_vars=['index', 'Country Code'], var_name='Year', value_name='value')

        # Pivot the DataFrame to have indicators as columns
        df_pivot = df_long.pivot_table(index=['Year', 'Country Code'], columns='index', values='value', aggfunc='first')

        # Add country name column
        df_pivot['Country Name'] = country

        # Reset index to have 'Year' and 'Country Code' as columns
        df_pivot.reset_index(inplace=True)

        # Append to the list of DataFrames
        dataframes.append(df_pivot)

    # Concatenate all DataFrames
    combined_df = pd.concat(dataframes, ignore_index=True)

    # Reorder columns to have 'Country Name', 'Country Code', 'Year', followed by indicators
    columns = ['Country Name', 'Country Code', 'Year'] + [col for col in combined_df.columns if col not in ['Country Name', 'Country Code', 'Year']]
    combined_df = combined_df[columns]

    return combined_df
