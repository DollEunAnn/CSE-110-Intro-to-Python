""" 
CSE 110 - Intro to Programming
W06 Prove: Project Milestone - Data Analysis
Dollete, Eunice Ann

"""
import csv

#over all
country_min = ''
life_year_min = 100

country_max = ''
life_year_max = -1


with open("life-expectancy.csv") as life_data:
    # iterate data line by line, use enumerate to get index
    for index, expectancy in enumerate(life_data):
        # skipped the header
        if index == 0:
            continue
        # strip and split each line into parts - comma
        per_expectancy = expectancy.strip().split(',')
        #convert year into float
        life_year = float(per_expectancy[3])
        country = per_expectancy[0]

        # check the max
        if life_year > life_year_max:
            life_year_max = life_year
            country_max = country
        
        # check the min
        if life_year < life_year_min and life_year > 0:
            life_year_min = life_year
            country_min = country

print(f'The highest value for life expectancy was {life_year_max} years.')
print(f'The lowest value for life expectancy was {life_year_min} years.')