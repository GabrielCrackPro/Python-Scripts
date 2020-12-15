import random
import datetime

actual_year = datetime.datetime.now().year

possible_male_names = ['Fredrick','John','Coleman','Johan','Raymond']
possible_female_names = ['Gaelle', 'Leilany','Ann','Alison','Pam']
possible_ages = random.randint(20,60)
possible_jobs = ['Student', 'Taxi Driver','Bus Driver','Teacher','Programmer','Chef','Caisher']
mail_domains = ['@gmail.com','@outlook.com','@yahoo.com']
possible_countries = ['EE.UU','Spain','Canada','Russia','France','India','England']
class Person:
    name = random.choice(possible_male_names)
    age = possible_ages
    birth_year = actual_year - age
    job = random.choice(possible_jobs)
    email = name.lower() + str(birth_year) + random.choice(mail_domains)
    country = random.choice(possible_countries)
print(Person.name)
print(Person.age)
print(Person.birth_year)
print(Person.job)
print(Person.email)
print(Person.country)