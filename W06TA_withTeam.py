"""
Team Activity

"""

with open('hr_system.txt') as hr_system_file:
    for employee in hr_system_file:
        # 1 print line by line
        #print(employee)

        # 2 names only
        employee_split = employee.strip().split()
        #print(employee_split)
        #print(employee_split[0])

        # 3 
        print(f'Name: {employee_split[0]}, Title: {employee_split[2]}')

