class StudentNotFoundError(Exception):
    pass


class CourseNotAvailableError(Exception):
    pass


class NotEnrolledError(Exception):
    pass


class InvalidGradeError(Exception):
    pass


class Discipline:
    def __init__(self, name, semester):
        self.name = name
        self.semester = semester

    def __str__(self):
        return f"{self.name} (семестр {self.semester})"


class Department:
    def __init__(self, name):
        self.name = name
        self.disciplines = {}

    def add_discipline(self, discipline, specialty):
        if specialty not in self.disciplines:
            self.disciplines[specialty] = []
        self.disciplines[specialty].append(discipline)

    def teaches(self, discipline_name, specialty):
        if specialty not in self.disciplines:
            return False
        for d in self.disciplines[specialty]:
            if d.name == discipline_name:
                return True
        return False


class Student:
    def __init__(self, student_id, name, specialty):
        self.id = student_id
        self.name = name
        self.specialty = specialty
        self.semester = 1
        self.courses = {}

    def __str__(self):
        return f"[{self.id}] {self.name}, {self.specialty}, семестр {self.semester}"


class Faculty:
    def __init__(self, name):
        self.name = name
        self.departments = []
        self.students = {}

    def add_department(self, department):
        self.departments.append(department)

    def enroll_student(self, student_id, name, specialty):
        if student_id in self.students:
            print("Такой студент уже существует.")
            return
        self.students[student_id] = Student(student_id, name, specialty)
        print(f"Студент {name} зачислен на специальность {specialty}.")

    def expel_student(self, student_id):
        if student_id not in self.students:
            raise StudentNotFoundError("Студент не найден.")
        del self.students[student_id]
        print("Студент отчислен.")

    def get_student(self, student_id):
        if student_id not in self.students:
            raise StudentNotFoundError("Студент не найден.")
        return self.students[student_id]

    def find_department(self, discipline_name, specialty):
        for dep in self.departments:
            if dep.teaches(discipline_name, specialty):
                return dep
        return None

    def add_student_to_course(self, student_id, discipline_name):
        student = self.get_student(student_id)
        dep = self.find_department(discipline_name, student.specialty)
        if dep is None:
            raise CourseNotAvailableError(
                f"Дисциплина '{discipline_name}' не читается для специальности '{student.specialty}'."
            )
        if discipline_name in student.courses:
            print("Студент уже записан на эту дисциплину.")
            return
        student.courses[discipline_name] = {"department": dep.name, "grade": None}
        print(f"Студент записан на дисциплину '{discipline_name}' (кафедра {dep.name}).")

    def remove_student_from_course(self, student_id, discipline_name):
        student = self.get_student(student_id)
        if discipline_name not in student.courses:
            raise NotEnrolledError("Студент не записан на эту дисциплину.")
        del student.courses[discipline_name]
        print("Студент удален из списка изучающих.")

    def set_grade(self, student_id, discipline_name, grade):
        student = self.get_student(student_id)
        if discipline_name not in student.courses:
            raise NotEnrolledError("Студент не записан на эту дисциплину.")
        if not isinstance(grade, int) or grade < 2 or grade > 5:
            raise InvalidGradeError("Оценка должна быть целым числом от 2 до 5.")
        student.courses[discipline_name]["grade"] = grade
        print(f"Оценка {grade} выставлена.")

    def promote_student(self, student_id):
        student = self.get_student(student_id)
        if not student.courses:
            print("У студента нет дисциплин.")
            return
        for name, info in student.courses.items():
            if info["grade"] is None or info["grade"] < 3:
                print(f"Нельзя перевести: по дисциплине '{name}' нет положительной оценки.")
                return
        student.semester += 1
        student.courses = {}
        print(f"Студент переведен в семестр {student.semester}.")

    def student_report(self, student_id):
        student = self.get_student(student_id)
        filename = f"ведомость_студент_{student_id}.txt"

        total = 0
        count = 0
        for info in student.courses.values():
            if info["grade"] is not None:
                total += info["grade"]
                count += 1
        avg = total / count if count > 0 else 0

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Ведомость успеваемости\n")
            f.write(f"Студент: {student.name} (ID {student.id})\n")
            f.write(f"Специальность: {student.specialty}\n")
            f.write(f"Семестр: {student.semester}\n\n")
            f.write("Дисциплины:\n")
            for name, info in student.courses.items():
                grade = info["grade"] if info["grade"] is not None else "нет оценки"
                f.write(f"  {name} (кафедра {info['department']}) — {grade}\n")
            f.write(f"\nСредний балл: {avg:.2f}\n")
        print(f"Ведомость сохранена в файл {filename}.")

    def discipline_report(self, discipline_name):
        dep_name = None
        students_grades = []

        for student in self.students.values():
            if discipline_name in student.courses:
                info = student.courses[discipline_name]
                if dep_name is None:
                    dep_name = info["department"]
                students_grades.append((student, info["grade"]))

        if not students_grades:
            print("Нет студентов, изучающих эту дисциплину.")
            return

        total = 0
        count = 0
        for _, grade in students_grades:
            if grade is not None:
                total += grade
                count += 1
        avg = total / count if count > 0 else 0

        filename = f"ведомость_дисциплина_{discipline_name}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Ведомость по дисциплине: {discipline_name}\n")
            f.write(f"Кафедра: {dep_name}\n")
            f.write(f"Средний балл: {avg:.2f}\n\n")
            f.write("Студенты:\n")
            for student, grade in students_grades:
                g = grade if grade is not None else "нет оценки"
                f.write(f"  [{student.id}] {student.name} ({student.specialty}) — {g}\n")
        print(f"Ведомость сохранена в файл {filename}.")


