# coding: utf-8
import abc


class Chairperson(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def organizeClass(self) -> None:
        ...


class Taro(Chairperson):
    def __init__(self) -> None:
        pass

    def organizeClass(self) -> None:
        self.enjoyWithAllClassmate()

    def enjoyWithAllClassmate(self) -> None:
        print("Enjoy with everyone.")


class Teacher:
    def __init__(self) -> None:
        pass

    def main(self) -> None:
        chairperson = Taro()
        chairperson.organizeClass()


if __name__ == "__main__":
    t = Teacher()
    t.main()
