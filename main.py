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
                f"Completed courses: {', '.join(self.finished_courses) if len(self.finished_courses) > 0 else 'Error, the student does not have any finished courses'}")
    
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
                f"Average grade for lectures: {statistics.mean([j for i in self.student_grades.items() for j in i[1]]) if len(self.student_grades) > 0 else 'Error, the lecturer has no grades'}")

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
    
student = Student('Матвей', 'Купцов', 'Мужской')
lecturer = Lecturer('Алексей', 'Морозов')
reviewer = Reviewer('Георгий', 'Коновалов')

student.courses_in_progress.append('Git')
student.courses_in_progress.append('Java')
student.courses_in_progress.append('Python')
lecturer.courses_attached.append('Git')
lecturer.courses_attached.append('Java')
lecturer.courses_attached.append('Python')
reviewer.courses_attached.append('Git')

reviewer.rate_hw(student, 'Git', 10)
student.lecturer_rate('Git', 10, lecturer)
student.lecturer_rate('Java', 8, lecturer)
print(student.average_value() == lecturer.average_value()) 