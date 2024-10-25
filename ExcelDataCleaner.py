import pandas as pd

# Menu
print('Excel Data Cleaner')
print('Please put the excel file inside the folder to be executed.')
file_name = input('Please enter the filename: ')


# Read the Excel file
df = pd.read_excel(file_name)

# Split the names in column 2 into last name and first name
df[['Last Name', 'First Name']] = df['name'].str.split(',', expand=True)

# Strip whitespace from the new 'First Name' and 'Last Name' columns
df['Last Name'] = df['Last Name'].str.strip()
df['First Name'] = df['First Name'].str.strip()

# Rename the columns appropriately
df.rename(columns={'employee_number': 'Id', 'department': 'Department'}, inplace=True)

# Add email_address column
df['email_address'] = df['Last Name'].str.lower() + '@astoria.com.ph'

# Reorder the columns
df = df[['Id', 'Last Name', 'First Name', 'Department','email_address']]

# Save the cleaned data back to an Excel file
output_file_path = 'cleaned_data.xlsx'  # Replace with your desired output file path
df.to_excel(output_file_path, index=False)

print("Data cleaned and saved to", output_file_path)