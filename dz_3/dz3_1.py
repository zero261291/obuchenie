class Student:
    students = []

    def __init__(self, name, surname, course, avg_grade):
        self.name = name
        self.surname = surname
        self.course = course
        self.avg_grade = avg_grade
        self.students.append(self)

    @classmethod
    def add_student(cls, student):
        cls.students.append(student)

    @classmethod
    def remove_student(cls, student):
        cls.students.remove(student)

    def change_name(self, name=None):
        if name:
            self.name = name

    def change_surname(self, surname=None):
        if surname:
            self.surname = surname

    def change_course(self, course=None):
        if course:
            self.course = course

    def change_avg_grade(self, avg_grade=None):
        if avg_grade:
            self.avg_grade = avg_grade

    @classmethod
    def print_students(cls):
        for student in cls.students:
            print(f"Name: {student.name} Surname: {student.surname} Course: {student.course} Avg Grade: {student.avg_grade}")

    @classmethod
    def search_student(cls, surname):
        for student in cls.students:
            if student.surname == surname:
                return student
        return None


# создаем объекты студентов
student1 = Student("Иван", "Иванов", 3, 4.5)
student2 = Student("Петр", "Петров", 2, 3.7)

# добавляем студента
student3 = Student("Сергей", "Сергеев", 1, 4.0)
Student.add_student(student3)

# изменяем данные студента
student1.change_course(4)

# выводим информацию о всех студентах
Student.print_students()

# ищем студента по фамилии
Student.search_student("Иванов")