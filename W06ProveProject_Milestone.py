""" 
CSE 110 - Intro to Programming
W06 Prove: Project Milestone - Data Analysis
Dollete, Eunice Ann

"""
import csv

country_min = ''
years_min = 100

country_max = ''
years_max = -1



with open("life-expectancy.csv") as life_data:
    # iterate data line by line
    for expectancy in life_data:
        #print(expectancy)

        # split each into parts
        per_expectancy = expectancy.split()
        #print(per_expectancy)

        # find the lowest expectancy and highest expectancy
        string_year = per_expectancy[-1]
        year = float(string_year)
        country = per_expectancy[0]

        if year > years_max:
            year_max = year
            country_max = country
        
        if year < years_min and year > 0:
            year_min = year
            country_min = country


print(f'The max life expectancy was in {country_max} with {years_max}')
print(f'The min life expectancy was in {country_min} with {years_min}')