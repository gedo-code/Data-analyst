import pandas as pd

# Read the Excel file
xls = pd.ExcelFile('sampledata.xlsx')

# Create a dictionary to store DataFrames for each sheet
dfs = {}

# Iterate over each sheet in the Excel file
for sheet_name in xls.sheet_names:
    # Read the sheet into a DataFrame
    df = xls.parse(sheet_name)

    # Create a list to store the modified rows
    modified_rows = []

    # Iterate over each row in the original DataFrame
    for _, row in df.iterrows():
        # Append the current row to the modified rows list
        modified_rows.append(row.to_dict())

        # Add four empty rows
        for i in range(1, 5):
            empty_row = {df.columns[0]: ['القيمة الاولي', 'القيمة الثانية', 'القيمة الثالثة', 'القيمة الرابعة'][i-1]}
            modified_rows.append(empty_row)

    # Create the modified DataFrame for the current sheet
    modified_df = pd.DataFrame(modified_rows)

    # Add the modified DataFrame to the dictionary
    dfs[sheet_name] = modified_df

# Save the modified sheets to a new Excel file
with pd.ExcelWriter('expanded_file.xlsx') as writer:
    for sheet_name, df in dfs.items():
        df.to_excel(writer, sheet_name=sheet_name, index=False)
