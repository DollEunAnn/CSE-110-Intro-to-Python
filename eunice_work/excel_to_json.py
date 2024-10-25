import pandas as pd

# Load the Excel file
excel_file = 'list_support_type.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file)

# Convert the DataFrame to a JSON string
json_str = df.to_json(orient='records', indent=4)

# Save the JSON string to a file
with open('support_types.json', 'w') as json_file:
    json_file.write(json_str)

print("Excel file has been converted to JSON and saved as 'output.json'.")