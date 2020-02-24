# coding: utf-8
import abc


class Chairperson(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def organizeClass(self) -> None:
        ...


class Taro:
    def __init__(self) -> None:
        pass

    def enjoyWithAllClassmate(self) -> None:
        print("Enjoy with everyone.")


class Hanako(Chairperson):
    def __init__(self) -> None:
        self._taro = Taro()

    def organizeClass(self) -> None:
        self._taro.enjoyWithAllClassmate()


class Teacher:
    def __init__(self) -> None:
        pass

    def main(self) -> None:
        chairperson = Hanako()
        chairperson.organizeClass()


if __name__ == "__main__":
    t = Teacher()
    t.main()
