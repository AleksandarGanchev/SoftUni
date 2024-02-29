from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element: str or int) -> None:
        self.data.append(element)

    def pop(self) -> str or int:
        return self.data.pop()

    def top(self) -> str or int:
        return self.data[-1]

    def is_empty(self) -> bool:
        return True if len(self.data) == 0 else False

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"

