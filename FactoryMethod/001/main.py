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


class Potato(Cuttable):
    def cut(self) -> None:
        print("Potato: cut")


class WoodCutPrint(AbstractProtocol):
    @abstractmethod
    def _draw(self, hanzai: Cuttable) -> None:
        pass

    @abstractmethod
    def _cut(self, hanzai: Cuttable) -> None:
        pass

    @abstractmethod
    def _print(self, hanzai: Cuttable) -> None:
        pass

    def createCuttable(self) -> Cuttable:
        return Wood()

    def createWoodCutPrint(self) -> None:
        hanzai = self.createCuttable()
        self._draw(hanzai)
        self._cut(hanzai)
        self._print(hanzai)


class TanakasWoodCutPrint(WoodCutPrint):
    def _draw(self, hanzai: Cuttable) -> None:
        print("tanaka draw")

    def _cut(self, hanzai: Cuttable) -> None:
        print("tanaka cut")
        hanzai.cut()

    def _print(self, hanzai: Cuttable) -> None:
        print("tanaka print")

    def createCuttable(self) -> Cuttable:
        return Potato()


if __name__ == "__main__":
    t = TanakasWoodCutPrint()
    t.createWoodCutPrint()
