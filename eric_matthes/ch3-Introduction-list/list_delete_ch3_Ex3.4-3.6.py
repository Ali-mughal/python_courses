"""
3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who would you invite?
 Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person,
 inviting them to dinner
"""

guests = ['Ali', 'Zubair', 'Haider', 'Hamza']

for guest in guests:
    print('I would like to Invite you in dinner %s' % guest)

"""
3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner,
 so you need to send out a new set of invitations. You’ll have to think of
  someone else to invite.
  • Start with your program from Exercise 3-4. Add a print statement at the end of your
    program stating the name of the guest who can’t make it.
  • Modify your list, replacing the name of the guest who can’t make it with 
    the name of the new person you are inviting.
  • Print a second set of invitation messages, one for each person who is still in your list
"""
removed_guest = guests.pop(2)
print('\n sorry ' + removed_guest.title()+" can't make the dinner")
guests.insert(2, 'Habi')
for guest in guests:
    print(guest.title() + " Please come to Dinner")

""" 3-6. More Guests: You just found a bigger dinner table, so now more space is
    available. Think of three more guests to invite to dinner.
    •	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
    statement to the end of your program informing people that you found a
    bigger dinner table.
    •	 Use insert() to add one new guest to the beginning of your list.
    •	 Use insert() to add one new guest to the middle of your list.
    •	 Use append() to add one new guest to the end of your list.
    •	 Print a new set of invitation messages, one for each person in your list."""

# removing element from list by passing the element name

