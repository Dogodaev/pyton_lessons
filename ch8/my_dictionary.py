my_dictionary = {}
my_dictionary['Дженни'] = '867-5309'

my_dictionary['Пол'] = '555-1201'
my_dictionary['Дейвид'] = '321-6617'
my_dictionary['Джейми'] = '771-0091'

my_dictionary['Джейми'] = '443-0000'
print (my_dictionary['Джейми'])

if 'Дженни' in my_dictionary:
    print('Номер телефона Дженни', my_dictionary['Дженни'])

print(my_dictionary)
if 'Джейми' in my_dictionary:
    del(my_dictionary['Джейми'])
    print()
print(my_dictionary)
