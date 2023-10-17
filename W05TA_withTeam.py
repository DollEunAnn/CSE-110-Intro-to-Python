number_list = []
user_input = ''
total_num = 0

print('Enter a list of numbers, type 0 when finished.')

while user_input != 0:
    user_input = int(input('Enter number: '))

    if user_input != 0:
        number_list.append(user_input)

print()

# sum
for num in number_list:
    total_num += num
print(f'The sum is: {total_num}')

# average
list_count = len(number_list)
average = total_num / list_count
print(f'The average is: {average}')

# largest number
largest = 0
for num in number_list:
    if num > largest:
        largest = num

print(f'The largest number is: {largest}')

# smallest number
smallest = largest

for num in number_list:
    if num < smallest and num > 0:
        smallest = num
print(f'The smallest positive number is: {smallest}')

# sort number
#sorted_list = sorted(number_list)
number_list.sort()

print('The sorted list: ')
#for num in sorted_list:
#    print(num)

for num in number_list:
    print(num)
