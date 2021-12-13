class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        if self.grades:
            temp_list = []
            for sublist in self.grades.values():
                for item in sublist:
                    temp_list.append(item)
            average_grade = sum(temp_list) / len(self.grades)
        else:
            average_grade = 0
        return f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка:{average_grade}
Курсы в процессе изучения:{''.join(self.courses_in_progress)}
Завершенные курсы: {self.finished_courses}"""

    def rate_lecturer(self, lecturer, course, grade):
        acceptable_grade = list(range(11))
        if grade in acceptable_grade:
            if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
                if course in lecturer.grades:
                    lecturer.grades[course].append(grade)
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Баллы должны быть в пределах 10 баллов'


class Mentor:
    def __init__(self, name, surname, courses_attached):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"""Имя:{self.name}
Фамилия: {self.surname}"""


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname, courses_attached=[])
        self.grades = {}

    def __str__(self):
        if self.grades:
            temp_list = []
            for grade in self.grades.values():
                for especially_that_one in grade:
                    temp_list.append(especially_that_one)
            average_grade = sum(temp_list) / len(self.grades)
        else:
            average_grade = 0
        return f"""Имя:{self.name}
Фамилия:{self.surname}
Средняя оценка за лекции: {average_grade}"""


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname, courses_attached=[])

    def __str__(self):
        return f"""Имя:{self.name}
Фамилия: {self.surname}"""

    def rate_hw(self, student, course, grade):
        acceptable_grade = list(range(11))
        if grade in acceptable_grade:
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course].append(grade)
                else:
                    student.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Оценка должна быть от в пределах 10 баллов'


def students_average_grade(student_list, course_name):
    for student in student_list:
        if course_name in student.courses_attached or course_name in student.finished_courses:
            return sum(student.grades[course_name]) / len(student.grades[course_name])


def lecturers_average_grade(lecturers_list, course_name):
    for lecturer in lecturers_list:
        if course_name in lecturer.courses_attached:
            return sum(lecturer.grades[course_name]) / len(lecturer.grades[course_name])


very_cool_student = Student('Evgeniy', 'Ponasenkov', 'male')
very_cool_student.courses_in_progress += ['Python']
another_student = Student('Dmitriy', 'Puchkov', 'male')
another_student.courses_in_progress += ['JavaScript']
very_cool_lecturer = Lecturer('Daisuki', 'Ishiwatari')
very_cool_lecturer.courses_attached += ['Python']
another_lecturer = Lecturer('Benedict', 'Cumberbatch')
another_lecturer.courses_attached += ['JavaScript']
very_cool_reviewer = Reviewer('Iron', 'Felix')
very_cool_reviewer.courses_attached += ['Python']
another_reviewer = Reviewer('Valeriy', 'Meladze')
another_reviewer.courses_attached += ['JavaScript']
another_reviewer.rate_hw(another_student, 'JavaScript', 7)
very_cool_reviewer.rate_hw(very_cool_student, 'Python', 6)
very_cool_student.rate_lecturer(very_cool_lecturer, 'Python', 8)
another_student.rate_lecturer(another_lecturer, 'JavaScript', 5)
print(very_cool_student)
print(another_student)
print(very_cool_lecturer)
print(another_lecturer)
print(very_cool_reviewer)
print(another_reviewer)
