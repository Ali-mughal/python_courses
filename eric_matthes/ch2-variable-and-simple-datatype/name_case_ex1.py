"""
2-3. Personal Message: Store a person’s name in a variable,
 and print a message to that person . Your message should be simple,
  such as, “Hello Eric, would you like to learn some Python today?”
"""
person_name = 'Ali'
message = "Hello %s, would you like to learn some Python today" % person_name

"""
2-4. Name Cases: Store a person’s name in a variable,
 and then print that per-son’s name in lowercase, uppercase, and titlecase 
"""
print(person_name.lower())
print(person_name.upper())
print(person_name.title())


"""2-5. Famous Quote: Find a quote from a famous person you admire.
Print the quote and the name of its author.Your output should look something like the following,
including the quotation marks:Albert Einstein once said,
 “A person who never made a mistake never tried anything new.”"""
print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')

"""
2-6. Famous Quote 2: Repeat Exercise 2-5, but this time store the famous per-son’s name in a variable called famous_person.
Then compose your message and store it in a new variable called message.
 Print your message .
"""
famous_person = 'Albert Einstein'
message_quote = famous_person + ' once said, “A person who never made a mistake never tried anything new.”'
print(message_quote)
"""2 -7.Stripping Names: Store a person’s name, and include some whitespace characters at the beginning and end of the name.
Make sure you use each character combination, "\t" and "\n", at least once.
Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, 
lstrip(), rstrip(), and strip().
"""
my_name = " \t Ali Raza  "
print(my_name)
print(my_name.strip())
