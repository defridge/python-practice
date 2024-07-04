# age = int(input('Enter your age: '))

# if age >= 18:
#     print('You are old enough to drive!')
# elif age < 18:
#     years_left = 18 - age
#     print(f'You need {years_left} more years to learn to dive!')


# my_age = 33
# your_age = int(input("Enter your age: "))

# if your_age > my_age:
#     age_difference = your_age - my_age
#     if age_difference == 1:
#         print("You are 1 year older than me.")
#     else:
#         print(f"You are {age_difference} years older than me.")
# elif your_age < my_age:
#     age_difference = my_age - your_age
#     if age_difference == 1:
#         print("You are 1 year younger than me.")
#     else:
#         print(f"You are {age_difference} years younger than me.")
# else:
#     print("You and I are the same age.")


# a = int(input('Enter first number: '))
# b = int(input('Enter second number: '))

# if a > b:
#     print(f'{a} is greater then {b}')
# elif a < b:
#     print(f'{b} is greater then {a}')
# else:
#     print('Both numbers are the same')


# name = input('Enter your name here: ')
# score = int(input('Enter your test score here: '))

# if score >= 0 and score <= 49:
#     print('Grade: F')
# elif score >= 50 and score <= 59:
#     print('Grade: D')
# elif score >= 60 and score <= 69:
#     print('Grade: C')
# elif score >= 70 and score <= 89:
#     print('Grade: B')
# elif score >= 90 and score <= 100:
#     print('Grade: A')


# month = input('Please enter month here to get the season: ')

# if month == 'September' or month == 'October' or month == 'November':
#     print('The season is Autumn')
# elif month == 'December' or month == 'January' or month == 'February':
#     print('The season is Winter')
# elif month == 'March' or month == 'April' or month == 'May':
#     print('The season is Spring')
# elif month == 'June' or month == 'July' or month == 'August':
#     print('The season is Summer')
# else:
#     print('Invalid input')


# fruits = ['banana', 'orange', 'mango', 'lemon']

# new_fruit = input('Please enter fruit here: ')

# if new_fruit in fruits:
#     print(f'{new_fruit} already exist in the list')
# else:
#     fruits.append(new_fruit)
#     print(fruits)


# person = {
#     'first_name': 'Luke',
#     'last_name': 'Masterson',
#     'age': 33,
#     'country': 'Ireland',
#     'is_married': False,
#     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
#     'address': {
#         'street': 'Space street',
#         'zipcode': '02210'
#     }
# }

# # Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# if 'skills' in person:
#     skills = person['skills']
#     middle_index = len(skills) // 2
#     print(f'The middle skill is: {skills[middle_index]}')

# # Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# if 'skills' in person:
#     has_python = 'Python' in person['skills']
#     print(f'Does the person have Python skill? {has_python}')

# # Determine the person's title based on their skills
# if 'skills' in person:
#     skills = person['skills']
#     if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
#         print('He is a front end developer')
#     elif 'Node' in skills and 'Python' in skills and 'MongoDB' in skills:
#         print('He is a backend developer')
#     elif 'React' in skills and 'Node' in skills and 'MongoDB' in skills:
#         print('He is a fullstack developer')
#     else:
#         print('Unknown title')

# # If the person is married and if he lives in Finland, print the information in the following format:
# if person.get('is_married') and person.get('country') == 'Finland':
#     print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married.")
# else:
#     print(f"{person['first_name']} {person['last_name']} lives in {person['country']}.")
