from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._extracted: int = 0
        self._stored: list[Any] = []

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def output(self) -> tuple[int, str]:
        if len(self._stored) == 0:
            return -1, "Error, stored is empty"
        self._extracted += 1
        return self._extracted - 1, self._stored.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(elem, int) for elem in data)
        return False

    def ingest(self, data: int | float |
               list[int] | list[float] | list[int | float]):
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for elem in data:
                self._stored.append(str(elem))
        else:
            self._stored.append(str(data))


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(elem, (int, float)) for elem in data)
        return False

    def ingest(self, data: str | list[str]):
        if not self.validate(data):
            raise ValueError("Improper text data")
        self._stored.append(data)


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def val_log(self, data: Any) -> bool:
        return (isinstance(data, dict)
                and all(
                isinstance(k, str) and isinstance(v, str)
                for k, v in data.items()
                )
                and len(data) == 2
                and "log_level" in data
                and "log_message" in data)

    def validate(self, data: Any) -> bool:
        return (self.val_log(data) or
                (isinstance(data, list)
                 and all(self.val_log(d) for d in data)))

    def append_log(self, log: dict[str, str]):
        for k, v in log.items():
            self._stored.append(k)
            self._stored.append(v)

    def ingest(self, data: dict[str, str] | list[dict[str, str]]):
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for elem in data:
                self.append_log(elem)
        else:
            self.append_log(data)


def main() -> None:
    print("=== Code Nexus - Data Processor ===\n")
    print("Testing Numeric Processor...")
    num_pr = NumericProcessor()
    print(f" Trying to validate input '42': {num_pr.validate(42)}")
    print(f" Trying to validate input 'Hello': {num_pr.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num_pr.ingest('foo')
    except ValueError as e:
        print(e)
    data = [1, 2, 3, 4, 5]
    num_pr.ingest(data)
    print("Extracting 3 values...")
    



if __name__ == "__main__":
    main()
