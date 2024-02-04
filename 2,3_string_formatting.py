# JOINING STRINGS

list = ['barney', 'george', 'jack', 'laurie', 'tom']

print('Instead of doing this:')

for x in list:
	print('Hello ' + x)

print('\n' + 'Actually do this:')

for x in list:
	statement = ' '.join(['Hello', x]) #Join takes one argument, so make that argument a list
	print(statement)


# STRING COCATENATION

#if you want the user to input some data for you, do it like this (not with the %s method):

print('____ bought __ ____')
who = input('Who? ')
how_many = input('How many? ')
what = input('what? ')

print('{} bought {} {}'.format(who, how_many, what.lower()))