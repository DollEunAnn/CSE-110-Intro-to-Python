# Opening Files
""" courses_file = open('courses.txt') """

# opens and closes
""" with open('courses.txt') as courses_file:
    # Get the data from it
    for course in courses_file:
        print(course.strip())

# courses_file.close()

print('The file is closed now.')
 """

with open('books.txt') as books_file:
    for book in books_file:
        print(book.strip())


people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

#1
for person in people:
    print(person.strip())

#2

oldest_age = -1
oldest_name = '' 

youngest_age = 100
youngest_name = ''

for person in people:
    person_split = person.split() # put the line in an array
    print(person_split[0], end='-')
    print(person_split[1])

    name = person_split[0]
    age = int(person_split[1])

    if age > oldest_age:
        oldest_age = age
        oldest_name = name

    if age < youngest_age and age > 0:
        youngest_age = age
        youngest_name = name

    
print(f'the oldest is {oldest_age} - {oldest_name}')
print(f'the youngest is {youngest_age} - {youngest_name}')

