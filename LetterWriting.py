
names_storage= []
with open('NamesToSent/invited_names.txt') as f:
  for x in f:
    print(x.strip())
    names_storage.append(x.strip())

print(names_storage)

with open('Letter_Format/letter_format.txt') as template_file:
    template = template_file.read()

for name in names_storage:
    personalized_letter = template.replace('{name}', name)
    output_path = f'LetterOutput/letter_for_{name}.txt'
    print(personalized_letter)
    with open(output_path, 'w') as output_file:
        output_file.write(personalized_letter)
