# Dictionaries, Oh Lovely Dictionaries
# Creating a mapping of state to abbreviation
from __future__ import annotations
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

# Create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

# Add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Print out some cities
print('-' * 10)
print('NY State has: ', cities['NY'])
print('OR State has: ', cities['OR'])

# Print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# Do it by using the state then cities dictionaries
print('-' * 10)
print('Michigan has: ', cities[states['Michigan']])
print('Florida has: ', cities[states['Florida']])

# Print every state abbreviation
print('-' * 10)
for state, abbrev in states.items():
    print(f"{state} is abbreviated {abbrev}")

# Print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print(f"{abbrev} has the city {city}")

# Now do both at the same time
print('-' * 10)
for state, abrrev in list(states.items()):  # can be done in two ways
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has the city {cities[abbrev]}")

print('-' * 10)
# Safely get a abrreviation by state that might not be there
state = states.get('Texas')

if not state:
    print('Sorry, no Texas.')

# Get a city with a default value
city = cities.get('TX', 'Does Not Exit')
print(f"The city for the state 'TX' is: {city}")

# for key in states.keys():
#     print(key)
#     if key == 'California':
#         print("true")
#     else:
#         print("false")

# if input("enter state : ") in states.keys():
#      print("true")
# else:
#      print("false")
