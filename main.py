# # Створити ієрархію класів для опису академії.
# #
# # Зразковий список класів: Person, Teacher, Student, Subject, Academy і т.д.
# #
# # Продумати архітектуру: реалізувати принципи ООП
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f"Name: {self.name}\n Age: {self.age}")
#
#
# class Student(Person):
#     def __init__(self, name, age, university=0):
#         super().__init__(name, age)
#         self.university = university
#
#     def show_info(self):
#         super().show_info()
#         print(f"University: {self.university}")
#
#
# class Teacher(Student):
#     def __init__(self, name, age, university, teaches=0.):
#         super().__init__(name, age, university)
#         self.teaches = teaches
#
#     def show_info(self):
#         super().show_info()
#         print(f"Teaches: {self.teaches}")
#
#
# class Faculty:
#     def __init__(self, name_faculty):
#         self.name_faculty = name_faculty
#
#     def show_info(self):
#         print(f"Name Faculty: {self.name_faculty}")
#
#
# class Subject(Faculty):
#     def __init__(self, name_subject, name_faculty):
#         Faculty.__init__(self, name_faculty)
#         self.name_subject = name_subject
#
#     def show_info(self):
#         super().show_info()
#         print(f"Name Subject: {self.name_subject}")
#
#
# class Building:
#     def __init__(self, year=0):
#         self.year = year
#
#     def show_info(self):
#         print(f"Year: {self.year}")
#
#
# class Academy(Building):
#     def __init__(self, year, color=0, university_name=0):
#         Building.__init__(self, year)
#         self.color = color
#         self.university_name = university_name
#
#     def show_info(self):
#         super().show_info()
#         print(f"Color: {self.color}\nUniversity Name: {self.university_name}")


# test = Teacher("Stas", 33, "Ui-pa", "Mathematics")
# test.show_info()
# print(Teacher.mro())
# test2 = Academy(1950, "green", "Ui-pa", )
# test2.show_info()
# print(Academy.mro())
# test3 = Subject("Mathematics","Mechanical Engineering")
# test3.show_info()
# print(Subject.mro())
