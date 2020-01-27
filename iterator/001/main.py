# coding:utf-8

from Student import Student
from StudentList import StudentList


def call_students(students: StudentList) -> None:
    for student in students:
        print(f"Name:{student.get_name()}, Sex:{student.get_sex()}")


def main() -> None:
    # Create student list
    students = StudentList()

    # Append students
    students.append_student(Student("fuga", 1))
    students.append_student(Student("hoge", 2))
    students.append_student(Student("fuge", 1))

    # Print property
    call_students(students)


if __name__ == "__main__":
    main()