faculty = Faculty("Факультет информационных технологий")

dep1 = Department("Кафедра прикладной информатики")
dep1.add_discipline(Discipline("Программирование", 1), "прикладная информатика")
dep1.add_discipline(Discipline("Базы данных", 2), "прикладная информатика")
dep1.add_discipline(Discipline("Алгоритмы", 1), "кибербезопасность")

dep2 = Department("Кафедра кибербезопасности")
dep2.add_discipline(Discipline("Криптография", 1), "кибербезопасность")
dep2.add_discipline(Discipline("Сетевая безопасность", 2), "кибербезопасность")

dep3 = Department("Кафедра математики")
dep3.add_discipline(Discipline("Математический анализ", 1), "прикладная информатика")
dep3.add_discipline(Discipline("Математический анализ", 1), "кибербезопасность")


faculty.add_department(dep1)
faculty.add_department(dep2)
faculty.add_department(dep3)


while True:
    print("\n--- Меню ---")
    print("1.Зачислить студента")
    print("2.Отчислить студента")
    print("3.Записать студента на дисциплину")
    print("4.Удалить студента с дисциплины")
    print("5.Выставить оценку")
    print("6.Перевести в следующий семестр")
    print("7.Ведомость по студенту")
    print("8.Ведомость по дисциплине")
    print("9.Показать всех студентов")
    print("0.Выход")

    choice = input("Выбор: ")

    try:
        if choice == "1":
            sid = input("ID студента: ")
            name = input("Имя: ")
            spec = input("Специальность: ")
            faculty.enroll_student(sid, name, spec)

        elif choice == "2":
            sid = input("ID студента: ")
            faculty.expel_student(sid)

        elif choice == "3":
            sid = input("ID студента: ")
            disc = input("Название дисциплины: ")
            faculty.add_student_to_course(sid, disc)

        elif choice == "4":
            sid = input("ID студента: ")
            disc = input("Название дисциплины: ")
            faculty.remove_student_from_course(sid, disc)

        elif choice == "5":
            sid = input("ID студента: ")
            disc = input("Название дисциплины: ")
            grade = int(input("Оценка (2-5): "))
            faculty.set_grade(sid, disc, grade)

        elif choice == "6":
            sid = input("ID студента: ")
            faculty.promote_student(sid)

        elif choice == "7":
            sid = input("ID студента: ")
            faculty.student_report(sid)

        elif choice == "8":
            disc = input("Название дисциплины: ")
            faculty.discipline_report(disc)

        elif choice == "9":
            if not faculty.students:
                print("Студентов нет.")
            for s in faculty.students.values():
                print(s)

        elif choice == "0":
            break

        else:
            print("Неверный ввод.")

    except (StudentNotFoundError, CourseNotAvailableError,
            NotEnrolledError, InvalidGradeError) as e:
        print(f"Ошибка: {e}")
