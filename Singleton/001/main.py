# coding: utf-8

from typing import Optional


class Singleton:
    _unique_instance: Optional["Singleton"] = None

    def __new__(cls) -> "Singleton":
        raise NotImplementedError("Not allowed")

    @classmethod
    def __internal_new__(cls) -> "Singleton":
        return super().__new__(cls)

    @classmethod
    def get_instance(cls) -> "Singleton":
        if not cls._unique_instance:
            cls._unique_instance = cls.__internal_new__()
        return cls._unique_instance


if __name__ == "__main__":
    s1 = Singleton.get_instance()
    s2 = Singleton.get_instance()
    assert s1 == s2

    try:
        s3 = Singleton()
    except NotImplementedError:
        print("NotImplementedError")
