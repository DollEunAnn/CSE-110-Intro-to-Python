"""
Individual Activity

Please enter the following information:

First name: Jane
Last name: Doe
Email address: JaneDoe@email.com
Phone number: (208) 555-1234
Job title: chief software architect
ID Number: 83-23821

The ID Card is:
----------------------------------------
DOE, Jane
Chief Software Architect
ID: 83-23821

janedoe@email.com
(208) 555-1234
----------------------------------------
"""
#Ask input from the user
print('Please enter the following information:')
first_name = input('First Name: ')
last_name = input('Last_Name: ')
email_address = input('Email address: ')
phone_number = input('Phone Number: ')
job_title = input('Job Title: ')
id_number = input('ID Number: ')
#STRECH CHALLENGE
hair_color = input('Hair Color: ')
starting_month = input('Month Started: ')
eye_color = input('Eye Color: ')
training = input('Have you completed the advance training? (Yes/No): ')

#Displays the information
print()
print('The ID Card is:')
print('----------------------------------------')
print(f'{last_name.upper()},{first_name.capitalize()}')
print(job_title.title())
print(f'ID: {id_number}')
print()
print(f'{email_address.lower()}')
print(phone_number)
print()
#STRECH CHALLENGE
print(
    f"Hair: {hair_color.capitalize():<10} Eyes: {eye_color.capitalize()}"
    )
print(
    f"Month: {starting_month.capitalize():<9} Training: {training.capitalize()}"
)

print('----------------------------------------')

