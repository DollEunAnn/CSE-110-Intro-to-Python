""" 
CSE 110 - Intro to Programming
W06 Prove: Project Final Creativity - Data Analysis
Dollete, Eunice Ann

"""
# I imported statistics to use the built-in formular for median and mode which I included as additional information
# I added a way for the user can choose between what interest of data they want either country or year. A while loop and if-else will handle invalid option too

import csv, statistics

# over all
country_min = ''
life_year_min = 100
country_max = ''
life_year_max = -1

# interest
year_of_interest = ''
country_of_interest = ''
interest = ''
i_country_min = ''
i_life_year_min = 100
i_country_max = ''
i_life_year_max = -1
choice = 0
country_code = ''

# average
total_life_expectancy = 0.0
average_life_expectancy = 0.0
counter = 0

# statistics
interest_column_values = []
median = 0.0
mode = 0.0


print('Select an option:')
print('1. Get data by year')
print('2. Get data by country')
print()

while choice not in [1,2]:
    choice = int(input('Enter your choice (1 or 2): '))

    if choice == 1:
        interest = 'year'
        print()
        year_of_interest = input('Enter the year of interest: ')
    elif choice == 2:
        interest = 'country'
        print()
        country_of_interest = input('Enter the country of interest:')
    else:
        print('Invalid choice. Please enter 1 or 2.')
        print()
    

with open('life-expectancy.csv') as life_data:
    # iterate data line by line, use enumerate to get index
    for index, expectancy in enumerate(life_data):
        # skipped the header
        if index == 0:
            continue
        # strip and split each line into parts by comma
        per_expectancy = expectancy.strip().split(',')

        country = per_expectancy[0]
        country_code = per_expectancy[0]
        year_date = per_expectancy[2]
        #convert year into float
        life_years = float(per_expectancy[3])

        # check the max
        if life_years > life_year_max:
            life_year_max = life_years
            country_max = country
            year_date_max = year_date
        
        # check the min
        if life_years < life_year_min and life_years > 0:
            life_year_min = life_years
            country_min = country
            year_date_min = year_date

        # year
        if choice == 1:
            if year_date == year_of_interest:
                interest_column_values.append(life_years)
        
                # statistics
                # mean = statistics.mean(interest_column_values)
                median = statistics.median(interest_column_values)
                mode = statistics.mode(interest_column_values)
            
                # check the max
                if life_years > i_life_year_max:
                    i_life_year_max = life_years
                    i_country_max = country
                
                # check the min
                if life_years < i_life_year_min and life_years > 0:
                    i_life_year_min = life_years
                    i_country_min = country
                
                #compute the average
                counter += 1
                total_life_expectancy += life_years                    
                average_life_expectancy = total_life_expectancy / counter

        # country  
        if choice == 2:
            if country.lower() == country_of_interest.lower():
                interest_column_values.append(life_years)

                # statistics
                #mean = statistics.mean(interest_column_values)
                median = statistics.median(interest_column_values)
                mode = statistics.mode(interest_column_values)
        
                # check the max
                if life_years > i_life_year_max:
                    i_life_year_max = life_years
                    i_country_max = country
                
                # check the min
                if life_years < i_life_year_min and life_years > 0:
                    i_life_year_min = life_years
                    i_country_min = country
                
                #compute the average
                counter += 1
                total_life_expectancy += life_years                    
                average_life_expectancy = total_life_expectancy / counter

    print()
    print(f'The overall max life expectancy is: {life_year_max} from {country_max} in {year_date_max}')
    print(f'The overall min life expectancy is: {life_year_min} from {country_min} in {year_date_min}')
    print()

    if interest == 'year':
        print(f'For the year {year_of_interest}:')
        print(f'The average life expectancy across all countries was {average_life_expectancy:.2f}')
        print(f'The max life expectancy was in {i_country_max} with {i_life_year_max}')
        print(f'The min life expectancy was in {i_country_min} with {i_life_year_min}')
    else:
        print(f'For the country {country_of_interest.title()}:')
        print(f'The average life expectancy across {country_of_interest.title()} was {average_life_expectancy:.2f}')
        print(f'The max life expectancy was {i_life_year_max}')
        print(f'The min life expectancy was {i_life_year_min}')

    print()
    print(f'Additional Information:')
    print(f'The median life expectancy is {median:.2f} years')
    print(f'The most frequent life expectancy is {mode:.2f} years')
    print()