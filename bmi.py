"""BMI script."""
family = []
addNew = True

while addNew:
    person = {}
    person['name'] = str(input('Type name: '))
    person['weight'] = float(input('Type weight: '))
    height = str(input('Type height: '))
    if '.' in height:
        height = float(height)
    else:
        height = int(height) / 100
    person['height'] = height
    person['bmi'] = round(person['weight'] / person['height'] ** 2, 2)
    family.append(person)
    addNextPerson = str(input('Add new person? [Y/n]: '))
    if addNextPerson.lower() != 'y':
        addNew = False
print("\n" + 'Family BMI:')
for familyPerson in family:
    print(familyPerson['name'] + ' BMI = ' + str(familyPerson['bmi']))
