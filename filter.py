import pandas as pd

# Load the Excel file
# Replace with your file path
file_path = 'eunice_work/Employees_List_ForFiltering_New.xlsx'
sheet_name = 'Sheet1'          # Replace with your sheet name if necessary

# Read the Excel file
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Replace 'DepartmentCode' with the actual column name in your Excel file
unique_department_codes = df['Department Code'].unique()

# Convert to a list if needed
unique_department_codes_list = unique_department_codes.tolist()

# Print or save the unique department codes
print(unique_department_codes_list)
