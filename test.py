import csv

f = open("KEN_ALL_ROME.CSV", "r")
reader = csv.reader(f)

city = 'error'

for i in reader:
	if i[0] == '0640941':
		city = i[3].decode('shift-jis')
		break

print city
