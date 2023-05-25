x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)
# Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"
print(students)
# In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres"
print(sports_directory)
# Change the value 20 in z to 30
z[0]["y"] = 30
print(z)
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.
passengers_upgraded = [
{'first_name':  'Greg', 'last_name' : 'Fichoux', 'nationality' : 'FRA', 'cabin' : 'C', 'seat' : '11D'},
{'first_name' : 'Michael', 'last_name' : 'Wilkinson', 'nationality' : 'NZL', 'cabin' : 'Y', 'seat' : '42K'},
{'first_name' : 'Angele', 'last_name' : 'Van Laeken', 'nationality' : 'BEL', 'cabin' : 'F', 'seat' : '1A'},
{'first_name' : 'Clark', 'last_name' : 'James', 'nationality' : 'USA', 'cabin' : 'C', 'seat' : '8H'},
]
def hospitality(seat, passengers):
    for passenger in passengers_upgraded:
        print(passenger['seat'])
hospitality('seat', 'passengers_upgraded')

#  Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:
one_world = {
    'locations': ['USA', 'UK', 'Hong Kong', 'Finland', 'Spain', 'Japan', 'Morocco', 'Sri Lanka', 'Australia', 'Malaysia', 'Qatar', 'Joradan'],
    'airlines': ['Alaska Airlines', 'American Airlines', 'British Airways', 'Cathay Pacific', 'Finnair', 'Iberia', 'Japan Airlines', 'Malaysia Airlines', 'QANTAS', 'Royal Air Maroc', 'Royal Jordanian', 'Sri Lankan Airlines']
}

def print_member_stats(alliance):
    for key in alliance:
        print(f'{len(key)} {key.upper()}')
        for value in alliance[key]:
            print(" " + value)

print_member_stats(one_world)