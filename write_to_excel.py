import pandas as pd
import os

def excel_writer(records):
    # records is expected to be a list of dictionaries
    new_df = pd.DataFrame(records)
    file_name = 'dice_simulation.xlsx'
    
    if os.path.exists(file_name):
        try:
            existing_df = pd.read_excel(file_name)
            
            # Get the unique 'Total Trials' from the new data
            new_trials = new_df['Total Trials'].unique()
            
            # Remove existing rows that match the new 'Total Trials'
            existing_df = existing_df[~existing_df['Total Trials'].isin(new_trials)]
            
            # Concatenate the filtered existing data with the new data
            df = pd.concat([existing_df, new_df], ignore_index=True)
            
        except Exception as e:
            print(f"Could not read existing file: {e}")
            df = new_df
    else:
        df = new_df

    try:
        df.to_excel(file_name, index=False)
        print(f"Data saved to {file_name}")
    except PermissionError:
        print(f"Error: Permission denied. Please close '{file_name}' if it is open in Excel and try again.")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
