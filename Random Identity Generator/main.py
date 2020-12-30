import random
import datetime

actual_year = datetime.datetime.now().year

#FILES

#MALE NAMES LIST
male_names = open('male_names.txt','r')
male_names_list = []
male_names_lines = male_names.readlines()
for line in male_names_lines:
    male_names_list.append(line.strip('\n').split('\n'))

#FEMALE NAMES LIST
female_names = open('female_names.txt', 'r')
female_names_list = []
female_names_lines = female_names.readlines()
for line in female_names_lines:
    female_names_list.append(line.strip('\n').split('\n'))

#JOB LIST
jobs = open('job_list.txt','r')
job_list = []
jobs_lines = jobs.readlines()
for line in jobs_lines:
    job_list.append(line.strip('\n').split('\n'))

#COUNTRIES LIST
countries = open('countries.txt', 'r')
countries_list = []
for line in countries:
    countries_list.append(line.strip('\n').split('\n'))

#CARS LIST
cars = open('cars.txt','r')
car_list = []
for line in cars:
    car_list.append(line.strip('\n').split('\n'))

possible_male_names = random.choice(male_names_list)
possible_female_names = random.choice(female_names_list)
possible_ages = random.randint(10,99)
possible_jobs = random.choice(job_list)
mail_domains = ['@gmail.com','@outlook.com','@yahoo.com']
possible_countries = random.choice(countries_list)
possible_phone_prefixes = ['+1','+34','+7','+33','+91','+44']
phone_numbers = str(random.randint(1,99)) + str(random.randint(1,99)) + str(random.randint(1,99))
possible_weight = random.randint(50,80)
possible_heigth = random.randint(150,190) / 100
possible_relationship = ['Single','Married','Not interested']
relationship_interests = ['Boys','Girls']
possible_car_makes = random.choice(car_list)
class Person:
    name = random.choice(possible_male_names or possible_female_names)
    age = possible_ages
    birth_year = actual_year - age
    job = random.choice(possible_jobs)
    email = name.lower() + str(birth_year) + random.choice(mail_domains)
    country = random.choice(possible_countries)
    phone = ''
    weight = str(possible_weight) + 'kg'
    heigth = str(possible_heigth) + 'm'
    relationship = random.choice(possible_relationship)
    interested = random.choice(relationship_interests)
    car = random.choice(possible_car_makes)

if Person.country == possible_countries[0] or Person.country == possible_countries[2]:
    Person.phone = possible_phone_prefixes[0] + phone_numbers
else:
    if Person.country == possible_countries[1]:
        Person.phone = possible_phone_prefixes[1] + phone_numbers
    else:
        if Person.country == possible_countries[3]:
            Person.phone = possible_phone_prefixes[3] + phone_numbers
        else:
            if Person.country == possible_countries[4]:
                Person.phone = possible_phone_prefixes[4] + phone_numbers
            else:
                if Person.country == possible_countries[5]:
                    Person.phone = possible_phone_prefixes[5] + phone_numbers
                else:
                    Person.phone = phone_numbers

if Person.relationship == possible_relationship[2]:
   Person.interested = 'Unkwon'

print('Name: ' + Person.name)
print('Age: ' + str(Person.age))
print('Birth Year: ' + str(Person.birth_year))
print('Job: ' + Person.job)
print('Email: ' + Person.email)
print('Country: ' + Person.country)
print('Phone Number: ' + Person.phone)
print('Car: ' + Person.car)
print('Weigth: ' + Person.weight)
print('Height: ' + Person.heigth)
print('Relationship: ' + Person.relationship)
print('Interested in: ' + Person.interested)