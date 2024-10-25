# import pandas as pd

# # Load the Excel file
# excel_file = 'eunice_work/additional_employees.xlsx'


# # Read the Excel file into a DataFrame
# df = pd.read_excel(excel_file)

# # Convert the DataFrame to a JSON string
# json_str = df.to_json(orient='records', indent=4)

# # Save the JSON string to a file
# with open('additional_employees.json', 'w') as json_file:
#     json_file.write(json_str)

# print("Excel file has been converted to JSON and saved as 'output.json'.")


# with a specific column lookup
import pandas as pd

# Load the Excel file
excel_file = 'eunice_work/AVLCI.xlsx'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file)

# Filter rows where 'seed_batch' column has a value of 1
filtered_df = df[df['property_code'] == 'AVLCI']

# Convert the filtered DataFrame to a JSON string
json_str = filtered_df.to_json(orient='records', indent=4)

# Save the JSON string to a file
with open('additional_employees_SPR.json', 'w') as json_file:
    json_file.write(json_str)

print("Filtered rows with 'seed_batch' value of 2 have been converted to JSON and saved.")
