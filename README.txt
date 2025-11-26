# CSV to TSV Merger

## Overview
A Python script that merges multiple CSV files from the current directory into a single TSV (tab-separated values) file. The script automatically finds all `.csv` files, extracts specific columns (`source`, `before`, `after`, and `distance`), and combines them into one output file.

## Requirements
- Python 3.10.18
- pandas 2.3.3

Install dependencies:
```
pip install pandas
```

**Note:** `os` and `glob` are standard libraries, so no additional installations are needed.

## Usage

1. Place the script in the directory containing your CSV files
2. Run the script:
   ```
   python merge_csv.py
   ```
3. The script will create a file named `merged_tsv` in the same directory

## What It Does

1. Scans the current directory for all `.csv` files
2. Reads each CSV file
3. Extracts only these columns: `source`, `before`, `after`, `distance`
4. Merges all data into a single dataset
5. Outputs the result as `merged_tsv` (tab-separated format)

## Output

- **Filename:** `merged_tsv` (no extension)
- **Format:** Tab-separated values (TSV)
- **Columns:** source, before, after, distance

## Example Console Output

```
Found 2 CSV file(s):
  - report_5699.csv
  - report_5458.csv

Processed: report_5699.csv
Number of rows: 150

Processed: report_5458.csv
Number of rows: 203

Success! Merged 2 file(s) into 'merged_tsv'
merged_tsv number of rows: 353
```

## Error Handling

- If no CSV files are found, the script will notify you and exit
- If a CSV file is missing required columns, an error message will be displayed
- Files with errors are skipped, and the script continues processing remaining files

## Notes

- The script processes **all** `.csv` files in the current directory
- All CSV files must contain the columns: `source`, `before`, `after`, and `distance`
- The output file overwrites any existing `merged_tsv` file
- A Jupyter notebook is included for experimentation and refinement

---
