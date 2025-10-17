numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]
print(squared_numbers)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
First_word = [name[0] for name in names]
short_names = [name.upper() for name in names if len(name) < 5]
print(First_word)
print(short_names)

range_list_multiplied = [x * 2 for x in range(1, 5)]
print(range_list_multiplied)