from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    _name: str

    def __init__(self) -> None:
        self._extracted: int = 0
        self._stored: list[Any] = []
        self._processed = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    @abstractmethod
    def ingest(self, data: Any) -> None:
        ...

    def get_processed(self) -> int:
        return self._processed

    def get_remaining(self) -> int:
        return len(self._stored)

    def output(self) -> tuple[int, str]:
        if len(self._stored) == 0:
            return -1, "Error, stored is empty"
        self._extracted += 1
        return self._extracted - 1, self._stored.pop(0)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self._name: str = "Numeric"

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return all(isinstance(elem, (int, float)) for elem in data)
        return False

    def ingest(self, data: int | float |
               list[int] | list[float] | list[int | float]) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for elem in data:
                self._stored.append(str(elem))
                self._processed += 1
        else:
            self._stored.append(str(data))
            self._processed += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self._name: str = "Text"

    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(elem, str) for elem in data)
        return False

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for msg in data:
                self._stored.append(msg)
                self._processed += 1
        else:
            self._stored.append(data)
            self._processed += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        self._name: str = "Log"

    def val_log(self, data: Any) -> bool:
        return (isinstance(data, dict)
                and len(data) == 2
                and "log_level" in data
                and "log_message" in data
                and isinstance(data["log_level"], str)
                and isinstance(data["log_message"], str))

    def validate(self, data: Any) -> bool:
        return (self.val_log(data) or
                (isinstance(data, list)
                 and all(self.val_log(d) for d in data)))

    def append_log(self, log: dict[str, str]) -> None:
        msg = f"{log['log_level']}: {log['log_message']}"
        self._stored.append(msg)
        self._processed += 1

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for elem in data:
                self.append_log(elem)
        else:
            self.append_log(data)


def _get_info(proc: DataProcessor) -> tuple[int, int]:
    return (proc.get_processed(), proc.get_remaining())


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[Any]) -> None:
        for data in stream:
            ingested = False
            for proc in self._processors:
                if proc.validate(data):
                    proc.ingest(data)
                    ingested = True
                    break
            if not ingested:
                print("DataStream error - "
                      f"Can't process element in stream: {data}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if len(self._processors) == 0:
            print("No processor found, no data")
            return
        for proc in self._processors:
            info = _get_info(proc)
            print(f"{proc._name} Processor: total {info[0]} items processed,"
                  f" remaining {info[1]} on processor")


def main() -> None:
    num_pr = NumericProcessor()
    text_pr = TextProcessor()
    log_pr = LogProcessor()
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()
    print()
    print("Registering Numeric Processor\n")
    stream.register_processor(num_pr)
    batch = ['Hello world', [3.14, -1, 2.71],
             [{'log_level': 'WARNING', 'log_message':
               'Telnet access! Use ssh instead'},
              {'log_level': 'INFO', 'log_message': 'User wil isconnected'}],
             42, ['Hi', 'five']]
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print("\nRegistering other data processors")
    stream.register_processor(text_pr)
    stream.register_processor(log_pr)
    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print("\nConsume some elements from "
          "the data processors: Numeric 3, Text 2, Log 1")
    num_pr.output()
    num_pr.output()
    num_pr.output()
    text_pr.output()
    text_pr.output()
    log_pr.output()
    stream.print_processors_stats()


if __name__ == "__main__":
    main()
