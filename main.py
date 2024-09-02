import statistics

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def lecturer_rate(self, course, grade, lecturer):
        if course in self.courses_in_progress and course in lecturer.courses_attached and isinstance(lecturer, Lecturer):
            if course in lecturer.student_grades:
                lecturer.student_grades[course].append(grade)
            else:
                lecturer.student_grades[course] = [grade]
        else:
            print('Error, this course has not been found or is not attached to the lecturer')
    
    def average_value(self):
        return 0 if len(self.grades) == 0 else statistics.mean([j for i in self.grades.items() for j in i[1]])
    
    def __gt__(self, object):
        return self.average_value() > object.average_value()
    
    def __lt__(self, object):
        return self.average_value() < object.average_value()
    
    def __eq__(self, object):
        return self.average_value() == object.average_value()
    
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Surname: {self.surname}\n"
                f"Average grade for homework: {statistics.mean([j for i in self.grades.items() for j in i[1]]) if len(self.grades) > 0 else 'Error, the student has no grades'}\n"
                f"Courses in progress: {', '.join(self.courses_in_progress) if len(self.courses_in_progress) > 0 else 'Error, the student does not have any active courses'}\n"
                f"Completed courses: {', '.join(self.finished_courses) if len(self.finished_courses) > 0 else 'Error, the student does not have any finished courses'}\n")
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.student_grades = {}

    def average_value(self):
        return 0 if len(self.student_grades) == 0 else statistics.mean([j for i in self.student_grades.items() for j in i[1]])
    
    def __gt__(self, object):
        return self.average_value() > object.average_value()
    
    def __lt__(self, object):
        return self.average_value() < object.average_value()
    
    def __eq__(self, object):
        return self.average_value() == object.average_value()
    
    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Surname: {self.surname}\n"
                f"Average grade for lectures: {statistics.mean([j for i in self.student_grades.items() for j in i[1]]) if len(self.student_grades) > 0 else 'Error, the lecturer has no grades'}\n")

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Error'

    def __str__(self):
        return (f"Name: {self.name}\n"
                f"Surname: {self.surname}\n")
    
student_1 = Student('Konstantin', 'Novikov', 'male')
student_2 = Student('Grigory', 'Sokolov', 'male')

lecturer_1 = Lecturer('Daniel', 'Yakovlev')
lecturer_2 = Lecturer('Alexander', 'Goncharov')

reviewer_1 = Reviewer('Alexey', 'Stolyarov')
reviewer_2 = Reviewer('Peter', 'Smirnov')

student_1.finished_courses += ['Java', 'C++']
student_2.finished_courses += ['JavaScript', 'Go']

student_1.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Python', 'Git']

lecturer_1.courses_attached += ['Git']
lecturer_2.courses_attached += ['Python', 'Git']

reviewer_1.courses_attached += ['Git']
reviewer_2.courses_attached += ['Python']

reviewer_1.rate_hw(student_2, 'Git', 10)
reviewer_1.rate_hw(student_2, 'Git', 8)

reviewer_2.rate_hw(student_2, 'Python', 9)

reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 8)

student_1.lecturer_rate('Python', 9, lecturer_2)

student_2.lecturer_rate('Git', 10, lecturer_1)
student_2.lecturer_rate('Git', 8, lecturer_2)
student_2.lecturer_rate('Python', 8, lecturer_2)


print(f'Student 1 > Lecturer 1: {"Yes" if student_1 > lecturer_1 else "No"}')
print(f'Student 1 < Lecturer 1: {"Yes" if student_1 < lecturer_1 else "No"}')
print(f'Student 1 = Lecturer 1: {"Yes" if student_1 == lecturer_1 else "No"}')

print(f'Student 1 > Lecturer 2: {"Yes" if student_1 > lecturer_2 else "No"}')
print(f'Student 1 < Lecturer 2: {"Yes" if student_1 < lecturer_2 else "No"}')
print(f'Student 1 = Lecturer 2: {"Yes" if student_1 == lecturer_2 else "No"}')

print(f'Student 2 > Lecturer 1: {"Yes" if student_2 > lecturer_1 else "No"}')
print(f'Student 2 < Lecturer 1: {"Yes" if student_2 < lecturer_1 else "No"}')
print(f'Student 2 = Lecturer 1: {"Yes" if student_2 == lecturer_1 else "No"}')

print(f'Student 2 > Lecturer 2: {"Yes" if student_2 > lecturer_2 else "No"}')
print(f'Student 2 < Lecturer 2: {"Yes" if student_2 < lecturer_2 else "No"}')
print(f'Student 2 = Lecturer 2: {"Yes" if student_2 == lecturer_2 else "No"}')

print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

def student_grades(student, course):
    average_value = []

    for i in student:
        if course in i.grades:
            average_value.extend(i.grades[course])
    
    return statistics.mean(average_value) if len(i.grades) > 0 else 0

def lecturer_grades(lecturer, course):
    average_value = []

    for i in lecturer:
        if course in i.grades:
            average_value.extend(i.grades[course])
    
    return statistics.mean(average_value) if len(i.grades) > 0 else 0

student = [student_1, student_2]
lecturer = [lecturer_1, lecturer_2]

print(f"The average value of student grades for a Python course: {student_grades(student, 'Python')}\n")
print(f"The average value of student grades for a Git course: {student_grades(student, 'Git')}\n")

print(f"The average value of lecturer grades for a Python course: {lecturer_grades(student, 'Python')}\n")
print(f"The average value of lecturer grades for a Git course: {lecturer_grades(student, 'Git')}\n")