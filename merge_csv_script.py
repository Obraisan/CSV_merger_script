

import pandas as pd
import glob
import os

# Get the current working directory
current_dir = os.getcwd()


# Find all CSV files in the current directory
csv_files = glob.glob(os.path.join(current_dir, "*.csv"))

if not csv_files:
    print("No CSV files found in the current directory.")
else:
    print(f"Found {len(csv_files)} CSV file(s):")
    for file in csv_files:
        print(f"  - {os.path.basename(file)}")
    
    # Read and merge all CSV files
    all_data = []
    for file in csv_files:
        try:
            df = pd.read_csv(file)
            # Keep only the required columns
            df = df[['source', 'before', 'after', 'distance']]
            all_data.append(df)
            
            print(f"\nProcessed: {os.path.basename(file)}")
            print(f"Number of rows: {len(df)}\n")
        except Exception as e:
            print(f"Error processing {os.path.basename(file)}: {e}")
    
    if all_data:
        # Combine all dataframes
        merged = pd.concat(all_data, ignore_index=True)
        
        # Save as TSV file with the name "merged_tsv"
        output_file = os.path.join(current_dir, "merged_tsv")
        merged.to_csv(output_file, sep='\t', index=False)
        
        print(f"\nSuccess! Merged {len(all_data)} file(s) into 'merged_tsv'")
        print(f"merged_tsv number of rows: {len(merged)}")
    else:
        print("No data to merge.")