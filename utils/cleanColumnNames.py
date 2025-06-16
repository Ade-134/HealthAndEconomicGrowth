def cleanColumnNames(df_list):
    # Check if the list is empty
    if not df_list:
        print("The list of DataFrames is empty.")
        return df_list
    
    # Iterate through each DataFrame in the list
    for i, df in enumerate(df_list):
        # Check if the DataFrame is None
        if df is None:
            print(f"DataFrame at index {i} is None and will be skipped.")
            continue
        
        # Check if the DataFrame has valid columns
        if not hasattr(df, 'columns'):
            print(f"Element at index {i} is not a DataFrame.")
            continue
        
        # Clean the column names by removing everything after ' ['
        df.columns = [col.split(' [')[0] for col in df.columns]
    
    return df_list
