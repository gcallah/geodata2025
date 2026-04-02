from abc import ABC, abstractmethod


class PostalCode(ABC):
    @abstractmethod
    def __init__(self, code: str):
        print("Can't init this class!")


US_POSTCODE_LEN = 5  # maybe handle 9-char codes later?


class USPostalCode(PostalCode):
    def __init__(self, code: str):
        if not isinstance(code, str):
            raise TypeError(f'Bad type for code: {type(code)}')
        self.code = code

    def get_code(self) -> str:
        return self.code



def main():
    us_code = USPostalCode('khjfjhk')
