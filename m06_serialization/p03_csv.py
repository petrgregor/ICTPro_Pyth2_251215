import csv

from m04_oop.p03_person import Person

try:
    with open("data.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        #header = reader.__next__()
        header = next(reader)
        persons = []
        for row in reader:
            print(row)
            persons.append(Person(row[1], row[2], int(row[3])))
        print(persons)
except Exception as e:
    print(f"ERROR: {e}")

print("="*80)
try:
    with open("data.csv", "r", encoding="utf-8") as f:
        dict_reader = csv.DictReader(f)
        persons2 = []
        for row in dict_reader:
            print(row)
            persons2.append(Person(row[' name'], row[' surname'], int(row[' age'])))
        print(persons2)
except Exception as e:
    print(f"ERROR: {e}")

