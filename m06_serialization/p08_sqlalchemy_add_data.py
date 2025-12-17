import sqlalchemy
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker

from m06_serialization.models import Student

db = sqlalchemy.create_engine("sqlite:///C:/Users/Student/PycharmProjects/ICTPro_Pyth2_251215/m06_serialization/school.db")

Session = sessionmaker(bind=db)
session = Session()

"""adam = Student("Adam", "Bernau", 12)
session.add(adam)
session.commit()"""

"""session.add(Student("Bedřich", "Novotný", 35))
session.commit()"""

"""session.add_all(
    [
        Student("Cyril", "Blažek", 25),
        Student("Dana", "Nováková", 24),
        Student("Eva", "Farná", 29)
    ]
)
session.commit()"""

print("All students:")
students = session.query(Student).all()
for student in students:
    print(student)

print("Count of students:")
count = session.query(Student).count()
print(f"Count = {count}")

print("Student with id=3:")
student3 = session.query(Student).filter(Student.id == 3)[0]
print(student3)

print("All students with name 'Eva':")
students_eva = session.query(Student).filter(Student.name == 'Eva')
for student in students_eva:
    print(student)

print("All students older 25 years:")
students = session.query(Student).filter(Student.age > 25)
for student in students:
    print(student)

print("All students with surname starts with 'N':")
students = session.query(Student).filter(Student.surname.like("N%"))
for student in students:
    print(student)

print("All students older 25 years with surname starts with 'N':")
students = session.query(Student).filter(Student.age > 25).filter(Student.surname.like("N%"))
for student in students:
    print(student)

print("All students older 25 years with surname starts with 'N':")
students = session.query(Student).filter(Student.age > 25, Student.surname.like("N%"))
for student in students:
    print(student)

print("All students older 25 years or with surname starts with 'N':")
students = session.query(Student).filter(or_(Student.age > 25, Student.surname.like("N%")))
for student in students:
    print(student)
