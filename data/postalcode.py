from abc import ABC, abstractmethod


class PostalCode(ABC):
    @abstractmethod
    def __init__(self, code: str):
        print("Can't init this class!")


class USPostalCode(PostalCode):
    def __init__(self, code: str):
        self.code = code

    def get_code(self) -> str:
        return self.code
