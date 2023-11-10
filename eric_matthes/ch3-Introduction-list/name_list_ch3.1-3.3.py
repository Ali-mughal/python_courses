""" 3-1. Names: Store the names of a few of your friends in a list called names.
    Print each person’s name by accessing each element in the list, one at a time.
"""
""" 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name,
 print a message to them . The text of each mes-sage should be the same, but each message should be personalized with the person’s name  """


names = ['Ali', 'Zubair', 'Haider', 'Hamza']
for name in names:
    print(name)

""" 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name,
 print a message to them . The text of each mes-sage should be the same, but each message should be personalized with the person’s name  """

for name in names:
    print('Salam, My Good friend %s'% name)

""" 3-3. Your Own List: Think of your favorite mode of transportation, such as a motorcycle or a car, 
    and make a list that stores several examples. Use your list to print a series of statements about these items, such as “I would like to own a Honda motorcycle.”
"""

favorite_transportations = ['Railway', 'Ferry', 'AirPlan']
print('I would like to go {}'.format(favorite_transportations[0]))
print('I would like to go %s'% favorite_transportations[1])
