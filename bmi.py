"""BMI script."""
family = []
addNew = True

while addNew:
    person = {}
    person['name'] = str(input('Type name: '))
    person['weight'] = float(input('Type weight: '))
    person['height'] = str(input('Type height: '))
    if '.' in person['height']:
        person['height'] = float(person['height'])
    else:
        person['height'] = int(person['height']) / 100
    person['bmi'] = round(person['weight'] / person['height'] ** 2, 2)
    family.append(person)
    addNextPerson = str(input('Add new person? [Y/n]: '))
    if addNextPerson.lower() != 'y':
        addNew = False
print("\n" + 'Family BMI:')
for familyPerson in family:
    print(familyPerson['name'] + ' BMI = ' + str(familyPerson['bmi']))
