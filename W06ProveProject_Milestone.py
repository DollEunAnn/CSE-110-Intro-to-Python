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
    counter = 0
    # iterate data line by line
    for index, expectancy in enumerate(life_data):
        if counter >= 372:
            break

        # skipped the header
        if index == 0:
            continue
        # strip and split each into parts but comma
        per_expectancy = expectancy.strip().split(',')

        year = float(per_expectancy[3])
        country = per_expectancy[0]

        if year > years_max:
            years_max = year
            country_max = country
        
        if year < years_min and year > 0:
            years_min = year
            country_min = country
     
        counter += 1


print(f'The max life expectancy was in {country_max} with {years_max}')
print(f'The min life expectancy was in {country_min} with {years_min}')