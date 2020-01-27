# coding: utf-8

from typing import Iterator, List

from Student import Student


class StudentList:
    def __init__(self) -> None:
        self._students: List[Student] = []
        self._i = 0

    def __iter__(self) -> Iterator[Student]:
        # print("__iter__ is called")
        return self

    def __next__(self) -> Student:
        # print("__next__ is called")
        if self._i == len(self._students):
            raise StopIteration
        value = self._students[self._i]
        self._i += 1
        return value

    def append_student(self, student: Student) -> None:
        self._students.append(student)
