import csv
a=[
	{'name': 'Masha', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Vasya', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Eduard', 'age': 48, 'job': 'Big boss'},
  ]
with open('export.csv', 'w', encoding='utf-8', newline='') as f:
	fields = ['name', 'age', 'job']
	writer = csv.DictWriter(f, fields, delimiter=';')
	writer.writeheader()
	for user in a:
		writer.writerow(user)