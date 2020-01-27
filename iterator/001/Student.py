# coding:utf-8


class Student:
    def __init__(self, name: str, sex: int) -> None:
        self.__name = name
        self.__sex = sex

    def get_name(self) -> str:
        return self.__name

    def get_sex(self) -> int:
        return self.__sex
