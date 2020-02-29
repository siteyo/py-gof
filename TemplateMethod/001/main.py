# coding: utf-8

from abc import ABCMeta, abstractmethod
from typing import Protocol


class AbstractProtocol(Protocol, metaclass=ABCMeta):
    pass


class Cuttable(AbstractProtocol):
    @abstractmethod
    def cut(self) -> None:
        ...


class Wood(Cuttable):
    def cut(self) -> None:
        print("Wood: cut")


class WoodCutPrint(AbstractProtocol):
    @abstractmethod
    def draw(self, hanzai: Cuttable) -> None:
        pass

    @abstractmethod
    def cut(self, hanzai: Cuttable) -> None:
        pass

    @abstractmethod
    def print(self, hanzai: Cuttable) -> None:
        pass

    def createWoodCutPrint(self) -> None:
        hanzai = Wood()
        self.draw(hanzai)
        self.cut(hanzai)
        self.print(hanzai)


class TanakasWoodCutPrint(WoodCutPrint):
    def draw(self, hanzai: Cuttable) -> None:
        print("tanaka draw")

    def cut(self, hanzai: Cuttable) -> None:
        print("tanaka cut")

    def print(self, hanzai: Cuttable) -> None:
        print("tanaka print")


if __name__ == "__main__":
    t = TanakasWoodCutPrint()
    t.createWoodCutPrint()
