"""
W05 Team Activity: Lists of Numbers
Dollete, Eunice Ann

"""

number_list = []
add_number = ''
total_num = 0

print('Enter list of numbers, type 0 when finished.')

while add_number != 0:
    add_number = int(input('Enter number: '))

    if add_number != 0:
        number_list.append(add_number)

# sum of all numbers
for num in number_list:
    total_num += num

print(f'The sum is: {total_num}')

#average
count_of_num =  len(number_list)
average = total_num / count_of_num

print(f'The average is: {average}')

# largest number
largest = number_list[0]

for num in number_list:
    if num > largest:
        largest = num

print(f'The largest number is: {largest}')


# smallest positive
smallest = number_list[0]

for num in number_list:
    if num < smallest and num > 0:
        smallest = num
print(f'The smallest positive number is: {smallest}')


# sorted list
sorted_list = sorted(number_list)

for num in sorted_list:
    print(num)