"""
W06 Team Activity: Human Resource System - Strecht
Dollete, Eunice Ann

"""

with open('hr_system.txt') as hr_list:
    for emp_list in hr_list:
        #print(employee)

        #1 split the date into array
        employee = emp_list.split()

        #2 get the name of the employee only
        #print(employee[0])

        #3 get the name and format and add details
        #1 strip
        #print(f'Name: {employee[0].strip()}, Title: {employee[2].strip()}')

        # name (ID: id_number), job_title - $salary
        # salary to int
        salary = int(employee[3])
        salary = salary * 2

        print(f'{employee[0]} (ID:{employee[1]}), {employee[2]} - ${salary:.2f}')