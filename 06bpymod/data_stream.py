from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
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
                self._processed += 1
        else:
            self._stored.append(str(data))
            self._processed += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, str)):
            return True
        if isinstance(data, list):
            return all(isinstance(elem, str) for elem in data)
        return False

    def ingest(self, data: str | list[str]):
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

    def append_log(self, log: dict[str, str]):
        msg = f"{log['log_level']}: {log['log_message']}"
        self._stored.append(msg)
        self._processed += 1

    def ingest(self, data: dict[str, str] | list[dict[str, str]]):
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for elem in data:
                self.append_log(elem)
        else:
            self.append_log(data)


def _get_info(proc: DataProcessor) -> tuple[str, int, int]:
    if isinstance(proc, NumericProcessor):
        type = "Numeric"
    elif isinstance(proc, TextProcessor):
        type = "Text"
    else:
        type = "Log"
    return (type, proc.get_processed(), proc.get_remaining())


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
            print(f"{info[0]} Processor: total {info[1]} items processed,"
                  f" remaining {info[2]} on processor")


def main() -> None:
    stream = DataStream()
    num_pr = NumericProcessor()
    text_pr = TextProcessor()
    log_pr = LogProcessor()
    stream.register_processor(num_pr)
    stream.process_stream([1, 2, 4, 5])
    num_pr.output()
    stream.print_processors_stats()

    stream.register_processor(text_pr)
    stream.register_processor(log_pr)


if __name__ == "__main__":
    main()
