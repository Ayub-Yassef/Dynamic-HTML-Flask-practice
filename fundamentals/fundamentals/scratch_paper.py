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