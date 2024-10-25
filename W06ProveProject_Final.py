""" 
CSE 110 - Intro to Programming
W06 Prove: Project Final - Data Analysis
Dollete, Eunice Ann

"""
import csv

# over all
country_min = ''
life_year_min = 100

country_max = ''
life_year_max = -1

# interest year
i_country_min = ''
i_life_year_min = 100

i_country_max = ''
i_life_year_max = -1

# average
total_life_expectancy = 0.0
average_life_expectancy = 0.0
counter = 0

year_of_interest = input('Enter the year of interest: ')


with open("life-expectancy.csv") as life_data:
    # iterate data line by line, use enumerate to get index
    for index, expectancy in enumerate(life_data):
        # skipped the header
        if index == 0:
            continue
        # strip and split each line into parts - comma
        per_expectancy = expectancy.strip().split(',')
        #convert year into float
        life_years = float(per_expectancy[3])
        country = per_expectancy[0]
        year_date = per_expectancy[2]

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

        if year_date == year_of_interest:
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
    print(f'For the year {year_of_interest}:')
    print(f'The average life expectancy across all countries was {average_life_expectancy:.2f}')
    print(f'The max life expectancy was in {i_country_max} with {i_life_year_max}')
    print(f'The min life expectancy was in {i_country_min} with {i_life_year_min}')
    print('\n')
    print('==================================================================================================')
