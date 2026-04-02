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
        if len(code) != US_POSTCODE_LEN:
            raise ValueError(f'Bad value for {code=}')
        if not code.isdigit():
            raise ValueError(f'Only numbers allowed in {code=}')
        self.code = code

    def __str__(self):
        return self.code

    def get_code(self) -> str:
        return self.code


def main():
    us_code = USPostalCode('khjfj')
    print(us_code)


if __name__ == '__main__':
    main()
