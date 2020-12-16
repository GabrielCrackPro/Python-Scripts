import random
import datetime

actual_year = datetime.datetime.now().year

possible_male_names = ['Fredrick','John','Coleman','Johan','Raymond']
possible_female_names = ['Gaelle', 'Leilany','Ann','Alison','Pam']
possible_ages = random.randint(20,60)
possible_jobs = ['Student', 'Taxi Driver','Bus Driver','Teacher','Programmer','Chef','Caisher']
mail_domains = ['@gmail.com','@outlook.com','@yahoo.com']
possible_countries = ['EE.UU','Spain','Canada','Russia','France','India','England']
possible_phone_prefixes = ['+1','+34','+7','+33','+91','+44']
phone_numbers = str(random.randint(1,99)) + str(random.randint(1,99)) + str(random.randint(1,99))
possible_weight = random.randint(50,80)
possible_heigth = random.randint(150,190) / 100
possible_relationship = ['Single','Married','Not interested']
relationship_interests = ['Boys','Girls']
class Person:
    name = random.choice(possible_male_names)
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

if Person.relationship == possible_relationship[2]:
    relationship_interests = 'Unkwon'

print('Name: ' + Person.name)
print('Age: ' + str(Person.age))
print('Birth Year: ' + str(Person.birth_year))
print('Job: ' + Person.job)
print('Email: ' + Person.email)
print('Country: ' + Person.country)
print('Phone Number: ' + Person.phone)
print('Weigth: ' + Person.weight)
print('Height: ' + Person.heigth)
print('Relationship: ' + Person.relationship)
print('Interested in: ' + Person.interested)